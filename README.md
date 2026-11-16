# Kivaryx — THE BUILD fictional fintech engineering journey

> **FICTIONAL ENGINEERING LAB.** Kivaryx is a simulated company. All merchant/payment/ML/AWS/cost/incident claims are fictional scenario assumptions unless independently verified in the synthetic lab. This is **not** an anonymised real client engagement or a live payment platform.

A single evolving repository for THE BUILD Series 01. One company; one continuing application and infrastructure; 12 working episodes; each episode teaches relevant technology, investigates evidence and produces a client-style report. Episode count and duration may expand when useful. Preserve tested **before** and **after** release checkpoints.

**Owner:** `thebuildconsulting`  
**Target repository:** `https://github.com/thebuildconsulting/kivaryx` (public visibility approved by owner)  
**Commercial site:** `https://thebuildconsulting.com` (separate repo and backend)  
**Final project / Git root:** `/Users/dare/Desktop/xterns/darey-new/kivaryx`  
**Root and visibility decision:** Owner approved this root and the existing public repository on 16 November 2026. No commit/push/tag or runtime exposure is authorized by that decision.  
**Current status:** Starter pack / Milestone 0; no EKS, independent microservices, GitOps, trained ML, Cilium, Hubble, Bedrock, or live payments are implemented.

## Read first

1. `AGENTS.md` — operating rules for Codex.
2. `CODEX_KICKOFF.md` — *only* what to do now.
3. `docs/company/BUSINESS_HISTORY.md` and `docs/company/PRODUCT_SPEC.md` — company and product.
4. `docs/architecture/as-is/CLIENT_DESCRIBED_AWS_ARCHITECTURE.md` — **fictional reported** AWS estate.
5. `docs/architecture/as-built/README.md` — **actually validated** local implementation.
6. `ROADMAP.md`, `CHECKPOINTS.md`, `DIAGRAM_STANDARD.md`, `PUBLICATION_POLICY.md`.

## Existing working source

`apps/prototype/` contains the previous FastAPI + SQLite application with public site, merchant dashboard, operator UI, synthetic payment endpoint and deterministic rules-based risk simulator. Basic idempotency tests exist; do not claim this is a trained ML model or a distributed microservice architecture.

```bash
cd apps/prototype
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765
```

Screens: `/`, `/app`, `/ops`, `/docs`. **Loopback only**. Generated SQLite file is deliberately excluded from Git; app seeds synthetic data at startup. It lacks authentication and tenant isolation and is NOT SAFE to publish as a live service.

## Working style

- The current Milestone 0 is planning, source reconciliation and architecture/evidence validation. Stop for sign-off before Milestone 1.
- One episode at a time; no future remediations before baseline evidence.
- All demonstrations use local VM/kind and synthetic data. AWS IaC, if authored, is *review-only* until separately approved, funded and provisioned.
- Do not modify the separate THE BUILD website or real CRM from this repository.
