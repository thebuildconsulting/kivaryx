# THE BUILD | Series 01 — Kivaryx (12-episode working arc)

**Episodes are chapter-sized engineering investigations**; typical 25–35 minutes, longer or split when teaching needs it. Exactly one primary consulting decision per chapter. Each episode generates its own report. Titles can be refined while producing; creative strategy and report-per-episode rule are locked.

| # | Working title | Technology lesson and investigation | Deliverable |
|---|---|---|---|
| 01 | A Fintech's Kubernetes and AI Stack: What Would I Audit First? | Asset discovery, EKS architecture, app dependencies, evidence taxonomy | Initial Platform Discovery & Assessment |
| 02 | One Payment, Six Services: Where Can It Go Wrong? | Distributed transactions, idempotency, retries, SQS/outbox options | Payment Integrity & Failure-Modes Review |
| 03 | Is This Fintech's Cloud Identity and Secrets Setup Safe? | IAM, pod identity, RBAC, Secrets Manager, rotation | Identity, Secrets & Access Controls Review |
| 04 | A Compromised Pod in a Payment Cluster: What Can It Reach? | Cilium, eBPF, Hubble, NetworkPolicy, alternatives | Network Security & Segmentation Assessment |
| 05 | The Payments Dashboard Is Green. Why Are Merchants Complaining? | SLOs, tracing, OpenTelemetry, AWS-native alternatives | Customer Experience Observability Assessment |
| 06 | This Payment Is Slow: Is Kubernetes Actually to Blame? | Critical path latency, database, gateway, model inference, profiling | Payments Latency Root-Cause & Performance Report |
| 07 | Where Is This Fintech's AWS Budget Really Going? | FinOps, Karpenter vs managed/Auto Mode, cost attribution | Cloud Cost & Capacity Optimisation Report |
| 08 | Running Fraud Detection on Kubernetes: What Would I Change? | Inference design, versions, SageMaker AI vs EKS, drift and rollback | ML Fraud Inference Operations Assessment |
| 09 | Should This Fintech Trust Its AI Operations Agent? | Bedrock runtime, RAG, AgentCore candidate, guardrails and tool permissions | AI Assistant Security & Bedrock Options Report |
| 10 | Can Payments Survive a Failed Node or Dependency? | Availability, retries, failure injection, RTO/RPO | Resilience & Recovery Assessment |
| 11 | GitOps Isn't Enough: How Do We Release a Payment Platform Safely? | Argo CD, policy checks, Gateway API weighted routes, rollback | GitOps & Release Risk Assessment |
| 12 | What I'd Recommend to the Fintech CTO After the Review | Decision synthesis, 30/60/90-day roadmap, business case | Consolidated CTO Decision & 90-Day Roadmap |

Extra deep-dive episodes may be inserted *only if* the educational depth benefits from dedicated treatments. The separate original 24-video Kubernetes Networking calendar remains unchanged.
