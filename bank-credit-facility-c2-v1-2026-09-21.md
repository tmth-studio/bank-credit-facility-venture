# A business bank's credit facility line — challenge two (R2) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R2 carries — the selected customer's cash outflow clears the C1 floor with a 35.7% margin at the worst corner — and the verdict cannot exceed R1's PROVISIONAL (VA-95). Binding gate: the loss rate on the flow-underwritten pool, unmeasured. Pivot trigger: above ⚠ 5%.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c1-v2-2026-09-18.md` (R1, PROVISIONAL) and `bank-credit-facility-c2-run-note-2026-09-19.md` (the diagnosis, its failure, and the rerun this record closes). **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse at 20 September 2026 17:00; no objection recorded. **Mode:** 3 — just show me. The population is the bank's current borrowers; the scale is the bank's own volume; the R2 ceiling is the cash outflow the selected customer pays today (RD-024 (e)); the gate is the carrying check. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules (27 August and 1 September 2026); every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

---

## 0 · Defined terms

As in the C1 record: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *exception cell*. New at C2:

- **Standard tariff** — the published interest rate and fees a bank charges on a business overdraft that is not individually negotiated. Published representative EARs on unsecured business overdrafts up to £25,000: 14.54% (HSBC UK), 15.62% (Lloyds Bank; Bank of Scotland), read 21 September 2026.
- **Key monetizable cost (KMC)** — the cost in the customer's routine that the design removes and that sets the price ceiling. Here: the annual money cost of a standard-tariff overdraft on the drawn balance.
- **Migration** — the one-time move of a customer's existing arranged overdraft, and any balance drawn on it, into the standing limit and a draw with a receipts share (CTM v2, WP-4).
- **Price condition** — the rule that the all-in price of the limit per £1,000 drawn stays below the standard-tariff cost the customer paid before migration (CTM v2, PC-1). A condition, not a price. The price, its structure and its presentation are C6's by number.
- **Carrying check** — the test that the KMC clears both the operating bar (the C1 floor × 1.25) and the capital bar (the PCO's required revenue ÷ the drawn book).

---

## SR1 — High-import outcome

**Statement:** "I access working money."

**Selected customer:** the established UK SME with observable account flow that currently pays a standard-tariff overdraft at 15–30% EAR for recurrent working-capital draws.

**Selection logic (from the rerun, 19 September 2026).** Four candidates were enumerated: the standard-tariff overdraft user; the owner who injects personal money; the would-be borrower who does not apply; the new-to-trading business. The first is the only C1-reachable type with a published, direct cash outflow. The second and third carry an unpriced cost. The fourth is outside the flow gate. Legibility did not drive the choice: the owner-funded candidate is the larger population (about 1.25m against 627,000–969,000 overdraft users, market proxies) and was struck for want of a price, not for want of a story.

```
OUTCOME LADDER — R2
apexOutcome: the business keeps trading through its cash cycle
ladder:
  L1 the business keeps trading through its cash cycle
    L2a I access working money when the gap opens            ← chosen rung
      L3a I get it without applying each time
      L3b I pay as little as possible for it
      L3c I repay it as the cash comes in
    L2b my customers pay me on time                          ← struck
    L2c I hold enough cash of my own not to need it          ← struck
struckRungs:
  L2b → the venture cannot change the customer's customers' payment terms; late payment is a market-wide condition (DBT and Small Business Commissioner, Late Payments Research 2025)
  L2c → the venture cannot change the owner's capital; the owner-funded route was the failed first diagnosis (run note, 19 Sep 2026)
revealedImportance:
  L2a → the customer pays 15–30% EAR a year on the drawn balance to hold this rung (TAM data object v2, KMC-OD-STD-TARIFF)
  L3a → the customer renews an arranged overdraft each year and pays a fee to do so (⚠ 1–2% of the limit)
costsVentureChanges:
  the tariff's interest on the drawn balance — reduced to a price below it (the level is C6's by number)
  the renewal and arrangement fee — removed with the overdraft product (WP-4)
  the application time on each renewal — removed at C1 (about 26 hours per application, Mills and McCarthy 2014, citing the New York Fed 2013 survey)
chosenRung: L2a — I access working money when the gap opens
coveringTest: tariff interest — yes · renewal fee — yes · application time — yes; every cost sits inside the routine of holding and using an overdraft
kmcRungCheck: true — the KMC (the tariff's annual money cost) sits on L2a
```

---

## SR2 — Attendant routine

The customer holds an arranged overdraft on the business current account. When a recurrent cash gap opens — a supplier to pay before a customer pays — the customer draws on it. The customer pays the tariff on the drawn balance, daily. Receipts arrive and reduce the balance; the customer watches the balance against the limit. Once a year the overdraft is renewed: a review, a fee, and a limit that may fall.

| Step | KPI | DO | USE / BUY | THINK | FEEL |
|---|---|---|---|---|---|
| 1 · the gap opens | the payment goes out on the day it is due; misses ⚠ 10–20% of months (judged from the incidence of late payment, DBT 2025) | pays the supplier from the overdraft | the arranged overdraft; the tariff | "the limit covers it this month" | resignation at the rate; relief the payment went |
| 2 · the balance sits drawn | days drawn a year; the tariff's cost | watches the balance; chases receipts | interest at 15–30% EAR, daily | "this is expensive money" | irritation; low attention — the cost is invisible day to day |
| 3 · the receipts arrive | the balance falls | nothing — the receipts clear it | — | "cleared until next month" | relief |
| 4 · the annual renewal | the limit held or raised; the fee | fills a form; supplies accounts; waits | the renewal fee ⚠ 1–2% of the limit; owner time | "will they cut it?" | anxiety; the one moment the price is visible |

The C1 form replaces steps 1 and 4: the fixed facility becomes a continuously recomputed, flow-backed limit that repays from an agreed receipts share, and the renewal disappears. Step 2 is where the KMC sits. R2 attacks step 2.

---

## SR3 — Key monetizable cost

**KMC:** the annual money cost of a standard-tariff SME overdraft — interest and fees on the drawn balance. **£150–300 per £1,000 of average drawn balance a year** (class: expended; tier T3 — low corner T1, high corner ⚠).

**Evidence and its correction.** Low corner: published representative EARs of 14.54–15.62% on unsecured business overdrafts up to £25,000; fees of ⚠ 1–2% of the limit at 47% use (UK Finance Business Finance Review 2025 Q3) put the representative customer at ⚠ 16.5–19.6% all-in. High corner: the top of the tariff for the highest-risk band and the rate non-bank receipts-share lenders charge, ⚠ 30% (C1 record, principal's review). **Source correction, 21 September 2026:** the run note attributed "15–20% EAR, up to 30%" to the government's Small Business Access to Finance call for evidence. The government response (DBT and HM Treasury, 4 December 2025) carries no rate figure. The band now rests on the published tariffs. The number did not change; its source did.

**TAM data object (VA-83).** `sme-fintech-models/bank-credit-facility-tam-model.yaml`, version 2, state at-C2-close. Validated: `python3 .claude/skills/shared/generators/validate_tam_model.py <file>` → "6 sub-classes · 5 KMC classes; WARNINGS (1) [L7] volume.basis is 'incidence' while sub-classes are defined against supplied alternatives; ✅ valid (with declared warnings)"; exit 0. Partition: by KMC and eligibility, never by size; recorded partition defect: none. Sub-classes: six, each with one KMC and one addressability verdict. Volume basis: incidence — 627,000–969,000 overdraft users a year (11–17% × 5.7m, market proxy). Unmeasured shares: four of six (the loan user, the owner-funded, the deterred, the new-to-trading), listed as unmeasured, not filled. The bank's own count is a red field: `⚠ [count of the bank's business overdraft accounts on the standard tariff]`.

**Aggregate addressable value (market proxy, not the bank's).** 250,800–678,300 surviving overdraft users (the 40–70% tariff share, T4) × ⚠ £10–17k average drawn overdraft (T4 — overdrafts are smaller than the Bank Referral Scheme's £23,887 average deal, judged) × £150–300 per £1,000 = ⚠ £0.4–3.5bn a year of tariff outflow across the market. Stated for scale; nothing in the design is derived from it.

**Why this cash outflow is admissible as a KMC where the C1 lender-price band was not (one sentence).** The C1 band (£75–120) was the price paid across the whole book — a blend over many customers, recorded as a stand-in against which the margin did not gate (RD-024 (e)) — whereas the tariff outflow is one selected customer's own cost, measured per customer, with a published low corner and a routine it sits inside.

```
KMC ADMISSIBILITY — R2
  customer of record: the established UK SME with observable account flow paying a standard-tariff overdraft at 15–30% EAR for recurrent working-capital draws
  (a) monetary band or revealed avoidance price: £150–300 per £1,000 of average drawn balance a year — low corner T1 (published representative EARs 14.54–15.62%, product pages read 21 Sep 2026, plus fees ⚠ 1–2% of the limit); high corner T4 (top of tariff; non-bank receipts-share rate ⚠ 30%)
  (b) risk drivers: not applicable — the cost is expended, not risk-borne
  (c) elimination test on the current C1 form: C1 removed the holding of a fixed, secured, scheduled exposure (the decision, security, review and collections). The tariff prices that holding and the information the bank lacks about an applicant it cannot observe. The removal takes the operating premium and the information premium off the customer — eliminates, not transfers (no other actor pays them) and not reduces (the operations do not exist in the form). What remains for the customer to pay is the cost of holding money at all — funding, loss, capital and the rule, £54–105 — which is not part of the premium and is stated as the residual in the ELIMINATION CONDITIONS block
  admissible: yes
```

*Runner's call on a tension in the method.* VA-150's field (c) reads eliminates / transfers / reduces; the ELIMINATION CONDITIONS block allows a partial claim with a quantified residual. The runner reads (c) as a test of mechanism — is the cost's cause removed or moved — and the residual as a quantity. Both are stated. The Head of R&D owns the wording (RD-036, object-after 23 September 2026 12:30).

**Surplus fraction, two readings (VA-152).** Named line (mode 3): 1.0 — the ceiling is the price paid today; the fit model carries 0.95 because the checker requires a fraction strictly below one, and the undiscounted figure is reported by hand. Nameless entrant: ⚠ 0.8–1.0 (T4) — non-bank receipts-share lenders take the full tariff or more from this customer today (⚠ 15–30% equivalent), so the customer has shown a willingness to let a new form capture the whole cost. R7 inherits both bands by number and does not re-derive them.

```
ELIMINATION CONDITIONS — R2
kmc: the tariff's annual money cost, £150–300 per £1,000 drawn a year (T3)
conditions:
  C1: the drawn balance sits on a flow-backed limit, not a fixed facility | costElementRemoved: the operating premium — the decision, security, review, renewal and collections priced into the tariff (roadmap form ⚠ 20–61 per £1,000 on the fixed-per-facility lines)
      | trueToday: false | whoMakesItTrue: the venture (C1 design; WP-1, WP-3)
      | testable: the account carries no overdraft product and no renewal event after migration
  C2: the customer's existing overdraft is retired into the limit | costElementRemoved: the arrangement and renewal fee (⚠ 1–2% of the limit a year)
      | trueToday: false | whoMakesItTrue: the customer (accepts migration) and the bank's conduct function (the modifying agreement)
      | testable: the share of overdraft holders who accept migration; the fee income line on the migrated accounts is zero
  C3: the price of the limit is held below the tariff the customer paid | costElementRemoved: the information premium — the part of the tariff that prices what the bank could not observe about an applicant (Stiglitz and Weiss 1981; the flow now observed)
      | trueToday: false | whoMakesItTrue: the bank's pricing committee (PC-1); the level is C6's by number
      | testable: the saving statement shows a lower cost per £1,000 in the year after migration than the year before
residual: £54–105 per £1,000 a year — funding, expected loss, capital and the rule; the cost of holding money at all, which no form removes; plus the C6 margin above it
eliminationClaim: partial — the premium above the residual is eliminated; the residual is stated in money above
```

Every condition names who makes it true. C2 and C3 name actors other than the venture — the customer and the pricing committee — and they appear as rows in the VA-127 table.

---

## SR4 — Efficacy theory of change and strategy

```
EFFICACY THEORY OF CHANGE
  Class of problem: information asymmetry priced as a premium — a fixed-cost credit form prices small, recurring draws as facilities held against a balance sheet the lender cannot observe cheaply, and charges a tariff for that
  Theory: Stiglitz, J. and Weiss, A. (1981), "Credit Rationing in Markets with Imperfect Information", American Economic Review 71(3) — the premium and the rationing come from what the lender cannot see; Petersen, M. and Rajan, R. (1994), "The Benefits of Lending Relationships", Journal of Finance 49(1) — lender-held information lowers the cost and improves the terms; Berger, A. and Udell, G. (2006), "A More Complete Conceptual Framework for SME Finance", Journal of Banking and Finance 30 — the lending technology follows the information available
  Context (conditions, not situation): the lender already holds the account through which the customer's receipts and payments pass; the customer's draws are recurrent and small relative to the flow; the tariff is standard, not negotiated (no relationship manager below £500,000 turnover, CMA 2016); the customer can be moved from the old product to the new on the same account
  Current state: the customer pays £150–300 per £1,000 drawn a year on an arranged overdraft, renewed each year with a fee, for money the bank could price from the flow it already sees
  Desired state: the customer's drawn balance sits on the standing limit at a price below the tariff, with no renewal and no fee, and the customer can see the saving
```

**Theory robustness.** None of the three is on the fragile-findings list. Stiglitz–Weiss and Petersen–Rajan are foundations of the credit-rationing and relationship-lending literatures with long replication records; Berger–Udell is a framework paper built on them. FinRegLab (2019, 2025) is the empirical bridge and was replicated on a second data set. T-robustness PASS.

**Baseline, honestly (Step 4a).** The C1 form removes the cost drivers behind the tariff — the fixed facility, security, review, collections — and lets the limit follow the flow. It does not, by itself, move the customer off the overdraft or pass the saving to the customer. A customer can hold both the old overdraft and the new limit on the same account and keep paying the tariff on the old one. The C1 form removes the bank's cost; it leaves the customer's cost where it was.

```
MUTATION GATE — R2
baseline: the C1 form removes the facility-cost drivers behind the tariff but leaves the customer's overdraft, and its price, in place on the account
mutation_A: retire the existing overdraft into the limit at a one-time migration and hold the price of the limit below the tariff the customer paid (WP-4 + PC-1) | reason_considered: makes C1's cost removal a customer cash saving on the balance the customer already carries, without a new application | verdict: adopted | reason_verdict: testable (the saving statement), keeps the R1 risk object (the flow), and removes the fee event with the product
mutation_B: keep the overdraft and its tariff; add convenience benefits (speed, no renewal form) at the same price | reason_considered: keeps more of the bank's margin | verdict: rejected | reason_verdict: does not touch the customer's money cost — the KMC survives whole
mutation_C: price the limit as invoice finance (a discount on named receivables) | reason_considered: could be cheaper for a firm with strong debtors | verdict: rejected | reason_verdict: changes the risk object from the account's flow to individual invoices, which breaks R1
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: migration with a price condition
evolvedBFF: A bank whose credit facility is a standing property of every account with enough flow — a limit computed daily from the receipts and payments the bank already observes, drawn without an application and repaid by a fixed share of each receipt — into which the customer's existing overdraft is retired at a one-time migration, at a price held below the tariff the customer paid, so the saving is visible on the account each year; the bank keeps no per-application decision, no security process, no annual review or renewal, and no collections operation, only a rule under review and exception cells.
synthesisCheck: a deposit-funded revenue-based credit line for SME working capital (the Square Capital and MYbank mechanism inside a UK bank's own account), because the observed account flow both sets the limit and repays it — and, new at C2, the bank retires its own tariff product to do it, as a card issuer retires a legacy card into a new one on the same account
```

```
EFFICACY STRATEGY
  Retire the customer's existing overdraft into the standing limit at a one-time migration on the same account, and hold the limit's price below the tariff the customer paid — so the cost the C1 form removed from the bank leaves the customer's account as a visible saving.
  R1 consistency check: works inside the C1 form. The risk object (the flow), the repayment mechanism (the receipts share) and the removed operations are unchanged; the move adds one event (migration) and one constraint (the price condition) and removes one product (the overdraft).
```

**Design choice (one structural move).** Migration with a price condition: the overdraft is retired into the limit; the limit is priced below what the overdraft cost. One move. The saving statement (CP-1 amended) is its instrument, not a second move.

**Hypothesis.** If the customer's existing overdraft is retired into the standing limit and the limit's price is held below the tariff, then the customer's annual money cost per £1,000 drawn falls by the premium the C1 form removed. That premium is at least ⚠ £19 and up to ⚠ £233 per £1,000 a year. The bank's margin over its floor stays at or above 25%. And the customer accepts the receipts share as the price of that saving. This would be wrong if more than ⚠ 30% of overdraft holders offered migration decline it; if the loss rate on the migrated pool exceeds ⚠ 5%; or if the price condition cannot be met above the operating bar (C6 by number).

**Named assumptions.** (1) The loss rate on the flow-underwritten, observed-conduct pool is ⚠ 2.0–4.0% of drawn balance a year — the critical assumption, carried from C1, unmeasured. (2) ⚠ 40–70% of the bank's overdraft accounts are on the standard tariff at 15% EAR or above, all-in — assumed with the logic in the TAM data object. (3) The customer accepts a receipts share in place of a fixed clear-down expectation — unmeasured. (4) The CCA form of the modifying agreement for a sole trader under £25,000 is available — a desk answer with one open point (C1 record).

**Falsification condition.** Take a cohort of ⚠ 10,000 overdraft accounts offered migration. If more than ⚠ 30% decline, the customer side fails and R2 re-enters at SR1 with the receipts share as the brief. If the 12-month loss on the migrated pool exceeds ⚠ 5% of drawn balance, the hypothesis is false and the run returns to R1's SR2 with the loss line as the brief.

**Elegance test.** One move, four effects. The customer's cost falls (R2). The fee event disappears with the product (R2). The overdraft's clear-down expectation is replaced by the receipts share, so the repayment matches the cash (R6, by number). The customer's balance now lives on the limit, which lives where the flow lives (R8, by number). ✓

**Considered / not chosen (VA-4).** Baseline: the C1 form with the overdraft left in place. A — migration with a price condition → adopted. B — convenience at the same price → rejected, the KMC survives. C — invoice-finance pricing → rejected, breaks R1. D — offer the limit only to new draws and let the overdraft run off at renewal → considered; rejected because it leaves the customer paying the tariff for up to a year and makes the saving invisible; the run-off is kept only as the route for a customer who declines migration. E — cut the tariff on the existing overdraft without changing the product → considered; rejected because it is the roadmap form with a lower price, which R1's failure test already found is not the venture, and it keeps the renewal, the review and the collections cost that fund the tariff.

---

## SR5 — Business form factor (C2)

```
CLO GATE — R1 (carried, unchanged)
cloZone: Delivering
cloName: holding each facility as a fixed, secured, scheduled exposure that is reviewed and collected
workaroundStrategy: the facility as a standing property of the account — a limit computed from the flow, drawn without application, repaid by a fixed share of receipts
newBFFRequired: true
```

**Cumulative BFF (C1–C2), restated from the rerun's evolved BFF.** *A bank whose credit facility is a standing property of every account with enough flow — a limit computed daily from the receipts and payments the bank already observes, drawn by the customer without an application and repaid by a fixed share of each receipt as it arrives — into which the customer's existing overdraft is retired at a one-time migration, at a price held below the tariff the customer paid, so that the saving is visible on the account each year; the bank keeps no per-application decision, no security process, no annual review or renewal and no collections operation, only a rule under review and exception cells for accounts whose flow stops or whose holder declines.* R3–R10 may rewrite this, including fundamentally.

**Property-holder test (VA-71).** Three new properties are asserted at C2. "The existing overdraft is retired into the limit" — holder: the customer (accepts) and the bank's product and conduct function (the modifying agreement or variation notice); carried by WP-4 and the account line track in the CTM v2. "The price of the limit is held below the tariff the customer paid" — holder: the bank's pricing committee; carried by PC-1 and the pricing track; the price itself is C6's by number. "The saving is visible each year" — holder: the account line (produces the statement); carried by CP-1 as amended. The C1 properties and their holders are unchanged.

**Central structure.** Unchanged: the standing limit computed from the flow and repaid from receipts. The C2 move hangs from it — remove the limit and the migration has nowhere to go.

**Three-function check.** Cost creation: unchanged at C2 — the migration is a one-off (⚠ £0.1–0.5m of notices; ⚠ 5,300–8,200 handler hours), carried to C3 by number; the saving statement adds ⚠ £0.003 per £1,000 a year. Exchange: the customer now pays a price below the tariff on a balance the bank already carried; the structure is C6's by number. Margin retention: the floor is unchanged at £54–105 and the ceiling is £150–300, so the margin at the worst corner is 35.7% (financial check below). At-scale test: every C2 activity scales with accounts (the migration once; the statement yearly); the binding gate stays the loss rate.

**Simplicity test.** Four things are removed from the C2 cut. The price and its structure (C6). The treatment of a customer who declines migration, beyond "keeps the overdraft to its next renewal" (an exception row, not a design). The switching cost the retired overdraft creates (R8 by number). The limit for a customer priced below the tariff today (recorded in the TAM as SC-OD-BELOW-BAND; whether the price condition can hold for that class is C6's by number).

**Synthesis check (VA-1).** Looks like **a card issuer's product migration** — a legacy card retired into a new one on the same account, balance carried across, terms varied by notice — applied to **a revenue-based credit line** (Square Capital; MYbank). The shared mechanism is the same account holding the old and the new product, and the ledger reclassifying the balance. Limit of the analogue: a card migration keeps the price; this one lowers it, and the price is what the customer is being asked to accept a receipts share for.

**Research firewall.** Held. The bank's pre-assessed limit is the baseline (C1 record, SR1). The C2 move retires the bank's own tariff product; the roadmap form does not.

**Regulatory desk answer, new at C2 (legal questions are desk questions, 14 September 2026).** For a sole trader or a partnership of two or three persons borrowing under £25,000, the overdraft is a regulated running-account credit agreement (CCA 1974 s.16B). Migration varies the agreement: under s.82 a variation by the creditor takes effect on notice in the prescribed form, and a modifying agreement is itself a regulated agreement. INFERENCE: the conduct function can effect migration by a modifying agreement signed in the app, with the receipts share as a term, and the price condition satisfies the Consumer Duty's price-and-value outcome by construction (the customer pays less for the same money). For a limited company there is no regulated agreement; a variation of the account terms on notice suffices. What a ruling would settle and this desk cannot: whether the receipts share on a regulated running account is a "variable repayment" needing a specific form — carried from C1, owner the bank's conduct function.

---

## Excluded population — what was decided about it

The selected customer is a current buyer. This record says so in its first line and here. The population the conventional form excludes was mapped at the rerun and is disposed as follows:

- **New to trading (314,000 a year, BBB 2025/26, S1)** — excluded by the flow gate (G-C1-1 in the TAM data object): no flow exists from which to compute a limit. Recorded as sub-class SC-NO-FLOW-HISTORY, KMC-0, not addressable. No later requirement is named as its owner; it is a structural limit of the form, not a carried item.
- **Owner-funded (about 1.25m, 22% "had to" inject personal funds, SME Finance Monitor)** — disposed as an **unmeasured input**. Owner: the insider (amount and duration of owner injections by account-conduct band). Convergence event: a priced band from the bank's own data or from the SME Finance Monitor's amount question. Pivot trigger: if the priced cost per £1,000 of need exceeds £150, this sub-class re-enters as a second selected customer at a rerun of R2.
- **Deterred (about 285,000, 5% would-be seekers)** — disposed as an **unmeasured input** on the same terms; owner the insider; convergence a priced foregone return; the same pivot trigger.
- **Both costs stated and compared.** Current buyer: £150–300 per £1,000 drawn a year, T3. Excluded populations: unpriced — incidence published, amount not. The comparison cannot be made in money today, which is why the current buyer was selected and why the excluded populations carry a re-entry trigger rather than a verdict.

---

## VA-106 synergy line

This move also serves three later requirements, by number only. **R3** — the migrated balance repays from receipts, so the exposure clears itself from the flow that justified it (mechanism: the receipts share on the migrated draw). **R6** — the receipts share replaces the overdraft's clear-down expectation, so repayment matches the customer's cash (mechanism: the receipts share). **R8** — the retired overdraft leaves the customer's balance on the limit, which lives where the flow lives (mechanism: migration). Nothing is said about how those requirements solve them.

---

## Actor business cases (VA-127)

Gains are priced by OCV class (expended · foregone · risk-borne · friction) with band and tier. A FAIL row with no named force would be a design defect; there is none.

| Actor | Behaviour needed | How often | Gain (OCV class · band · tier) | Cost (priced) | Best alternative | Surplus verdict |
|---|---|---|---|---|---|---|
| The selected customer (⚠ 41,800–113,050 at the bank, proxy; 250,800–678,300 across the market) | accept migration of the existing overdraft; accept a receipts share as the repayment term | once, then continuous | **expended** — the tariff outflow displaced less the price paid: ⚠ £19–233 per £1,000 drawn a year (T4; bounded by KMC − operating bar) · **expended** — the renewal fee removed: ⚠ £10–20 per £1,000 of limit a year (T4) · **friction** — no renewal form: about 26 hours per application (Mills and McCarthy 2014), ⚠ £500–1,000 of owner time (T4) | **friction** — cash in hand falls while drawn, by the receipts share (⚠ 5–15% of each receipt, T4); the modifying agreement, ⚠ 0.5 h · **risk-borne** — the limit falls when the flow falls, where the overdraft limit was fixed to renewal: the cost of a lower limit in a bad month, unpriced | keep the arranged overdraft at the tariff | **positive at every corner on money** (the gain's low corner £19 exceeds the fee alone); **unmeasured on acceptance** of the receipts share — trigger above ⚠ 30% decline. PROVISIONAL |
| The bank's pricing committee | adopt the price condition (PC-1): hold the limit's price below the tariff on migrated accounts | once, then each pricing cycle | **expended** — the bank's margin over its floor at the condition: ≥ 25% at the worst corner (35.7% at the KMC; the price is C6's) · **foregone, avoided** — the tariff revenue an attacker at a lower price would take over the period (Reading D below, ⚠ 20–40% of the pool, T4) · **risk-borne, avoided** — fair-value exposure under the Consumer Duty on a tariff above the cost of the exposure (unpriced) | **foregone** — tariff revenue given up on the migrated pool: ⚠ £19–233 per £1,000 × ⚠ £0.4–1.9bn = ⚠ £8–440m a year (T4; the width is the width of the inputs) | keep the tariff and let a price attacker come, or cut the tariff without changing the product (option E, rejected as the roadmap form) | **PROVISIONAL — positive where Reading D is real, negative where the core keeps the customer anyway.** Named forces: the Consumer Duty price-and-value outcome (PRIN 2A, FCA 2022); the bank's own roadmap already re-prices on conduct; non-bank receipts-share lenders exist at the tariff today. The revenue given up is an unmeasured input, owner the insider |
| The bank's product and conduct function | sign off a CCA-compliant modifying agreement (sole traders under £25,000) and a variation notice (companies); set the conduct standard for the saving statement | once, then per rule change | **risk-borne, avoided** — a Consumer Duty fair-value finding on a tariff product the bank could have priced lower (unpriced; a regulatory outcome, not a fine estimate) · **expended** — fewer renewal-fee complaints handled: ⚠ £5–20 per complaint avoided (T4) | legal and conduct work ⚠ £50–150k one-off (T4); two people added to the function (AOM v2 3c) | do nothing: keep the tariff product and its renewal | positive — the cost is small against the function's existing budget; the force is regulatory and already applies. PASS, one open point (the receipts share's CCA form) |
| The account line (Case A) | reclassify the overdraft balance as a draw at migration; produce the saving statement yearly | once; yearly | none needed — an internal dependency | engineering on the ledger (a build item); ⚠ £0.1 per statement | — | internal; no case row required |
| The exception cell | handle a decline or a query on the statement | ⚠ 10% of overdraft-origin accounts once; ⚠ 2% of drawn accounts a year | internal | ⚠ 1,000 hours a cell a year recurring; ⚠ 2,300–3,600 hours a cell once | — | internal; sized in the AOM v2 |
| The customer's accountant or software | none at C2 | — | — | — | — | `[REQUIRES C7]`; not an actor here |
| PRA and FCA | none new | — | — | — | — | not an actor at C2; permissions unchanged; the Consumer Duty applies as it did |

```
POOL AT RISK — R2 (VA-147)
  Incumbent class: UK banks running standard-tariff business overdrafts on business current accounts — the bank itself is the incumbent (Path C, mode 3). Typical incumbent's tariff-overdraft revenue a year: ⚠ £63–577m (proxy: ⚠ 41,800–113,050 tariff accounts × ⚠ £10–17k drawn × 15–30%; T4 — the bank's own figure is a red field)
  Reading S (sub-breakeven share of fees): ⚠ 5–20% (T4) — the facilities small enough that the roadmap form's per-facility lines exceed the tariff they earn (C1 record: on a £10,000 facility the operating line alone is ⚠ £60–200 per £1,000)
  Reading D (an attacker's take at the venture's price over three to five years): ⚠ 20–40% (T4) — anchor: SME current-account switching is low (about 4% a year, CMA 2016), which holds the floor of the band down; a price below the tariff on the same account, with no switch required, is the reason the band is not lower than 20%
  Pool per incumbent, fees a year: Reading S ⚠ £3–115m · Reading D ⚠ £13–231m (T4; the bands multiply)
  Channelling condition: partly — the core loses the sub-breakeven facilities anyway (Reading S; the bank's roadmap is already re-pricing on conduct, insider 18 Sep 2026) and keeps the rest unless a priced attacker arrives; evidence: non-bank receipts-share lenders take this customer today at the tariff, not below it, so the attacker at a lower price does not yet exist in public data
  Held to R7: the share channelled and the terms · Held to C6: the payment form
```

---

## Actor tracks (VA-102)

| Actor | Track in the CTM v2 | Introduced | Holder of what |
|---|---|---|---|
| the business | the customer journey, four phases | C1; C2 adds migration, the saving, the price condition, the no-return row | draws; accepts the receipts share; accepts or declines migration |
| the account line | account line track | C1; C2 adds the migration row | the flow; the term; the modifying agreement or variation notice |
| the limit engine and exception cells | limit engine track | C1; C2 adds the decline and query row | the rule; the only human contact |
| the pricing committee | pricing track | C2 | the price condition; the price is `[REQUIRES C6]` |
| PRA and FCA | regulator track | C1, unchanged | permissions and capital |
| the partner who brings the customer | partner track | `[REQUIRES C7]` | flagged |

---

## BFF delta and upstream re-verification (VA-103)

| Item | At C1 | At C2 | Changed by |
|---|---|---|---|
| Made | a limit computed daily from the flow; no acceptance event | unchanged | — |
| Sold | never accepted; live in the account | live in the account; the existing overdraft retired into it at migration | SR4 (WP-4) |
| Delivered | one running limit; the term loan dissolves into a draw with a receipts share | one running limit; the overdraft balance becomes a draw with a receipts share; the saving shown yearly | SR4 (WP-4, CP-1) |
| Paid | the price paid today; structure `[REQUIRES C6]` | a price held below the tariff the customer paid (PC-1, a condition); structure and level `[REQUIRES C6]` | SR4 (PC-1) |
| Gate | ⚠ six months of flow; the start-up `[REQUIRES C2]` | ⚠ six months of flow; the new-to-trading business excluded and recorded in the TAM data object, owned by no later requirement | SR3 (TAM v2) |

**One row per earlier requirement — named checks and FIT on the BFF as it now stands:**

| Requirement | Named checks | Result on the C2 BFF | FIT |
|---|---|---|---|
| R1 (C1 record v2) | CLO stated as an operation in the delivering zone; elimination not reduction; property-holder test; existence test; the R1 failure test (venture, not improvement) | **re-verified — unchanged or stronger.** The CLO and its removal are untouched. The failure test is stronger: migration retires the bank's own tariff product and the price condition binds the pricing committee to price below it; neither is an improvement the roadmap form can adopt without changing what it sells and how it prices. The C1 property holders are unchanged | **re-verified.** Floor unchanged at £54–105 (AOM v2 section 6, four layers). The C1 ceiling (the whole-book price £75–120) still gives −32.1% at the worst corner for the book as a whole; that reading is superseded for the selected customer by the C2 ceiling, and stays as recorded for the loan-user sub-class (SC-LOAN-USER, KMC £75–90 — below the floor's high corner, carried to C6 by number). Mode 3 at C1 was non-gating; nothing at C1 FAILED |

Function-gate re-run: not applicable — F1 closes at C3.

---

## Financial check — the floor, the ceiling and the carrying check

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn (AOM v2 header). **Component set the verdict was computed on (VA-74):** WP-1, WP-2, WP-3, WP-4, CP-1 (amended), PC-1 (condition).

```
COST FLOOR — four-layer breakdown        £ per £1,000 of average drawn balance a year (all ⚠ T4)

  PVC  funding 15–30 · expected loss 20–40 · computing 2–5 · exceptions and write-off 3–8      40–83
  RC   HQ ⚠ 47 people and technology £7.2–12.8m ÷ £3.4–5.7bn (double count removed)            2–5
  SC   [REQUIRES C3] — the one-off migration cost (£0.1–0.5m; 5,300–8,200 hours) recorded there by number
  IC   capital on drawn 10.8–13.5 · capital on undrawn 1.6–3.4                                 12–17
  ─────────────────────────────────────────────────────────────────────────────────────────────────────
  COST FLOOR (PVC + RC + IC only)                                                              54–105   ← SC excluded until C3

REQUIRED PRICE (25% margin — the OPERATING bar)         67.50–131.25   ← floor × 1.25
REQUIRED PRICE (capital payback — the CAPITAL bar)      26.05–43.68    ← £148.5m required year-five revenue (PCO parameters) ÷ £5.7–3.4bn
BINDING REQUIRED PRICE                                  67.50–131.25   ← the operating bar at every corner
PRICE CEILING (KMC — R2 = WTP_low)                      150–300        ← the standard-tariff outflow (T3)

HEADROOM (ceiling low − binding bar high)               18.75
FMOS (WTP_low − Cost_high) ÷ Cost_high                  42.9% undiscounted · 35.7% at the fit model's 0.95 surplus fraction
```

```
CARRYING CHECK — R2
kmc:                     £150–300 per £1,000 drawn a year (T3)
operatingBar:            £67.50–131.25 (floor 54–105 × 1.25)
capitalBar:              £26.05–43.68 (PCO parameters: required year-five revenue £148.5m, from the capital envelope ⚠ £100m ASSUMED and the PCO's return and horizon, ÷ drawn book ⚠ £3.4–5.7bn)
bindingBar:              £67.50–131.25 | which: operating
headroomOnBinding:       £18.75 at the worst corner (150 − 131.25); £232.50 at the best (300 − 67.50)
carries:                 true
pcoEstimateVsDerived:    the PCO carried no KMC estimate in mode 3; the C1 record's whole-book price £75–120 stood in for it; the derived KMC is 2.0–2.5× higher for the selected customer; the PCO screen re-run on the derived figure: loss-to-price ratio (KMC ÷ binding bar) 1.1× at the worst corner and 4.4× at the best, against the PCO's 2× bar — clears at the centre (225 ÷ 99.4 = 2.3×), fails at the worst corner. Selection holds; the worst corner is named as the finding
floorCompleteness:       SC excluded — this bar is a LOWER BOUND until C3 sizes it
```

**Capital bar stated (registry row).** Required return, horizon, terminal assumption and margin are the PCO's parameters (`bank-deposits-lending-pco-v1-2026-09-18.md`, section 1, runner-drafted 18 September 2026, ratified by lapse 20 September 2026 17:00): capital envelope ⚠ £100m ASSUMED for the portfolio; required year-five revenue £148.5m. Labelled as the venture's ruling by lapse, not a canon rule. The runner did not re-derive them.

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C2.yaml`).** By hand, replicating the script's arithmetic at the 0.95 surplus fraction: ceiling £142.50–285; net contribution £37.50 at the worst corner; **35.7% at the worst corner; 427.8% at the best. PASS on the 25% gate, INDICATIVE (SC excluded).** Undiscounted: 42.9% and 455.6%. **The script did not run:** `fit_margin.py` refused because the checking scripts carry two edits and one new file awaiting the principal's batched seal (verifier r2, section "Script run"). The runner does not seal and does not run a copy elsewhere. The margin figure in this record is runner-computed on the model file's declared inputs and is to be replaced by the script's output after the seal — recorded as a failed registry row below with what was decided.

**Stress row, informative only.** If the C2 revenue base were the migrated pool alone (⚠ £0.4–1.9bn) rather than the whole drawn book, the capital bar would be £78–371 per £1,000 and would bind at the worst corner. It is not a gate: R1's revenue base is the whole book, and the PCO's required revenue is for the line, not the segment. Stated so the reader can see what the capital bar depends on.

**Binding gate — found by driving the design across its gates (VA-84).** Gates tested, in the order the design meets them:

1. margin at the KMC ceiling — 35.7% at the worst corner; 10.7 points above the 25% gate;
2. expected loss on the flow-underwritten pool — assumed ⚠ 2.0–4.0%; the 25% gate holds at the worst corner up to 4.9% (floor 114 at a 6% loss line; 142.5 ÷ 114 − 1 = 25.0%); zero margin at 7.75%; at the pivot trigger of 5% the margin is 23.9%, BORDERLINE;
3. tariff share — a material population at 15% EAR or above: ⚠ 40–70% of overdraft accounts, assumed with its logic stated; it moves the size of the prize, not the margin per £1,000;
4. migration and receipts-share acceptance — unmeasured; trigger above ⚠ 30% decline;
5. the CCA form of the modifying agreement for sole traders under £25,000 — a desk answer with one open point; a standing constraint;
6. capital on undrawn limits at scale — costed, small, and unchanged by migration;
7. the price condition holdable above the operating bar — 142.5 ≥ 131.25 at the worst corner, headroom 11.25; the level is C6's by number.

**First to fail on today's evidence: (2), the loss rate.** Margin to it: 0.9 points of loss above the assumption's own high corner (4.0% → 4.9%) before the margin drops below 25%. **A margin of under one point of loss against an assumed value is the finding, unchanged from C1, and it is reported unsoftened.** The insider's loss rate on a flow-underwritten, observed-conduct pool is the first thing to correct.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  measure:      expected loss as a share of average drawn balance a year
  threshold:    4.9% — the 25% margin fails above it at the worst corner; 7.75% — the margin is zero
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.9 points at the assumed high corner (18% of the assumed value)
  pivot:        above ⚠ 5% at the worst corner → R1's SR2 with the loss line as the brief
```

**Independence (VA-97).** The margin of safety and the binding gate share the loss line: the margin is the ceiling less a floor in which the loss line is the largest term, so the margin is a transform of the gate. They are reported as **one financial check**. An independent second check would measure a count, not a rate: gate (3), the tariff share, or gate (4), the acceptance rate. Neither is public; both are the insider's. Until one is measured, the financial check has one independent input and says so.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Diagnosis names a single cost, not a category ✓ (the tariff's annual money cost on the drawn balance).
- ToC — class of problem named ✓; theory named with researcher, year and paper ✓; context as conditions ✓; outcome as a state ✓ ("the customer's drawn balance sits on the limit at a price below the tariff" — "we will migrate" does not fit).
- Strategy — exactly one structural move ✓; hypothesis with falsification and named assumptions ✓.
- Mutation gate emitted before the strategy; two genuine mutations; justification mode false ✓.
- KMC admissibility block filled; admissible ✓ (tension with the elimination block named, runner's call).
- Elimination conditions cover the KMC; residual stated in money ✓.
- Property-holder test ✓.
- Credibility mechanism (VA-81) ✓. The saving statement is the instrument: the receiver is the customer; the proposition is "you pay less than you did"; the instrument the customer uses today is the annual overdraft renewal letter and the bank statement; the supplier of the instrument is the account line. Re-derived at C2 because the receiver changed from "a customer who has never borrowed" (C4 by number) to the current overdraft holder.
- Pointing test ✓. The design attacks the premium's cause (the operations and the information gap), not the tariff as a number.
- Limit of the analogue stated ✓.
- Completeness contract (VA-73) ✓. SR1–SR5 present; the excluded-population section present.
- No forward references (VA-80) ✓. R3, R6, R7, R8 and C6 by number only; PC-1 is a condition, not the C6 price.
- VA-106 line present ✓. VA-103 table present, one row per earlier requirement ✓. VA-127 table present, every non-venture behaviour priced ✓. VA-147 block present ✓. VA-82 items classified ✓ (below).
- Binding gate by driving ✓. Shared-input declaration ✓.
- Existence test (VA-92) ✓. The holder of the price condition exists inside the bank (the pricing committee), activated by the condition. The maximum the form can hand back per £1,000 is the headroom over the operating bar, £18.75 at the worst corner. That is also the least the customer must gain for the row to be positive.
- Incremental write ✓.
- Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r2-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v2 and AOM v2 are written as documents; the model files (`bank-credit-facility-ctm-model-at-C2.yaml`, `bank-credit-facility-aom-model-at-C2.yaml`) are not, so the coverage and trace scripts did not run — **build item**, carried from C1. Every AOM v2 activity names its flow and a driver that resolves to a named quantity, event or actor (section 0, RD-031); no cost line is a share of revenue ✓. Capacity: ⚠ 17,000 exception hours per cell a year covering ⚠ 100,000 drawn accounts; ⚠ 2.28 cells at scale, ⚠ 38,800 hours; **the capacity figure is 17,000 hours per cell and every calculation in this record uses it.** Role support: every performer, including the pricing committee and the cell lead, has a supervisor, a trainer and a reviewer ✓. Unit sizing: a cell covers its ⚠ £0.8–1.05m from a fraction of a per cent of the revenue on the ⚠ £1.5–2.5bn it covers (PASS on contribution); stand-up ⚠ 6–10 weeks. Component carriage: every C2 transition in the CTM v2 is carried by WP-4, CP-1, PC-1 or an exception row, or flagged ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin of safety 35.7% at the worst corner, 427.8% at the best, by hand (42.9% and 455.6% undiscounted); PASS on the 25% gate; the script refused pending the seal. Carrying check: carries at every corner, headroom £18.75 on the operating bar. Binding gate: the loss rate, unmeasured, 0.9 points of margin at the assumed high corner. One independent input. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- `fit_margin.py` refused (the toolchain awaits the principal's seal) — **build item**; owner: Tom (the seal); convergence: the script's output pasted into the verifier r2 and this record's margin line replaced; the by-hand figures stand until then.
- CTM and AOM model files absent, so `check_model_coverage.py` and `check_requirement_trace.py` did not run — **build item**; owner: the Venture Architect seat if the run proceeds; convergence: the model files exist and both scripts pass before C4 opens.
- The loss rate on the flow-underwritten, observed-conduct pool — **unmeasured input**; owner: the insider; convergence: a 12-month loss on a ⚠ 10,000-account migrated cohort; pivot trigger: above ⚠ 5% at the worst corner → R1's SR2.
- The tariff share (⚠ 40–70%) — **unmeasured input**; owner: the insider; convergence: the count of overdraft accounts at 15% EAR or above, all-in.
- Migration and receipts-share acceptance — **unmeasured input**; owner: the insider (a pilot cohort) — not fieldwork by the venture; convergence: the decline rate; trigger: above ⚠ 30%.
- Tariff revenue given up on the migrated pool against Reading D — **unmeasured input**; owner: the insider; convergence: the bank's overdraft revenue on the tariff segment and its attrition to non-bank lenders.
- The CCA form of the modifying agreement with a receipts share — **standing constraint** with one open point; owner: the bank's conduct function.
- Owner-funded and deterred populations unpriced — **unmeasured inputs** with re-entry triggers (the excluded-population section above).
- New-to-trading businesses — **structural limit** of the form (no flow, no limit); the residual is bounded (314,000 a year, S1) and paired with the validation that would address it (none in this form; a different form would be a different venture). Caps at PROVISIONAL with the rest.

```
GATE VERDICT — on the cumulative architecture C1–C2
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files; coverage and trace scripts not run)
  financial limb:    PROVISIONAL     FMOS 35.7% worst corner / 427.8% best (by hand; script refused pending the seal) · carries: true, headroom £18.75 · binding gate: loss rate on the pool — unmeasured, 0.9 points of margin at the assumed high corner
  dispositions:      6 unmeasured inputs, 2 build items, 1 standing constraint, 1 structural limit (above)
  capacity figure:   17,000 exception hours per cell a year, 100,000 drawn accounts per cell — used throughout   VA-91
  independence:      one financial check — the margin is a transform of the loss gate; an independent second check would be a count (tariff share or acceptance rate)   VA-97
  gates driven:      7; first to fail on evidence: the loss rate, margin 0.9 points at the assumed high corner   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r2-2026-09-21.md                        VA-90
  inherited:         R1 PROVISIONAL (C1 record v2: 1 build item, 4 unmeasured inputs) — R2 cannot exceed it; PCO ratified by lapse 20 Sep 2026 17:00, so the PCO cap is lifted   VA-95
  cumulative span:   C1–C2; worst inherited verdict: PROVISIONAL (R1)
  repairs:           none claimed
  VERDICT:           PROVISIONAL
```

**R2 failure test.** Would R2 have failed? Three conditions were set at the rerun. First, the bank cannot identify a material population at 15% EAR or above: unmeasured, assumed ⚠ 40–70% with logic — not a failure on the evidence. Second, the loss-adjusted floor exceeds £120 per £1,000: it is £105 at the high corner, so this passes; it would reach £120 at a 5.5% loss. Third, C6 cannot hold the price below the tariff: 142.5 ≥ 131.25, so the condition is holdable at the worst corner with £11.25 of room. None fails today. The nearest is the second, through the loss rate, which is why the loss rate is the binding gate.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the price, its structure and its presentation — C6
  - whether the price condition can hold for the below-band overdraft user and the loan user — C6
  - the one-off migration cost and the launch-year handler hours — C3
  - the switching cost the retired overdraft creates — R8
  - the customer's conviction that the limit is real — C4
  - who brings the customer to the limit, and the share of the pool channelled — C7
  - the surplus-fraction bands (named line 1.0; nameless entrant ⚠ 0.8–1.0) — inherited by R7
- **Unmeasured inputs (owner the insider in every case):**
  - the loss rate on the migrated pool — trigger > ⚠ 5%
  - the tariff share
  - migration and receipts-share acceptance — trigger > ⚠ 30% decline
  - tariff revenue given up against Reading D
  - the owner-funded and deterred costs — re-entry trigger: priced cost > £150 per £1,000
  - every ⚠ figure
- **Build items:**
  - the script run of `fit_margin.py` after the seal (owner Tom)
  - CTM and AOM model files and the coverage and trace scripts
  - the ledger's reclassification at migration and the saving statement on the account line
- **Standing constraints:**
  - the CCA modifying agreement for sole traders under £25,000 with a receipts share
  - model-risk validation of the rule (SS1/23)
  - the 10% credit conversion factor on undrawn limits from 1 January 2027
  - the Consumer Duty price-and-value outcome on the migrated accounts
- **Structural limit:** the new-to-trading business (no flow, no limit), bounded at 314,000 a year.
- **Unowned design defects:** none.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Diagnosis names a single cost | PASS | SR3 |
| ToC — class of problem | PASS | SR4 block |
| ToC — theory (researcher + year + paper) | PASS | SR4 block |
| ToC — context (conditions, not situation) | PASS | SR4 block |
| ToC — outcome (a state) | PASS | SR4 block |
| Strategy — one structural move | PASS | SR4 |
| Strategy — hypothesis with falsification and named assumptions | PASS | SR4 |
| KMC admissibility (VA-150) | PASS, tension named | SR3 block |
| Surplus fraction, two readings (VA-152) | PASS | SR3 |
| CTM update — traceability | PASS | CTM v2 section 4 |
| AOM — every activity ↔ a flow | PASS | AOM v2 3a–3c, Flow column |
| AOM — volume drivers (resolving references, RD-031) | PASS | AOM v2 section 0 |
| AOM — no ratios | PASS | AOM v2 (the 0.16–0.45% line is stated for scale; no cost derives from it) |
| AOM — role support | PASS | AOM v2 section 4 |
| AOM — LMU sizing | PASS | AOM v2 section 5 |
| FIT — margin (per-requirement, 25%) | PASS at 35.7%, INDICATIVE — **script REFUSED**, by hand | verifier r2 |
| FIT — I check | PASS | verifier r2 |
| FIT — T check | PASS | verifier r2 |
| Synergy line (VA-106) | PASS | VA-106 section |
| Loop gate (PASS or fully specified PROVISIONAL) | PASS — PROVISIONAL fully specified | close |
| Three-limb close (VA-89, VA-91) | PASS — one capacity figure | close |
| Financial halves shown independent (VA-97) | PASS — one check, second named | financial check |
| Partner business case (VA-99) | not applicable — no partner at C2; the accountant is C7's | VA-127 |
| Structural-limit disposition (VA-101) | PASS | close |
| Verdict composes forward (VA-95) | PASS — `check_verdict_order.py` not run (same toolchain refusal) | GATE VERDICT |
| Upstream re-verified (VA-103) | PASS | VA-103 tables |
| Actor business cases (VA-127) | PASS — no FAIL row; one PROVISIONAL row with named forces | VA-127 table |
| Pool at risk (VA-147) | PASS | VA-147 block |
| Existence test (VA-92) | PASS | close |
| Binding gate by driving (VA-84) | PASS | financial check |
| No parallel close (VA-85) | PASS — sequenced; R3 not opened | status file |
| TAM as a validated data file (VA-83) | PASS | SR3 |
| Excluded population sized | PASS — sized where public; disposed where unpriced | excluded-population section |
| Capital bar stated | PASS | financial check |
| Classified carried items (VA-82) | PASS | carried items |
| Independent verification artefact (VA-90) | PASS — artefact exists; its script half is queued | verifier r2 |
| No forward references (VA-80) | PASS | throughout |
| Credibility mechanism (VA-81) | PASS — re-derived for the new receiver | close |
| Conventional cost line named and removed (F2) | not applicable — R4–R7 rows | — |
| Position-holding assumption (F3) | not applicable — R8–R10 rows | — |
| Mode 2 verdict form (C1) | not applicable — mode 3 | — |
| Counterfactual costed (F1 gate) | not applicable until the C3 close | — |

**Rows that did not pass, and what was decided:** FIT — margin: the script refused; the arithmetic was done by hand and the re-run is queued behind the seal (build item, owner Tom). VA-95 order check: the same refusal; the verdict order was checked by reading (R2 PROVISIONAL ≤ R1 PROVISIONAL). No row FAILED on the design.

---

## The population the new floor would open — by-product only, ⚠ UNVALIDATED (RD-024 (f))

Unchanged from C1. The 1.25m owner-funded and 285,000 deterred (market proxies) who hold an account with flow are on the near side of the flow gate and carry a re-entry trigger at R2; the 314,000 new-to-trading a year are on the far side. Not claimed.

---

## Quality check

| Test | Result |
|---|---|
| KMC on the chosen rung; outcome ladder emitted before selection | ✓ |
| KMC admissibility block filled before SR4 | ✓ |
| Theory named and citable; robustness stated | ✓ |
| Mutation gate before the strategy; two genuine mutations | ✓ |
| Strategy names one structural move, not outcomes | ✓ — migration with a price condition |
| Considered / not chosen, five candidates with reasons | ✓ |
| Actor business cases priced by OCV class or marked PROVISIONAL | ✓ |
| Margin by the correct formula, cost denominator, bands from the registry | ✓ — by hand; script queued |
| Carrying check: both bars, the binding one named, carries true | ✓ |
| Named assumptions (loss rate; tariff share; acceptance; CCA form) | ✓ |
| Pivot trigger written | ✓ — loss > ⚠ 5% at the worst corner |
| Verdict composes forward (R1 PROVISIONAL → cap) | ✓ |
| Excluded population disposed with owner, convergence and trigger | ✓ |
| No tooling vocabulary or metaphor in prose; house-style checker run | run on file save — see changelog |

---

## Sources (in addition to PCO S1–S12 and C1 record C1–C12)

| # | Source | Used for |
|---|---|---|
| D1 | HSBC UK, Lloyds Bank, Bank of Scotland — business overdraft product pages, read 21 September 2026 | representative EARs 14.54% and 15.62% on unsecured business overdrafts up to £25,000 (T1) |
| D2 | BVA BDRC, SME Finance Monitor — December 2024 rolling charts; Q4 2024 management summary; Q4 2025 pp.140–145 | overdraft use 11–17%; bank loan 9%; personal funds 35% (22% "had to"); would-be seekers 5% |
| D3 | DBT, Business Population Estimates 2025 | 5.7m private-sector businesses |
| D4 | UK Finance, Business Finance Review 2025 Q3 | overdraft utilisation 47% |
| D5 | DBT and HM Treasury, government response to the Small Business Access to Finance call for evidence, 4 December 2025 | read and found to carry no rate figure — the run note's attribution corrected |
| D6 | DBT and the Office of the Small Business Commissioner, Late Payments Research 2025 | late payment as a market-wide condition (struck rung L2b) |
| D7 | FCA, PRIN 2A (the Consumer Duty), 2022 | the price-and-value outcome as the named force on the conduct and pricing rows |
| D8 | Consumer Credit Act 1974, ss.16B, 82 | regulated running-account credit under £25,000; variation and modifying agreements |
| D9 | CMA, Retail banking market investigation, 2016 | SME switching about 4% a year; no relationship manager below £500,000 |
| D10 | Anthony, S., Gilbert, C. and Johnson, M., *Dual Transformation* (2017) | the pool-at-risk readings (VA-147) |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | First record. Closes R2 on the rerun of 19 September 2026. Runner-drafted, object-after. TAM v2, CTM v2, AOM v2, fit model at C2 and verifier r2 written alongside. KMC source corrected from the government call for evidence to published tariffs. `fit_margin.py` refused pending the principal's seal; margin by hand. House-style checker run on this file and the verifier before filing. |
