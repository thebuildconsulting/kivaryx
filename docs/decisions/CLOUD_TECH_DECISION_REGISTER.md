# Cloud services and technology — candidate decision register

**Policy:** A service is introduced for a business or technical problem, not because it is fashionable or newly released. Every episode must compare options and explain costs, risk, operations, reliability, lock-in and evidence.

| Candidate | Problem that would justify assessment | Baseline / alternative | Education we owe the viewer | Decision gate |
|---|---|---|---|---|
| Amazon Bedrock runtime | Internal operator wants natural-language insight grounded in approved incidents | deterministic search / self-hosted model / other API | Foundation models, tokens, inference, IAM, retrieval, data handling and guardrails | Reproducible support use case, permission tests, evaluation, cost estimate |
| Bedrock Knowledge Bases | Operator retrieval quality poor or runbooks unsearchable | conventional indexed search, other vector store | RAG architecture, retrieval, citations, drift and privacy | Accuracy/latency/cost test using synthetic documents |
| Bedrock AgentCore / Strands | Controlled multi-tool operations assistant with tracing and access controls | simple read-only orchestrator; no agent at all | tools, approvals, tool-specific IAM, prompt injection, auditability | Threat model, deny tests, cost and supported features |
| SageMaker AI endpoints | CPU inference service can't hit latency/operations requirement or model lifecycle burden high | in-EKS model server, batch scoring | inference hosting, scaling, versions, deployment and pricing | Correctness and tail-latency benchmark, effort/cost |
| EKS Auto Mode | node/network/storage operational overhead higher than value | managed node groups, Karpenter self-managed | managed responsibility boundary, cost, add-ons, debugging | capability match, version/support, cost and operational tradeoff |
| Karpenter | capacity slow or wasteful under varying load | managed node groups + autoscaler | provisioning, consolidation, disruption budgets | cost/availability evidence, regression tests |
| Cilium / Hubble | insufficient network security/flow visibility | VPC CNI policy, other CNIs/flow telemetry | eBPF, policy model, datapath, identities, Hubble limitations | known issue, compatibility, complexity and failure test |
| Envoy Gateway / Gateway API | Route ownership, weighted rollout, advanced traffic control challenges | ALB ingress and native AWS-managed Gateway | GatewayClass, Gateway, HTTPRoute, controller vs dataplane | requirements, conformance, supported features, operating cost |
| AWS X-Ray / CloudWatch / OpenTelemetry | transaction SLO and tracing missing | existing app logging and dashboards | context propagation, traces, sampling, costs | reproducible signal gap, meaningful reduction in diagnosis time |
| AWS SQS | asynchronous reconciliation/retry reliability | direct synchronous call, Kafka/NATS | queue semantics, DLQ, at-least-once, idempotency | replay/duplicate and recovery tests |
| AWS WAF / Shield | edge abuse or rate-limit risk | existing ALB controls and app rate limits | edge threat model, filtering vs identity | security evidence and operational tradeoff |

## Current official reference points (verified for planning Nov 2026; verify again before filming)

- Bedrock's API and builder tooling: https://docs.aws.amazon.com/bedrock/
- Bedrock Agents Classic availability / newer AgentCore approach: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- EKS Auto Mode responsibilities and pricing caveats: https://docs.aws.amazon.com/eks/latest/best-practices/automode.html
- EKS Gateway API Auto Mode updates: https://docs.aws.amazon.com/eks/latest/userguide/auto-change.html
