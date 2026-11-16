# Technology education and selection rule

Every change introduced in the show must be justified by an established client question or measured lab observation. The video should explain essential concepts, current architecture, tool role, why existing implementation may be insufficient, candidate alternatives, adoption/operating burden, risks, cost, and validation outcomes.

Potential technologies **NOT APPROVED TO IMPLEMENT YET**:
- Cilium, eBPF, Hubble vs existing EKS/VPC CNI and policy options
- OpenTelemetry, Prometheus/Grafana, CloudWatch improvements
- Amazon Bedrock / AgentCore, RAG vs non-GenAI runbooks and simpler approaches
- SageMaker AI, model serving vs existing CPU service
- Karpenter, EKS Auto Mode vs existing managed node groups
- Gateway API, Envoy, progressive release controls
- Optional service mesh/mTLS only if needs justify it

For a new managed service, inspect current official AWS/provider docs, region support, permissions, pricing, availability and restrictions **at episode production time**. New does not mean superior. Document why the current design might remain best.
