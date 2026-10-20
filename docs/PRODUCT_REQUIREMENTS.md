# Product requirements brief — conditional delivery offers

**Document type:** Hypothetical product discovery brief, not a launched product specification.

## Product concept

Offer customers rapid delivery **only when** the product and operational circumstances match their stated conditions. Make important terms understandable *before* checkout, with special attention to treatment of couriers.

## Actors
- Customer considering a particular delivery offer in a specific context.
- Delivery operations team managing capacity and achievable ETAs.
- Trust / worker-standards team able to verify protections and response processes.
- Product analyst responsible for data integrity, experiment design and decision traceability.

## Priority requirements

| Requirement | Evidence motivation | Proposed acceptance criteria | Observability |
|---|---|---|---|
| Category-specific eligibility | E02 | Category check runs before fee/ETA scoring | `eligibility_checked` with category code |
| Context-aware offer | E03 | Home or work contexts selectable; disallowed setting blocks offer | context field, no address in analytics event |
| Worker protection transparency | E04 | Published, verified standards visible before purchase; minimum safeguards mandatory | `courier_policy_seen`, independent compliance review |
| Reliable offer disclosure | E01 | Fee, ETA and availability displayed before checkout | impression and error events |
| Capacity and service-zone check | E05 | No promise if route/zone/service capacity unavailable | aggregate capacity and promise-kept events |
| Research and metric traceability | E01–E06 | Every feature hypothesis maps to a metric and guardrail | privacy-conscious, documented event schema |

## Safety and privacy constraints

- Worker treatment protections cannot be weakened to increase conversion without a documented independent ethics/compliance review.
- No raw interview transcripts, health information, exact addresses or worker identities stored in product analytics events.
- Do not infer protected personal attributes from locations or purchasing behaviour.
- Service availability and worker safeguards must be verifiable in reality; the prototype's numerical score is not a substitute.

## Non-goals for this project

It is not a delivery service, pricing algorithm for consumers, real-time operations system, real-world predictive model, employment-law compliance instrument or a claim about UK demand.

## Validation roadmap

1. Verify source dissertation and reproduce the actual themes with participant confidentiality protected.
2. Conduct targeted follow-up interviews with consent to validate product eligibility rules.
3. Obtain an operations feasibility review, real unit-cost estimates and worker-safeguard verification.
4. Pilot event collection with privacy review and metrics definitions.
5. Preregister and conduct an A/B test; analyse outcomes by predeclared strata and guardrails.
6. Iterate only where benefits withstand sensitivity checks and stakeholder scrutiny.
