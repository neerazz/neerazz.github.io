---
title: "EmbedGuard: Cross-Layer Defense for RAG Embedding Attacks"
date: 2026-02-05T00:00:00.000+00:00
thumbnail: images/portfolio/embedguard.png
service: AI Safety Research, RAG Security
client: Self-funded research
shortDescription: >
  Cross-layer detection and provenance attestation for adversarial embedding attacks in RAG systems.
challenge: >
  Production RAG systems are vulnerable to adversarial embeddings — poisoned vectors that mimic legitimate ones closely enough to slip past similarity filters. Existing defenses are either too slow for production traffic or miss optimization-based attacks that craft embeddings specifically to evade single-layer checks.
solution: >
  A cross-layer detector combining embedding-space anomaly scoring with provenance attestation, so attacks have to defeat both the geometric signal and the chain-of-custody signal at the same time. Released with Docker-reproducible benchmarks and a CC-BY 4.0 license so other teams can replicate and extend the eval.

---
Adversarial embeddings are easy to overlook because they look right under cosine similarity. The poisoned vectors live close enough to legitimate ones that retrieval still returns them, but the content they carry has been rewritten to steer downstream generation. Single-layer defenses — anomaly scoring on embeddings alone, or provenance checks alone — get bypassed by attackers who know the layer they have to defeat.

EmbedGuard combines both. The detector scores embedding-space geometry for anomalies and verifies provenance attestation on every candidate vector. An attack has to defeat the geometric layer and forge the provenance signal in the same shot, which raises the cost of a successful attack significantly.

On a 500K-embedding production-scale evaluation, the detector caught 94.7% of optimization-based attacks at a mean latency overhead of 51 ms. That latency budget is small enough to stay inside typical RAG response targets, which was the constraint that made earlier defenses unusable in production.

Paper: [DOI 10.22399/ijcesen.4869](https://doi.org/10.22399/ijcesen.4869). Code and Docker benchmarks: [github.com/neerazz/embedguard](https://github.com/neerazz/embedguard).
