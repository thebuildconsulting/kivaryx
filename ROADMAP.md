# Phased implementation roadmap — no prebuilding

**Gate 0 — NOW:** Verify original source, story, technical assumptions, diagrams and repo structure. Deliver Milestone 0 review. No fixes or migration.

**Gate 1 — After approval:** Establish functioning local fintech baseline. Preserve existing public site + dashboard + operator UI, payment flow, fraud rules, synthetic PSP, idempotency and trace/request IDs. Split application only where needed to reproduce the fictional 2026 estate; do not invent trained ML. Containerise safely; deterministic fixtures, app tests, service contracts.

**Gate 2 — After Gate 1:** Reconstruct a representative local Kubernetes baseline using kind, preferably with appropriate PostgreSQL and local queue/emulator where justified. Capture a complete verified *as-built* inventory and divergence from fictitious AWS as-is. Add health checks and clear teardown.

**Baseline freeze:** Only when tests, diagrams, reproducibility, synthetic data and security review pass, label `baseline-v1.0.0`. No untested/impossible tag; need explicit release approval.

**Gate 3 — Episode 01:** Simulated CTO discovery and bounded read-only platform audit, report with evidence, priority/uncertainty, no wholesale remediation.

**Episodes 02–11:** One diagnostic question at a time. Pause before implementing technology introduced in later episodes (Cilium/Hubble, OTel, Bedrock/AgentCore, managed ML, Karpenter, progressive delivery etc.). Compare alternatives; report per episode.

**Episode 12:** Summarise existing report findings and decisions, propose 30/60/90-day CTO plan. Do not invent savings or improvements.

## Hard acceptance criteria for every gate
- Reproducible from clean checkout with documented host and container versions.
- Synthetic data and mock payment flows only.
- Existing baseline tests still pass and new tests cover changed behaviour.
- Evidence attached with exact commands, dates, environment and expected/actual distinction.
- Editable diagrams accurately track as-is, as-built and target states.
- Decision record with alternatives and rejected proposals.
- Client-facing episode report where applicable.
- No external/public/cloud action without explicit approval.
