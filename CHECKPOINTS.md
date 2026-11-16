# Checkpoints and Git strategy

## Rule
Single evolving repo per fictional company. Use short-lived `episode/NN-topic` feature branches and normal PR review. `main` = newest reviewed code. Avoid long-lived `before` and `after` branches; preserve source via immutable commit IDs and release tags.

## Standard references
- `baseline-v1.0.0` — approved original reconstructed local platform (not current proposal).
- `s01e01-before-v1.0.0` — input for Episode 01, may point at the baseline commit.
- `s01e01-after-v1.0.0` — validated Episode 01 source/report.
- `s01e02-before-v1.0.0` then `s01e02-after-v1.0.0`, etc.
- New patch release if published episode changes: `s01e02-after-v1.0.1`, never silently retarget public releases.

For each episode: source SHA, tag, app/image digests, IaC/GitOps snapshot, declared scenario, setup requirements, evidence manifest, report hash, diagrams and link to YouTube/website when published.

## State vs intentionally failing scenario
The main baseline must be functional. Reproduce adverse conditions via explicit, reversible, disabled-by-default scenario. Use `make scenario NAME=...` only after actual implementation and validation, and a documented `make reset` to restore clean operation.

## Build command contract to implement over time
`make doctor`, `make up`, `make seed`, `make check`, `make scenario NAME=...`, `make evidence EP=NN`, `make reset`, `make down`.

Currently `apps/prototype/Makefile` supports only `serve` and `test`. The root `Makefile` supports basic local prototype checks; all other targets are future requirements, not implemented functionality.

## Release packet
`episodes/NN.../BRIEF.md` + `evidence-manifest.json` + `docs/reports/...` + versions + tag + sha + runnable instructions + at least one diagram showing delta. Do not publish a release without verifiable state or approval.
