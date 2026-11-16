# Kivaryx fictional business history and engineering decisions (2022–2026)

**Truthfulness:** This is an invented client narrative for THE BUILD. Every merchant count, transaction volume, cost and event below is a storytelling assumption, never a real company claim or lab measurement. Working brand 'Kivaryx' remains provisional pending name clearance.

## Business proposition
Kivaryx is a UK-based, API-first payment orchestration fintech for mid-market merchants. It offers a single merchant integration, simulated payments routing and transaction lifecycle, a console for operations and CPU-based fraud risk scoring. It connects to external payment processors (mocked in the lab). It is **not** a bank, and the fictional story does not claim regulatory authorisation, card data processing or PCI certification.

## Chronology and rational decisions
| Period | Fictional growth and pressure | Engineering choice made then | Why the choice seemed appropriate | Later questions |
|---|---|---|---|---|
| 2022, MVP | Small founding team; first merchant integrations | Modular Python application, PostgreSQL, managed AWS foundation | Fast iteration and straightforward operations | Where are merchant boundaries and evidence? |
| 2023, adoption | ~25 merchant integrations; processor adapters multiplying | Separate payment, merchant and event concerns; SQS for async tasks | Isolated retry and event processing from synchronous payments | Retry ordering, idempotency, failure visibility |
| 2024, platform shift | More APIs, release coordination issues, team already Kubernetes-capable | EKS, managed node groups, VPC CNI, ALB, Argo CD; existing RDS retained | Consistent deployment and team ownership | Was operational complexity justified? |
| 2025, fraud expansion | Merchant risk demands and fast fraud decision requirements | In-cluster CPU fraud scorer, model artifact delivered with service | Low inference latency, control over dependencies | Versioning, shadow tests, fallback policy, model drift |
| 2026, review | Narrative assumption: ~110 merchants, ~160,000 payment attempts/month, 12 engineers, illustrative AWS $18k/month | Iterative additions: CloudWatch dashboard, Secrets Manager, CI/CD hardening, early read-only support assistant | Incremental investment rather than overhaul | Customer-centric SLOs, egress/east-west controls, cloud TCO, human approval of AI tools |

## Company staffing (fictional)
- CTO: executive sponsor and architecture decision maker, not counted among 12 engineers.
- 5 backend/payment engineers; 2 frontend/merchant experience engineers; 2 platform/SRE engineers; 2 ML/risk engineers; 1 QA/reliability engineer.
- Finance lead approves budget trade-offs, security/compliance adviser clarifies obligations, product lead explains merchant experience. These are fictional stakeholder roles, not actor names.

## Current business questions (not pre-proven failures)
- How do merchant checkout latency and payment error rates differ from infrastructure averages?
- What happens during PSP timeout, duplicate retries, delayed fraud scoring and stale model versions?
- Do platform security controls support segmentation and least privilege without blocking operations?
- Can recovery preserve transaction correctness, not just application availability?
- How much does each service and environment cost, and what is the actual capacity headroom?
- Is a managed GenAI service (e.g. Bedrock) the right choice for safe read-only diagnostic assistance?

## Fictional executive brief (opening premise)
> We have a working platform and a capable engineering team. But as we grow, we need independent evidence that we can keep checkout reliable, secure sensitive workflows, understand what AI is doing and make cost-conscious infrastructure decisions. We do not want a wholesale rewrite without evidence.

## Narrative rules
Good existing controls should be acknowledged. Introduce a failure only with a labelled reproducible scenario. Any measured result must come from a local test with tool versions, timestamp, scenario and sample count. Do not conflate simulated business numbers with actual AWS billing or performance.
