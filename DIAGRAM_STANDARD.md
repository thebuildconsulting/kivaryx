# Architecture diagrams as code — source of truth

1. Maintain C4 context and container boundaries, payment sequence, cloud logical deployment, local physical deployment, trust/security boundaries, and episode-specific before/after deltas.
2. Mermaid `.mmd` canonical; SVG/PNG generated only for presentation and kept in sync. Record renderer/version when used.
3. **As-is** = unverified fictional client-described AWS estate until assessed. **As-built** = actually tested local resources. **Target** = proposed future options, not implemented. **Episode state** = verified before/after overlay and commit hash.
4. Include legend, version, direction of calls, boundaries, dependencies, data sensitivity and evidence IDs where available.
5. A fictional architecture may mention AWS EKS, RDS, ALB, SQS, IAM, CloudWatch, Argo CD etc. This does not imply AWS deployment.
6. Future changes must be reflected in runtime diagrams, not just cloud boxes: ingress, RPC/HTTP paths, model, data persistence, queue and failure recovery.

## Required inventory
- `docs/architecture/as-is/client-system-context.mmd`
- `docs/architecture/as-is/client-service-containers.mmd`
- `docs/architecture/as-is/client-aws-deployment.mmd`
- `docs/architecture/as-is/payment-sequence.mmd`
- `docs/architecture/as-built/local-prototype.mmd`
- `docs/architecture/episodes/NN/` as episodes are produced.
