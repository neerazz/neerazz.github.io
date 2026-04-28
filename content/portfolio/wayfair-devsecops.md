---
title: "Wayfair DevSecOps Platform: Policy-as-Code at 20K Apps"
date: 2023-06-01T00:00:00.000+00:00
thumbnail: images/portfolio/wayfair-devsecops.png
service: DevSecOps, Policy-as-Code, Identity
client: Wayfair (~20K applications across the platform)
shortDescription: DevSecOps platform serving 50M+ security checks/month with a 3%
  false-positive rate; selected as 1 of 3 architects from 50+ to define Wayfair's
  security roadmap.
challenge: 20K+ applications across the engineering org, no consistent security
  posture across teams, and a legacy scanner stack pushing a >25% false-positive rate.
  The combination produced exactly the failure mode you would expect — alert fatigue,
  ignored findings, and security teams that had stopped being trusted by application
  teams. The platform needed both new tooling and a new operating model.
solution: A Kubernetes-native policy-as-code engine built on OPA and Kyverno, unified
  OAuth 2.0 with mTLS for service-to-service identity, and centralized SBOM generation.
  Architected as a self-service platform: teams enrolled, got coverage automatically,
  and consumed security as a paved-road default rather than a tax imposed on them.

---
Throughput at steady state landed at 50M+ security checks per month with the false-positive rate driven down to 3% — the alert-fatigue dynamic that had broken trust with application teams reversed once the noise dropped below the threshold where engineers stop reading alerts. The identity platform sits at 125M+ API calls per week with 99.97% uptime, which is the load profile that made teams willing to depend on it for production paths.

The architecture choice that made the rest possible was self-service enrollment. Centralized security teams cannot hand-hold 20K applications, and any model that requires them to do so collapses under its own weight. Policy-as-code with OPA + Kyverno meant security policies were code that lived next to application code, reviewed in pull requests like anything else. Unified OAuth + mTLS gave services one identity story instead of a per-team improvisation. Centralized SBOM gave incident response a single place to look when a CVE dropped.

Selected as one of three architects from a pool of 50+ to define the Wayfair security roadmap. Mentored 20+ engineers over the program; eight were promoted to senior or staff during that window.
