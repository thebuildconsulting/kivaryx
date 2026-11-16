# THE BUILD Method — Fintech + AI/ML Edition

**B — Business context:** Merchant payment outcomes, transaction integrity, risk tolerance, obligations, growth, cost, SLOs, fraud-related business impact and model oversight.  
**U — Understand the environment:** AWS topology, EKS, service graph, data flows, payment state transitions, risk model invocation, AI assistant tools, identity, release ownership, backups and cost attribution.  
**I — Investigate evidence:** Falsifiable hypothesis, scope/authority, safe tests, logs/metrics/traces, config and state, model version and inference behaviour, test repeatability and alternative explanations.  
**L — Lay out options:** Minimal config, native cloud service, open source tool, architecture change or do nothing; compare impact, risk, cost, migration path, rollback and team ownership.  
**D — Deliver outcomes:** Controlled change, before/after measurements, residual risk, executive recommendations, docs and handover.

## Evidence classifications

- **E0** fiction/scenario assumption, not observable evidence.
- **E1** actual lab config or manifest, scoped to the known lab profile.
- **E2** reproducible controlled behaviour, tied to a test and time.
- **E3** measured before/after performance or spend model with documented limits.
- **E4** authorised actual client evidence, not used in this fictional season.

Findings must include hypothesis, observation, alternative explanations, business impact, priority, options, estimated effort/cost, selected decision, remaining risk, falsification criteria and evidence IDs.

## Additional fintech / AI questions

- Can duplicate requests create duplicate synthetic transactions? What does the code/test actually prove?
- What is the security and data scope of the payment service? Are secrets, identity and egress appropriate?
- What are the consequence and detection path of a stuck processor call or an ambiguous payment state?
- Does a model-version change impact inference latency or review rates? Is the model output auditable?
- Does the AI operations assistant have only read permission on synthetic data? Are tools and network permissions both restricted?
- Which signals represent merchant/customer outcomes rather than pod health?
- Which costs belong to transaction traffic, observability and inference workloads?

## Framework references

- AWS Well-Architected: https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html
- FinOps: https://www.finops.org/framework/
- Kubernetes Security Checklist: https://kubernetes.io/docs/concepts/security/security-checklist/
- PCI DSS (scope assessment only, not certification): https://www.pcisecuritystandards.org/standards/pci-dss/
- NIST GenAI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
