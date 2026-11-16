# Owner quick start

1. Use the existing **public** `thebuildconsulting/kivaryx` repository. Its visibility was explicitly accepted by the owner on 16 November 2026; no settings change is needed.
2. The final existing checkout/project root is `/Users/dare/Desktop/xterns/darey-new/kivaryx`. The future CentOS VM remains an unapproved runtime decision; do not clone inside this checkout.
3. The extracted pack has been moved into the clone root with owner approval. Keep `.git` in place. The original archive is retained locally under ignored `handoff/`; do not nest another `kivaryx/` project.
4. Check `git status`, inspect `.gitignore`, and ensure generated `*.sqlite3` is not tracked.
5. Open VS Code at the repository root, open Codex, paste `PROMPT_FOR_CODEX.md`.
6. Approve only Milestone 0. Review its report and diagrams with THE BUILD before authorising Milestone 1.

Suggested local commands (if `git` and GitHub access already work):

```bash
cd /Users/dare/Desktop/xterns/darey-new/kivaryx
# Contents and the local review environment are already prepared here.
.venv/bin/python -m pip check
PATH="$PWD/.venv/bin:$PATH" make doctor
PATH="$PWD/.venv/bin:$PATH" make check
```

No push to the remote, AWS provisioning or public publication is authorised by these instructions. `make check` checks the existing prototype tests, not the future Kubernetes baseline.
