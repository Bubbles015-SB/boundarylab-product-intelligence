# BoundaryLab — Conditional Adoption Intelligence

> **Not will they use it. Under what conditions?**

A research-inspired, testable **product discovery and operations decision laboratory** based on the conditional-acceptance insight reported in Salonee Shrigandhamurthy's MSc dissertation application materials. Built as a standalone interactive web app with reproducible synthetic data, rule-based eligibility, scenario economics, constrained optimisation, an A/B-test planner and research-to-requirement traceability.

**Important:** The original dissertation and anonymised interview transcripts were not provided. The project contains **zero real respondents**; all 1,200 profiles, segmentation patterns, numerical preference thresholds and commercial outcomes are **synthetic and illustrative**. Do not present its conversion percentages as original research findings.

## Run it

**Zero setup:** Open `BoundaryLab_Standalone.html` from the distributed package in Chrome or Edge. It contains the entire app, including styling and synthetic data.

**GitHub Pages / development:** `index.html` loads `assets/styles.css`, `src/engine.mjs`, `src/app.mjs` and `src/data.mjs`. To serve locally:

```bash
python3 -m http.server 8000
```

Visit `http://localhost:8000` in a browser. Requires no Node packages, database, paid APIs or logins.

## Workspaces

| Workspace | Capability | What it demonstrates |
|---|---|---|
| Project overview | Question reframing + scenario KPIs | Research synthesis and caveated decision reporting |
| Conditional adoption | First-failed-rule waterfall and fictional segment explorer | Segmentation limits, guardrails and heterogeneous preferences |
| Offer & policy lab | Fee/ETA/context/category/courier settings | Product economics and scenario sensitivity |
| Decision frontier | Enumerate up to 126 candidate offers | Constrained multi-objective decision analysis |
| Experiment planner | Approximate A/B-test sample size and instrumentation | Hypothesis validation and causal inference discipline |
| Evidence to roadmap | Reported evidence → hypotheses → metrics | Requirements traceability without fabricating qualitative evidence |
| Methods & limitations | Provenance, limitations, ethics | Transparent, reproducible decision science |

## Test and regenerate

```bash
node --test tests/*.test.mjs
python3 scripts/audit_dataset.py
python3 -m pytest -q tests/test_data.py
python3 scripts/make_panel.py
python3 scripts/bundle.py
```

No npm dependency installation is required. The optional Python test suite needs `pytest`.

## Ethical source discipline

- **Reported, not independently verified here:** 11 qualitative interviews; conditional acceptance by category, context and ethical treatment; six identified themes; NVivo/Braun and Clarke methodology. Source: user's provided CV and application-writing materials, not the dissertation itself.
- **Proposed:** requirement backlog, operational guardrails and A/B-test plan.
- **Synthetic:** fictional personas, segmentation patterns, pricing thresholds, commercial economics, demand/interest rates and optimised configurations.

A customer-research case study is not improved by inventing interview quotes, participant percentages, demographic statistics or false experimental results. BoundaryLab intentionally omits all of them.

## Documentation

- [`docs/CASE_STUDY.md`](docs/CASE_STUDY.md) — story and product case study.
- [`docs/PRODUCT_REQUIREMENTS.md`](docs/PRODUCT_REQUIREMENTS.md) — proposed PRD and acceptance criteria.
- [`docs/EXPERIMENT_PLAN.md`](docs/EXPERIMENT_PLAN.md) — pre-registered experiment template.
- [`docs/METHODS.md`](docs/METHODS.md) — exact modelling rules and assumptions.
- [`docs/INTERVIEW_WALKTHROUGH.md`](docs/INTERVIEW_WALKTHROUGH.md) — candidate demo and interview defence.

## Reproducibility and CI

Code is split into a pure JS engine, simple frontend, a seeded Python synthetic data generator and 20 Node.js tests plus Python data checks. `.github/workflows/check.yml` runs the tests on every proposed change.

## Attribution and appropriate portfolio use

**Prepared as an AI-assisted implementation for Salonee's portfolio.** Publishing it does not demonstrate that Salonee independently authored the source. Before claiming personal technical proficiency, she should inspect, rerun, improve and be able to defend the analysis, with a clear statement of her specific contributions. Do not include participant-level dissertation data without appropriate explicit permissions.

No paid services or data-sharing permissions are required for the standalone demonstration. This repo is designed for GitHub Pages, but is **not yet published to any GitHub account**.
