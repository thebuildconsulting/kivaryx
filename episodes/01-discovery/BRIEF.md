# Episode 01 — A Fintech's Kubernetes and AI Stack: What Would I Audit First?

## Business hook
Kivaryx's fictional CTO wants an independent health review before funding additional cloud and AI infrastructure. The product currently operates, so avoid drama: start with discovery and produce actionable, prioritised hypotheses.

## Content learning contract
Audience should understand what an infrastructure consultant asks, how to map a production system, Kubernetes vs managed cloud responsibilities, control plane vs dataplane, service/dependency boundaries, evidence confidence and why initial assumptions cannot be called confirmed findings.

## Demo story
- Open Kivaryx public website and merchant console; generate a **synthetic** payment; observe status, risk score and trace/request ID.
- Open Ops console, correlate the payment's audit event timeline.
- Draw the fictional original AWS estate and distinguish it from what runs locally. Disclose single-process v3 prototype before Codex reconstructs microservices.
- Inspect the first real kind deployment (once Codex has built it): workloads, namespaces, Services, EndpointSlices, configs, resource footprints and selected telemetry.
- Generate initial evidence IDs, hypotheses and follow-up investigations without promising unsupported savings or risks.

## Client report
`reports/01-initial-platform-review.md` using `TEMPLATES/CLIENT_REPORT.md`. Include an initial inventory, business goals, architectural sketch, assumptions, verified lab observations, unknowns, candidate risk register and prioritisation.

## Completion gate
- Real web dashboard and API path exercised with mock data.
- Two or more actual technical observations tied to saved evidence.
- Clearly differentiate scenario assumptions and lab measurement.
- End episode with client-ready Episode 01 report and next-investigation decisions.
