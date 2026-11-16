# Kivaryx — First CTO Discovery Meeting and Assessment Charter

**Episode 01 working title:** A Fintech's Kubernetes and AI Stack: What Would I Audit First?

**Engagement simulation:** 45-minute initial discovery, then a time-boxed read-only technical assessment. Nothing in this document claims that a real meeting occurred.

## Meeting agenda (45 minutes)
- **00–05 | Context:** What triggered the review now? Who signs off? What would a satisfactory first 30 days look like?
- **05–12 | Transaction lifecycle:** Merchant journey, sync/async dependencies, processor failure, refunds/disputes scope, data integrity priorities.
- **12–19 | Architecture and platform:** What runs in EKS, RDS, SQS and outside the cluster? Environment/account separation and operational ownership.
- **19–26 | Reliability and observability:** Recent incidents, merchant SLOs, telemetry, alert escalation, rollback, RTO/RPO and drills.
- **26–33 | Security and AI/ML:** Trust boundaries, access approvals, secret lifecycle, ML model/version governance, read-only agent limits and logging.
- **33–39 | Spend and delivery:** True cost allocation, commitment discounts, capacity, release cadence, on-call burden, engineering effort and optimisation constraints.
- **39–45 | Scope and permissions:** Confirm artifacts, read-only access scope, sensitive exclusions, timelines, decision meetings and report reviewers.

## Questions to ask the CTO (then confirm with technical owners)
1. Which merchant journey would you protect even during a partial outage?
2. How do you define a successful payment attempt, and where is that truth recorded?
3. What customer-visible incident would you most like explained?
4. What architecture decision currently concerns you, and which is working well?
5. Which teams are accountable for the gateway, fraud model, datastore, queue and incident response?
6. What data, secrets and financial records must not leave your controlled environment?
7. What are the acceptable outage, data-loss and degraded-service trade-offs?
8. How do you roll out and roll back risk-scoring changes?
9. Do you know which customer flows generate the largest costs and operational effort?
10. What would make you prefer a managed AWS service to an existing in-cluster component?
11. Which risks have been formally accepted and why?
12. Who owns the 30/60/90-day prioritisation and budget decisions?

## Suggested engagement scope
- Included initially: architecture inventory, network and identity diagrams, sampled configs, CI/CD, read-only cluster state, synthetic payment lifecycle, evidence mapping, risk hypotheses, priorities.
- Excluded initially: production writes, pentesting, destructive testing, customer-record exports, regulatory certification, real card payment activity, cloud changes.
- All credential and private-account requests require an explicit separate approval; local Kivaryx lab uses synthetic proof only.

## Starter deliverables
1. Meeting brief and assumptions/unknowns log.
2. Asset and service inventory with source references.
3. Trust-boundary/dataflow diagram.
4. Initial risk hypothesis register, confidence and evidence status.
5. Episode 01 client report and proposed next technical investigations.

## Opening narrative prompt for the camera
'A CTO doesn't usually ask you to install Cilium or Karpenter. They ask whether their payments platform can continue scaling safely, whether it is sufficiently visible, and whether its costs make sense. Our first job is to understand the business and the existing system before suggesting tools.'
