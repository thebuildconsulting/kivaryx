# Kivaryx web platform — functional synthetic v0.1

**Fictional fintech. Local, synthetic, educational demonstration only.** This application does **not** connect to a payment processor, perform real ML inference, handle real card/bank data, have production-grade authentication or fulfil compliance obligations.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765
```

- Public fintech website: http://127.0.0.1:8765/
- Merchant dashboard: http://127.0.0.1:8765/app
- Internal operator console: http://127.0.0.1:8765/ops
- Test API documentation: http://127.0.0.1:8765/docs

The application automatically seeds a local SQLite database in `data/kivaryx.sqlite3`. Delete that file *only when the local demo server is stopped* to reset to synthetic fixtures, or configure `KIVARYX_DB` to a dedicated test database. No real credentials.

## Demonstrate

1. Open merchant console. Observe seeded transactions and the approval-rate summary based on SQLite rows.
2. Use **New test payment** and choose amount and injected outcome. View its transaction ID, risk score, and request ID.
3. Open a transaction's detail; inspect sequential synthetic events.
4. Open internal Ops console to correlate the same data and view **unverified hypotheses**; don't present these as audit findings.
5. Reuse the same merchant and idempotency key with identical payload: backend returns the same synthetic payment. Change the payload with the same key: HTTP 409.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

## Scope and next Codex work

This is a **genuinely running full-stack vertical slice**, but currently a monolithic prototype using vanilla browser JS, FastAPI, SQLite and simulated risk rules. Treat it as product UX/workflow source and an API contract: Codex should refactor into independent services, Postgres, fixtures, trace propagation, a proper frontend project and local/Kubernetes deployment with evidence — *without pretending this prototype already has those features*.

The demo intentionally has **no authentication or merchant access isolation**. It is bound to loopback by default and must never be publicly exposed. Real authentication, RBAC and tenant enforcement are later engineering milestones.
