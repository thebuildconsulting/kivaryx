"""Local review evidence validation only; does not execute app tests or deploy anything."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

base = Path('docs/evidence/milestone-0')
assert Path(subprocess.run(['git','rev-parse','--show-toplevel'],capture_output=True,text=True,check=True).stdout.strip()).resolve()==Path.cwd().resolve()
assert not Path('kivaryx').exists(), 'Nested project directory must not remain'
source = json.loads((base / 'prototype-source-sha256.json').read_text())
changed = [name for name, digest in source['files'].items()
           if hashlib.sha256(Path(name).read_bytes()).hexdigest() != digest]
assert not changed, changed
tracked = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True).stdout.splitlines()
assert tracked == [], tracked
ignore_paths = ['apps/prototype/data/kivaryx.sqlite3',
                'apps/prototype/data/milestone0-review.sqlite3',
                'apps/prototype/data/milestone0-review.sqlite3-journal',
                'docs/evidence/milestone-0/uvicorn.log',
                'docs/evidence/milestone-0/artifacts/merchant.png',
                'docs/evidence/milestone-0/artifacts/dependency-install.txt', 'handoff/THE_BUILD_Kivaryx_Complete_Codex_Handoff_v1.zip', '.venv/']
ignored = {p: subprocess.run(['git', 'check-ignore', '-q', p]).returncode == 0 for p in ignore_paths}
assert all(ignored.values()), ignored
routes = json.loads((base / 'http-smoke.json').read_text())['routes']
assert len(routes) == 13 and all(v['status'] == 200 for v in routes.values())
ui = json.loads((base / 'browser-smoke.json').read_text())
assert all(s['exit_code'] == 0 and s['screenshot_exists'] and s['synthetic_disclosure_present']
           and not s['data_loading_error'] for s in ui['screens'])
tests = (base / 'api-tests.txt').read_text()
assert 'Ran 5 tests' in tests and '\nOK\n' in tests
assert json.loads((base / 'github-metadata.json').read_text())['private'] is False
listen = subprocess.run(['lsof', '-nP', '-iTCP:8765', '-sTCP:LISTEN'], capture_output=True, text=True)
assert listen.returncode == 1 and not listen.stdout, listen.stdout
files = ['MILESTONE_0_REVIEW.md', 'AGENTS.md', 'README.md', 'CODEX_KICKOFF.md', 'START_HERE.md', 'PROMPT_FOR_CODEX.md', 'PUBLICATION_POLICY.md', 'docs/architecture/INVENTORY_M0.md',
         'docs/architecture/as-built/README.md',
         'docs/architecture/as-is/CLIENT_DESCRIBED_AWS_ARCHITECTURE.md',
         'docs/decisions/ADR-0001-monorepo-and-gitops.md']
broken = []
for f in files:
    for link in re.findall(r'\]\(([^)]+)\)', Path(f).read_text()):
        if '://' in link or link.startswith('#'):
            continue
        clean = link.split('#')[0]
        if clean.endswith(('validation.json', 'evidence-manifest.json')):
            continue  # Generated below in this same run.
        if not (Path(f).parent / clean).exists():
            broken.append({'file': f, 'target': link})
assert not broken, broken
diagrams = list(Path('docs/architecture').rglob('*.mmd'))
assert len(diagrams) == 7
assert all(any(label in p.read_text() for label in
               ('LOCAL TESTED', 'CUSTOMER-DESCRIBED FICTIONAL', 'PROPOSED')) for p in diagrams)
result = {
    'completed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'final_root': str(Path.cwd().resolve()),
    'root_normalization': 'owner-approved; existing Git directory preserved',
    'prototype_source_files_checked': len(source['files']), 'prototype_changed_files': changed,
    'tracked_files': tracked, 'ignored_generated_paths': ignored,
    'api_test_count': 5, 'api_tests_status': 'verified: original five pass',
    'http_get_routes_count': len(routes), 'http_status': 'verified: all 200; normal create/detail also passed',
    'browser_status': 'verified: desktop render smoke only', 'diagram_sources': len(diagrams),
    'diagram_rendering': 'unavailable: mmdc not installed; manual source review only',
    'review_links_broken': broken,
    'server_teardown': 'verified: no listener on 127.0.0.1:8765 after stopping review process',
    'github_visibility_observed': 'public: explicitly accepted by owner on 2026-11-16; no settings changed',
    'milestone_1': 'not started',
    'commits_pushes_tags_settings_changes': 'none; index remains empty',
}
(base / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
paths = [p for p in base.iterdir() if p.is_file()
         and p.name not in ('evidence-manifest.json', 'uvicorn.log')]
paths += [Path(f) for f in files] + diagrams + [Path('.gitignore'),
          Path('docs/reports/01-initial-platform-review-DRAFT.md')]
manifest = {
    'generated_at_utc': result['completed_at_utc'],
    'classification': 'Local M0 review evidence; not published, signed or released',
    'source_sha': 'unavailable: unborn main',
    'exclusions': 'Self, ignored DB/logs/raw captures/install output and venv; no transaction dump included',
    'sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))},
}
(base / 'evidence-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps(result, indent=2))
