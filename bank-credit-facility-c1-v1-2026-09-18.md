# A business bank's credit facility line — challenge one (R1) record v1 · Path C, mode 3 · 18 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-deposits-lending-pco-v1-2026-09-18.md`, runner-drafted, object-after to 20 September 2026 17:00 — **not yet confirmed**. This run is therefore **PROVISIONAL on the PCO** and can reach no higher verdict than PROVISIONAL, whatever the checks below say. If Tom objects to the PCO, this record is re-entered at SR1. **Mode:** 3 — just show me; the population is the bank's current borrowers; the scale is the bank's own volume; the margin against the price paid today is reported and does not gate; the gate is the R1 failure test (a form the incumbent could not adopt without changing architecture — RD-024 (d)). **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules (27 August and 1 September 2026). **Confidentiality:** the bank is not named; every internal figure is a red field `[name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

```
R1 sub-requirements
  [x] 1. Conventional business form factor
  [x] 2. Critical limiting operation (CLO)
  [x] 3. Workaround theory of change
  [x] 4. Workaround strategy
  [x] 5. Business form factor (C1)
```

---

## 0 · Defined terms

*Flow* — the receipts and payments the bank observes in the customer's account. *Standing limit* — the amount a customer may draw at any time, recomputed from the flow, with no application. *Draw* — the customer's transfer from the limit to the account balance. *Receipts share* — the fixed fraction of each receipt that repays the drawn balance until it is cleared. *Account line* — Case A of the levelled line (the Kept design occupies it). *Exception cell* — the only team of people in the new form. *Decision event* — the moment in the conventional form when a person or a scorecard reads what the applicant supplied and says yes or no.

---

## SR1 — Conventional business form factor (the levelled case)

Read by path: Path C — how the incumbent's line is made, sold, delivered and paid for today. Entered with PCO section 7 as the draft; the draft was tested, not held fixed.

- **Made.** A credit decision. The applicant supplies financial statements, a credit history (business and the owner's personal file), account conduct and security — a personal guarantee, a debenture or a charge over property. Below a threshold a scorecard decides; above it a credit underwriter decides, with a relationship manager's recommendation. The output is a limit, a rate, a term and conditions. FACT: application success is 47% overall and falls from 94% for the largest SMEs to 39% for the smallest (SME Finance Monitor Q4 2024, S2). FACT: the most common reasons given are the applicant's credit history, the business's financial position and insufficient security (S2).
- **Sold.** By application. The customer asks; the bank decides in days to weeks. FACT: just under 20% of SMEs hold a loan (CMA 2016); 28% use a core product (S2). Below £500,000 of turnover there is no relationship manager (CMA 2016, para 8.146, FACT).
- **Delivered.** As a facility. A term loan is drawn to the account and repaid on a schedule. An overdraft is a limit on the account, reviewed each year. FACT: overdraft use is 47% (UK Finance BFR 2025 Q3, S3).
- **Paid.** Interest at a margin over Bank Rate plus an arrangement fee; overdrafts carry a renewal fee. FACT: the effective rate on new SME loans was 6.18–7.00% through 2025 (Bank of England, Money and Credit, November 2025). Capital is held against the exposure under the standardised approach (75% risk weight for regulatory retail SME, FACT); expected loss is provisioned.

**Single-case check.** One form, one way of making the product: a decision on evidence the applicant produces, then a facility. Term loan and overdraft differ in the shape of the drawing and the repayment, not in the decision. The next-broader case — asset and invoice finance, where the decision rests on the asset or the debtor — is delivered a different way and was excluded at PCO 2d. ✓

**Research firewall.** The bank's own pre-assessed borrowing limits (a limit shown in the app before the customer applies) are the incumbent's closest feature to the design below. They are the baseline, not an analogue: the customer still applies, a decision event still occurs, security applies above a threshold, repayment is on a schedule and the facility is reviewed each year. Section SR5 tests the difference.

---

## SR2 — Critical limiting operation

*Method note.* Mode 3 diagnoses the incumbent's form for its current borrowers at its current volume. The within-form cost hunt runs on the eight-zone map (making · selling · delivering · getting paid) at the bank's volume: `[average drawn SME balance £]`, public proxy ⚠ £3.4–5.7bn (AOM header).

**Where the cost sits — per £1,000 of drawn balance a year, blended small-business book, all ⚠ (AOM 3d and 6):**

| Cost line | ⚠ £ per £1,000 | ⚠ Share | Zone |
|---|---|---|---|
| Funding — deposits | 15–30 | 20–25% | Delivering |
| Expected loss on a filtered, part-secured pool | 10–25 | 15–17% | Making |
| Regulatory capital at the cost of equity | 10–14 | 9–17% | Delivering |
| The decision — assessing each application on financial statements, credit history and security: ⚠ £500–1,500 per person-decision (judged from the US benchmark of $3,000–4,000 per small loan, ProSight, T3), on a ⚠ £24k average small facility (Bank Referral Scheme average deal £23,887, FACT), over a ⚠ 2–3 year life | 7–31 | 12–20% | Making |
| Annual review of each facility | 8–21 | 13–14% | Making |
| Collections and recoveries (FCA SME collections review 2022, 11 banks) | 5–15 | 8–10% | Delivering |
| Relationship management allocated to lending | 5–20 | 8–13% | Selling |
| **Conventional floor** | **⚠ 60–154** | | |

INFERENCE: the operating lines — the decision, the review, collections and the relationship — are ⚠ 25–85 of the ⚠ 60–154, about half. Every one of them is near-fixed per facility. FACT (Mills and McCarthy, Harvard Business School working paper 15-004, 2014): the transaction cost of underwriting a $100,000 loan is comparable to that of a $1m loan. INFERENCE: on a £10,000 facility the operating line alone is ⚠ £60–200 per £1,000, above the whole price. The gate refuses that customer because the form cannot afford to decide on it, not because the customer would not pay.

**The operation, stated as a verb.** *Assessing each application, one at a time, on evidence the applicant must produce — financial statements, a credit history and security — before any money moves.* Not "underwriters" or "credit policy" — those are the resources. The operation that forces them to be spent.

**Why the cost is inherent to the form.** Four named mechanisms:

1. **The borrower knows and the bank does not.** FACT: under asymmetric information a lender rations credit rather than raising the price, because a higher price selects the worse borrower (Stiglitz and Weiss, *American Economic Review*, 1981). INFERENCE: the decision event is the form's rational answer to not knowing; it is not a defect the bank could remove by policy.
2. **The evidence is produced by the applicant, so the smallest applicant has the least of it.** FACT: lending technologies rest on the information available — financial statements for the audited, credit scores for the owner, relationship lending for the rest (Berger and Udell, *Journal of Banking and Finance*, 2006). FACT: the smallest businesses fail most often on credit history, financial position and security (S2). INFERENCE: the form's evidence requirement excludes by size, by construction.
3. **The decision cost does not scale with the loan.** FACT: Mills and McCarthy (2014), above. INFERENCE: the bank sets a minimum ticket, so the excluded population is the small one.
4. **Relationship lending — the incumbent's answer to thin files — is the dearest resource in the form.** FACT: relationship lending produces soft information at a cost in people (Petersen and Rajan, *Journal of Finance*, 1994). FACT: below £500,000 of turnover no relationship manager is offered (CMA 2016). INFERENCE: the form withholds its own remedy from the customers who need it.

**Essential and tightly coupled.** Remove the decision on applicant evidence and the conventional form has no product: the facility is the output of the decision. The security process, the annual review and the collections operation all hang from it. ✓

**Cost threshold, for current borrowers.** The price paid today — ⚠ 7.5–12% all-in — covers the blended floor of ⚠ 60–154 only across the book; on its smallest facilities the form loses money and refuses them. In mode 3 there is no cost-to-value barrier for the current borrower; the threshold reported is the drop and the population the gate refuses (PCO section 3: about 1.5m businesses self-funding or deterred, ⚠ UNVALIDATED).

**CLO statement (registry, Phase 1): a process step, not a market condition.** ✓ Zone: Making.

**Secondary cost, recorded.** Funding and capital — ⚠ 25–44 of the floor — are the balance-sheet cost of holding exposure. Same in every form that lends; not the limiting operation. Held for R3.

---

## SR3 — Workaround theory of change (CMO)

- **Class of problem.** Information asymmetry served by a per-object decision: verification is bought one small object at a time, so it never amortises, and the evidence it needs is held by the party least able to produce it. Secondary: a fixed transaction cost on a small object.
- **Theory.** Stiglitz and Weiss (1981): rationing is the rational response to not knowing; remove the not-knowing and the rationing has no cause. Berger and Udell (2006): the lending technology follows the information available — transaction lending on hard information replaces relationship lending where hard information exists. FinRegLab, *The Use of Cash-Flow Data in Underwriting Credit* (2019) and *Sharpening the Focus* (2025, 38,000 small-business loans from two lenders, 2015–2024): cash-flow variables from bank-account data predict default across every segment tested, independently of the owner's credit score, with the largest gains for young businesses and low-score owners. Mills and McCarthy (2014): the fixed cost of the decision is the exclusion mechanism. Coase (1937): information inside the firm is cheaper than information bought across a market — the bank that holds the account already holds the flow.
- **Context (the conditions).** The bank holds the customer's account and so observes the flow (FACT: the four largest banks hold 85% of business accounts, S9 — a secondary source); receipts arrive through the bank's own payment systems; the customer's need is working money, small relative to the flow; the price paid today is ⚠ 7.5–12%.
- **Mechanism (how actors reason).** The bank reasons: "I do not need the applicant to prove what I already see; the flow is the evidence, and repayment from the flow is the security." The customer reasons: "the limit is already there; I draw when I need it and it clears itself from what comes in; I never apply." The rule reasons for no one: a limit is a function of observed flow, and the receipts share makes the exposure fall as the evidence that justified it falls.
- **Outcome (a state).** A business with an account draws working money without applying, and repays it from its receipts; the per-application decision operation does not exist inside the bank. Substitution test: "we will use cash-flow data in underwriting" is an activity inside the old form; the outcome is the state in which no application is assessed.
- **Current state, observable.** FACT: success 47%, falling to 39% for the smallest; 22% of SMEs put in personal money because they had to; 5% deterred from applying (S2); a person or a scorecard decides each application on applicant-produced evidence; a relationship manager only above £500,000 of turnover.
- **Desired state.** ⚠ 760,000 accounts carry a standing limit; ⚠ 228,000 are drawn at any time; no application, no decision event, no security process, no annual review, no collections operation; ⚠ 25 people in exception cells are the only human contact.

**Theory robustness.** Stiglitz–Weiss, Berger–Udell, Petersen–Rajan and Coase are economics with long replication records; FinRegLab is an independent empirical study replicated on a second data set in 2025. None is on the fragile-findings list. T-robustness PASS.

---

## SR4 — Workaround strategy

**Design choice (one structural move).** Make the credit facility a standing property of the account rather than the output of an application: the limit is computed continuously from the flow the bank already observes, the customer draws against it without asking, and repayment is a fixed share of receipts taken as they arrive. The decision event, the applicant's evidence, the security process and the collections operation are removed, not automated.

**Hypothesis.** If the facility is a standing limit on the account, computed from the flow and repaid from receipts, then the operating cost of lending no longer depends on the size of the facility, so the bank can carry the small facility it refuses today at a floor inside the price its borrowers pay now — provided the expected loss on a flow-underwritten pool stays at or below ⚠ 4% of drawn balance. This would be wrong if the loss on that pool exceeds ⚠ 5%, or if customers will not accept a receipts share as a term of the account.

**Critical assumption.** Expected loss on the flow-underwritten pool of the bank's own account holders is ⚠ 2.0–4.0% of drawn balance a year. Public anchors: FinRegLab shows the direction and the independence of the signal, not the level; the level at a large bank on its own accounts is not published anywhere found.

**Falsification condition.** If, in a cohort of ⚠ 10,000 drawn accounts held for 12 months, the loss exceeds ⚠ 5% of drawn balance at the price paid today, the hypothesis is false and the run returns to SR2 with the loss line as the new brief. If more than ⚠ 30% of customers offered the standing limit decline the receipts share, the form fails on the customer side and R2 re-enters.

**Elegance test.** One move, five effects: the decision operation is gone (R1); the limit exists before the need, so there is nothing to doubt about eligibility (R4, by number); repayment follows receipts, so the repayment matches the customer's cash (R6, by number); the exposure self-liquidates from the flow that justified it, so the balance-sheet shape changes (R3, by number); the limit lives where the flow lives, so moving the account means losing the limit (R8, by number). ✓

**Considered / not chosen (VA-4).**
- **A — the standing limit on the flow, repaid from receipts:** adopted.
- **B — joint liability (Grameen; Ghatak and Guinnane, *Journal of Development Economics*, 1999):** rejected. Peer screening needs a group that knows each other and can sanction; UK small businesses do not form such groups, so the mechanism's conditions are absent.
- **C — lend on the receivable (the debtor's credit, not the borrower's):** outside the levelled case — asset and invoice finance, excluded at PCO 2d. Not chosen on that ground; noted for R3 by number.
- **D — pooled pricing with no individual decision (insurance form):** rejected as the whole. Pooling fails when the good risks leave (Rothschild and Stiglitz, *Quarterly Journal of Economics*, 1976). Used inside A: the flow is what makes the pool safe, because good and bad risks cannot fake their receipts.
- **E — a government guarantee (the British Business Bank's schemes):** an improvement inside the old form. The loss is shifted; the decision, the evidence and the cost remain.
- **F — the application pre-filled from accounting software (the iwoca model):** an improvement inside the old form. The decision remains inside the lender; the ledger is self-reported by the borrower (bank-conventional-model-object.yaml, 14 Sep 2026).

---

## SR5 — Business form factor (C1)

```
CLO GATE — R1
cloZone: Making
cloName: per-application decision on applicant-produced evidence
cloIsOperationNotResource: true   (the operation is assessing each application on evidence the applicant produces; underwriters, scorecards, security administrators and collectors are what it consumes)
cloStatedAsVerb: assessing each application, one at a time, on evidence the applicant must produce — financial statements, a credit history and security — before any money moves
cloIsEssential: true   (remove it and the conventional form has no product — the facility is the output of the decision)
cloEliminatesNotReduces: true   (restructured: no application is assessed; the residue — a rule under model-risk review and exception cells for accounts whose flow stops — is named and costed in the AOM, not hidden)
workaroundStrategy: the facility as a standing property of the account — a limit computed from the flow, drawn without application, repaid by a fixed share of receipts
theoryGrounded: Stiglitz & Weiss (1981); Berger & Udell (2006); FinRegLab (2019, 2025); Mills & McCarthy (2014); Coase (1937)
newBFFRequired: true   (the incumbent's form decides once on applicant evidence and holds a fixed exposure to a schedule; the seed never decides, holds a variable exposure that follows the flow, and repays from receipts; the object sold, the risk held and the people employed all change)
cloAuditFlag: false
```

**Property-holder test (VA-71).** Four properties are asserted. "The limit is computed from the flow" — holder: the bank's own ledger on the account line; carried by WP-1 and the limit engine track in the CTM. "The customer draws without applying" — holder: the customer; carried by WP-2. "Repayment is a fixed share of receipts" — holder: the customer's agreement to a term of the account; carried by WP-3; for a sole trader or a partnership of two or three persons borrowing under £25,000 the agreement is regulated under the Consumer Credit Act 1974 (s.16B exempts business credit above £25,000; a limited company is never a CCA borrower) — a compliance line in the AOM, not a decision. "The loss on the pool stays at or below ⚠ 4%" — holder: the pool itself; an unmeasured input, not a property this design can assert; flagged and carried as the critical assumption.

**Central structure.** The standing limit computed from the flow and repaid from receipts: remove it and R1, R3 (by number), R4 (by number) and R6 (by number) all fall.

**BFF (C1) — first cut.** *A bank whose credit facility is a standing property of every account with enough flow: a limit computed daily from the receipts and payments the bank already observes, drawn by the customer without an application, and repaid by a fixed share of each receipt as it arrives — so the bank has no per-application decision, no security process, no annual review and no collections operation, only a rule under review and exception cells for accounts whose flow stops.* First cut — R2–R10 may rewrite this, including fundamentally.

**Three-function check.** Cost creation: the decision, the security process, the review and collections are gone; the rule, the engine team, model risk and the exception cells remain. Exchange: unchanged at C1 — the customer pays interest on the drawn balance at the price paid today (the structure is C6 territory). Margin retention: the operating floor per £1,000 no longer depends on the size of the facility, so the floor holds at any ticket the rule permits. **At-scale test:** designed for the bank's own volume (⚠ £3.4–5.7bn drawn) and holds above it, because every activity in the form scales with accounts, not with people; the binding gate is the loss rate, not capacity.

**Simplicity test.** Removed from the first cut: the limit for an account with no flow history (the start-up); the price and how it is presented; who brings the customer to the limit; how the limit is set for an account that receives cash rather than payments through the bank. None changes the mechanism at C1.

**Synthesis check (VA-1).** Looks like **Square Capital** (Block) and **MYbank** (Ant Group's "3-1-0": three minutes to apply, one second to approve, zero people) inside a UK bank's own account, because the mechanism — a limit from observed flow, repaid from the flow — is theirs. Limit of the analogue: Square and Ant observe only the sales that pass through their own payment systems and lend to merchants they process for; a UK bank holding the business current account observes the whole flow, in and out, and funds the limit from the same account's deposits. The bank's position is the stronger one on information and funding and the weaker one on speed of change. That difference is what section SR5's failure test rests on.

**Research firewall.** Held. The bank's pre-assessed borrowing limit is the baseline (section SR1); the design removes the operations that limit retains. The venture is not "faster overdrafts".

**Portfolio note (by number).** The account line — Case A, the Kept design — is the holder of the flow and of the deposits that fund the drawn book. Nothing in Kept is designed or changed here. If Kept is not built, the flow still exists in the bank's existing account ledger; the dependency is on the ledger, not on Kept.

**Regulatory desk answers (legal questions are desk questions, 14 Sep 2026).** Permissions: a UK bank's Part 4A permission covers accepting deposits and lending; no new permission. Capital: the drawn balance is a regulatory retail SME exposure at 75% under the standardised approach; the undrawn limit is an unconditionally cancellable commitment, which carries a 10% credit conversion factor under Basel 3.1 from 1 January 2027 (PRA PS9/24) — costed in the AOM. The rule: a model under the PRA's model-risk principles (SS1/23), so independent validation is a cost line, not a question. Consumer credit: regulated for sole traders and small partnerships under £25,000 (CCA 1974 s.16B); Consumer Duty applies to those customers. Set-off: bank terms already carry a right of set-off against the customer's balances; the receipts share is a narrower, agreed form of it. What a ruling would settle and this desk cannot: whether a receipts share on a CCA-regulated running account is a "variable repayment" that needs a specific form of agreement — carried as an unmeasured input, owner the bank's conduct function.

---

## Actor business cases (VA-127)

| Actor | Behaviour needed | How often | Gains (priced) | Costs (priced) | Best alternative | Surplus |
|---|---|---|---|---|---|---|
| Business with an account (current borrower, ⚠ 1.6m across the market, S2 and S8) | draw against a standing limit; accept a receipts share as a term | continuous | working money the same day, no application (FACT: applicants spend about 26 hours on an application — Mills and McCarthy 2014, citing the New York Fed's 2013 survey — worth ⚠ £500–1,000 of owner time); no security over the home; a limit that grows with the business | interest at the price paid today ⚠ 7.5–12%; a receipts share that reduces cash in hand while drawn; the limit falls when the flow falls | apply for an overdraft or loan (47% succeed, S2); a card; personal money (22% "had to", S2) | PROVISIONAL — positive at central for a borrower who values time, certainty and no personal security; negative for a borrower who wants a fixed schedule and a fixed rate for a long-lived asset (that customer belongs to the excluded next-broader case, asset finance) |
| Business the gate refuses today (⚠ 1.5m self-funding or deterred, PCO section 3, UNVALIDATED) | the same | continuous | a facility where none exists; the value is R2's question by number | the same | personal money, family, a card, going without | not claimed at C1 — R2 sizes the loss and the ceiling for this population |
| The bank (capital holder, sponsor of the venture) | fund the limit engine, the model, the exception cells; hold capital on drawn and undrawn exposure; accept a higher expected loss for a lower operating cost | once, then continuous | the operating lines of the conventional form (⚠ 25–85 per £1,000) fall to ⚠ 7–18; the refused population becomes servable at the same floor per £1,000 | expected loss ⚠ 20–40 against ⚠ 10–25; capital on undrawn limits ⚠ 1.6–3.4 per £1,000; the build (`[capital envelope £]`, PCO section 1, ⚠ £100m ASSUMED for the portfolio) | keep the conventional form and its gate | PROVISIONAL — the net floor falls ⚠ 6–49 per £1,000 at the corners (60–154 → 54–105); the whole of it depends on the loss rate |
| The account line (Case A) | expose the ledger to the limit engine; carry the receipts share as a term | continuous | none needed — an internal dependency | engineering on the ledger (a build item) | — | internal; no case row required |
| PRA and FCA | none new | — | — | — | — | not an actor at C1; permissions unchanged |
| Credit bureau | supply an identity and fraud signal | per account | commodity | — | — | commodity vendor; no case row required (VA-99) |

---

## Actor tracks (VA-102)

| Actor | Track in the CTM | Introduced | Holder of what |
|---|---|---|---|
| the business | the customer journey, four phases | C1 | draws; accepts the receipts share |
| the account line | account line track | C1 | the flow; the term |
| the limit engine and exception cells | limit engine track | C1 | the rule; the only human contact |
| PRA and FCA | regulator track | C1, unchanged | permissions and capital |
| the partner who brings the customer | partner track | `[REQUIRES C7]` | flagged |

---

## BFF delta and upstream re-verification (VA-103)

| Item | At entry (PCO section 7 draft) | At C1 | Changed by |
|---|---|---|---|
| Made | a credit decision on financials, rating and security | a limit computed from the flow; no decision event | SR4 |
| Sold | on application | never applied for; shown in the account | SR4 |
| Delivered | a facility — loan or overdraft | one running limit; the term loan dissolves into a draw with a fixed receipts share | SR5 |
| Paid | interest at a margin plus a fee | unchanged at C1 — the price paid today; structure `[REQUIRES C6]` | — |
| Gate | evidence the applicant must produce | ⚠ six months of flow (the start-up is `[REQUIRES C2]`) | SR4 |

Earlier requirements this move also serves (VA-106): **R3** — the exposure self-liquidates from the flow that justified it (mechanism: the receipts share) · **R4** — the limit exists before the need, so eligibility is not in doubt (mechanism: the standing limit shown) · **R6** — repayment follows receipts, so it matches the customer's cash (mechanism: the receipts share) · **R8** — the limit lives where the flow lives (mechanism: the account as the holder). Named by number; nothing about how those requirements solve them. Earlier requirement rows: none — first requirement. Function-gate re-run: not applicable at C1.

---

## Financial check — the floor and the drop, at the bank's volume

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `[average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn (AOM header). **Component set the verdict was computed on (VA-74):** WP-1, WP-2, WP-3.

**Floor of the new form (AOM 6), all ⚠ Tier 4, bottom-up:**

| Layer | £ per £1,000 a year | Content |
|---|---|---|
| PVC | 40–83 | funding 15–30 · expected loss 20–40 · computing and payments 2–5 · exceptions and write-off handling 3–8 |
| RC | 2–5 | ⚠ 70 people and technology, £8.5–14.5m, across the drawn book |
| SC | not designed until C3 | — |
| IC | 12–17 | capital on drawn 10.8–13.5 · capital on undrawn limits 1.6–3.4 |
| **Floor** | **54–105** | scaling cost excluded — indicative |

**The drop.** Conventional floor on the same unit ⚠ 60–154 (SR2). New form ⚠ 54–105. **The operating lines fall from ⚠ 25–85 to ⚠ 7–18 — a drop of ⚠ 70–80%.** Expected loss rises from ⚠ 10–25 to ⚠ 20–40 because the pool is no longer filtered by the gate or protected by security. Capital rises by ⚠ 1.6–3.4 for the undrawn limits. **Net floor: down ⚠ 6 at the low corner and ⚠ 49 at the high corner — ⚠ 10–32%.** The form's real change is not the size of the drop at the blended book; it is that the floor per £1,000 no longer rises as the facility shrinks, which is what lets the bank carry the customer it refuses today.

**Margin of safety against the price paid today (non-gating in mode 3, RD-024 (e)).** Price the borrower pays today: ⚠ £75–120 per £1,000 (FACT: 6.18–7.00% effective on new SME loans through 2025; overdrafts and small unsecured ⚠ 10–15%; fees ⚠ 1–2% equivalent; blended ⚠ 7.5–12%). By the script (`fit_margin.py`, ceiling = the price paid with the fee element discounted by a twentieth, £71.25–114): **−32.1% at the worst corner; 111.1% at the best.** By hand on the undiscounted price: (75 − 105) ÷ 105 = −28.6%; best corner (120 − 54) ÷ 54 = 122%. At the centre of both bands (floor 79.5, price 97.5): 22.6% — BORDERLINE band. The conventional form on the same unit sits at (75 − 154) ÷ 154 = −51% at its worst corner and (120 − 60) ÷ 60 = 100% at its best — the same shape, because both forms carry the same funding and capital and differ in where the rest sits. **The check reports a margin; it does not pass or fail the design.** The script's output is in `sme-fintech-models/bank-credit-facility-fit-verifier-r1-2026-09-18.md`.

**What the margin says.** The worst corner is negative in both forms. In the conventional form the negative corner is the small facility, which the gate refuses. In the new form the negative corner is the high-loss pool, which the rule must avoid. **The design has moved the binding constraint from the size of the facility to the loss rate on the pool.** That is the finding of this run, and it is reported unsoftened.

**Binding gate — found by driving the design across its gates (VA-84).** Gates tested:
1. margin at the price paid today — negative at the worst corner, 22.6% at the centre;
2. expected loss on the flow-underwritten pool at or below ⚠ 4% — unmeasured;
3. share of accounts with enough flow history to carry a limit — ⚠ 80%, unmeasured; start-ups (314,000 a year, S1) excluded until C2;
4. customer acceptance of a receipts share as a term — unmeasured;
5. the CCA form of a variable-repayment running account for sole traders under £25,000 — a desk answer with one open point;
6. capital on undrawn limits at scale — costed, small.
 **First to fail on today's evidence: (2), the loss rate.** Margin to it: at the central price (£97.5) and the central non-loss floor (£49.5), the floor equals the price at a loss of 4.8%; the assumption's own high corner (4.0%) leaves a margin of 0.8 points, and at 5% the central margin is negative. **A margin of under one point of loss against an assumed value is the finding: the loss rate is the first thing the insider corrects**, from the bank's own loss experience by account-conduct band, which is not public.

**Independence (VA-97).** The margin of safety measures cost per £1,000 drawn against price; the binding gate measures a loss rate on a pool against a threshold. The two share the loss line, so they are not independent on that line: the margin is a function of the gate. Shown, and stated as a limit — the independent gates are (3) and (4).

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Property-holder test ✓.
- Credibility mechanism (VA-81) ✓. The bank's instrument at C1 is the rule's validation under model risk and its loss reporting by cohort — an existing function. The customer's belief that the limit is real is a later requirement's question.
- Pointing test ✓. The design attacks the operation, not the resource.
- Coverage of the elimination conditions ✓. The four SR2 mechanisms: not-knowing (the flow is known); applicant-produced evidence (none is asked for); fixed decision cost (no decision); relationship lending withheld (no relationship needed).
- Limit of the analogue stated ✓.
- Completeness contract (VA-73) ✓. SR1–SR5 present.
- No forward references ✓. R2, R3, R4, R6, R7, R8 and C6 by number only.
- Binding gate by driving ✓.
- Shared-input declaration ✓. The loss line is shared between the margin and the gate; declared.
- Incremental write ✓.
- Existence test (VA-92) ✓. The underwriting instrument's holder is the bank's own ledger, internal, activated by the rule. The affordability screen is the operating cost the conventional form spends per facility (⚠ £500–1,500 per decision plus ⚠ £200–500 a year of review). That is the maximum the form can hand back per facility.
- Independence shown with its limit ✓.
- Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r1-2026-09-18.md`.

Checks failed: 0. **PASS.**

**Operational check.** The AOM is written (`sme-fintech-models/bank-credit-facility-aom-v1-2026-09-18.md`) as a document, not a model file, so the coverage and trace scripts did not run — **build item**. Capacity: ⚠ 16,000 exception hours per cell a year covering ⚠ 100,000 drawn accounts; ⚠ 2.3 cells at scale, ⚠ 36,500 hours; **the capacity figure is 16,000 hours per cell and every calculation above uses it.** Role support: every performer has a supervisor, a trainer and a reviewer; the rule has independent validation; PASS. Unit sizing: a cell covers its ⚠ £0.7–0.9m from a fraction of a per cent of the revenue on the ⚠ £1.5–2.5bn it covers (PASS on contribution); stand-up ⚠ 6–10 weeks. Component carriage: every C1 transition in the CTM is carried by WP-1, WP-2, WP-3, CP-1 or the exception activity, or flagged. **PROVISIONAL** (one build item).

**Financial check.** Margin of safety −32.1% to 111.1% by script (−28.6% to 122% by hand; 22.6% at the centre), non-gating. Binding gate: the loss rate on the pool, unmeasured, with under one point of margin at the assumption's own high corner. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- CTM and AOM not run through the model scripts — **build item**; owner: the Venture Architect seat if the run proceeds; convergence: the model files exist and the coverage script passes before C4 opens.
- The loss rate on the flow-underwritten pool — **unmeasured input**; owner: the insider (the bank's loss by account-conduct band, not public); convergence: a 12-month loss on a ⚠ 10,000-account cohort; pivot trigger: above ⚠ 5% at the central price → return to SR2 with the loss line as the brief.
- Share of accounts with enough flow to carry a limit — **unmeasured input**; owner: the insider (accounts by age and monthly receipts); convergence: the count.
- Customer acceptance of the receipts share — **unmeasured input**; owner: R2 fieldwork by number; convergence: the share who decline; trigger: above ⚠ 30%.
- The CCA form of a variable-repayment running account under £25,000 — **standing constraint** with one open point; owner: the bank's conduct function; convergence: a form of agreement signed off.
- Every ⚠ cost figure in the new form — **unmeasured input**; owner: the insider; convergence: the bank's cost by function, which is not public.

```
GATE VERDICT — on the cumulative architecture C1
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     FMOS −32.1% to 111.1% by script (−28.6% to 122% by hand; 22.6% central; non-gating, mode 3) · binding gate: loss rate on the pool — unmeasured, < 1 point of margin at the assumed high corner
  dispositions:      4 unmeasured inputs, 1 build item, 1 standing constraint (above)
  capacity figure:   16,000 exception hours per cell a year, 100,000 drawn accounts per cell — used throughout   VA-91
  independence:      shown with its limit — the loss line is shared; gates (3) and (4) are independent           VA-97
  gates driven:      6; first to fail on evidence: the loss rate, margin 0.8 points at the assumed high corner  VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r1-2026-09-18.md                        VA-90
  inherited:         PCO unconfirmed (object-after to 20 Sep 2026 17:00) — caps the verdict at PROVISIONAL       VA-95
  repairs:           none
  VERDICT:           PROVISIONAL
```

**R1 failure test (RD-024 (d), the gate in mode 3).** Could the bank adopt this without changing its architecture? No. Its credit architecture is built around the decision event: a credit policy that says what evidence is required, delegated authorities that say who may decide, a security process that follows the decision, an annual review that repeats it, and a collections function that acts when the schedule is missed. Its pre-assessed borrowing limit sits in front of that architecture and leaves every part of it in place. The seed removes the decision event and with it the policy, the authorities, the security process, the review and the collections operation; it replaces a fixed exposure held to a schedule with a variable exposure that follows the flow; it replaces the borrower's balance sheet as the risk object with the continuity of the borrower's receipts; and it makes the account, not the facility, the product. Risk governance, the people employed, the risk object and the object sold all change. **A new form is required. Verdict on the qualitative test: venture, not improvement.** The honest tension: a bank could build the limit engine as a feature. It could not run it as the form without removing the operations above, and removing them is the architecture change.

**Principal's review, 18 September 2026.** Tom asked whether banks already make the facility a standing property of the account. Answer on record: the bank already makes the *decision* cheaply (pre-assessed limits in the app, priced on account conduct); it has not *removed* the decision — an acceptance step with a check, a point-in-time assessment refreshed on a cycle, security above a threshold, a schedule or a clear-down expectation, and annual review and collections all remain. Non-banks (Square Capital, PayPal Working Capital, Shopify Capital, iwoca) do the receipts-share repayment, on their own transaction data only, at ⚠ 15–30% equivalent rates. Falsification stated to Tom: if inside the bank the pre-assessed limit is drawable with no acceptance step, recomputed from the flow, and unsecured, unscheduled and unreviewed, the design is the bank's existing form and C1 fails as a venture. Tom's response: "think you are right." The failure-test verdict stands; the falsification remains the insider's to apply if any of the five operations turns out to be absent already.

---

## Carried items (VA-82)

- Forward-referenced: the limit for an account with no flow history — C2 by number; the price and its presentation — C6 by number; who brings the customer to the limit — C7 by number; the balance-sheet shape of a self-liquidating exposure — R3 by number; the customer's conviction that the limit is real — C4 by number.
- Unmeasured inputs: the loss rate on the pool (owner the insider; trigger > ⚠ 5%); the share of accounts with enough flow (owner the insider); customer acceptance of the receipts share (owner R2 fieldwork; trigger > ⚠ 30% decline); every ⚠ figure (owner the insider; convergence the corrected frame).
- Build items: CTM and AOM model files and the script runs; the ledger integration on the account line.
- Standing constraints: the CCA form for sole traders under £25,000; model-risk validation of the rule (SS1/23); the 10% credit conversion factor on undrawn limits from 1 January 2027.
- Unowned design defects: none.

---

## The population the new floor would open — by-product only, ⚠ UNVALIDATED (RD-024 (f))

INFERENCE. The operating floor per £1,000 no longer rises as the facility shrinks, so the size gate has no cause. What still excludes is the flow gate: an account with less than ⚠ six months of receipts, or one whose receipts arrive as cash outside the bank's payment systems. The 314,000 start-ups a year (S1) and the cash trades are on the far side of it. The 1.25m self-funders and 285,000 deterred (PCO section 3, ⚠ UNVALIDATED) who hold an account with flow are on the near side. Sized at R2, not claimed here.

---

## Quality check

| Test | Result |
|---|---|
| CLO stated as a verb, an operation, essential, tightly coupled | ✓ |
| CLO GATE block present before the BFF | ✓ |
| Theory named and citable; robustness stated | ✓ |
| Workaround changes the theorem, not the tactics | ✓ — the decision event is removed, not automated |
| Considered / not chosen, six candidates with reasons | ✓ |
| Actor business cases priced or marked PROVISIONAL | ✓ |
| FMOS by the correct formula, cost denominator, bands from the registry | ✓ |
| Load-bearing assumptions named (loss rate; flow coverage; receipts-share acceptance) | ✓ |
| Pivot trigger written | ✓ — loss > ⚠ 5% at the central price |
| Verdict composes forward (PCO unconfirmed → PROVISIONAL cap) | ✓ |
| No tooling vocabulary or metaphor in load-bearing text; house-style checker run | run on file save — see changelog |

---

## Sources (in addition to PCO S1–S12)

| # | Source | Used for |
|---|---|---|
| C1 | Bank of England, Money and Credit, November 2025 | effective rate on new SME loans 6.18–7.00% through 2025; Bank Rate 4.0% from August 2025 |
| C2 | FinRegLab, *The Use of Cash-Flow Data in Underwriting Credit* (2019); *Sharpening the Focus: Using Cash-Flow Data to Underwrite Financially Constrained Businesses* (2025) | cash-flow variables predict default independently of the owner's score; 38,000 loans, 2015–2024 |
| C3 | Mills, K. and McCarthy, B., *The State of Small Business Lending*, HBS working paper 15-004 (2014) | fixed transaction cost of the decision; about 26 hours per application (citing the New York Fed 2013 survey) |
| C4 | Stiglitz, J. and Weiss, A., *American Economic Review* 71(3), 1981 | credit rationing under asymmetric information |
| C5 | Berger, A. and Udell, G., *Journal of Banking and Finance* 30, 2006 | lending technologies follow the information available |
| C6 | Petersen, M. and Rajan, R., *Journal of Finance* 49(1), 1994 | relationship lending and its cost |
| C7 | Coase, R., *Economica* 4(16), 1937 | information inside the firm is cheaper than across the market |
| C8 | Ghatak, M. and Guinnane, T., *Journal of Development Economics* 60, 1999; Rothschild, M. and Stiglitz, J., *Quarterly Journal of Economics* 90(4), 1976 | joint liability and pooling — considered, not chosen |
| C9 | CMA, Retail banking market investigation, final report, 9 August 2016 | no relationship manager below £500,000; just under 20% of SMEs hold a loan |
| C10 | PRA, PS9/24 Basel 3.1 near-final rules (2024); CRR Art. 123; PRA SS1/23 model risk management | 75% regulatory retail SME risk weight; 10% credit conversion factor on unconditionally cancellable commitments from 1 January 2027; model validation |
| C11 | Consumer Credit Act 1974, s.16B | business credit above £25,000 exempt |
| C12 | `sme-fintech-models/bank-conventional-model-object.yaml` (14 September 2026) — ProSight (US benchmark), Bank Referral Scheme statistics, FCA SME collections review 2022, Glassdoor pay, Funding Circle FY2025 | cost per decision, average small deal, collections, relationship cost, automated-lender cost per £1,000 |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | First draft. Runner-drafted on the principal's behalf; PROVISIONAL on the object-after PCO. Model files, verifier and status file written alongside. |
| v1.1 | 18 September 2026 | Principal's review of the R1 failure test added (pre-assessed limits: the decision made cheaply, not removed); falsification recorded. |
