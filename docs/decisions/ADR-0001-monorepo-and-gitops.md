# ADR-0001 — Educational monorepo and the source/deployment boundary

**Status:** Reviewed proposal at Milestone 0; **owner acceptance pending**. This document does not authorize a rollout, commit, release or repository change.  
**Date:** 16 November 2026  
**Evidence:** M0-GIT, M0-SRC, M0-TEST; `MILESTONE_0_REVIEW.md`.

## Context and current state

Kivaryx is a fictional educational company. A viewer should be able to reproduce one complete episode revision: app, synthetic fixtures, lab configuration, diagrams and report. The existing implementation is one FastAPI process with SQLite, not a deployed microservice platform. `gitops/`, `infra/`, `observability/` and root `tests/` contain planning placeholders. Git has no commit or baseline tag. The owner approved normalizing the pack into the existing Git root `/Users/dare/Desktop/xterns/darey-new/kivaryx` on 16 November 2026, and that move is complete. The existing public repository visibility is also approved. Initial checkpoint/commit/push permissions are still pending.

## Recommended decision, pending approval

Use one self-contained repository per fictional company for this educational season, with logical directories for source, local infrastructure, GitOps desired state, synthetic data, evidence and publication metadata. Keep the commercial website and all other fictional-company projects separate. This is an educational reproduction trade-off, not an assertion that a regulated production organisation should combine all repositories.

Preserve the working HTML/JS/FastAPI/SQLite slice. No service extraction, frontend rewrite, PostgreSQL installation or queue choice is approved by this ADR. Those decisions require specific Gate 1 scope and, where material, separate ADRs. Compose-first is the current recommendation for process/network reconstruction; kind is Gate 2. An in-process module may remain preferable to a new service when no contract or investigation needs a network boundary.

Argo CD's [official best practices](https://argo-cd.readthedocs.io/en/stable/user-guide/best_practices/) recommend separating application source from deployment configuration. We reviewed that guidance on 16 November 2026. The educational monorepo intentionally prioritises one-revision playback. It cannot supply genuine separate-repository permissions by naming directories differently.

## Options and trade-offs

| Option | Value | Cost / limitation | Position |
|---|---|---|---|
| Keep current single app and no deployment controller | Simplest faithful executable reference; least new state | Cannot demonstrate cross-process failures yet | Keep as preserved reference; suitable M0 |
| One educational repo with explicit internal boundaries | One revision and release packet for viewers; coordinated review | Shared repository permissions; accidental app/config coupling | Recommended for this fictional season, pending acceptance |
| Separate source, GitOps and Terraform repos | Distinct access/promotion histories and permissions | Requires a version bundle and coordination across repos | Production alternative; revisit if the lesson requires actual separation |
| Repo per service | Independent ownership/releases | Fragmented historical reproduction; larger operational burden | Not justified for the current tiny prototype |

## Source vs GitOps responsibilities, when implemented later

- App CI: test source and contracts, build images, record immutable digests; do not edit running clusters as a side effect.
- Desired-state review: explicitly review `gitops/` and environment changes separately, reference immutable images, and avoid rewriting live image tags.
- Deployment reconciliation: a future locally scoped controller would read approved desired state. Argo CD is **not installed** at this gate and is not a Gate 1 prerequisite.
- Proposed CODEOWNERS/path checks and branch protections provide review structure, not a repository-level security boundary. No rules or organisation settings are configured now.
- Never store secrets, local state, SQLite files, Terraform state or raw captures in source. Local runtime logs and SQLite journals are ignored by the M0 housekeeping change.
- Real account, tenant, credential, network and CI trust controls must be evaluated separately if this ever becomes a non-educational platform.

## Checkpoint / rollback strategy

With the Git layout now approved, after the owner separately approves an initial **local** commit, record its real SHA and the current prototype hashes. Do not call that commit `baseline-v1.0.0`: that tag is reserved for the tested, approved reconstructed baseline after Gate 2. A review acceptance is not permission to push/tag.

Each later episode starts from an approved source SHA and environment/fixture snapshot. Preserve `s01eNN-before-vX.Y.Z` and `s01eNN-after-vX.Y.Z` only after explicit release approval. A discovery-only episode may have the same runtime before/after with changed documentation. Tags locate code, not mutable database state: record fixture version, UTC-relative seeding behavior, images, tools, migrations and reset procedure too. Never retarget a published tag; use a patch version and retain the evidence/report hashes.

Rollback means restoring an approved source/image/config revision **and** an appropriate synthetic datastore snapshot or reset plan. It is not just `git checkout`. No checkpoint/tag/release has been created during M0.

## Acceptance / reconsideration criteria

Before accepting Gate 1: owner agrees host/isolation choice, minimal service boundaries and data/queue scope; repo layout is now settled. Before baseline release: clean-checkout run, exact dependencies/images, deterministic fixture contract, payment invariants, local exposure bounds, setup/reset/down proof and as-built diagrams must pass. Before any external publication or GitHub settings change: separate approval, licence review and history/artifact inspection.

Revisit repository separation if demonstrating release authority, policy controls or real deployment ownership becomes the core lesson. No availability, compliance or security result is claimed by this repository decision.
