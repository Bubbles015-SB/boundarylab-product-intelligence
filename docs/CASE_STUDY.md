# BoundaryLab: From conditional acceptance to product decisions

**Portfolio case study | Research-inspired product analytics and experimentation**  
Prepared for Salonee Shrigandhamurthy's portfolio as an AI-assisted prototype. Salonee should validate the interpretation against her primary dissertation and personally review, test and explain any outputs before presenting this as her own completed work.

## The problem

Rapid-commerce product teams often ask whether a customer would adopt fast delivery. A binary adoption measure can mask restrictions: the same customer might accept delivery for some products, in certain places, and only when the treatment of delivery couriers satisfies their standards.

Salonee's supplied CV and application materials **report** eleven interviews undertaken for her MSc dissertation. They describe a central insight: adoption is conditional, with individual boundaries around product category, context (home versus work), and courier treatment. A supplied CV also reports a survey, six themes developed in NVivo with Braun and Clarke thematic analysis, and geography as a consideration. The original dissertation, coding tree, transcripts, survey sample and numerical frequencies have **not** been provided to this project.

## Reframed research question

**Under what observable conditions should an offer be shown, and which of those conditions are hard vetoes rather than negotiable preferences?**

The operational question is not answered by the original qualitative finding alone. Translating it into a product policy requires new assumptions, user testing, operational evidence and responsible safeguarding.

## Design response

BoundaryLab demonstrates six steps:

1. Record reported qualitative insights in an evidence ledger, without adding fictional quotes or frequency estimates.
2. Draft a requirement/hypothesis/metric chain so each decision is traceable to a research motivation.
3. Construct **synthetic**, non-identifiable personas with fictional preferences and non-negotiable thresholds.
4. Evaluate scenarios through ordered hard eligibility gates, followed by a demonstrative soft-interest score.
5. Add capacity and contribution scenarios with adjustable unit economics; seek non-dominated policy/price/speed choices under minimum worker-protection assumptions.
6. Write a preregistration-style experiment plan including randomised assignment, the primary metric, guardrails and an approximate power calculation.

## Model implementation

The front-end is plain HTML, CSS and JavaScript without network dependencies. It includes seven workspaces: Overview, Condition Explorer, Policy Lab, Decision Frontier, Experiment Planner, Research Traceability and Methods. Synthetic profiles are generated deterministically by a Python script. The business logic is in `src/engine.mjs` and is tested separately from the UI.

### What outcomes mean

**Modelled qualified interest** is the mean of individual illustrative propensities after hard gates; it is **not** an empirical conversion rate or calibrated demand forecast.

**Capacity-constrained orders** are hypothetical monthly intents multiplied by modelled interest, limited by hypothetical service capacity.

**Modelled contribution** is a scenario ledger: (basket × assumed gross margin + delivery fee − invented fulfilment costs) × hypothetical fulfilled orders − fixed cost assumption. It is **not** observed revenue, profit, P&L or unit economics from a real company.

**Courier safeguard tier** is an invented proxy for demonstrating ethical hard vetoes and hypothetical cost trade-offs. It is not labour law compliance, actual courier protections or a certification.

## Decisions a product team could investigate next

- Is a contextual fee-and-ETA disclosure valuable, or does it add avoidable friction?
- What happens if consumers reject an offer for ethical reasons even when the delivery time and price are favourable?
- Do restrictions vary by category and delivery setting in a new, properly sampled study?
- How does a capacity-constrained operation change which offers should be tested first?
- Can exposure to transparent, independently verified worker-protection policies affect qualified intent without harming couriers?

None of these answers is established by the prototype. A rigorous programme would combine consented qualitative research, observed usage data and pre-registered field experiments.

## Portfolio relevance

This project can support discussions for **product analyst, junior product manager, business analyst, UX researcher, operations analyst and customer insights** roles. Its differentiated value is the chain from research framing to requirements, measurement, sensitivity analysis and acknowledged uncertainty—not the headline modelled numbers.

## Limitations

- Primary dissertation not supplied; no respondent-level data, original quotations or validated segment labels.
- No observed behaviour, real conversion, commercial cost, delivery performance or emissions data.
- Synthetic 1,200-person panel does not represent any population or provide generalisable inference.
- Assumed parameters are manually chosen, not estimated, cross-validated or causally identified.
- The ordered first-failed-condition reasons are a design convention; not causal attribution.
- Optimisation is exhaustive over a small discrete scenario grid, not a production optimisation engine.
- Power formula is approximate for independent two-arm Bernoulli outcomes, α=.05, 80% power.

## Ethical data handling

Raw interviews must **not** be uploaded to a public repository without consent and appropriate approval, even if names are removed. Research participants and dissertation content should remain within their original ethical permissions. This project contains no such records.
