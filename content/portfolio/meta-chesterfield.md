---
title: "Project Chesterfield: GenAI-Powered CI/CD at Meta Reality Labs"
date: 2024-12-01T00:00:00.000+00:00
thumbnail: images/portfolio/meta-chesterfield.png
service: CI/CD Modernization, GenAI Integration
client: Meta Reality Labs (Quest, Ray-Ban Stories)
shortDescription: >
  Led CI/CD modernization for Quest and Ray-Ban hardware lines using GenAI-powered migration tooling — 95% manual-effort reduction, $386K/year savings.
challenge: >
  Reality Labs CI/CD carried 50+ legacy build configurations that needed manual maintenance every release. Each hardware line — Quest, Ray-Ban Stories — had its own dialect of the build system, and keeping them in sync burned roughly twenty hours of engineer time per team per week. The toil scaled with hardware launches, not down.
solution: >
  A GenAI-powered migration tool that auto-converted legacy build specs into the modern unified format, with human-in-the-loop validation on every conversion so engineers stayed in the loop on edge cases instead of rubber-stamping output. The companion piece was UBM, a metadata service for build metadata and deduplication that let the unified pipeline scale without redundant work.

---
The migration tool removed the bulk of the manual conversion work — 95% manual-effort reduction across the affected build configurations — and the savings landed at roughly $386K/year in recovered engineer time. UBM, the metadata service that paired with it, handled 100K+ build operations per month, cut failures by 99%, and reclaimed roughly 22K compute-hours per month.

The harder part of the project was the human side. Engineers do not adopt GenAI tooling that produces output they cannot audit, especially in a domain where a bad build config breaks a hardware launch. The human-in-the-loop validation step was deliberately designed so engineers reviewed the diff, not the prompt — they saw exactly what the tool was about to change and could accept, reject, or edit per file. That shape of UX made the rollout sticky in a way that prior automation attempts had not been.

Six engineers were mentored through the program; three were promoted to Staff inside twelve months. The mentorship lane mattered as much as the tooling — the migration was a vehicle to grow people, not just a cost-saving project.
