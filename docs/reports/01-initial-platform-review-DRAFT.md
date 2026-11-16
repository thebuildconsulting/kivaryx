# UNVALIDATED DRAFT — NOT A COMPLETED ASSESSMENT

This draft comes from the earlier Kivaryx planning material. It is not a verified consulting report and must not be published as a finished result. Replace hypotheses with checked evidence during Episode 01.

# Kivaryx — 01 Initial Platform Review

**FICTIONAL CLIENT / SYNTHETIC DEMO**  
**Status: DRAFT — pre-engagement baseline, not an assessment result**  

## Executive brief
The fictional CTO requested a review of operational maturity, payment resilience, cloud costs and AI/ML readiness. The available source of business context is a simulated client brief, not a real cloud account. No claims about security posture, network exposure, runtime performance or savings have been verified.

## Current known scope
- Fictional AWS estate: EKS, ALB, RDS, SQS, S3, CloudWatch, Secrets Manager and IAM, with in-EKS CPU fraud-scoring.
- Implemented local baseline: see `apps/prototype/README.md` and run API tests. Note it is one FastAPI process and SQLite; do not misrepresent it as the actual AWS microservice estate.

## Preliminary hypotheses (all UNVERIFIED)
- H-001: transaction tracing may not cross the fraud-scoring and processor boundaries consistently.
- H-002: network isolation may not enforce the intended trust zones across the cluster.
- H-003: CPU reservation/cost allocation may not reflect observed transaction demand.
- H-004: the internal AI operator assistant's future permissions may exceed its justified read-only use case.

## First diagnostic evidence to collect
- Local prototype health and test run, with test date and code revision.
- `make doctor` output once Codex builds lab; cluster/node versions and scope proof.
- Pod/Service/EndpointSlice state, deployed app image digests and OpenTelemetry traces when available.
- Any presented synthetic cost model marked *illustrative*, not measured billing data.

## CTO recommendation (provisional)
Approve a time-boxed baseline mapping and evidence collection before selecting new services or authorising remediations. Prioritise payment correctness, trust boundaries and customer-facing observability; leave the current production architecture unchanged until tests justify alterations.
