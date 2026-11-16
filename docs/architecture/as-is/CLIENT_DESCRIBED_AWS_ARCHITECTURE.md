# Kivaryx — original architecture before the consultant arrives

## Provenance

Everything in **Part A** is **fictional customer-provided architecture**. It is not an AWS deployment. Everything in **Part B** is the *local reconstruction strategy*. Do not call Part A a verified audit finding.

## A. Fictional AWS architecture (current state)

Canonical editable deployment diagram: [client-aws-deployment.mmd](client-aws-deployment.mmd). It is **CUSTOMER-DESCRIBED FICTIONAL**, not an observed AWS environment. Keeping one source avoids the earlier duplicated `EKS` node/subgraph identifier and a misleading DNS → WAF → ALB proxy chain. See [the M0 inventory](../INVENTORY_M0.md) for source and validation limits.

AWS documents [Route 53 as DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) and [WAF protection as an association with web resources](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html). Those references clarify the drawing, not the fictional platform's actual configuration.


The diagram is logical: network subnets, DNS zones, separate environment accounts, database failover policies and network trust rules will be added to an actual assessment inventory. Avoid claiming single points of failure without validating them.

### Original design assumptions

| Area | Fictional current approach | Why it was reasonable | What we should investigate |
|---|---|---|---|
| Entry | ALB, ACM TLS and WAF | AWS-managed edge integration | Route ownership, TLS backend, access logs, rules |
| Compute | EKS managed node groups | Familiar upstream Kubernetes control | Compute capacity, scaling, upgrade burden |
| Network | VPC CNI and kube-proxy | Established EKS default architecture | East-west access, IP budgets, policy, visibility |
| Identity | IAM workload roles + secrets storage | Managed integration | Least privilege, secret rotation, audit |
| Data | PostgreSQL Multi-AZ | Familiar transaction persistence | Retries, idempotency, consistency, backup/restore |
| Async | SQS + worker | Managed durable queuing | DLQ, retry, deduplication semantics |
| Fraud | In-cluster CPU scoring | Low latency and developer familiarity | Model version, drift, latency, release risk |
| Delivery | GitHub Actions, ECR, Argo CD | Automated builds and GitOps | Promotion, rollback, ownership boundaries |
| Observability | CloudWatch and application dashboards | Practical first operational setup | Transaction SLO, correlation, cost, tracing |
| AI assistant | Read-only proof of concept | Potential operator productivity | Retrieval quality, Bedrock vs alternatives, control |

### Business and technical constraints

- Proposed critical checkout end-to-end p95 SLO: **under 350 ms** for local *fake processor* scenario (provisional target, not achieved guarantee).
- No external provider or real cardholder data in the demonstration.
- Production and nonprod must not share real customer data.
- No demand for GPU serving initially; evaluate managed inference only if evidence justifies it.
- UK-facing architecture should assess data residency, privacy responsibilities and payment-industry scoping; never declare a fictional lab compliant.

## B. Local reconstruction phases

**Phase 0, included now:** FastAPI + SQLite functional merchant site, dashboard, mock payment APIs, deterministic risk simulator, in-process processor-result simulation and audit event records. There is no independent processor service or network request. A *single process* provides the truthful initial visual application and reproducible data.

**Phase 1, Codex:** separate service processes/containers for merchant API, payment orchestration, scoring and fake provider; PostgreSQL; repeatable fixtures and tests; local Compose profile; explicit network interactions.

**Phase 2, Codex:** kind lab with services, probes, requests/limits and scenario runner. Security/observability features only as episodes require.

**Phase 3, with separate approval:** isolated AWS sandbox, pinned IaC, cost budgets and teardown. No current permission to create AWS resources.

## Source references to reverify at production time

- https://docs.aws.amazon.com/eks/latest/userguide/automode.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html
- https://www.pcisecuritystandards.org/standards/pci-dss/
