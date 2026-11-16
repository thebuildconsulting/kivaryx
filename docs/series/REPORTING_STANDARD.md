# Client-ready report at the end of EVERY episode

Each episode ends with a real downloadable **assessment report**, tied to reproducible evidence. The final executive report aggregates these, but is not the first report. Each report includes:

1. **1-page executive brief:** question, why this matters to the fintech, observations, severity/uncertainty, decision and next step.
2. **Technical evidence annex:** architecture, commands, tool versions, timestamps, anonymised/synthetic outputs, logs, sample sizes, reproducibility, limitations.
3. **Findings register:** identifier, condition, evidence ID, cause (if proven), business impact, likelihood/consequence, confidence.
4. **Alternatives/options matrix:** do nothing, improve existing, introduce managed/cloud/open-source candidate, reason for recommendation, owner, cost/TCO, risks and rollback.
5. **Outcome record:** baseline vs after test (measured ONLY when measured), unverified forecast otherwise, assumptions and next action.
6. **Learning appendix:** core technology explained, how it works, why selected or rejected, official technical references.

## Planned report per episode

| Ep | Report title | Mandatory output |
|---|---|---|
| 01 | Initial Platform Discovery & Assessment | asset inventory, discovery questions, trust boundaries, initial hypotheses, evidence/unknowns |
| 02 | Payment Integrity & Failure-Modes Review | sequence diagram, retry/idempotency tests, transaction correctness and priority decisions |
| 03 | Identity, Secrets & Access Controls Review | permissions map, least privilege, threat paths, risk register |
| 04 | Network Security & Segmentation Assessment | reachability matrix, packet/flow evidence, policy options and tested bounds |
| 05 | Customer Experience Observability Assessment | signal gaps, SLI/SLO proposal, trace/metric/log correlation, alert design |
| 06 | Payments Latency Root-Cause & Performance Report | latency decomposition, methodology, bottleneck evidence, before/after benchmark |
| 07 | Cloud Cost & Capacity Optimisation Report | allocated cost model, utilisation, reliability guardrails, scenario forecasts |
| 08 | ML Fraud Inference Operations Assessment | model quality proxy, versioning, performance, drift monitors, platform alternatives |
| 09 | AI Assistant Security & Bedrock Options Report | Bedrock vs alternatives, RAG/tool threat model, deny tests, guarded permissions |
| 10 | Resilience & Recovery Assessment | fault injection, RTO/RPO assumptions, state correctness, recovery plan |
| 11 | GitOps & Release Risk Assessment | promotion model, rollout proof, rollback time, separation of duties |
| 12 | Consolidated CTO Decision & 90-Day Roadmap | verified findings across reports, phased remediation and investment options |

### Example output nomenclature

`reports/01-initial-platform-review.md` (source), and optional generated PDF for publishing. Evidence should live under `evidence/01/YYYY-MM-DD/` with a manifest and checksums where appropriate. Report status is `draft`, `technically-verified`, or `approved-for-publication`.
