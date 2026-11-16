# Kivaryx — Architecture and Reproducible Reconstruction

## A. Fictional AWS business estate (narrative only)

- UK-based fintech payments orchestration: merchant-facing APIs, payment initiation and status, fake processor in our reconstruction, transaction audit trail, risk scoring and an internal support assistant pilot.
- Primary platform: AWS EKS, VPC/network boundary, HTTP entry via load balancer/ingress or gateway, managed Postgres, optional Redis/cache, eventing layer, audit/telemetry services.
- Development, staging and production are narrative environments. Their actual topology and separation are design questions, not already verified facts.
- Identity/secrets, delivery, backup and operational controls are investigation subjects; do not deliberately make every component broken.
- ML fraud inference initially uses a **small CPU model** to fit an $18k illustrative infrastructure budget. GPU serving, Karpenter and managed inference are alternatives to evaluate, not assumed requirements.
- Support AI assistant is an internal read-only operations tool with synthetic retrieval and strict tool permissions. LLM deployment is optional, not required for the baseline.
- PCI DSS applicability and scope must be examined if payment card data is stored, processed or transmitted or systems affect the cardholder-data environment. The *demo* never contains real payment card data; it is not a PCI compliance audit.

## B. Local CentOS reconstruction — minimum viable workload

Dedicated CentOS VM -> named isolated kind cluster `kivaryx-lab` with these initial logical services. Codex should start lean and separate services only when measurable or educationally useful.

```text
Synthetic merchant client / load generator
                 |
           merchant-api
                 |
           payments-api -----> fraud-scoring (CPU, synthetic deterministic model)
                 |
       fake-processor (never external real payment API)
                 |
       transaction-events -----> transaction-worker
                 |
        audit/ledger records (synthetic PostgreSQL)

LATER PROFILE (not day one):
  support-agent (read-only) -> synthetic knowledge + approved tool stubs
  distributed tracing, Prometheus/Grafana, log stack, Cilium/Hubble
  optional event broker, progressive-delivery controller
```

- Use trace IDs / request IDs across payments and fraud. Build deterministic fixtures and an idempotency-key test early.
- Ledger is a synthetic append-only-style audit demo; don't claim accounting-grade double-entry guarantees without implementing and proving them.
- Never store PAN/CVV, payment tokens, real consumer identifiers or real transactions.
- Fraud model must be deterministic and explainable enough for testing; record model version in response, score and telemetry. Initial lightweight Python implementation is acceptable after resource verification.
- Agent is disconnected from production and should have no side-effecting tools. A mock RAG/tool response can demonstrate boundary enforcement without an LLM API.
- Do not install GPU drivers, run models requiring GPUs, or spend on model API calls as baseline dependencies.
- Expose local services only to loopback or dedicated isolated interfaces by default.

## C. Module profiles

- `local-core`: baseline kind, merchant/payments, fake processor, small fraud-scoring, transaction/audit record support; no billable cloud services.
- `local-security`: Kubernetes RBAC/NetworkPolicy test fixtures, then Cilium/Hubble only if chosen in the episode and supported by VM/resources.
- `local-observe`: OTel collection + metrics/logging/traces as supported by resources.
- `local-ml`: model version and synthetic training/inference lifecycle, inference metrics, rollback.
- `local-agent`: read-only synthetic retrieval + tools; optional separately-approved model API.
- `aws-sandbox`: future explicit approval, costs capped, permissions minimal, teardown validated, account isolated from employer systems. Not authorised by this document.

## D. Initial scenarios

1. `baseline`: payment initiation returns deterministic synthetic transaction and risk model version, one trace/request ID, and expected provider state.
2. `missing-readiness`: payments or risk replica becomes unready and EndpointSlice reflects its loss.
3. `duplicate-retry`: client resends same idempotency key; prove intended synthetic transaction semantics.
4. `slow-processor`: controlled fake-provider delay; demonstrate p95 tail latency and propagation.
5. `open-east-west`: harmless debug workload can contact service it shouldn't; later enforce policies.
6. `fraud-version-shift`: controlled model version update, inference result changes and rollback.
7. `agent-denied-tool`: read-only agent attempts a prohibited synthetic action and is blocked.
8. `release-drift`: controlled nonprod drift/reconcile/rollback.

Every scenario needs explicit setup, expected observation, test, evidence path, reset. Only `baseline` and `missing-readiness` are required for the first Codex milestone; avoid building all eight at once.

## E. System diagrams and evidence

Diagrams must identify trust zones: public/merchant entry; payments processing; risk scoring; transaction audit/data; internal AI operations. Diagram architecture drawn from narrative separately from actually-deployed resources.

Record real tool versions, VM capacity, cluster settings, test dates, reproducible runs, timings, sample size and known limitations. No invented results. Use synthetic cost CSV for modelling only.

Sources for current verification:
- https://docs.aws.amazon.com/eks/latest/userguide/ml-on-eks.html
- https://docs.aws.amazon.com/eks/latest/best-practices/aiml-performance.html
- https://www.pcisecuritystandards.org/standards/pci-dss/
