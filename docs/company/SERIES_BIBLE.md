# Kivaryx — canonical fictional company bible

## Identity

- Working brand: **Kivaryx**; pronounced *KIV-ah-riks*. Fictional case-study label in every video and report. No claim of name clearance, company registration, authorisation or financial regulatory status.
- Public positioning: **Intelligent payment infrastructure for modern businesses.**
- UK-headquartered, merchant-first payment orchestration platform. Its real-world product analogue would connect merchants to external payment service providers while exposing a unified API, merchant reporting and risk controls.
- Founded in the fictional backstory in 2022; scaled from a modular application into EKS-based services. 12 engineering staff, one CTO, small platform function, payment-domain developers, and an emerging ML function.
- Fictional 2026 customer story: ~110 merchants, ~160,000 payment attempts per month, a mix of recurring and ecommerce use cases. These are **narrative figures only**. The local prototype operates on a handful of deterministic synthetic records.
- Illustrative AWS spend: **$18,000/month** across nonprod and production (modelled, not observed). Cost episode must replace estimates with actual sandbox data or clearly labelled modelling.

## Product line

1. **Kivaryx Gateway** — merchant API to initiate synthetic payments, view status and follow idempotent request semantics.
2. **Kivaryx Console** — merchant workspace showing transaction history, approval rates, volumes, risk disposition and test-payment creation.
3. **Kivaryx Risk** — low-latency fraud scoring. Original fictional baseline is a CPU-friendly packaged model; local prototype uses deterministic **rules as a scoring simulator**, clearly differentiated from trained ML.
4. **Kivaryx Ops** — internal read-only transaction diagnostics, audit/event explorer, exception review and incident insight. Future GenAI assistant under human oversight.

## Operating narrative — reasonable choices, credible tensions

- First production migration to EKS was motivated by heterogeneous services and the engineering team's familiar Kubernetes operating model, not because EKS is universally superior.
- Payments use idempotency keys, service-level retries and a mock external processor. A transaction event stream supports asynchronous downstream operations. Risk scoring is synchronous on the payment path with bounded latency requirement.
- Initial AWS architecture uses EKS managed node groups, AWS VPC CNI, kube-proxy, ALB, RDS PostgreSQL, SQS, S3, Secrets Manager, IAM, ECR and CloudWatch. No default assumption of Cilium, Bedrock, Service Mesh, EKS Auto Mode or GPU use.
- Existing metrics/logging are useful but may not cover customer-level outcomes and distributed traces. Actual gaps must be demonstrated or called hypotheses.
- Network segmentation may be uneven across namespaces because the team developed application policies independently. This is a *hypothesis*, not an established finding before evidence exists.
- Internal AI assistant is an early, read-only evaluation using approved, synthetic diagnostic data. No AI controls payment authorisation or can issue refunds/transfers.
- The company is not a cartoonishly broken platform: many decisions were rational at the time. Some original services should remain unchanged after review.

## Scenarios and editorial truthfulness

All adverse conditions used in filming must be declared as **injected test scenarios** unless organically reproduced from the canonical baseline. No fictional figures masquerading as benchmark results; every report should distinguish illustrative baseline, direct observation, validation, and untested recommendation.

## Business questions

- Can transaction processing remain correct during retries, timeouts and recovery?
- Can the platform explain which transaction failed and why?
- Are the payment and risk workloads appropriately isolated?
- Do new cloud services reduce *total* operational burden enough to justify cost, risk and migration?
- Can the fraud model be updated without hidden accuracy, latency or rollback regressions?
- Is GenAI appropriate for approved troubleshooting tasks, and how is tool access constrained?
- What investments offer the most risk reduction or value per engineering week?
