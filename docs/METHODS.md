# Technical methods and honest interpretation

## Dataset

The deterministic script `scripts/make_panel.py` creates 1,200 fictional profiles with the random seed `20261020`. Each has labelled attributes: allowed categories and contexts, price/ETA/reliability thresholds, a courier-protection threshold and model sensitivity parameters. Four hypothetical archetypes are algorithmically generated; they are **not** learned from or intended to describe the original interview participants.

## Individual-level rule

Check in fixed order: category allowed → context allowed → courier threshold met → fee within limit → ETA within limit → reliability within limit. If any gate fails, assign zero illustrative interest and a single *first failed* reason. Qualifying profiles receive a bounded logistic soft score with hand-chosen coefficients.

The first-failed reason distribution is a **decision debugging waterfall**; it is not an interpretable causal decomposition. An alternate gate order changes these reason totals.

## Aggregation

Modelled interest `A = (1/N) sum_i propensity_i`. Potential orders `D = monthly_intents * A`. Fulfilled orders `F = min(D, monthly_capacity)`.

`contribution_per_order = basket * gross_margin + delivery_fee - (courier_cost + operations_cost + speed_premium)`.

`net_modelled_contribution = F * contribution_per_order - monthly_fixed_cost`.

Parameters have no calibration against observed company data. Modelled order emissions are an additional manually-assumed proxy and have not been footprint-assessed.

## Optimisation

Enumerate 3 safeguard tiers × 6 ETAs × 7 fees = at most 126 offers. Exclude tiers that fall below the selected worker minimum; exclude offers below modelled acceptance requirements. Mark an option Pareto-efficient if no other **tested feasible** option has both greater interest and greater contribution, with one strict improvement. Label the top net-contribution result as a scenario candidate, not a recommended market policy.

## A/B-test sample-size planning

Two-sided z-normal approximation for equal sample sizes and independent Bernoulli outcomes:

`n ≈ [(z_{1−α/2} sqrt(2pbar(1−pbar)) + z_{1−β} sqrt(p0(1−p0)+p1(1−p1))) / (p1−p0)]²`.

Here α=.05, power=.8. The UI lets the user choose `p0` and *absolute* detectable percentage-point lift, p1=p0+lift.

## Reproducibility

- Source logic: `src/engine.mjs` (no dependencies).
- Front-end: `src/app.mjs`, `index.html` and `assets/styles.css`.
- Bundler: `scripts/bundle.py` generates a single HTML file with embedded synthetic data.
- Tests: `node --test tests/*.test.mjs` and `python -m pytest tests/test_data.py`.
- Data regeneration: `python scripts/make_panel.py`.
- Data integrity: `python scripts/audit_dataset.py`.

## AI contribution note

An AI assistant initially generated this implementation from reported dissertation summaries. Its presence in a portfolio does not by itself demonstrate that the named candidate independently wrote the code. The candidate should verify the research mapping, review and improve the implementation, test the findings and be precise about personal contributions.
