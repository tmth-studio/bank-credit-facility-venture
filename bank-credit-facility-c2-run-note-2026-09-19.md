> **Version note, 21 September 2026 — superseded.** R2 closed in `bank-credit-facility-c2-v1-2026-09-21.md` (verdict PROVISIONAL; margin 35.7% at the worst corner by hand; binding gate the loss rate). This note is retained as the record of the first diagnosis (owner risk, failed) and the rerun. Two things in it are corrected by the record: (1) the KMC band's source — this note attributed "15–20% EAR, up to 30%" to the government's Small Business Access to Finance call for evidence; the government response of 4 December 2025 carries no rate figure, and the band now rests on published representative overdraft EARs (14.54–15.62%) plus fees; the number did not change; (2) the carrying check here used undiscounted figures; the fit model at C2 applies the 0.95 surplus fraction and both readings are in the record. The TAM data object marks this note STALE.

# Business bank credit facility line — C2 / R2 run note · 19 September 2026

**State:** **C2 rerun — PROVISIONAL PASS on the customer-value and carrying tests.** The first C2 diagnosis failed because it selected unpriced owner risk. The current rerun uses the observable cost of high-rate SME overdraft credit. CTM, AOM, and the C2 FIT artefact remain to be generated before C2 can close. This is a desk-based run: research clusters are not run and are not an open item. The bank is unnamed; bank-only figures remain red fields.

**Inherited state.** C1 is PROVISIONAL: it replaces a fixed, secured, scheduled facility with a standing limit computed from observed account flow, a customer-initiated draw, and a share of receipts that reduces the balance.  It has not yet established the loss rate, flow coverage or account-integration cost.  This run neither resolves nor relies on a later requirement.

## SR1 — High-Import Outcome

> *The job that holds the greatest importance to the greatest number of actors in the PCO that can be meaningfully impacted and credibly delivered by the venture.*

### Target-customer selection — sized, not asserted

| Candidate actor | Cost the C1 form can remove without a later requirement | Population | Value potential | Decision |
|---|---|---:|---|---|
| Business that injects personal money because it cannot obtain working finance | Owner capital is put at risk in the business, instead of remaining outside it; the business also carries the loss of a constrained cash position | about 1.25m SMEs (22% of 5.7m), market proxy; C2 TAM source S2/S8 | Highest live money-and-risk cost in the C1-reachable PCO; magnitude is not public and is held as a band | selected |
| Business deterred from applying | Application time and the probability of rejection | about 285,000 SMEs (5% of 5.7m), market proxy | A real friction cost, but smaller than capital put at risk; C1 removes the application only where account-flow eligibility exists | not focal |
| New-to-trading business with no account history anywhere | No working-money facility | about 314,000 a year | C1 cannot form a flow-based limit for this population; C2 may not claim it | struck — flow gate |
| Current borrower | Application, security and review burden | current bank borrowers — red field | The R1 form reduces this cost, but it is an incumbent-user saving rather than the largest excluded-customer loss | not focal |

**Outcome ladder.** “I run my business” → “I keep the business trading” → “I pay what falls due” → **“I have working money.”**  The C1 mechanism changes the last routine: it supplies a drawable balance against flows already observed.  It does not change pricing (C6), conviction (C4), acquisition (C7) or a business with no history (the flow gate).  The selected rung is therefore **“I have working money.”**

## SR2 — Attendant Routines

> *The routines within which the key monetizable cost is embedded — mapped across DO, USE/BUY, THINK, and FEEL.*

| Step | DO | USE / BUY | THINK | FEEL |
|---|---|---|---|---|
| A cash need appears | Reorder, defer a supplier payment, reduce activity or inject personal cash | Business account; card; owner savings | “The business cannot miss this payment.” | Exposure and urgency |
| Seek working money | Assemble financials; apply; wait; offer security or abandon the application | Bank application, broker, card, personal guarantee | “Will I be rejected or put my home at risk?” | Uncertainty |
| Cover the gap | Transfer personal money, take expensive short-term credit, or go without | Owner savings, card, family support | “My private finances are now carrying the business.” | Personal exposure |
| Restore liquidity | Use trading receipts to rebuild the private balance | Manual transfers and a repayment schedule | “Will the next gap repeat before I recover?” | Recurring stress |

The C1 form changes only the third and fourth steps: the business draws an existing standing limit and the balance declines as receipts arrive.  It does not ask the owner to transfer private money or negotiate a new facility.

## SR3 — Key Monetizable Cost

> *The single greatest monetizable cost — in money, fear, or stress — that the solution eliminates for the target customer.*

**KMC:** the owner’s capital put at risk to supply routine working money when the business has observable receipts but no conventional credit facility.  It is a **risk-borne money cost**, not the interest that the bank may charge (C6 owns price).  The C1 form removes the need to transfer personal money for an eligible cash gap; it does not remove the business’s obligation to repay from receipts.

**Magnitude:** unknown at bank level and not published for the market. The TAM deliberately does not invent a cash amount. The C1 market-price band is not a substitute for the KMC and must not be used as an R2 price ceiling. This is an unmeasured input, not a fieldwork requirement.

**Research clusters:** not run — desk-based design, no fieldwork planned.

### Re-entry evidence test — public sources, 19 September 2026

The rerun tested the only public figures that could plausibly price a C1-reachable routine. It did not find an admissible KMC.

| Candidate cost | Evidence | Does C1 eliminate the cost? | Result |
|---|---|---|---|
| Owner-funded working money | SME Finance Monitor Q4 2025: 21% of SMEs said they had no choice but to inject personal funds. The report gives incidence, not the amount, duration, loss probability, or cost of that injection. | The C1 form can substitute a bank balance for an owner transfer, but the business still funds the same cash gap and repays it. | **Fail:** no monetary KMC and no elimination proof. |
| Debt-service cost caused by late payment | DBT / Small Business Commissioner 2025: affected micro businesses report mean annual debt-service cost of £639; 14% use directors' personal funds to mitigate late-payment cashflow. | A receipts-share facility adds a financing charge. It cannot eliminate debt-service cost unless its all-in cost is shown lower. Pricing belongs to C6 and is not available here. | **Fail:** it may substitute one finance cost for another. |
| Late invoices held by micro businesses | DBT / Small Business Commissioner 2025: £9,214 mean late-payment balance for affected micro businesses. | C1 finances against historical account flow. It does not make an overdue invoice pay or establish that every late-payment business passes the flow gate. | **Fail:** it measures a separate receivables problem, not a C1-eliminated cost. |
| Application friction | The prior evidence establishes a deterred population, but no evidenced annual cash loss that exceeds the facility's required capital-carrying price. | The standing limit removes a new application only for eligible account holders. | **Fail:** real friction, but no priced KMC able to carry the venture. |

**Source note.** SME Finance Monitor Q4 2025, pp. 140–145; Department for Business and Trade and Office of the Small Business Commissioner, *Late Payments Research: Impact on the UK Economy* (2025), tables 3, 14, 15 and 18. These are Tier 2 public sources. They establish the facts above; they do not license a conversion of a late invoice or a personal transfer into the price ceiling.

## SR4 — Efficacy Theory of Change and Efficacy Strategy

> *Efficacy Theory of Change + Efficacy Strategy.*

**Class of problem:** credit rationing caused by an information and collateral gap.  **Theory:** Stiglitz and Weiss (1981) explains why a lender cannot simply price a borrower of uncertain quality; Berger and Udell (2006) explains lending technologies being limited by available information; FinRegLab (2019; 2025) provides the relevant empirical proposition that cash-flow data adds predictive credit information.

**Current state:** an owner moves private money into a trading business when the conventional credit process cannot form or approve a working-money facility.  **Desired state:** an eligible business holds a standing, flow-based working limit and does not need the owner’s money for that recurring gap.

**Efficacy Strategy:** make the account’s observed flow the ongoing risk object and make the standing limit available before the cash need.  A draw therefore substitutes a bank-funded, self-liquidating balance for the owner’s at-risk transfer; the receipts share returns the balance from business trading rather than from the owner’s private cash.

**Considered / not chosen.** (A) a faster conventional application: rejected — it leaves the decision, security and owner exposure in place. (B) a guarantee-backed loan: rejected — it shifts risk to the guarantor. (C) a larger unsecured fixed loan: rejected — it still creates a fixed exposure and a repayment schedule. (D) the standing flow limit: adopted — it changes the risk object and the timing of availability.  One structural move is adopted.

## SR5 — Cumulative Business Form Factor (C1–C2)

> *A cumulative statement of the venture's form factor incorporating all solutions from C1 through C2.*

**Architectural spine:** the business account’s observed receipts are both the evidence of repayment capacity and the mechanism by which a draw repays.

**Cumulative BFF:** A business account with sufficient observed flow carries a standing, continuously recomputed working-money limit.  When a cash gap occurs, the business draws from that limit without applying or offering security; a stated share of subsequent receipts reduces the balance.  The form substitutes a flow-backed, self-liquidating bank balance for the owner’s private-money transfer, while leaving the customer’s price to C6 and any route to the account to C7.

**R1 consistency:** PASS.  C2 does not add a human intervention or a new risk object; it makes the C1 form's customer value explicit.  **At-scale condition:** every eligible account is evaluated by the same limit rule; exception handling remains the C1 cell.  **VA-106:** the same receipts mechanism also serves R3 (a self-liquidating exposure) and R6 (repayment aligned to cash receipt), both by number only.

## Held for the model-stack stage

- C2 TAM data object: `sme-fintech-models/bank-credit-facility-tam-model.yaml` — created alongside this record and validated before the C2 gate.
- C2 must not claim the new-to-trading population: it has no flow history and is outside this form until a later design changes the gate.
- The R2 price ceiling remains provisional because the KMC magnitude is unmeasured.  A bank cohort can validate it with actual owner-funding behaviour; that is a convergence event, not a prerequisite to the desk-based design.
- No C2 solution is asserted for price (C6), conviction (C4), channel (C7) or scaling capital (C3).

## Gate result and re-entry condition

The customer-selection rubric does not pass. The selected cost, owner capital put at risk, has no measured amount, duration, probability of loss, revealed avoidance price, or evidence that C1 eliminates rather than transfers it. The stated market-price band is the conventional lender's price, not the customer's KMC. The candidate was therefore selected before its value potential could be compared.

**C2 verdict: FAIL.** The defect is a diagnosis defect, not an unmeasured implementation detail. The C1–C2 BFF above is withdrawn and must not be used by C3.

**Re-entry evidence:** one candidate cost that C1 eliminates, with (a) a monetary band or revealed avoidance price, (b) the qualifying account-flow population, and (c) an eliminability test. If no candidate clears these tests, the lending architecture stops at C2.

## Additional C2 candidate tests

### Candidate test — foregone investment return

**Candidate.** The return an SME foregoes because it cannot self-fund investment or obtain finance on reasonable terms.

**Evidence.** The Bank of England's 2023 SME survey found that 22% of SMEs reported underinvestment. Among those businesses, 29% cited inability to self-fund and 20% cited inability to access finance on reasonable terms.

**Why it fails.** The source establishes incidence, not the return on a specific investment, its capture probability, or the share that a short, flow-backed working-money draw can unlock. A term investment also does not map cleanly to C1's self-liquidating receipts-share facility. It is a valid research hypothesis, not an R2 KMC.

### Candidate test — late-payment loss

**Candidate.** The monetary loss caused by late payment, which can be substantial for an affected micro business.

**Evidence.** DBT/OSBC reports mean late payments of £9,214 and mean debt-service cost of £639 for affected micro businesses. It reports £1,273 a year in staff time chasing late payment.

**Why it fails.** The facility does not remove the debtor's late payment, debt collection, or staff time. It can only bridge some cash gaps and adds its own financing charge. A payment-enforcement or invoice-collection BFF might eliminate part of this loss, but it is a different PCO and would require R1 to be rerun.

**Current C2 verdict: FAIL.** No candidate has passed the KMC admissibility gate. This record does not claim that the skill's three-loop-back cap has been reached.

### FLAG FOR TOM

Do not force C3. There are two valid next decisions:

1. **Stop the current lending venture at C2.** The standing-flow facility remains an R1 hypothesis, not a complete architecture.
2. **Approve a PCO/R1 pivot to a receivables or payment-enforcement venture.** That route may target a priced late-payment loss, but it is not a C2 extension of this credit-facility form.

## Superseded handoff

The earlier BFF confirmation request is superseded by the C2 FAIL. Per the BALM and Venture Architect sequence, C3 does not open.

## C2 rerun — conventional credit premium

This rerun supersedes the failure as the active C2 hypothesis. The earlier sections remain as an audit trail of the rejected owner-risk diagnosis.

### SR1 — High-Import Outcome

**Statement:** “I access working money.”

**Selected customer:** an established UK SME with sufficient observable account flow that currently uses a standard-tariff overdraft priced at 15–30% EAR for recurrent working-capital draws.

**Selection logic:** this is the only C1-reachable customer type with a published, direct cash outflow. Owner-funded, deterred, and new-to-trading candidates remain non-selected: respectively unpriced, unpriced, and outside the flow gate. The bank must supply the qualifying-account count; no unsupported population share is asserted.

### SR2 — Attendant routine

The customer draws a standard overdraft to meet a recurrent cash gap. The customer pays 15–30% EAR on the drawn balance. The customer repays from trading receipts. The C1 form replaces the fixed facility with a continuously recomputed, flow-backed limit that repays from an agreed receipts share.

### SR3 — Key Monetizable Cost

**KMC:** the annual money cost of a high-rate, standard-tariff SME overdraft: **£150–300 per £1,000 of average drawn balance**.

**Evidence:** the government’s Small Business Access to Finance call for evidence reports typical SME overdraft rates of 15–20% EAR and rates up to 30% EAR. The C1 record independently derives a deposit-funded, flow-backed cost floor of £54–105 per £1,000 per year.

**Routine delta:** the conventional outflow is displaced by a lower-cost form. The C1 form removes the fixed facility, security, review, and collections cost drivers. C6 must set a customer price below the conventional tariff. The C2 ceiling is the conventional cash outflow, not the C6 price.

### SR4 — Efficacy Theory of Change and Strategy

**Class of problem:** a fixed-cost credit form prices small, recurring draws as facilities rather than as continuously observed cash-flow risk.

**Theory:** relationship lending and transaction-data lending predict that lender-held account information reduces information-production cost and permits credit terms that a stand-alone application cannot support (Petersen and Rajan, 1994; Berger and Udell, 2006).

**Efficacy Strategy:** use the account’s observed flow as the risk object and its receipts as the repayment mechanism. This removes the conventional facility operations that create the tariff premium. C6 must pass part of that removed cost to the customer as a price below the standard overdraft tariff.

### Mutation gate — R2

```text
baseline: C1 removes facility-cost drivers but does not by itself guarantee that the customer receives the saving.
mutation_A: Keep the C1 limit price below the published standard-tariff overdraft ceiling | reason_considered: converts C1's removed cost into a customer cash saving | verdict: adopted | reason_verdict: makes the cost removal testable without changing the R1 risk object.
mutation_B: Retain the tariff and add non-price convenience benefits | reason_considered: preserves more bank margin | verdict: rejected | reason_verdict: does not eliminate the customer's money cost.
mutation_C: Use an invoice-finance price | reason_considered: may be lower for some firms | verdict: rejected | reason_verdict: changes the risk object from account flow to invoices and breaks R1 coherence.
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: customer-saving price condition
evolvedBFF: A flow-backed business-account limit replaces the fixed overdraft form, and its price remains below the standard overdraft cash outflow it displaces.
synthesisCheck: A deposit-funded revenue-based credit line for SME working capital, because observed account flow both forms the limit and repays it.
```

### Carrying check — R2

| Measure | £ per £1,000 average drawn balance per year | Basis |
|---|---:|---|
| KMC / price ceiling | 150–300 | 15–30% standard-tariff SME overdraft |
| Operating bar | 67.50–131.25 | C1 floor £54–105 × 1.25 |
| Capital bar | 26.05–43.68 | £148.5m required year-five revenue ÷ C1 public drawn-book proxy £5.7bn–£3.4bn |
| Binding bar | 67.50–131.25 | operating bar |
| Headroom on binding bar | 18.75–232.50 | KMC less binding bar |
| FMOS | 42.9%–455.6% | (KMC − C1 floor) ÷ C1 floor |

**Verdict:** **PROVISIONAL PASS.** The low KMC and high operating-cost corner clears the 25% per-requirement bar. This is a Tier 2/4 evidence mix. It would fail if the bank cannot identify a material population paying at least 15% EAR, if the C1 loss-adjusted floor exceeds £120 per £1,000, or if C6 cannot hold the customer price below the conventional tariff.

**Next gate:** update the TAM to the high-rate-overdraft segment, then generate C2 CTM, AOM, financial-simulation, and independent FIT artefacts. C3 remains unopened until those C2 completion conditions pass.
