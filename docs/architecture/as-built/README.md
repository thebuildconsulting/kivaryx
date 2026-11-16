# As-built local state — factual only

Milestone 0 on 16 November 2026 ran the unchanged `apps/prototype/` source on macOS 14.5 arm64 with Python 3.12.11: one loopback-only Uvicorn/FastAPI process, SQLite and deterministic risk rules. Five existing tests passed. No container, CentOS VM, kind cluster, independent service or AWS resource was deployed by this review. The local review server was stopped after evidence capture.

See [local-prototype.mmd](local-prototype.mmd), [payment-sequence.mmd](payment-sequence.mmd), [inventory and fidelity matrix](../INVENTORY_M0.md), and [Milestone 0 review](../../../MILESTONE_0_REVIEW.md). Curated outputs are in `docs/evidence/milestone-0/`; raw browser captures/runtime logs and generated DB are ignored. Source hashes, rather than an invented SHA, identify the uncommitted prototype.

The default three synthetic merchants and 42 seeded transactions are not the fictional business's merchant/traffic volume. No trained ML, real PSP, durable queue, tenant authorization or distributed telemetry was verified. Editable diagrams were manually reviewed; Mermaid rendering/SVG export was unavailable.
