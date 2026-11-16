# Fictional client data-room request and safe lab equivalence

All items are fictional or synthesized. Never use an employer resource, credential, private dashboard, payment record or actual merchant data in a public recording.

| Request | Why asked | Fictional client attachment / local evidence | Restriction |
|---|---|---|---|
| Business critical services and merchant journeys | Prioritise impact | product spec, synthetic transaction workflow | no production merchant PII |
| AWS account/VPC/EKS topology | Identify boundaries and ownership | baseline architecture diagram | no real accounts |
| Kubernetes namespaces, Deployments, Services, EndpointSlices | Discover runtime and Service reachability | isolated kind read-only export | local context only |
| IAM/RBAC and secret configuration inventory | Inspect least privilege | synthetic identity map; no secret values | never export tokens or secrets |
| RDS and SQS dependency map | Understand consistency/failure modes | fake queue/db topology | no sensitive DB dump |
| 30-day incident and alert summary | Spot operational blind spots | synthetic incident descriptions | label simulated |
| Cloud cost by resource/team | Build FinOps baseline | illustrative_costs.csv | not AWS invoice |
| Release/promotion process | Examine rollback risk | local GitOps simulation | no employer CI secrets |
| Fraud model version and evaluation assumptions | Inspect ML operations | deterministic scorer + documented limitations | not a deployed trained model |
| Read-only AI assistant permissions | Examine agent attack surfaces | simulated agent and mock tool catalogue | no external LLM/API by default |

## Lab evidence protocol
- Record commands, tool versions, UTC timestamps, current cluster context and sanitized outputs.
- For each claim, tag `scenario_assumption`, `observed_lab`, `modelled_estimate`, or `not_yet_verified`.
- Avoid vendor cost/performance claims absent a real controlled comparison.
- A viewer can repeat proof using `make doctor`, `make up`, `make check`, `make scenario`, `make reset`, and `make down` once Codex implements these.
