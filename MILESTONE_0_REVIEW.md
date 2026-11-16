# Milestone 0 review — Kivaryx

**FICTIONAL ENGINEERING LAB — synthetic records and simulated business only.**  
**Date:** 16 November 2026. Evidence capture begins 12:34 UTC; HTTP/browser capture about 12:36 UTC.  
**Status:** Milestone 0 review complete; **awaiting owner review. Milestone 1 NOT started.**  
**Working directory / final approved root:** `/Users/dare/Desktop/xterns/darey-new/kivaryx`  
**Git root:** `/Users/dare/Desktop/xterns/darey-new/kivaryx`  
**Branch/source SHA:** unborn `main`; **no commit SHA exists**. Exact prototype bytes are identified by the [14-file SHA-256 snapshot](docs/evidence/milestone-0/prototype-source-sha256.json), not an invented release reference.

## 1. Decision summary and blockers

The supplied prototype runs unchanged: **all five existing API tests pass**, 13 HTTP routes return 200, and the three product screens render in local Chrome with synthetic data. It is one Python/FastAPI process and one SQLite file, not a deployed AWS platform, distributed system, trained fraud model or authenticated fintech service.

**Owner follow-up, 16 November 2026:** Both initial root/visibility issues below are now resolved by explicit owner instruction. Milestone 1 and commit/push/tag permissions remain pending.

1. **Public visibility accepted.** The original M0 checks reported `private=false`, `visibility=public`, `size=0`, with no heads/tags. The owner has accepted the repository being public; the brief and publication policy now reflect that decision. No GitHub setting was changed. Uploads/releases and public runtime exposure remain separate approval gates. Evidence: [historical GitHub metadata](docs/evidence/milestone-0/github-metadata.json).
2. **Root normalized with approval.** The project contents have been moved from the nested pack folder into `/Users/dare/Desktop/xterns/darey-new/kivaryx`, preserving the existing `.git`. The nested directory is removed; the original handoff ZIP is retained under ignored `handoff/`. The local Python environment was recreated from the recorded resolved package snapshot so its scripts use the final root. No app feature, source checkpoint or remote reference was changed.

These two decisions no longer block repository preparation. There is still no source-SHA checkpoint because no commit is authorized or present. No CentOS VM, cloud account, budget or runtime platform approval is inferred from the company story.

## 2. Scope and evidence classification

Read the operating policies, kickoff/roadmap/checkpoint/diagram/publication/technology policies, company and series documents, episode 01 briefs, architecture diagrams, ADR, publication YAML, Makefiles, source/static UI and the original tests. Future folders were inspected as placeholders. The commercial website, other fictional projects and employer/client sources were not accessed or changed.

- **STORY / E0:** fictional business history, ~110 merchants, ~160k attempts/month, 12 engineers, $18k illustrative monthly spend, AWS estate and assistant pilot.
- **OBSERVED / E1:** actual source, configuration, Git metadata and documented dependency resolution.
- **OBSERVED / E2:** existing tests, normal local HTTP flow and rendered browser screens within the recorded setup.
- **PROPOSED:** service decomposition, PostgreSQL/queue choice, Compose/kind, CI, release process and all future episode technologies.
- **NOT RUN / UNAVAILABLE:** concurrency, recovery, latency/load, network policy, real ML, cloud checks, CentOS reproduction and Mermaid rendering.

This is an internal review, not the Episode 01 client report or publication approval. The supplied Episode 01 report remains explicitly unvalidated draft.

### Evidence index

| ID | Evidence | Meaning / limits |
|---|---|---|
| M0-GIT | [preflight](docs/evidence/milestone-0/preflight.txt), [GitHub metadata](docs/evidence/milestone-0/github-metadata.json), empty [remote refs](docs/evidence/milestone-0/remote-refs.txt) | Actual local/remote metadata; no source revision exists |
| M0-SRC | [prototype hashes](docs/evidence/milestone-0/prototype-source-sha256.json), inspected `apps/prototype/app/main.py`, static files/tests | All 14 original prototype files preserved; source reasoning is not a stress-test result |
| M0-ENV | [runtime](docs/evidence/milestone-0/runtime.txt), [resolved packages](docs/evidence/milestone-0/python-packages.txt), [pip check](docs/evidence/milestone-0/pip-check.txt), [doctor](docs/evidence/milestone-0/make-doctor.txt) | One tested macOS/arm64/Python environment, not CentOS support or a dependency security audit |
| M0-TEST | [original five tests](docs/evidence/milestone-0/api-tests.txt) | Sequential TestClient behaviours; no distributed or concurrent correctness claim |
| M0-HTTP | [HTTP smoke](docs/evidence/milestone-0/http-smoke.json) | 13 GET routes + ordinary create/detail on a dedicated synthetic DB |
| M0-UI | [browser summary](docs/evidence/milestone-0/browser-smoke.json) | Desktop render/DOM/screenshot inspection; not interactive E2E, mobile or accessibility certification |
| M0-FINAL | [validation](docs/evidence/milestone-0/validation.json), [evidence checksums](docs/evidence/milestone-0/evidence-manifest.json) | Source preservation, ignore/docs checks and final inventory; no release signature |

Raw browser DOM/screenshots, package-install output and runtime logs remain local/ignored. Curated summaries are review evidence; generated DB/merchant/transaction dumps are not committed.

## 3. Exact commands, versions and actual results

The full invocation/working-directory record, browser flags and actual-vs-equivalent reproduction commands are in [commands.md](docs/evidence/milestone-0/commands.md).

### Environment actually used

| Tool | Actual version / outcome |
|---|---|
| Host | macOS 14.5 (23F79), Darwin 23.5.0, arm64; **not the future dedicated CentOS VM** |
| System Python | `python3` is 3.9.6; `python` initially absent. No compatibility result is claimed for 3.9 |
| Selected existing Python | `/opt/homebrew/bin/python3.12`, **3.12.11**; isolated `.venv`, pip 25.1.1 |
| Core resolved packages | FastAPI **0.163.1**, Starlette **1.10.0**, Pydantic **2.14.3**, uvicorn **0.54.0**, httpx **0.28.1** |
| SQLite | **3.53.1** from the selected Python runtime |
| Browser | Google Chrome **157.0.8103.78**, headless, 1440×1100 |
| Git / gh | Git **2.39.3** (Apple Git-146), gh **2.76.2** |
| Node / npm | Node **22.22.0**, npm **10.9.4**, discovered only; not application dependencies |
| Diagram renderer | `mmdc` **unavailable**; not installed, no SVG rendered |
| Infrastructure | Docker/kind/kubectl/Terraform binaries found, but no resource/cluster/account inspection or provisioning commands run; versions/support remain unvalidated |

The original requirement ranges were installed unchanged. The full resolved package snapshot includes transitive `opentelemetry-api`; its presence does **not** mean the application has instrumentation or a telemetry stack. No dependency pinning policy or framework migration was introduced at M0.

### Commands actually executed

```sh
# Historical M0 run was nested; repeat from the final approved project root
python3.12 -m venv .venv
.venv/bin/python -m pip install -r apps/prototype/requirements-dev.txt
.venv/bin/python -m pip freeze
.venv/bin/python -m pip check
PATH="$PWD/.venv/bin:$PATH" make doctor
PATH="$PWD/.venv/bin:$PATH" make check
```

| Check | Actual result | Status |
|---|---|---|
| Dependency install / `pip check` | Original ranges resolved; `No broken requirements found.` | verified |
| `make doctor` with `.venv` on PATH | Python 3.12.11; prototype dependencies present | verified |
| `make check` | `Ran 5 tests in 0.042s`, `OK`; all five named tests below pass | verified |
| Deprecation output | Starlette warns that TestClient's `httpx` use is deprecated in favour of `httpx2` | observed warning; not fixed |
| HTTP | All 13 inspected GET routes return 200; ordinary POST create returns 200; detail has three expected events | verified, local/synthetic only |
| Browser | `/`, `/app`, `/ops` render, have synthetic/fictional disclosures, and show no data-loading error in rendered DOM | verified render smoke only |
| Mermaid | Seven editable sources manually reviewed; no renderer available | render/export unavailable |
| Git/source | No tracked DB; 14 original prototype file hashes unchanged; no commit/tag exists | verified |

Existing tests, unchanged:

1. `test_dashboard_seeded`: response 200, synthetic flag and >10 records. It does not assert the exact default fixture count.
2. `test_high_value_review`: a synthetic high-value payment goes to `requires_review`. It does not evaluate real fraud accuracy.
3. `test_key_conflict`: changed amount with the same merchant/key returns 409.
4. `test_no_sensitive_fields`: returned rows lack `card_number`, `cvv`, `payload_hash`. It does not prove the API rejects all sensitive input or establish compliance.
5. `test_payment_and_same_key_replay`: same payload/key gives the same transaction, expected rules version and three events. It does not test concurrent requests, crashes, external side effects or durable delivery.

Tests create a temporary SQLite file before importing the app and remove it on completion. They share a test client/database within the class; they are not five independently seeded environments.

For HTTP/browser review, a **different** fresh DB was used:

```sh
cd apps/prototype
KIVARYX_DB="$PWD/data/milestone0-review.sqlite3" ../../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8765
```

`lsof` confirmed a single listener at `127.0.0.1:8765`. All local smoke clients used that endpoint; no public listener/tunnel was created. The review process was stopped after capture. SQLite remains ignored for local inspection, not release data.

### Observed product behavior

- Fresh seed: **3 merchants, 42 transactions, 126 events**, with 34 approved, 4 declined and 4 review records. The **81.0%** initial aggregate is a computed synthetic fixture statistic, not a business approval-rate claim.
- One normal GBP 25.00 (`amount_minor=2500`) synthetic create returned `approved`, a `pay_demo_...` ID, `req_...` ID and `risk-simulator-rules-v0.1`. Its events are `payment.created`, `risk.scored`, `payment.approved`; no funds moved.
- After that create, Ops rendered **43** records. The merchant console defaults to alphabetically first **Fieldstone Studio Demo**, so it still displayed **14** records, GBP **1,250.97**, **78.6%** approval and **2** review records; the new payment belongs to Meridian. These are different filter contexts, not inconsistent totals.
- `/` contains an explicitly illustrative hard-coded GBP 42,890 showcase. `/app` and `/ops` query SQLite-backed aggregates/records; the marketing illustration is not an observed transaction KPI.
- `/docs` HTML returns 200 but references Swagger UI assets on jsDelivr and a FastAPI favicon. Offline Swagger rendering was not tested. Product-screen CSS/JS are local.
- No interactive browser payment modal, mobile/a11y audit, latency/p95 benchmark, restart/backup/restore, concurrency or fault injection was performed. The ordinary API create was tested separately from browser rendering.

### Revalidation after the owner-approved root move

From the final root, `PATH="$PWD/.venv/bin:$PATH" make doctor` and `make check` pass: Python 3.12.11, **five tests in 0.074s**, same Starlette/httpx deprecation warning. `pip check` reports no broken requirements. The environment was recreated from the original package snapshot; all 14 original prototype file hashes remain unchanged. See [root-normalization.json](docs/evidence/milestone-0/root-normalization.json), [final-root doctor](docs/evidence/milestone-0/final-root-doctor.txt) and [final-root tests](docs/evidence/milestone-0/final-root-api-tests.txt). Historical M0 outputs retain their original nested paths; no browser/HTTP or cloud result is newly claimed by this move.

## 4. Fidelity, inventory and architecture

The detailed [service/technology-gap matrix](docs/architecture/INVENTORY_M0.md) proposes owners and stage gates per component.

| Fictional customer-reported estate | Actually found / verified | Remaining gap |
|---|---|---|
| Merchant frontend + independent APIs | Static HTML/vanilla JS and JSON routes in one process | Service contracts/boundaries; no reason yet to mandate React/Next |
| CPU fraud inference with model artifact | Deterministic hash/amount rules in a local function | No trained model, dataset, inference server, drift/accuracy evidence |
| External PSP / adapter | In-process status branch and fake reference string | No PSP HTTP hop at all; fake service proposed for reconstruction |
| RDS PostgreSQL Multi-AZ | One local SQLite file and transaction/event writes | No PG migrations, replicated DB, backup/restore or accounting ledger proof |
| SQS publisher/worker, audit exports | Three local DB event records per create | No queue, worker, DLQ, outbox or S3 pipeline |
| Route 53/WAF/ALB/TLS/VPC/EKS | One loopback HTTP listener on macOS | No verified region, account, AZ, subnet, policy, ingress, node or cluster |
| IAM/Secrets Manager/operator identity | No prototype authentication/tenant enforcement | UI role labels and merchant filters are not authorization |
| CloudWatch/transaction tracing | DB aggregates, event trail, stored request IDs, local server log | No distributed trace propagation, telemetry exporter or SLO instrumentation |
| GitHub Actions/ECR/Argo CD | Placeholder READMEs; no executable workflow/images/reconciliation | Delivery controls still proposed; no installs authorized |
| Read-only support AI pilot | Static unverified questions in Ops | No agent, RAG, model API, tool permissions or read-only service enforcement |
| $18k spend / 110 merchants / 160k attempts | Fictional source documents and illustrative CSV | Not cost/performance/capacity evidence; no savings measured |

### Confirmed limits, not unperformed exploit claims

There is no auth dependency/middleware in the inspected app, and ordinary reads/create succeed without credentials. This confirms a local prototype limitation; no pentest or cross-network attack was run. Do not expose it publicly. The SQL merchant filter is not tenancy enforcement.

Idempotency is a useful existing control: merchant/key uniqueness, payload comparison and sequential replay are present. The replay read occurs **before** `BEGIN IMMEDIATE`; source handles a later SQLite uniqueness conflict with rollback/409. No claim of exactly-once external processing, concurrent replay returning one response, or crash-safe recovery is justified by these five tests. No remediation was made.

The event trail is an application record set, not tamper-evident or double-entry accounting. Event query order is SQLite `rowid`; timestamps have second precision. A stored request ID is not a trace spanning services that do not exist yet.

### Editable diagrams reviewed

Four as-is sources are labelled **CUSTOMER-DESCRIBED FICTIONAL**, two as-built sources **LOCAL TESTED**, and one target source **PROPOSED**. Each includes version/date, paths/boundaries, data sensitivity and evidence/limits. See the [diagram inventory](docs/architecture/INVENTORY_M0.md#diagram-inventory).

Corrections include DNS lookup vs application traffic, WAF association vs a DNS proxy hop, connected S3/worker story, response through the merchant API, local function calls vs service RPCs, and DB event records vs queue delivery. Removed the stale duplicated inline AWS diagram from the Markdown narrative so `.mmd` remains canonical. Added the actual local payment sequence; target options are staged rather than presented as deployed.

**Render status:** unavailable. No Mermaid parser/CLI or SVG was installed/run; syntax/render layout is not claimed to pass. Optional renderer approval is not a blocker to reading/editing sources, but render acceptance is required before filming/publication.

## 5. ADR, GitOps and sequential releases

[ADR-0001](docs/decisions/ADR-0001-monorepo-and-gitops.md) is now a reviewed proposal awaiting owner acceptance. Recommendation: one educational repo per fictional company, preserve the current prototype, maintain logical source/infrastructure/GitOps/evidence boundaries, and pin a complete release bundle when those runtime pieces exist. Compare with separate app/config/IaC repos; folders alone do not enforce different repository permissions.

The official Argo CD guidance recommends source/config separation; the educational monorepo is a deliberate reproduction trade-off, not a universal production or compliance recommendation. No Argo CD install, CODEOWNERS/branch-protection setup or CI workflow was added.

Keep this sequence:

1. **M0 now:** source/test/fidelity/diagram/ADR review; this document. No releasable baseline SHA yet.
2. **Owner acceptance and repo preparation:** root layout and public visibility are settled; separately authorize initial commit/push. A pack import is not the reconstructed baseline.
3. **Gate 1:** implement only the approved minimal local reconstruction, one tested slice at a time.
4. **Gate 2:** separately approve representative kind reconstruction, probes/resources/reset checks and an evidence-backed as-built map.
5. **Baseline freeze:** only after both gates pass and release approval exists, create `baseline-v1.0.0` at a real tested SHA.
6. **Episode 01:** discovery/report from that baseline. A read-only episode may change evidence/docs without changing runtime.
7. **Episodes 02 onward:** approved `episode/NN-topic` branches, before checkpoint, bounded scenario, evidence, foundational teaching/options, one justified change, validation, report, after checkpoint.

Use `s01eNN-before-vX.Y.Z` and `s01eNN-after-vX.Y.Z` only for actual approved states. Record SHA, images/digests, lab/fixture version, DB migration state, scenario, reset instructions, diagrams, evidence/report hashes and later approved publication URLs. Never retarget published tags; publish a patch when necessary. Source tags do not preserve mutable DB state.

`publication/series.yaml` correctly remains `not_published`, `engineering_lab`, `fictional: true`, with null tag/YouTube/site URLs. Root `series.yaml` stays milestone 0, no reproducible Kubernetes baseline, no cloud provisioned. No links or statuses were fabricated.

## 6. Proposed Milestone 1 scope — approval required, NOT implemented

The recommendation is **Compose-first, preserving the existing UI**, followed by kind at Gate 2. A dedicated CentOS VM is the pack's intended isolation target; its version, capacity, Docker access and host interfaces need confirmation. An explicitly approved macOS local profile is an alternative, not proof of CentOS reproducibility.

| Proposed ordered slice | Why / bounded deliverable | Acceptance before moving on |
|---|---|---|
| 1A. Reproducibility contract | Approve Python/constraints or lockfile, fixture/time contract, local-only configuration and setup/down procedures; preserve original prototype snapshot | Clean environment reproduces five tests and the ordinary UI/API journey; generated DB/log/artifacts ignored; exact versions captured |
| 1B. Define minimal process boundaries | Merchant API facade plus payments core, deterministic scoring and fake PSP; start with explicit contracts, retain modules unless network boundary is needed | Same frontend/API semantics; network calls only where intentionally extracted; request identity rules documented; no real endpoints |
| 1C. Extract one payment path incrementally | If approved: payment orchestration + deterministic score endpoint + fake PSP endpoint behind preserved merchant UI; no trained model | Existing tests retained/adapted transparently; normal create/status/detail, identical-key replay, payload conflict and merchant-scoped key behaviour verified. No future fixes silently added |
| 1D. Persistence / events decision | Prefer local PostgreSQL only after specific ADR/migrations/fixture approval; event log first, queue/emulator/outbox only if required for baseline fidelity | Correct persistence across restart, migrations/reset tested, event vs delivery semantics explicit. Compare SQLite, PostgreSQL, direct call and queue options before install |
| 1E. Local containers and handover | Approve pinned base images and Compose profile with explicit loopback bindings; record service inventory and non-cloud divergences | Clean startup, smoke/contracts, expected service inventory, reproducible fixture reset and teardown; docs/as-built updated from observed state |

Frontend framework, four independent services vs fewer processes, PostgreSQL timing, worker/queue/outbox design, image versions and isolation host are **choices needing agreement**, not simultaneously approved tasks. No new frontend framework is necessary just to preserve the working experience.

### Practical CI and fixture contract to implement only after approval

- Read-only CI checks: exact Python/OS matrix, install pinned app/test inputs, `pip check`, original five tests, source/secret/generated-file checks and isolated synthetic DB. No live AWS/CRM/payment credentials.
- Add contract/integration tests per extracted boundary, including payload conflicts, merchant-scoped keys, ordinary event detail and documented timeout/error semantics. New failure/concurrency scenarios require their explicit approved baseline/episode scope.
- Later Compose CI: loopback-only network configuration, pinned images, unique test DB/project names, startup health smoke and guaranteed cleanup in `finally`/job teardown. Do not fake Kubernetes deployment checks before Gate 2 exists.
- Future diagram CI should pin a Mermaid renderer, parse/render all canonical `.mmd`, check classification/version/links and catch drift. Currently manual source review only.
- Fixtures: preserve deterministic amounts/merchant IDs while distinguishing relative timestamps, random new IDs and random event IDs. Adopt a versioned seed clock if chosen later. Do not commit generated SQLite dumps.
- Setup/teardown: retain simple root `doctor/check/serve-prototype`; implement `up/seed/reset/down` only when underlying commands exist. `scenario/evidence` remain future contracts. Do not add placeholder targets that print a false pass.

## 7. Unknowns, inconsistencies and release risks

| Item | Status / required decision |
|---|---|
| GitHub visibility | Resolved: owner accepts public repository; no settings changed. Content uploads/releases still require approval |
| Project root / handoff ZIP | Resolved: pack moved into Git root, nested directory removed, ZIP retained under ignored `handoff/`; index still empty |
| No initial SHA or lockfile | Exact file hashes and resolved packages captured; reproducibility across future resolutions/platforms remains open |
| Starlette/httpx deprecation | Tests pass with warning; choose and verify a dependency policy later, without hiding the warning now |
| CentOS VM / Docker resources | Not inspected, provisioned or validated; need approved host/version/capacity/isolation before Gate 1 |
| Current docs bring scenarios forward | `KIVARYX_ENVIRONMENT.md` section D asks for `missing-readiness` in “first milestone”; narrower kickoff/roadmap wins. No readiness/fault scenario now; propose at Gate 2 or later explicit gate |
| Path drift in series/episode docs | `diagrams/`, `reports/`, `TEMPLATES/CLIENT_REPORT.md` differ from canonical `docs/architecture`, `docs/reports`, `docs/templates`; reconcile before production. One missing `platform/README.md` pointer was corrected |
| Region/accounts/AZs/RTO/RPO/SLO | Story intent/unknowns. Provisional <350ms fake-processor p95 is not a measured result or accepted production SLO |
| Scoring/PSP/queue/ledger fidelity | Local rules/branch/event records only; no trained ML, real PSP RPC, queue or ledger guarantees |
| Security/public exposure | No auth or tenant boundary; localhost only. No security control fixed or vulnerability exploit demonstrated |
| Offline `/docs`, browser flow, resilience | Swagger CDN dependency observed; offline docs, interactive browser submission and failure/recovery behavior not tested |
| Renderer / diagram presentation | No `mmdc`; no parse/render/export result. Need approved pinned tooling before presentation acceptance |
| Cloud feature/pricing/legal assumptions | No account/service/region/pricing audit or regulatory conclusion. Verify official provider docs at the relevant future decision, not by assuming the register's old “verified” label |
| Publication and licences | Story/brand/domain clearance and public licences remain undecided; no release/case study/compliance/savings claim approved |

## 8. Files changed and scope preservation

All original `apps/prototype/` files, the five tests, requirements, static screens, Makefiles, company history and publication YAML are preserved. Because the repository is wholly untracked, `git diff` alone is not preservation evidence; the 14 original hashes are checked instead.

Review changes:

- This `MILESTONE_0_REVIEW.md`.
- `docs/architecture/INVENTORY_M0.md`: services, technology gaps, trust boundaries, diagram inventory and story conflicts.
- Four as-is `.mmd` sources; `as-is/CLIENT_DESCRIBED_AWS_ARCHITECTURE.md`: factual labels/flows and removal of duplicate inline drawing.
- `as-built/local-prototype.mmd`, new `as-built/payment-sequence.mmd`, `as-built/README.md`: tested local state and limits.
- `targets/initial-story.mmd`: explicitly proposed stage options.
- `docs/decisions/ADR-0001-monorepo-and-gitops.md`: reviewed proposal, alternatives, trust and release trade-offs.
- `docs/reports/01-initial-platform-review-DRAFT.md`: corrected one stale source link only; draft remains unvalidated.
- `.gitignore`: generated runtime `*.log`, SQLite journals and retained `/handoff/*.zip` are ignored; no app/security remediation.
- Root follow-up: project contents moved into the existing Git root with explicit owner approval; `.git` and original prototype bytes preserved. Brief, setup, publication policy and ADR reflect approved public visibility.
- `docs/evidence/milestone-0/`: curated command/version/test/HTTP/UI/metadata/source-preservation evidence. `.venv`, review DB, raw DOM/screenshots/install output and server logs are ignored local artefacts.

## 9. Approval requested — STOP HERE

1. Accept/revise this M0 review and the fidelity boundaries. The owner-approved root move is complete.
2. Repository public visibility is accepted by the owner and documented. No visibility change is needed; separately approve any content upload or release.
3. Accept/revise ADR-0001 and approve a **specific** Gate 1 scope: host/isolation, minimal service boundaries, UI preservation, database/event decision and image/dependency policy. Alternatively authorize only slice 1A first.
4. Give separate explicit approval for any local commit, remote push/tag, branch-protection/CI setting, public release, cloud example implementation or deployment. M0 acceptance does not silently grant these actions.

**Stopped at the Milestone 0 review gate. No Milestone 1 application work, infrastructure, scenario implementation or remote mutation has begun.**

## Official references consulted for this review

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) and [release notes](https://fastapi.tiangolo.com/release-notes/): check TestClient/runtime context; observed warning is retained.
- [Argo CD best practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/): source/config separation trade-off in ADR, not an install recommendation.
- [Mermaid flowchart syntax](https://mermaid.js.org/syntax/flowchart.html): manual diagram source review; not a successful renderer result.
- [Route 53 overview](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) and [AWS WAF operation](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html): correct diagram semantics only; no real AWS resources inspected.
