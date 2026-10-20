# Experiment protocol (proposed, not conducted)

**Question:** Does early, context-sensitive eligibility disclosure improve qualified completed checkout compared with a generic offer presentation?

**Population:** Consented, eligible users in a real delivery pilot with a fully reviewed employment and data-privacy framework. Do not assume the synthetic personas describe this population.

**Randomisation:** Session-stable assignment to one of two variants. Check for repeated-session contamination and household-level interference; if material, randomise at account/household level and adjust sample-size assumptions for clustering.

**Control:** Normal fee and ETA disclosure at checkout.  
**Treatment:** Category + home/work eligibility, fee, ETA and verifiable courier safeguards disclosed before checkout.

**Primary metric:** Completed checkout / randomised eligible sessions, predeclared window. Both variants must fulfil at least the *same actual* worker-protection standards; only the information and timing vary.

**Secondary metrics:** checkout starts, complaints, cancellations, observed promise-kept rates, eligibility failures by class. 

**Guardrails:** courier incidents, complaint rate, actual pay compliance, delivery lateness, personal-data minimisation. Predefine stop rules before any trial.

**Power planning:** Normal approximation to two independent proportions with α=.05 and power=.8. Set p0 and absolute MDE before observing experiment outcomes. Adjust for multiplicity, clustering, attrition and unequal allocation as needed.

**Analysis:** intention-to-treat effect, uncertainty interval, predeclared robustness checks, guardrail review, and limitations. Do not draw causal claims from the synthetic simulator.

**Ethics:** never run a live experiment that lowers real courier safety or legal protections in any arm.
