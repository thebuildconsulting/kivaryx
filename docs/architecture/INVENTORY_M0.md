# Milestone 0 architecture inventory and fidelity matrix

**Fictional engineering lab. Reviewed 16 November 2026.** `STORY/E0` is the invented company estate. `OBSERVED/E1–E2` is source or controlled local behaviour. `PROPOSED` is not implemented. No AWS account was inspected or assumed.

Evidence IDs and exact commands are in `MILESTONE_0_REVIEW.md` and `docs/evidence/milestone-0/`.

## Services, data and boundaries

| Logical component / proposed owner role | Fictional customer description | Actual local implementation / evidence | Gap and proposed gate |
|---|---|---|---|
| Public site / frontend | Fintech marketing and merchant entry | `/` serves `index.html`; hard-coded £42,890 showcase is explicitly illustrative, not a DB KPI (M0-SRC/HTTP/UI) | Preserve surface; framework choice deferred; no redesign in M0 |
| Merchant console / frontend | Merchant reporting and payment creation | `/app`, shared `app.js`, JSON calls to the same process; initial alphabetic merchant is Fieldstone, 14 visible records (M0-UI) | Merchant selector is a filter, not identity; preserve workflows before framework choice |
| Merchant API / backend | Separate merchant-facing service | `/api/merchants`, `/api/dashboard`, `/api/payments` in `app/main.py` (M0-SRC) | Logical boundary only; proposed Gate 1 contract before extraction |
| Payments / backend | Independent orchestration and processor adapter | `initiate_payment` local function, merchant/key uniqueness, payload hash, `BEGIN IMMEDIATE`, 3 events and commit (M0-SRC/TEST/HTTP) | Sequential replay verified; concurrency/recovery/distributed effects not tested; Gate 1 contract |
| Fraud / risk engineers | Packaged CPU model in EKS | `risk_score`: SHA-derived pseudo component plus amount thresholds; `risk-simulator-rules-v0.1` (M0-SRC/TEST) | Rules simulator, no trained artifact, dataset, serving process, accuracy/drift/rollout proof. Extract only when justified; ML lifecycle later |
| Processor / backend | External payment service provider | No socket/HTTP client to a PSP; local status branch and random `sim_` reference (M0-SRC/HTTP) | Proposed fake HTTP adapter service in Gate 1; never real processor credentials |
| Event delivery / backend | SQS publisher and worker | Three SQLite event rows in the same transaction; no broker, worker, consumer, retry or DLQ (M0-SRC/HTTP) | Decide local table/outbox vs broker emulation separately; do not conflate event log with delivery |
| Data / backend + platform | RDS PostgreSQL Multi-AZ, S3 export, possible cache | One local SQLite file, 3 tables, foreign keys and unique merchant/key; initial 3 merchants/42 transactions/126 events (M0-HTTP) | No migrations, PostgreSQL, cache, backup/restore, S3 export or accounting-grade ledger; staged DB decision Gate 1 |
| Ops / support role | Authenticated internal diagnostics; read-only assistant pilot | `/ops` uses same unauthenticated APIs; `/api/ops/insights` serves four static **unverified** questions (M0-UI/SRC) | Ops page lacks write controls but API is writable to local callers. No RBAC, identity or assistant/LLM/tool runtime |
| Edge + network / platform | Route 53, WAF, ALB/ACM, VPC, EKS, managed node groups, VPC CNI, kube-proxy | Review-only Uvicorn listener on `127.0.0.1:8765`; no containers/cluster created (M0-HTTP) | CentOS VM topology/capacity not inspected. Compose candidate Gate 1; kind Gate 2; no cloud authorization |
| Telemetry / platform | CloudWatch dashboards and application signals | Console aggregates, stored per-transaction `req_` ID, event rows and Uvicorn log; no propagated inbound trace context (M0-SRC) | Installed dependency `opentelemetry-api` is not evidence of app instrumentation/exporter. OTel stack deferred to justified episode |
| Identity / platform + security | Workload IAM, Secrets Manager and production roles | No auth middleware/dependencies in inspected prototype; API reads and normal create succeed without credentials (M0-SRC/HTTP) | No tenant isolation, IAM, secret lifecycle or authorization enforcement. Do not expose. No remediation at M0 |
| CI, images, GitOps / platform | GitHub Actions → ECR → Argo CD | Only README placeholders in `.github/workflows/`, `gitops/`, `infra/`; no Dockerfile, executable workflow, deployment or reconciliation (M0-SRC/GIT) | CI proposal and ownership in ADR-0001. No controller/install/repo settings changes |
| FinOps / finance + platform | $18k/month, 110 merchants, 160k attempts/month, 12 engineers | `illustrative_costs.csv` totals $18k by arithmetic; no AWS billing/utilisation (M0-SRC) | STORY, not actual spend, capacity, margin or savings. No benchmark or SLO claim |

Owner roles above are proposed responsibilities consistent with the fictional staffing story, not configured permissions or real employees.

## Runtime and trust interpretation

1. Loopback limits the demonstrated listener's network scope; it does not authenticate users of the machine. No TLS or browser/merchant/operator identity boundary is enforced in this process.
2. Static HTML routes and JSON APIs share one process and origin. Browser-facing UI labels are not access controls. JSON queries can omit/change merchant filters.
3. Scoring and processor behavior are local function calls, not HTTP services. Generated `request_id` is per stored transaction, not a distributed trace. Multiple event rows can share second-resolution timestamps; the query orders by SQLite `rowid`.
4. SQLite stores synthetic records. Transactions/events are atomic in the normal inspected create path; this is not a tamper-evident immutable ledger. Replay lookup occurs before the write transaction; concurrent/restart/crash behavior remains unverified. No concurrency fault was injected at M0.
5. `/docs` HTML is served locally but references external Swagger UI CSS/JS on jsDelivr and a FastAPI favicon. The API and three product screens use local assets; an offline Swagger UI was not proved.
6. The fictional edge, VPC, workload, data and ops boundaries are proposed intent, not locally enforced network or IAM controls. No determination of PCI scope/compliance is made.

## Diagram inventory

| Source | Classification | Review status |
|---|---|---|
| `as-is/client-system-context.mmd` | CUSTOMER-DESCRIBED FICTIONAL v0.1 | Merchant/operator/PSP/cloud boundaries; payments remain story |
| `as-is/client-service-containers.mmd` | CUSTOMER-DESCRIBED FICTIONAL v0.1 | Distinguishes roles, fraud service story, DB vs queue/worker/export; no enforced controls claimed |
| `as-is/client-aws-deployment.mmd` | CUSTOMER-DESCRIBED FICTIONAL v0.1 | DNS query separated from HTTPS data path; WAF association, VPC and control/data arrows clarified; S3 no longer disconnected |
| `as-is/payment-sequence.mmd` | CUSTOMER-DESCRIBED FICTIONAL v0.1 | Response now returns through merchant API; no assumed outbox or exactly-once semantics |
| `as-built/local-prototype.mmd` | LOCAL TESTED v0.1 | Actual macOS host, loopback, one process, local functions, SQLite; evidence IDs and limitations |
| `as-built/payment-sequence.mmd` | LOCAL TESTED v0.1 | New companion sequence showing sequential replay, conflict and normal commit as tested; concurrency branch labelled source-only |
| `targets/initial-story.mmd` | PROPOSED v0.1 | Stage-labelled candidate; no CPU model, agent, queue or telemetry falsely presented as implemented; kind remains later |

Mermaid CLI `mmdc` was **unavailable** on PATH. Sources were manually reviewed against code/story and official syntax guidance; **no renderer, parser or SVG export was run or installed**. Mermaid render acceptance remains unverified, not passed. The canonical files include classification, version/date, direction and synthetic-data/trust limitations. No episode diagram is claimed without a real before/after SHA.

## Story/document reconciliation requiring owner acceptance

- `KIVARYX_ENVIRONMENT.md` section D says baseline plus `missing-readiness` in the first milestone. `CODEX_KICKOFF.md` and `ROADMAP.md` explicitly make M0 review-only and defer kind. Follow the narrower gate: no scenario today; propose readiness scenario only at Gate 2 or a later approved gate.
- Product spec later quality bar and prototype README mention framework/service/Postgres expansion. This is direction, not an approval to rebuild all components now. Preserve vanilla HTML/JS and contracts first.
- The initial pack was nested. On 16 November 2026 the owner approved `/Users/dare/Desktop/xterns/darey-new/kivaryx` as the final root; the contents are now there, with the existing `.git` preserved and the handoff ZIP ignored under `handoff/`. Public repository visibility is accepted. No initial commit or push is authorized yet.
- Canonical diagrams are `docs/architecture/`; some editorial notes still say `diagrams/`. Canonical reports/templates are `docs/reports/` and `docs/templates/`; some episode/series text says `reports/` or `TEMPLATES/CLIENT_REPORT.md`. Resolve aliases before episode production, without changing approved story/history here.
- The Episode 01 draft referenced missing `platform/README.md`; that stale pointer is corrected to `apps/prototype/README.md`, without promoting its draft status.
- The cloud technology register claims planning references verified in November 2026. This review did not revalidate all candidate AWS products, regions or pricing. They remain future decision-time research, never present-day implementation evidence.
