"""Kivaryx synthetic fintech demonstration API.

FICTIONAL / LOCAL ONLY. Not real payments, authentication, trained ML, or production security.
SQLite persistence is used only for an educational reference implementation.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from contextlib import closing
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
DB_FILE = Path(os.environ.get("KIVARYX_DB", str(ROOT.parent / "data" / "kivaryx.sqlite3")))
STATIC = ROOT / "static"
MERCHANTS = [
    ("mrc_meridian", "Meridian Goods Demo", "Retail"),
    ("mrc_fieldstone", "Fieldstone Studio Demo", "Services"),
    ("mrc_lumina", "Lumina Market Demo", "Digital goods"),
]
MODEL_VERSION = "risk-simulator-rules-v0.1"

app = FastAPI(title="Kivaryx Synthetic Demo API", version="0.1.0", description="Local demo only. No real payments or cardholder data.")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def conn():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB_FILE, timeout=10)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA foreign_keys=ON")
    return c


def event(c: sqlite3.Connection, txid: str, stage: str, details: dict, when: str | None = None):
    c.execute(
        "INSERT INTO events(event_id,transaction_id,stage,details_json,created_at) VALUES (?,?,?,?,?)",
        ("evt_" + uuid4().hex[:14], txid, stage, json.dumps(details, sort_keys=True), when or utc_now()),
    )


def risk_score(amount_minor: int, merchant_id: str) -> tuple[float, str]:
    # Deterministic simulator. Deliberately NOT machine learning.
    pseudo = int(hashlib.sha256(f"{merchant_id}:{amount_minor}".encode()).hexdigest()[:4], 16) / 65535
    score = min(0.98, 0.075 + pseudo * 0.12 + (0.46 if amount_minor >= 100000 else 0) + (0.31 if amount_minor >= 400000 else 0))
    reason = "Amount requires manual review" if score >= 0.5 else "Low synthetic risk signal"
    return round(score, 3), reason


def initialize():
    with closing(conn()) as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS merchants (
            merchant_id TEXT PRIMARY KEY, display_name TEXT NOT NULL, sector TEXT NOT NULL, status TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY, merchant_id TEXT NOT NULL REFERENCES merchants(merchant_id),
            amount_minor INTEGER NOT NULL, currency TEXT NOT NULL, status TEXT NOT NULL,
            risk_score REAL NOT NULL, risk_reason TEXT NOT NULL, model_version TEXT NOT NULL,
            provider_reference TEXT, request_id TEXT NOT NULL, idempotency_key TEXT NOT NULL,
            payload_hash TEXT NOT NULL, created_at TEXT NOT NULL,
            UNIQUE(merchant_id,idempotency_key)
        );
        CREATE TABLE IF NOT EXISTS events (
            event_id TEXT PRIMARY KEY, transaction_id TEXT NOT NULL REFERENCES transactions(transaction_id),
            stage TEXT NOT NULL, details_json TEXT NOT NULL, created_at TEXT NOT NULL
        );
        """)
        c.executemany("INSERT OR IGNORE INTO merchants VALUES (?,?,?,'active')", MERCHANTS)
        count = c.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
        if count == 0:
            now = datetime.now(timezone.utc)
            # Stable seeded amounts/statuses with timestamps relative to run time.
            for i in range(42):
                mid = MERCHANTS[i % len(MERCHANTS)][0]
                amount = [1299, 2450, 4999, 7900, 12900, 21200, 51000, 124000, 8400, 6200][i % 10]
                score, reason = risk_score(amount, mid)
                status = "requires_review" if score >= 0.5 else ("declined" if i % 13 == 0 else "approved")
                txid = f"pay_demo_{i+1:04d}"
                ts = (now - timedelta(hours=i * 4 + (i % 3))).replace(microsecond=0).isoformat()
                c.execute("""INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (txid,mid,amount,"GBP",status,score,reason,MODEL_VERSION,f"sim_{i+1:06d}",f"req_seed_{i+1:04d}",f"seed_{i+1:04d}",
                     hashlib.sha256(f"seed-{i}".encode()).hexdigest(),ts))
                event(c,txid,"payment.created",{"amount_minor":amount,"currency":"GBP"},ts)
                event(c,txid,"risk.scored",{"score":score,"model_version":MODEL_VERSION,"reason":reason},ts)
                event(c,txid,"payment."+status,{"provider":"synthetic"},ts)
        c.commit()


initialize()


class PaymentRequest(BaseModel):
    merchant_id: str
    amount_minor: int = Field(ge=100, le=2_000_000)
    currency: Literal["GBP"] = "GBP"
    idempotency_key: str = Field(min_length=4, max_length=128)
    simulate_outcome: Literal["auto", "declined", "review"] = "auto"


def as_payment(row: sqlite3.Row) -> dict:
    return {key: row[key] for key in row.keys() if key != "payload_hash"}


@app.get("/api/healthz")
def healthz():
    return {"ok": True, "environment": "synthetic-local", "model_version": MODEL_VERSION}


@app.get("/api/merchants")
def merchants():
    with closing(conn()) as c:
        return {"items": [dict(r) for r in c.execute("SELECT * FROM merchants ORDER BY display_name")]}


@app.get("/api/dashboard")
def dashboard(merchant_id: str | None = None):
    with closing(conn()) as c:
        where = " WHERE merchant_id=?" if merchant_id else ""
        args = [merchant_id] if merchant_id else []
        rows = [dict(r) for r in c.execute("SELECT amount_minor,status,risk_score,created_at FROM transactions"+where,args)]
        approved = [r for r in rows if r["status"] == "approved"]
        volume = sum(r["amount_minor"] for r in approved)
        totals = {s: sum(r["status"] == s for r in rows) for s in ("approved","declined","requires_review")}
        days = []
        now = datetime.now(timezone.utc)
        for d in reversed(range(7)):
            date = (now-timedelta(days=d)).date().isoformat()
            records = [r for r in rows if r["created_at"][:10] == date and r["status"]=="approved"]
            days.append({"date": date, "volume_minor":sum(x["amount_minor"] for x in records),"count":len(records)})
        return {"synthetic":True,"currency":"GBP","total":len(rows),"approved":len(approved),
                "approval_rate":round(100*len(approved)/len(rows),1) if rows else 0,
                "approved_volume_minor":volume,"counts":totals,"last_7_days":days,"model_version":MODEL_VERSION}


@app.get("/api/payments")
def payments(merchant_id: str | None = None, status: str | None = None, limit: int = Query(default=100,ge=1,le=300)):
    conditions=[]
    args=[]
    if merchant_id:
        conditions.append("merchant_id=?");args.append(merchant_id)
    if status:
        conditions.append("status=?");args.append(status)
    where=" WHERE "+" AND ".join(conditions) if conditions else ""
    with closing(conn()) as c:
        rows=c.execute("SELECT * FROM transactions"+where+" ORDER BY created_at DESC LIMIT ?",[*args,limit]).fetchall()
        return {"synthetic":True,"items":[as_payment(r) for r in rows]}


@app.get("/api/payments/{transaction_id}")
def payment_detail(transaction_id: str):
    with closing(conn()) as c:
        row=c.execute("SELECT * FROM transactions WHERE transaction_id=?",(transaction_id,)).fetchone()
        if not row: raise HTTPException(404,"Synthetic transaction not found")
        events=[{"stage":e["stage"],"created_at":e["created_at"],"details":json.loads(e["details_json"])}
                 for e in c.execute("SELECT * FROM events WHERE transaction_id=? ORDER BY rowid",(transaction_id,))]
        return {"synthetic":True,"transaction":as_payment(row),"events":events}


@app.post("/api/payments")
def initiate_payment(request:PaymentRequest):
    with closing(conn()) as c:
        known=c.execute("SELECT merchant_id FROM merchants WHERE merchant_id=?",(request.merchant_id,)).fetchone()
        if not known: raise HTTPException(404,"Synthetic merchant not found")
        payload={"merchant_id":request.merchant_id,"amount_minor":request.amount_minor,"currency":request.currency,
                 "simulate_outcome":request.simulate_outcome}
        digest=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
        previous=c.execute("SELECT * FROM transactions WHERE merchant_id=? AND idempotency_key=?",
                           (request.merchant_id,request.idempotency_key)).fetchone()
        if previous:
            if previous["payload_hash"]!=digest: raise HTTPException(409,"Idempotency key reused with different payload")
            return {"synthetic":True,"replayed":True,"transaction":as_payment(previous)}
        score, reason=risk_score(request.amount_minor,request.merchant_id)
        if request.simulate_outcome=="review": score=max(.82,score);reason="Manual review scenario injected"
        status="requires_review" if score >= 0.5 else "approved"
        if request.simulate_outcome=="declined" and status!="requires_review":status="declined"
        txid="pay_demo_"+uuid4().hex[:12]
        reqid="req_"+uuid4().hex[:12]
        now=utc_now()
        provider="sim_"+uuid4().hex[:10] if status != "requires_review" else None
        try:
            c.execute("BEGIN IMMEDIATE")
            c.execute("""INSERT INTO transactions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (txid,request.merchant_id,request.amount_minor,request.currency,status,score,reason,MODEL_VERSION,
                 provider,reqid,request.idempotency_key,digest,now))
            event(c,txid,"payment.created",{"amount_minor":request.amount_minor,"currency":request.currency})
            event(c,txid,"risk.scored",{"score":score,"model_version":MODEL_VERSION,"reason":reason})
            event(c,txid,"payment."+status,{"processor":"fake-local-adapter", "simulated":True})
            c.commit()
        except sqlite3.IntegrityError:
            c.rollback()
            raise HTTPException(409,"Concurrent idempotency conflict: retry with same payload")
        row=c.execute("SELECT * FROM transactions WHERE transaction_id=?",(txid,)).fetchone()
        return {"synthetic":True,"replayed":False,"transaction":as_payment(row)}


@app.get("/api/architecture")
def architecture():
    return {"synthetic":True,"runtime":"single FastAPI process + local SQLite", "fictional_aws_estate":
            ["Route 53","AWS WAF","ALB","Amazon EKS","AWS VPC CNI","RDS PostgreSQL","SQS",
             "S3","Secrets Manager","CloudWatch","ECR","Argo CD"],
            "caution":"The AWS estate is fictional; these services are NOT deployed by this prototype."}


@app.get("/api/ops/insights")
def ops_insights():
    return {"synthetic":True,"assessment_status":"not-yet-audited","hypotheses":[
        {"id":"H-001","area":"Observability","question":"Can a failing payment be traced end-to-end?","status":"unverified"},
        {"id":"H-002","area":"Security","question":"Are payment and risk trust boundaries enforced?","status":"unverified"},
        {"id":"H-003","area":"Cost","question":"Are compute requests aligned with workload demand?","status":"unverified"},
        {"id":"H-004","area":"AI controls","question":"Can an operations assistant access only read-only tools?","status":"unverified"},
    ]}


@app.get("/")
def landing(): return FileResponse(STATIC / "index.html")


@app.get("/app")
def merchant_console(): return FileResponse(STATIC / "dashboard.html")


@app.get("/ops")
def operator_console(): return FileResponse(STATIC / "ops.html")


@app.get("/assets/{file_name}")
def asset(file_name:str):
    if file_name not in ("style.css", "app.js"): raise HTTPException(404)
    return FileResponse(STATIC / file_name)
