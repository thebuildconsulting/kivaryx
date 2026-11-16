# How THE BUILD Teaches While Consulting

## The series is both consulting demonstration and technical education

Avoid two extremes: (a) jumping directly from a diagnosis to installing an unfamiliar tool; (b) turning a client narrative into a generic tutorial with no decision or outcome.

For every material technology introduction or configuration change, viewers should be able to answer:

1. **Problem:** What observable condition or risk creates the need?
2. **Principle:** What networking, security, distributed-systems, cloud or AI/ML mechanism underlies it?
3. **Architecture:** What are the components, interfaces, dependencies, control plane and dataplane (where applicable)?
4. **Existing setup:** What exactly is deployed, and what are its limitations? What evidence supports that assessment?
5. **Alternatives:** Could a configuration fix, native managed feature or different technology solve the problem? Why not choose them?
6. **Implementation:** What changed and how was it tested safely and reversibly?
7. **Outcome:** What measurement changed, and what remains an estimate, risk or unknown?
8. **Operational ownership:** Who will maintain the solution, patch it, pay for it and respond when it fails?

## Example — Introducing Cilium

- First demonstrate unexpected access to a payment-facing workload and identify the actual existing CNI and policy features, without claiming that adopting Cilium is required.
- Teach Pod IPs, Services, NetworkPolicy, identity and how kernels enforce rules.
- Explain eBPF in appropriate depth: programs, hooks, maps, observability, policy and Service dataplane differences. Show what Cilium controls and what Kubernetes controls.
- Compare existing CNI capabilities plus standard NetworkPolicy, Cilium as CNI or layered policy engine where compatible, and changes outside the cluster such as cloud security groups.
- Choose a defensible option based on Kivaryx's needs and operational burden; only deploy Cilium if evidence favours it.
- Use Hubble to verify flows where applicable, and separately verify L7 visibility and policy instrumentation claims.
- Explain rollback, cluster migration implications and residual cloud-level controls.

## Example — Fraud model inference

- Explain the real-time fraud-scoring request and its latency budget.
- Teach features, model versions, batch training vs online inference, decision threshold and drift, without overstating the capability of a toy model.
- Compare CPU model server, managed inference and accelerated GPU service; choose based on traffic, inference cost and capability.
- Demonstrate model version rollout, inference SLI, simulated bad model output and rollback.
- Separate test performance from real-world fraud accuracy, fairness and compliance claims.

## Suggested long-form structure (adaptable)

| Chapter | Typical time for a 30–35 minute video |
|---|---|
| Business consequence, scope and simulation disclosure | 0–3 min |
| Current architecture and hypothesis | 3–7 min |
| Technical foundation / how it works | 7–14 min |
| Inspect evidence and compare approaches | 14–20 min |
| Configure/implement the option | 20–29 min |
| Re-test, limitations, business verdict | 29–35 min |

This is guidance, not a mandatory formula. Longer episodes must justify the additional depth and use chapters; focused topics can be shorter.

## Quality gate

No episode is ready unless (a) the creator can explain the technology without depending on the demo transcript, (b) the code and tests are repeatable, (c) the claim is supported by labelled evidence, (d) the viewer understands the business trade-off, and (e) the runtime serves the learning rather than a time target.
