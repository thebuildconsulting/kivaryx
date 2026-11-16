# First episode evidence and hypothesis register

| ID | Hypothesis / validation question | Evidence method | Current status | Impact if confirmed |
|---|---|---|---|---|
| KIV-01 | Which components handle a synthetic payment? | Trace IDs, API and Pod mapping | to validate in local lab | misdiagnosis during incidents |
| KIV-02 | Are all dependencies explicit and owned? | service map, deployment manifests, queue and DB relationships | fictional architecture only | unknown failure domains |
| KIV-03 | Is payment idempotency retained during retries? | duplicate and conflicting request tests | prototype tests exist; verify in separated services | duplicate processing risk |
| KIV-04 | Can merchant-specific latency be established? | timestamped end-to-end checks + telemetry | not yet verified | customer impact hidden |
| KIV-05 | What east-west reachability is allowed? | policy inventory + safe pod connectivity tests | not yet verified | lateral movement potential |
| KIV-06 | How quickly can a fault be understood and recovered? | injected degraded dependency + observation | not yet verified | incident response delay |
| KIV-07 | Is cost allocated to workloads meaningfully? | illustrative model; AWS cost evidence only if separately authorised | modelled only | poor investment choices |
| KIV-08 | Is ML fraud inference versioned, monitored and safely reversible? | synthetic scorer metadata, version rollbacks | no trained ML model yet | risk decision inconsistency |
| KIV-09 | Could AI operations tools exceed read-only permission? | synthetic tool permission and network deny tests | not yet verified | unintended changes or exposure |

**Do not report a severity as a confirmed finding until reproducible evidence supports it.**
