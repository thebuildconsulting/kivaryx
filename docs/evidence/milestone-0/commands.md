# Milestone 0 command record

Historical M0 commands below ran from `/Users/dare/Desktop/xterns/darey-new/kivaryx/kivaryx` unless a block changes directory. The owner subsequently approved normalization to `/Users/dare/Desktop/xterns/darey-new/kivaryx`; use that final root to repeat relative commands. Old absolute paths in captured outputs are historical evidence, not current setup instructions. Actual outputs are linked in the review. Commands below record inspection only; future/proposed commands are explicitly separated in the review. No commit/push/tag, cloud call, resource creation or cluster command was run.

## Git, host and ignore checks actually run

```sh
pwd
ls -la
git status --short --branch
git status --porcelain=v1 --untracked-files=all
git remote -v
git rev-parse --show-toplevel
git ls-files
git log -1
git tag --list
git ls-files --error-unmatch apps/prototype/data/kivaryx.sqlite3
git check-ignore -v apps/prototype/data/kivaryx.sqlite3 apps/prototype/data/milestone0-review.sqlite3 .venv/
git check-ignore -v docs/evidence/milestone-0/uvicorn.log docs/evidence/milestone-0/artifacts/merchant.html
git ls-remote --heads --tags origin
gh repo view thebuildconsulting/kivaryx --json nameWithOwner,isPrivate,defaultBranchRef
gh api repos/thebuildconsulting/kivaryx --jq '{full_name,private,visibility,size,default_branch}'
python3 --version
command -v python
ls -l /opt/homebrew/bin/python*
uname -srm
sw_vers
git --version
gh --version
node --version
npm --version
command -v docker kind kubectl terraform mmdc
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --version
```

`git log -1` fails because `main` is unborn. `git ls-files --error-unmatch ...sqlite3` fails because the file is not tracked; `git ls-files` is empty. These are expected inspection outcomes, not failed application tests. `command -v python` and `command -v mmdc` produce no executable. Docker/kind/kubectl/Terraform binaries were located, not used to inspect/deploy any infrastructure.

Source inspection used `rg --files`, `cat` and `nl -ba ...main.py` for the handoff docs, prototype source/static screens/tests/requirements, diagrams, Makefiles and metadata. No other project code/data was read.

## Isolated interpreter and the original tests actually run

```sh
mkdir -p docs/evidence/milestone-0
python3.12 -m venv .venv
# Originally captured here; raw install output was subsequently moved under ignored artifacts/.
.venv/bin/python -m pip install -r apps/prototype/requirements-dev.txt > docs/evidence/milestone-0/dependency-install.txt 2>&1
.venv/bin/python -m pip freeze > docs/evidence/milestone-0/python-packages.txt
.venv/bin/python -m pip check > docs/evidence/milestone-0/pip-check.txt
.venv/bin/python -c 'import sys,sqlite3,platform;print(sys.version);print("SQLite",sqlite3.sqlite_version);print(platform.platform())' > docs/evidence/milestone-0/runtime.txt
PATH="$PWD/.venv/bin:$PATH" make doctor > docs/evidence/milestone-0/make-doctor.txt 2>&1
PATH="$PWD/.venv/bin:$PATH" make check > docs/evidence/milestone-0/api-tests.txt 2>&1
```

The Makefile executes `cd apps/prototype && python -m unittest discover -s tests -v`. Exactly the existing five tests ran. Their source sets `KIVARYX_DB` to a temporary test database before app import, and cleans it up. No new application test or fix was introduced.

To repeat the observed resolved dependency set in a fresh Python 3.12 environment, `pip install -r docs/evidence/milestone-0/python-packages.txt` was initially a **suggested reproduction command, not tested at the original review**; the root-normalization follow-up below subsequently executed it successfully. The package snapshot is not a hash-locked, multi-platform support policy. Root/prototype dependency inputs remain unchanged.

## Local listener actually launched

Working directory for this command was `apps/prototype`:

```sh
KIVARYX_DB="$PWD/data/milestone0-review.sqlite3" ../../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 > ../../docs/evidence/milestone-0/uvicorn.log 2>&1
```

No worker count or host wildcard was supplied. `lsof -nP -iTCP:8765 -sTCP:LISTEN` confirmed one Python listener on `127.0.0.1:8765` (PID 54952 during capture). The server is stopped at review teardown; DB is retained ignored for owner inspection. Do not reuse the fixed smoke key in a dirty DB and expect `replayed=false`.

## HTTP checks actually run through Python urllib

A `.venv/bin/python -` snippet performed `urllib.request.urlopen('http://127.0.0.1:8765' + path, timeout=5)` for these paths, recording status and byte count in `http-smoke.json`:

```text
/ /app /ops /docs /openapi.json /assets/style.css /assets/app.js
/api/healthz /api/merchants /api/dashboard /api/payments /api/architecture /api/ops/insights
```

The snippet read the dashboard seed summary and SQLite table counts, then performed one ordinary create and GET detail. Exact create input:

```json
{"merchant_id":"mrc_meridian","amount_minor":2500,"currency":"GBP","idempotency_key":"milestone-0-smoke-20261116","simulate_outcome":"auto"}
```

Equivalent manual reproduction (not a claim these curl variants were executed):

```sh
curl -fsS http://127.0.0.1:8765/api/healthz
curl -fsS http://127.0.0.1:8765/api/dashboard
curl -fsS -H 'Content-Type: application/json' --data '{"merchant_id":"mrc_meridian","amount_minor":2500,"currency":"GBP","idempotency_key":"milestone-0-smoke-20261116","simulate_outcome":"auto"}' http://127.0.0.1:8765/api/payments
```

## Browser invocation actually run

A Python `subprocess.run(..., capture_output=True, text=True, timeout=40)` loop created a separate temporary Chrome profile for each route `/`, `/app`, `/ops`. For each route, the literal argument list was:

```text
/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
--headless=new
--no-first-run
--disable-background-networking
--disable-sync
--user-data-dir=<temporary kivaryx_m0_chrome_ directory>
--window-size=1440,1100
--virtual-time-budget=4000
--dump-dom
--screenshot=<project>/docs/evidence/milestone-0/artifacts/{landing,merchant,ops}.png
http://127.0.0.1:8765{/,/app,/ops}
```

Rendered DOM was saved under ignored `artifacts/`; a regex extracted KPI values/row counts into `browser-smoke.json`. Screenshots were visually inspected. No interactive browser form submit, mobile/a11y audit, fault injection or load/performance test was run. `/docs` was fetched as HTML only, so its external CDN scripts were not checked in browser.

## Source-preservation check actually run

A Python `hashlib.sha256(Path(path).read_bytes())` snapshot of all 14 original prototype files was written before tests to `prototype-source-sha256.json`. The final check recalculates each listed digest; it does not use `git diff` as proof of unchanged untracked files. Generated SQLite/bytecode are excluded. `validation.json` records the final result.

## Final review validation and teardown actually run

```sh
# PID belongs to the review-only loopback listener confirmed above.
kill 54952
.venv/bin/python docs/evidence/milestone-0/validate_review.py
git status --short --branch
git diff --cached --stat
```

The first inline validation used an incorrect expected count of 14 GET routes and stopped on that assertion. Inspecting `http-smoke.json` established the actual count as **13 GET routes**, plus the ordinary create/detail flow. The review count was corrected; this did not change the passing HTTP responses or the prototype. The checked-in review-only validator records the corrected count and verifies the seven labelled diagram sources, generated-file ignores, original source hashes, curated evidence and stopped listener. It does not parse Mermaid or replay the API/browser checks.

## Owner-approved root normalization follow-up

The owner accepted the final clone root and existing public visibility after the initial review. A Python `Path.rename` loop first checked for name collisions, then moved every child of the nested project directory into its parent and removed the empty nested directory. The original ZIP was moved under ignored `handoff/`, and the existing `.git` was retained. No files were overwritten.

Because Python virtual-environment scripts contain absolute paths, the moved environment was retained under ignored `docs/evidence/milestone-0/artifacts/venv-before-root-move`, then these exact commands were run from `/Users/dare/Desktop/xterns/darey-new/kivaryx`:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r docs/evidence/milestone-0/python-packages.txt > docs/evidence/milestone-0/artifacts/root-move-install.log 2>&1
PATH="$PWD/.venv/bin:$PATH" make doctor > docs/evidence/milestone-0/final-root-doctor.txt 2>&1
PATH="$PWD/.venv/bin:$PATH" make check > docs/evidence/milestone-0/final-root-api-tests.txt 2>&1
.venv/bin/python -m pip check
.venv/bin/python docs/evidence/milestone-0/validate_review.py
git rev-parse --show-toplevel
git remote -v
git status --short --branch
```

Five tests pass at the final root; no app source changed. Brief, policy, ADR and review wording record owner decisions, while original captured preflight/test evidence remains historical. No commit, push, tag, GitHub settings change or Milestone 1 work was performed.
