# BoundaryLab — Conditional Adoption Intelligence

**Consumer research · product analytics · operational decision modelling · experimentation**

> **The question is not simply whether a customer will adopt a service, but under what conditions.**

BoundaryLab examines the conditions that shape consumer acceptance of quick-commerce and rapid-delivery services. The system connects qualitative research insights with an interactive rules engine, product-offer evaluation, operational economics and experimental design.

Its research framing draws on an MSc Management study of quick-commerce adoption, including 11 qualitative interviews. The central insight is that acceptance varies by product category, purchasing context and expectations around courier treatment. BoundaryLab translates these dimensions into explicit decision rules that can be explored, tested and refined.

![BoundaryLab overview](media/overview.png)

## Functional modules

| Module | Purpose |
|---|---|
| **Research overview** | Connect the central adoption question to measurable product and operational decisions. |
| **Conditional adoption** | Trace category, context, service-policy, price and reliability requirements through an eligibility waterfall. |
| **Offer & policy lab** | Adjust fees, delivery windows, ordering situations, product categories and courier-protection settings. |
| **Decision frontier** | Compare up to 126 offer configurations under competing product and commercial objectives. |
| **Experiment planner** | Define A/B-test hypotheses, measurement plans, guardrails and approximate sample sizes. |
| **Evidence to roadmap** | Connect research insights to product requirements, testable hypotheses and decision criteria. |
| **Methods** | Explain eligibility logic, weighting, calculations and reproducibility. |

![Offer and policy analysis](media/policy.png)

## Analytical workflow

### Conditional eligibility

The evaluation begins with explicit category, purchasing-context and service-policy conditions. Offers must satisfy those requirements before price, delivery time and reliability are evaluated.

### Offer evaluation

For eligible cases, the engine computes a preference score using configurable fee, timing, service-quality and operational inputs. The resulting metrics can be compared across multiple configurations.

### Operational decision analysis

The decision engine evaluates candidate service offers, compares their estimated commercial contribution and identifies non-dominated options. This produces a structured basis for comparing policy choices.

### Experiment design

The experiment planner connects a proposed product change to its hypothesis, primary measurement, guardrail metrics and indicative sample requirements. It is designed for planning future validation work.

### Research traceability

An evidence-to-roadmap layer ties qualitative adoption themes to requirements, analytical rules and proposed product decisions.

## Data and research basis

The research themes originate from the reported qualitative study. The application’s **1,200 computational profiles are generated reproducibly by `scripts/make_panel.py`** as inputs to its analytical engine; they are **not individual interview records**. Quantitative outputs are calculated by the model and are not presented as observed customer-conversion measurements.

No identifying interview transcripts or participant-level research records are stored in this repository.

## Implementation

- **Frontend:** HTML, CSS and JavaScript ES modules.
- **Decision engine:** rule-based eligibility and preference calculations.
- **Data preparation:** seeded Python data-generation workflow.
- **Analytics:** multi-objective comparison, commercial calculations and sample-size planning.
- **Verification:** 20 JavaScript tests, Python data checks and browser interaction tests.
- **Delivery:** local web application with no paid dependencies or external API keys.

```text
Research insights
       │
       ▼
Research-to-rule mapping
       │
       ▼
Reproducible computational panel
       │
       ▼
Eligibility and preference engine
       │
       ├──────► Offer and policy analysis
       ├──────► Decision frontier
       └──────► Experiment planning
                       │
                       ▼
              Evidence and reporting
```

## Running the application

Run a local web server from the repository root:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` in a browser. The interactive application uses native JavaScript modules and does not require a database or a Node package installation.

### Regenerating data and bundle

```bash
python3 scripts/make_panel.py
python3 scripts/bundle.py
```

### Tests and quality checks

```bash
node --test tests/*.test.mjs
python3 scripts/audit_dataset.py
python3 -m pytest -q tests/test_data.py
```

The optional Python test suite uses `pytest`. GitHub Actions runs the repository's configured automated checks.

## Documentation

- [Research and product case study](docs/CASE_STUDY.md)
- [Product requirements](docs/PRODUCT_REQUIREMENTS.md)
- [Experiment plan](docs/EXPERIMENT_PLAN.md)
- [Technical methods](docs/METHODS.md)
