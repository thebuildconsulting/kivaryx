# Directory ownership — repeat for future fictional companies

```text
kivaryx/
  apps/prototype/             # ALREADY RUNNABLE original fastapi/sqlite source
  apps/*                      # Future separate services, only when justified
  data/                       # Synthetic generators/fixtures, not generated DBs
  infra/local/                # Compose then kind, each validated
  infra/terraform/aws/        # Example AWS IaC; apply prohibited until approved
  gitops/                     # As-is and changes with versioned snapshots
  observability/              # Future telemetry, dashboards and config
  scenarios/                  # Reversible failure and operational drills
  tests/                      # Cross-service integration/acceptance (future)
  docs/company/               # Fictional history, product, business questions
  docs/architecture/as-is/    # Client-described hypothetical AWS estate
  docs/architecture/as-built/ # Actually deployed and validated local state
  docs/architecture/targets/  # Proposed options only
  docs/architecture/episodes/ # Episode before/after, preserved
  docs/decisions/             # ADRs and alternatives
  docs/evidence/              # Evidence manifest and redacted capture
  docs/reports/               # One client-style report per episode
  episodes/                   # Investigation, teaching, demo, editorial brief
  publication/                # Metadata for external website, public releases
  .github/workflows/          # Scoped CI introduced during milestone gates
```

The self-contained repo favours audience reproducibility. It is not a recommendation to combine all regulated-company source, production IaC and GitOps in one repo; note Argo CD's recommendation to separate source and deployment configuration and evaluate that in Episode 11.
