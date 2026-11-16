# Codex instructions — Kivaryx (must obey)

## Mission
Act as the engineering team reconstructing a **fictional 2026 fintech** so THE BUILD can demonstrate a multi-episode consulting engagement. The goal is not to build a perfect target solution on day one: preserve the current state, investigate, educate, evaluate options, introduce one justified improvement and publish evidence incrementally.

## Strict scope
- Repository `thebuildconsulting/kivaryx`; **public visibility approved by the owner on 16 November 2026**.
- Final project and Git root: `/Users/dare/Desktop/xterns/darey-new/kivaryx`. Do not reintroduce a nested project directory.
- Company brand is provisional Kivaryx; repository name approved as working identifier; do not state trademark/domain clearance.
- Do not work in `thebuildwebsite`, `lab-incubator`, `infrastructure-assessment-toolkit` or employer/client repos.
- Use only isolated local CentOS VM, disposable kind/Compose, localhost, fake merchants/processors, synthetic records; never real payment credentials, card data, third-party live APIs, real financial or employee information.
- Do not deploy AWS resources, use paid cloud/AI services, commit/push/tag, alter org/repository settings or expose a running demo without explicit approval. Public repository visibility is approved; uploading content and public runtime exposure are separate actions.
- Never use a real client/customer name or imply an actual engagement.

## Source of truth
1. `docs/company/*` and `docs/series/*` supplied story/editorial documents.
2. Current implementation and executable tests in `apps/prototype/` — validate them independently.
3. `docs/architecture/as-is/` is client-*described* fictional AWS estate, not proven live.
4. `docs/architecture/as-built/` contains ONLY deployed and verified local state.
5. `docs/architecture/targets/` is proposals only, not implemented.
6. `docs/evidence/` supports **observations**, never invented metrics.

## Stage gates
**Now: Milestone 0 only.** Inspect, test, document, create diagram sources and an ADR. Prepare Milestone 1 plan. NO application redesign, microservice extraction, PostgreSQL migration, Terraform apply, GitOps rollout, security fixes or future tech installs before acceptance.

For later episodes: create prior-state checkpoint; formulate hypothesis; run bounded synthetic reproducer; record pre-change evidence; teach concepts and compare options; implement only selected change; validate and document results; produce client-facing report; preserve after-state.

## Implementation standards
- Tests and reproducibility before claims. Share commands, versions, outputs and limitations.
- Pin versions/lockfiles when introducing dependencies; verify versions against official documentation at time of implementation.
- Repo should be self-contained for public education but distinguish this from ideal regulated-production repo separation; write ADR discussing source vs GitOps config.
- Diagrams-as-code canonical. Explicit as-is, as-built, target and episode diff. Maintain C4 context/container, runtime sequence, deployment, trust boundaries.
- Generated database files, Terraform state, secrets, logs, video raw captures, cloud keys and personal data MUST be gitignored, not merely deleted from working tree.
- Never describe hypothetical risk as demonstrated vulnerability, simulated financial spend as invoice data, or deterministic rules as trained ML.
- No false claims of compliance, availability, measured savings or production readiness.

## End-of-run report
Return: changed files, exact commands/tests and results, architecture fidelity/assumptions, findings/unknowns, design decisions and risks, *the next decision requiring approval*. Do not continue to next gate automatically.
