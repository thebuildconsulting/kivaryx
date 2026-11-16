# Codex kickoff — Milestone 0 ONLY

## A. Preflight / do not assume
1. Confirm final project/Git root `/Users/dare/Desktop/xterns/darey-new/kivaryx`, Git remote (if present), working tree state and user permissions. Public visibility is owner-approved; commit/push/tag and public runtime exposure still need explicit approval. Do not force-push or overwrite an existing repo.
2. Read `README.md`, `AGENTS.md`, `ROADMAP.md`, `CHECKPOINTS.md`, `DIAGRAM_STANDARD.md`, and the preserved story/series documents.
3. Inspect `apps/prototype` source and run its 5 existing unit/API tests; record Python/package versions and exceptions. Inspect web screens if browser available. Don't change behaviour yet.
4. Verify generated `apps/prototype/data/kivaryx.sqlite3` is ignored and not tracked. If already tracked, STOP and report; do not blindly rewrite Git history.

## B. Reconcile the company's starting position
5. Produce a service/data inventory and a clear **Fidelity Matrix**: fictional customer-described AWS architecture vs actual FastAPI/SQLite prototype vs future local reconstruction.
6. Document existing product workflows and trust boundaries. Identify which original baseline capabilities are missing or merely simulated.
7. Define pre-production constraints and high-risk assumptions: payments idempotency already exists, but is single-process; risk scoring is deterministic rules, NOT ML.

## C. Diagrams and engineering documentation
8. Review supplied editable `.mmd` diagrams, fix inaccurate labels, and export SVG only if the renderer is available. All illustrations must label `customer-described`, `local tested`, or `proposed`.
9. Finalise `docs/decisions/ADR-0001-monorepo-and-gitops.md` and create an architecture inventory and preliminary verification matrix. No deliberate fault injection yet.
10. Review `publication/series.yaml` and episode checkpoint naming; propose practical CI validation, fixture data, setup and teardown requirements.

## D. Milestone 1 proposal (do not implement)
11. Produce a sequence to evolve current prototype into a realistic *original* local platform: frontend, merchant/payment API boundary, synthetic fraud scoring, mock PSP, database, event delivery, locally runnable containers and then kind. Distinguish original reconstruction from later consulting improvements.
12. Flag choices requiring sign-off (service decomposition, Compose vs kind, Postgres/queue emulator, images, cloud examples).

## End and stop
Provide `MILESTONE_0_REVIEW.md` with verified source status, tests, architecture/fidelity table, diagram list, unresolved questions, proposed Milestone 1 tasks and precise approval gates. Do not start Milestone 1 without approval.
