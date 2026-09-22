# A business bank's credit facility line — challenge three (R3) record v2 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R3 carries — the scaling working capital sits in the wait for loss evidence, not in the drawn book, and the one move removes the wait by validating the rule on exposure the bank already holds — and the verdict cannot exceed R1's and R2's PROVISIONAL (VA-95). F1 closes at this record with a floor of ⚠ £54–106 per £1,000 drawn a year on all four layers and a margin of 34.4% at the worst corner. Binding gate: the loss rate on the flow-underwritten pool, unmeasured; 25% margin fails above 4.8% at the C3 floor — **re-driven at the C10 floor to 4.45% at the set price of £140 (4.05% at ⚠ £135)**; the trial band below carries the C10 value (v2, route-back H1 of the C10 consistency audit). Pivot trigger: above ⚠ 5% (C2's ruling, unchanged).

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c2-v1-2026-09-21.md` (R2, PROVISIONAL, object-after to 23 September 2026 17:00) and `bank-credit-facility-c1-v2-2026-09-18.md` (R1, PROVISIONAL). **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse at 20 September 2026 17:00. **Mode:** 3 — just show me. The population is the bank's current account base; the scale is the bank's own volume; the R2 ceiling is the cash outflow the selected customer pays today; the gate is the three-check close. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules (27 August and 1 September 2026); every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**Sections in this record.** Defined terms. SR1 to SR4. The two models and the capital path. Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the F1 re-run. Financial check. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

As in the C1 and C2 records: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *exception cell*, *standard tariff*, *migration*, *price condition*, *carrying check*. New at C3:

- **Working capital, in a bank.** A bank has no stock and no plant. What it commits before a unit earns is (a) the funded balance, (b) regulatory capital held against the exposure and (c) the loss allowance it books on day one under IFRS 9. The third is the one that moves with evidence: an allowance on a new rule is held higher while the rule is unproven and released as outcomes arrive.
- **Shadow limit** — the standing limit the rule computes and records for an account, without the customer being able to draw on it. The same computation as the live limit; only the release differs.
- **Back-test** — running the rule over the bank's own past daily flow on the same accounts, and comparing the limit it would have set with the loss the bank actually took. Evidence that arrives in weeks, not in the years a forward cohort takes.
- **Release** — the event at which a shadow limit becomes drawable in the account. Released by stage, never by application.
- **Stage** — a step of the scaling path with its own capital, its own kill band and its own reading. Stage 0 the back-test; Stage 1 the migrated overdraft accounts; Stage 2 the replicas; Stage 3 at scale.
- **Trial band and replica band (VA-163)** — the kill band read at the first instance of a kind (the trial) and the band read at each repeat (the replica). Two bands, because one band for both overstates capital.
- **Overlay** — the extra loss allowance the finance function books above the modelled figure while a model is new. In public supervisory correspondence this is a "post-model adjustment" (PRA letters to chief financial officers, 2021–2023). Held while unproven; released when proven.

---

## SR1 — Critical limiting operation II

**The question.** Which operation commands the most working capital as the venture scales — the most money and time out before it earns?

**Key activities and resources scan — the four products.**

| | Get paid (payment) | Make (working) | Sell (communications) | Deliver (partner) |
|---|---|---|---|---|
| Key activities | take the receipts share and the interest with each receipt (WP-3) | compute the limit daily (WP-1); execute the draw (WP-2); retire the overdraft into the limit (WP-4); validate the rule as a model | show the limit in the account (CP-1); the saving statement once a year | none at C3 — `[REQUIRES C7]` |
| Key resources | the ledger (durable, the account line's — exists) | the limit engine (durable — ⚠ 25 people; on the bank's roadmap already, insider 18 September 2026); **the rule's loss history (durable — accumulates only by lending under the rule, or by testing the rule on history)**; model-risk people (personnel); migration notices (consumable, one-off) | the account screen (durable — exists) | — |

Durables identified: the ledger and the account screen exist and cost the venture nothing new. The limit engine is a durable but the bank's roadmap already funds it, so it is not the venture's commitment (insider, 18 September 2026 — fact for this run, a red field in public). **The one durable the venture must build before the rule can run at scale is the rule's loss history.** It cannot be bought. On the conventional path it is made by lending under the rule and waiting.

**Diagnostic questions, answered on the form as it stands at C2.**

*What capital goes out before a unit earns, and when?* Per £1,000 of new drawn balance released under the rule:

| Line | £ per £1,000 drawn | When | Source |
|---|---|---|---|
| the funded balance | 1,000 (deposits at ⚠ 1.5–3.0% a year) | at the draw | C1 record; Bank Rate 4.0% from August 2025 (FACT) |
| regulatory capital on the drawn balance | 90 (75% risk weight × ⚠ 12% total capital) | at the draw | CRR Art. 123, standardised (FACT); ⚠ 12% T4 |
| regulatory capital on the undrawn limit | 13.5–22.5 (⚠ 1.5–2.5 undrawn per £1 drawn × 10% CCF × 75% × ⚠ 12%) | at release of the limit, from 1 January 2027 (0% CCF on unconditionally cancellable commitments before that) | PRA PS9/24 (FACT) |
| day-one loss allowance, modelled | 20–40 (⚠ 2.0–4.0% expected loss, 12-month) | at release; on drawn and expected undrawn under IFRS 9 5.5.20 for revolving facilities (FACT) | C1 record; IFRS 9 |
| **overlay while the rule is unproven** | **⚠ 5–40 (⚠ 25–100% of the modelled allowance, T4 — the range of post-model adjustments the PRA has written to chief financial officers about)** | **at release; held until the rule is validated** | **runner's call, logic: a new decision model with no outcome history draws an overlay by default; the PRA's letters treat overlays above 25% as needing a plan to remove them** |

*When is revenue received?* With each receipt: the receipts share carries the interest (structure `[REQUIRES C6]`; level between the operating bar and the KMC). ⚠ 300 receipts a year per drawn account (AOM section 0). Lag from draw to first revenue: ⚠ 1–2 days.

*What is the financing lag?* Two different lags, and the diagnosis turns on telling them apart.

- On the funded balance and its regulatory capital: **days.** The share repays and the interest arrives with every receipt. The balance is stock in trade, priced in the floor (PVC funding 15–30; IC 12–17). There is no lag to circumvent here. The receipts share (C1, C2) already makes the exposure self-liquidating — an input to R3, not R3's answer.
- On the loss history: **12–24 months per cohort.** The overlay goes out at release. It comes back only when the rule has 12 months of observed outcomes on a cohort large enough to read (C2 set ⚠ 10,000 accounts as the convergence event). Until then the rule cannot be validated under SS1/23 Principle 4 (independent validation before use, and outcomes analysis in use — FACT), and a rule that is not validated cannot be released on the whole book by any bank's own governance. The lag is the wait for evidence.

*Working capital per unit.* Overlay ⚠ £5–40 per £1,000 drawn, held ⚠ 12–24 months. Cost of holding it at ⚠ 12–15% cost of equity: ⚠ £0.6–12 per £1,000 over the wait. The migration one-off (⚠ £0.1–0.5m notices; ⚠ 5,300–8,200 handler hours, ⚠ £0.2–0.35m loaded) is **too small** to be the CLO II: ⚠ £0.3–0.85m against a book of ⚠ £3.4–5.7bn is under £0.25 per £1,000. The engine build (⚠ 12–18 months × ⚠ £3–4m) is too small and is the roadmap's, not the venture's.

*At-scale working capital requirement — on the conventional scaling path.* Two conventional paths, both costed:

| Conventional path | Capital committed before evidence | Time to at-scale | Against the PCO envelope ⚠ £100m ASSUMED |
|---|---|---|---|
| release the whole eligible book at once under the unproven rule | overlay ⚠ £17–228m (£3.4–5.7bn × £5–40 per £1,000) plus whatever appetite buffer the risk committee sets (unpriced; T4) | ⚠ 12–24 months to the reading | exceeds the envelope above the low corner; and no bank's model-risk governance releases a whole book on an unvalidated rule (SS1/23 Principles 2 and 4) |
| forward cohorts: ⚠ 10,000 accounts, 12–24 months; then ⚠ 100,000; then the book | overlay ⚠ £0.05–0.4m, then ⚠ £0.5–4m, then the remainder — small at each step; **the cost is time**: the HQ layer ⚠ £7.2–12.8m a year runs for the whole ramp on a cohort's revenue | ⚠ 36–60 months | fits the envelope; fails the clock — three to five years of a running-cost layer on a cohort's revenue is ⚠ £22–64m of fixed cost carried before the book carries it |

**CLO II, stated as one operation:** *releasing a standing limit under a rule whose loss rate has not been observed.* Capital committed per unit: the overlay, ⚠ £5–40 per £1,000 drawn, at release. Revenue received: with each receipt from day ⚠ 1–2 — the revenue is not the problem. Financing lag: ⚠ 12–24 months per cohort, the wait for the outcome history that lets the rule be validated and the next cohort released. Working capital per unit: ⚠ £5–40 per £1,000 drawn, held for the wait. At-scale requirement: ⚠ £17–228m at once, or ⚠ 36–60 months by cohorts. The evidence, not the money, is what the venture has to make before it can scale. **Runner's call: confirmed as the CLO II.**

**Launch constraints (VA-23).** None of the above is "no cash", "founder hours" or "pilot volume". The ⚠ 10,000-account cohort is C2's convergence event, not a launch constraint, and it is not carried into the strategy below.

---

## SR2 — Scaling theory of change

Run as `/theory-of-change-custom`, invoked as "R3 Scaling", desk-only.

```
SCALING THEORY OF CHANGE — R3
  Class of problem:  learning by doing where the knowledge to learn before doing already exists — an
                     irreversible commitment (capital and a released exposure) made to buy information
                     (the rule's loss rate) that the firm's own records could yield without the commitment.
                     A named category: the locus-of-learning problem (Pisano), a member of the wider
                     class of investment under resolvable uncertainty (Dixit and Pindyck).
  Theory:            Pisano, G. (1994), "Knowledge, Integration, and the Locus of Learning: An Empirical
                     Analysis of Process Development", Strategic Management Journal 15 (S1), 85–100.
                     Finding: where the underlying knowledge base is deep enough to predict outcomes,
                     learning before doing (laboratory and simulation) outperforms learning by doing
                     (in-plant trials) on both cost and time; where it is shallow, only learning by doing
                     works. Supporting: Dixit, A. and Pindyck, R. (1994), Investment under Uncertainty —
                     an irreversible investment made before information that will arrive anyway carries an
                     option cost equal to the value of waiting; staging the commitment to the arrival of
                     information recovers it.
  Context:           conditions, not a situation. (1) The bank holds daily flow on every eligible account
                     for at least ⚠ 3 years (UK record-keeping for business relationships is five years
                     under MLR 2017 and SYSC 9 — FACT for retention; whether the flow is held in a form the
                     rule can read is ⚠ T4). (2) The bank already carries an overdraft exposure on
                     ⚠ 104,500–161,500 of those accounts, with the loss it took on them recorded. (3) The
                     rule's inputs are all observable in that history: receipts, payments, balance,
                     conduct. (4) SS1/23 Principle 4 names outcomes analysis and back-testing as validation
                     methods — validation on history is recognised, not novel.
  Mechanism:         when the rule is run on the bank's own history and on exposure it already holds, the
                     loss history model risk needs is produced without a new release; the overlay is
                     not booked because no new exposure exists; the wait falls from a forward cohort's
                     12–24 months to the weeks a back-test takes plus the time an existing exposure
                     takes to show its conduct under the new repayment term.
  Current state:     the rule has no outcome history; any release books an overlay and starts a
                     12–24-month clock; the roadmap's own pre-approved limit will meet the same clock.
  Desired state:     the rule is validated under SS1/23 on the bank's own history and on exposure it
                     already carries, before any exposure it does not; no new exposure is released under
                     an unvalidated rule; the overlay at each later release is read from a measured band,
                     not assumed.
```

**Theory stress test.** Pisano's finding is empirical (pharmaceutical process development, 23 projects) and has been replicated in software and in clinical-trial design; the mechanism — that the value of simulation rises with the depth of the prior knowledge base — is the one this venture uses, and the condition it needs (a deep, structured history on the same population) is stronger here than in Pisano's sample. Robustness: T2 for the finding; the transfer to credit-model validation is the runner's inference, tagged. It is falsifiable: if the back-tested loss and the Stage 1 observed loss differ by more than ⚠ 1 point, the history did not predict the outcome and the theory did not hold here.

**What the theory does not say.** It does not say the rule is good. It says the evidence of whether it is good can be produced from records before capital is committed. The design claim is SR3's.

---

## SR3 — Scaling strategy

**Step 3a — baseline.** The C2 form already makes every drawn balance self-liquidating (the receipts share) and already retires the bank's existing overdraft exposure into the limit (migration). So the form carries no financing lag on the funded balance. What it leaves unresolved: it says nothing about the order in which limits are released, so by default every account with enough flow gets a live limit on day one under a rule with no outcome history — the whole-book release costed in SR1. The migration event is the only thing in the C2 form that touches exposure the bank already holds, and the C2 record used it for the saving, not for the evidence.

**Step 3b and 3c — mutations generated and decided.**

```
MUTATION GATE — R3
baseline: every eligible account receives a live limit at launch under a rule with no outcome history; the overlay and the 12–24-month wait attach to the whole book; the migrated exposure is used for the saving (C2) and not for the evidence.
mutation_A: release by existing exposure — the rule runs first as a shadow limit on the whole eligible book and is back-tested on the bank's own history; it is released as a drawable limit first where it is at or below the exposure the bank already carries (the migrated overdraft accounts), so the loss history is produced on exposure already held and already provisioned; each later stage opens against a pre-registered kill band read from that history | reason_considered: the durable the venture needs (the loss history) can be made from records and existing exposure, at no new overlay and in weeks not years (Pisano 1994) | verdict: adopted | reason_verdict: transforms the constraint — the evidence is produced instead of bought; needs this venture's form to work (a rule on observed flow, C1; existing exposure migrated onto it, C2); adds no line to the at-scale floor; leaves R1 and R2 untouched
mutation_B: sell the first loss on the early cohorts to a guarantor — a portfolio guarantee of the ENABLE Guarantee kind (British Business Bank) or a private first-loss buyer — so the overlay is someone else's | reason_considered: removes the overlay from the bank's own books at release | verdict: rejected | reason_verdict: cost-shifting — any incumbent can buy a guarantee without changing its form; the guarantee fee (⚠ 0.5–2% of the guaranteed amount a year, T4) is a new floor line; the loss history is still produced by lending and waiting, so the clock is unchanged; and the evidence lands with the guarantor's monitoring, not the bank's model-risk function
mutation_C: forward-flow sale of each early cohort's drawn book to a non-bank funder until validated, then retain | reason_considered: capital and overlay leave the bank's balance sheet during the wait (asset standardisation, Fabozzi 2000) | verdict: rejected | reason_verdict: cost-shifting for a deposit-funded bank — the funder's cost of money (⚠ 7–10%) exceeds the bank's deposits (⚠ 1.5–3.0%), so the sale destroys the C1 funding advantage during the very period the evidence is made; and the loss history goes to the buyer
mutation_D: release every limit at launch but capped at ⚠ 10–25% of monthly receipts until validated | reason_considered: small exposure, small overlay | verdict: rejected | reason_verdict: a launch constraint (VA-23), not an architecture — it reduces the exposure per account without changing when the evidence arrives; at 12–24 months the clock is the same; and a limit visibly below the customer's overdraft breaks the C2 price condition's premise that the customer loses nothing at migration
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: A — release by existing exposure
evolvedBFF: a bank whose credit facility is a standing property of every account with enough flow — a limit computed daily from the receipts and payments the bank already observes, drawn without an application and repaid by a fixed share of each receipt as it arrives — into which the customer's existing overdraft is retired at a one-time migration at a price held below the tariff, and whose rule is proven before it is trusted: run first as a shadow limit on the whole base and back-tested on the bank's own history, released first where it is at or below the exposure the bank already carries, and released to the rest by stages against a kill band read from that exposure's outcomes; the bank keeps no per-application decision, no security process, no annual review or renewal and no collections operation, only a rule under review, a release order, and exception cells for accounts whose flow stops or whose holder declines.
synthesisCheck: Square Loans (Block, Inc.) for flow-based small-business credit, because the offer is pre-computed from sales the platform already observes, shown to existing sellers without an application, repaid as a fixed share of each day's card receipts, and was extended to the platform's own existing sellers first — the rule was validated on flow the lender already held (Square press release, May 2014; Block 10-K FY2024: $5.7bn originated in 2024, loss rates under 3% historically).
```

**Scaling strategy (one structural move, three sentences).** The limit is released in the order of the bank's existing exposure, not the customer's demand: the rule runs as a shadow limit on every eligible account and is back-tested on the bank's own daily flow and recorded overdraft loss for ⚠ 3–5 years, and it is released as a drawable limit first where it is at or below the exposure the bank already carries — the migrated overdraft accounts of C2. Every later stage opens against a kill band pre-registered in this record and read from that exposure's outcomes. At scale the shadow, the back-test and the release order fall away, and the form is the C1–C2 form unchanged.

**Hypothesis.** If the rule's loss on the migrated accounts under the receipts share, read at ⚠ 12 months, is within ⚠ 1 point of the back-tested figure, then model risk accepts the back-test as evidence for the unreleased population and the replicas open without a forward cohort. **Falsified if** the observed and back-tested losses differ by more than ⚠ 1 point, or model risk requires a forward cohort on the unreleased population regardless of the back-test — in which case the wait returns and the scaling path is the conventional cohort path (SR1, row 2). **Named assumptions:** (1) the bank holds ≥ ⚠ 3 years of daily flow in a readable form (T4; retention is FACT, form is not); (2) model risk accepts back-test plus observed conduct on existing exposure as validation for a Tier ⚠ 1 model (SS1/23 Principle 4 recognises both methods — T2; acceptance for release is the risk committee's — T4); (3) the overlay auditors require on exposure the bank already carried is ⚠ 0–25% (T4); (4) the rule's limit is at or below the existing overdraft limit for ⚠ 50–80% of migrated accounts (T4 — for the rest, Stage 1 releases the existing limit and the rule's higher figure waits for Stage 2).

**Cost-shifting test.** No third party holds anything. The evidence is produced from the bank's own records and its own existing exposure. Value created: the validation evidence at ⚠ £0.3–0.8m (Stage 0) instead of a forward cohort's ⚠ £0.5–1.5m of validation work plus ⚠ 12–24 months of a ⚠ £7.2–12.8m running layer; the time to at-scale falls from ⚠ 36–60 months to ⚠ 27–42 months (capital path below). **Creates new value: yes.**

**New-BFF test.** An application-based lender cannot run a shadow limit: it holds no flow on accounts it has not lent to and no rule that computes from flow. A bank on the roadmap form (pre-approved limits, insider 18 September 2026) could shadow-run its pre-approved limit, but its pre-approved limit is a fixed exposure with a scheduled repayment, so the observed conduct under the new repayment term — the receipts share — is not in its history. The move needs C1 (the rule on observed flow) and C2 (existing exposure migrated onto the receipts share). **Requires this venture's architecture: yes.**

**R1/R2 consistency test.** No annual line is added at scale; the SC layer carries the one-off cost amortised (financial check below, ⚠ £0–1 per £1,000). The KMC is untouched; the price condition holds at the worst corner with the new floor (142.5 ≥ 132.5). Stage 1 is the C2 migration event itself, so the two records describe one event. **Consistent.**

**Stage gates, kill bands and the yes-threshold (VA-163).** Stated here, before any count is read.

| Kind of instance | Band | Reading | What the reading buys |
|---|---|---|---|
| **Trial band** — Stage 1, the migrated overdraft accounts (one instance, the first of its kind) | observed 12-month loss on the migrated pool under the receipts share: **continue** at or below ⚠ 4.45% at the set price of £140 (4.05% at ⚠ £135 — the 25% margin holds at the C10 floor; v2, re-set from the C3-floor value of 4.8%); **borderline** 4.45–5.0%; **kill and pivot** above ⚠ 5.0% → R1's SR2 with the loss line as the brief (C2's pivot, unchanged). Second reading: observed loss within ⚠ 1 point of the back-tested figure — the hypothesis | at ⚠ 12 months from migration, on ≥ ⚠ 10,000 accounts (C2's convergence event; the pool is ⚠ 104,500–161,500, so the reading is ten times over-sampled) | the replica band's first value; the overlay's release |
| **Replica band** — each Stage 2 replica (a repeat of a proven kind) | **a named unmeasured input until the trial reads.** Provisional value, to be replaced: the trial's observed loss ± ⚠ 1 point. A replica is killed if its 6-month loss annualises above the trial's reading + ⚠ 1 point | at ⚠ 6 months from release, per replica | the next replica's release |
| **Yes-threshold and the pre-registered acquisition budget** | the acquisition spend a stage may buy before its count is read: **£0.** The limit is a standing property of an account the bank already holds; there is no acquisition line in the form (C1, C2) and none is opened here. So any count read at a stage is a count of behaviour, not of spend, and the yes-threshold is the band itself | — | a count no acquisition line could have bought |

---

## Two models — the scaling architecture and the at-scale architecture (rocket framing)

The two are different designs and are stated apart. Conflating them is the recorded R3 failure.

| | Scaling architecture (Stages 0–2) | At-scale architecture (Stage 3) |
|---|---|---|
| What the rule does | computes a limit for every eligible account; records it as a shadow; is back-tested on history | computes a limit for every eligible account; the limit is live |
| What the customer sees | a migrated customer sees the limit at migration (Stage 1); an unreleased customer sees nothing until the replica that carries the account is released | every account with enough flow shows its limit |
| What model risk does | validates on the back-test; reads the trial band at 12 months; reads each replica band at 6 months; signs each release | monitors in use under SS1/23 (outcomes analysis each quarter) — the same function that monitors the bank's other Tier 1 models today |
| What finance books | the overlay on Stage 1 (⚠ 0–25%) and on each replica (the replica band); releases it at each reading | the modelled allowance only; no overlay |
| Capital | the overlay, staged; lending capital allocated per replica by the treasury as for any lending | the IC layer of the floor (12–17 per £1,000 a year) |
| The release order | by existing exposure, then by replica | none — no release event exists |
| What falls away, and when | **after Stage 0:** the back-test as a gate (it stays as a validation record). **After Stage 1's reading:** the trial overlay. **After the last replica's reading:** the shadow ledger, the release gate, the replica overlay, the stage readings | nothing further; the form is the C1–C2 form |

**The scaling architecture is not the product.** It is the path. A reader who finds a stage reading, a shadow ledger or a release gate in the at-scale AOM has found a defect.

---

## Capital path by stage — bands

Venture spend is what the PCO envelope (⚠ £100m ASSUMED) pays for. Lending capital is the bank's, allocated by the treasury as for any exposure, and is shown separately so the two are not added.

| Stage | Population | Venture spend, one-off ⚠ | Overlay held, then released ⚠ | Lending capital allocated ⚠ (not venture spend) | Time ⚠ | Revenue during the stage ⚠ |
|---|---|---|---|---|---|---|
| 0 — back-test and shadow | 760,000 eligible accounts; no exposure | £0.2–0.5m engine time (5–8 people, 3–6 months) + £0.1–0.3m validation (2–4 people, 3–6 months) | none | none | 3–6 months | none |
| 1 — migrated overdraft accounts (the trial) | 104,500–161,500 accounts; drawn balance £0.4–1.9bn (the C2 migrated pool); new exposure none — the released limit is at or below the existing overdraft limit | £0.1–0.5m notices + £0.2–0.35m handler hours (the C2 one-off, carried here by number) | £0–19m (£0.4–1.9bn × 2–4% × 0–25%), 12 months | none new — the exposure was already risk-weighted at 75% and its undrawn limit already carried the commitment treatment | 12 months to the reading | £27–249m a year (£0.4–1.9bn × the price between the operating bar 67.50 and the KMC 131.25 at the worst corner, T4) |
| 2 — replicas | the remaining 598,500–655,500 eligible accounts, released in replicas of ⚠ 333,000 accounts (⚠ 100,000 drawn — one exception cell, VA-91); ⚠ 2 replicas | £0.02–0.04m per reading (2 people, 2–4 weeks) | £0–50m per replica (£1.5–2.5bn × 2–4% × the replica band, provisionally 0–50%), 6 months, sequential | £155–281m per replica (£1.5–2.5bn × £103.5–112.5 per £1,000) — ⚠ £0.31–0.56bn across both; about 1–3% of a large UK bank's common equity (T3, public capital disclosures of the four largest UK banks) | 6 months per replica; replicas open on the previous reading | rising to the at-scale figure |
| 3 — at scale | 760,000 accounts with limits; 228,000 drawn; £3.4–5.7bn | none | none | the IC layer | — | the whole book at the price |
| **Totals** | | **£0.6–1.7m one-off, plus ⚠ £0.04–0.08m of readings** | **peak ⚠ £0–50m held at any time; carrying cost at 12–15% ⚠ £0–10.4m over the path** | **⚠ £0.31–0.56bn allocated, priced in the floor** | **⚠ 27–42 months to at-scale** | |

**Against the conventional paths (SR1):** whole-book release, ⚠ £17–228m at once and no governance that permits it; forward cohorts, ⚠ 36–60 months with ⚠ £22–64m of running cost carried on a cohort's revenue. The move's peak venture capital ⚠ £1–50m sits inside the envelope at every corner; its clock is ⚠ 9–18 months shorter. **Stage 1 is viable standalone:** revenue ⚠ £27–249m a year against the running layer ⚠ £7.2–12.8m at every corner (27 > 12.8). The thin corner is the margin per £1,000 at the Stage 1 count, reported in the financial check (VA-162).

---

## SR4 — Business form factor (C1–C3)

**The central structure.** Remove the rule computed daily from observed flow and everything falls: no standing limit (C1), nothing to migrate the overdraft into (C2), nothing to shadow or back-test (C3). The central structure is the rule on observed flow. The opening sentence is written around it.

**Cumulative BFF (C1–C3):** *A bank whose credit facility is a standing property of every account with enough flow — a limit computed daily from the receipts and payments the bank already observes, drawn by the customer without an application and repaid by a fixed share of each receipt as it arrives — into which the customer's existing overdraft is retired at a one-time migration at a price held below the tariff the customer paid, so that the saving is visible on the account each year, and whose rule is proven before it is trusted: run as a shadow limit on the whole base and back-tested on the bank's own history, released first where it is at or below the exposure the bank already carries and to the rest by stages against a kill band read from that exposure's outcomes; the bank keeps no per-application decision, no security process, no annual review or renewal and no collections operation, only a rule under review, a release order that ends when the last replica is read, and exception cells for accounts whose flow stops or whose holder declines.*

**Read cold, labels removed:** one product — a limit that lives in the account, repays from receipts, replaces the overdraft, and is proven on the bank's own book before it is extended. Not a checklist. The release order is the only element that belongs to the path rather than the product, and the sentence says when it ends.

**Fault-line check.** C1 says every account with enough flow carries a limit; C3 says an unreleased account shows nothing until its replica opens. The tension is real and is resolved by the two-model statement: C1's claim is the at-scale form; C3's is the path to it. No other pull.

BFF C1–C3 confirmed. Sections 5–8 (CTM v3, AOM v3, fit model at C3, verifier r3) run next, before the close.

---

## Considered / not chosen (VA-4)

Baseline on this dimension: the C2 form releases every eligible limit at launch under an unproven rule and uses the migrated exposure for the saving only.

- A. Release by existing exposure, back-tested, staged on a kill band → makes the evidence from records and exposure already held → **adopted**.
- B. Portfolio guarantee or first-loss sale on early cohorts (ENABLE-type) → removes the overlay from the bank's books → rejected: cost-shifting; a fee line; the clock unchanged; the evidence lands with the guarantor.
- C. Forward-flow sale of early cohorts to a non-bank funder → capital and overlay leave the balance sheet → rejected: cost-shifting; loses the C1 funding advantage during the wait; the loss history leaves with the book.
- D. Whole-book release with limits capped at a share of receipts → small exposure → rejected: a launch constraint (VA-23); the clock unchanged; breaks the C2 migration premise.
- E. Equity or a capital injection to fund the overlay → rejected before the gate: equity as R3 is the recorded failure; it transfers the constraint at the highest cost of capital and produces no evidence.

Decision: A adopted; the evolved BFF restated in SR4.

---

## Synthesis check (VA-1)

**Real-business analogue:** the venture now looks like **Square Loans** (Block, Inc.) for flow-based small-business credit — because the offer is pre-computed from receipts the lender already observes, shown in the account without an application, repaid as a fixed share of each receipt, and was extended to the platform's own existing sellers first, so the rule was proven on flow the lender already held before it was extended. Limit of the analogue: Square is not deposit-funded and its sellers' receipts are card receipts it processes, not a bank account's whole flow; its capital path was funded by the parent's balance sheet and by loan sales to institutional investors — which is mutation C, rejected here for a deposit-funded bank. The mechanism shared is the release to existing flow-holders first; the funding is not shared. Analogue costed in the counterfactual file (Section 7, function-gate re-run).

---

## VA-106 synergy line

This move also serves two earlier requirements and later ones by number only.

- **R1** — the shadow limit compared with the decision the bank actually took on the same account is the evidence that the rule can stand in for the per-facility decision, which R1 asserted and could not evidence at C1 (mechanism: the back-test on the bank's own history).
- **R2** — the trial population and the saving-statement population are the same accounts, so the C2 pool converges first and the saving and the loss are read on one cohort (mechanism: release order = the migrated accounts).
- **R6** by number (mechanism: the migrated cohort's repayment under the receipts share). **R9** by number (mechanism: the loss history as a resource). Nothing is said about how those requirements solve them.

---

## Actor business cases (VA-127)

One row per behaviour the scaling mechanism needs from anyone but the venture. Gains priced by OCV class with band and tier; the two VA-157 arithmetic lines are literal. A row with no positive surplus and no named force would be a design defect; there is none.

| Actor | Behaviour needed | How often | Gain (OCV class · band · tier) | Cost (priced) | Best alternative | Surplus verdict |
|---|---|---|---|---|---|---|
| Model risk and credit oversight (the independent reviewer of models, SS1/23 Principle 4) | validate the rule on the back-test and on the Stage 1 conduct; sign each release; read each band | once, then per stage (⚠ 3 readings) | **expended, avoided** — a forward-cohort validation not run: ⚠ £0.5–1.5m (3–5 people, 12–24 months; T4) · **risk-borne, avoided** — a release with no evidence (unpriced; the function's own standard forbids it) | back-test validation ⚠ £0.1–0.3m; readings ⚠ £0.04–0.08m | the forward cohort (⚠ £0.5–1.5m and 12–24 months) | **PASS** |
| | | | | | | central: gain £1.0m − cost £0.25m − alternative's surplus £0 = surplus £0.75m · pessimistic: gain £0.5m − cost £0.38m − alternative's surplus £0 = surplus £0.12m | |
| The board risk committee | set the appetite that lets a release proceed on back-test plus existing-exposure evidence | once per stage | **risk-borne, avoided** — an unproven rule on the whole book, or three to five years of a running layer on a cohort's revenue: ⚠ £22–64m of fixed cost not carried (SR1, T4) | the committee's time (existing; unpriced) | the forward-cohort path | **PASS** — the named force is its own governance: SS1/23 Principle 2 puts model risk with the board |
| | | | | | | central: gain £43m − cost £0 − alternative's surplus £0 = surplus £43m · pessimistic: gain £22m − cost £0 − alternative's surplus £0 = surplus £22m | |
| Treasury and the asset and liability committee | allocate lending capital per replica as the release order calls for it: ⚠ £155–281m a replica | once per replica (⚠ 2) | **expended** — the margin over the floor on the replica's book: price − floor, from £26.5 per £1,000 at the worst corner (132.5 − 106) to £96 at the best of the price condition (150 − 54), on £1.5–2.5bn | the capital's own cost is inside the floor (IC, 12–17), so no cost is counted twice | lend the same capital elsewhere at the hurdle — a surplus of £0 above the hurdle by construction, since IC charges the hurdle | **PASS** |
| | | | | | | central: gain £42m − cost £0 − alternative's surplus £0 = surplus £42m (70 per £1,000 × £0.6bn) · pessimistic: gain £11.9m − cost £0 − alternative's surplus £0 = surplus £11.9m (26.5 × £0.45bn) | |
| Finance (the chief financial officer's function) and the external auditor | book the overlay at ⚠ 0–25% on Stage 1 and at the replica band on each replica; release it at each reading | once per stage | **expended, avoided** — the overlay on a whole-book release, ⚠ £17–228m, not booked (T4) | the overlay actually booked: ⚠ £0–19m then ⚠ £0–50m, released within 12 months; carrying cost ⚠ £0–10.4m | the whole-book release or the cohort path | **PROVISIONAL** — positive at the centre; at the pessimistic corner the auditor requires 100% on Stage 1 (⚠ £76m) and the surplus is the time saved, unpriced here |
| | | | | | | central: gain £122m − cost £5m − alternative's surplus £0 = surplus £117m · pessimistic: gain £17m − cost £10.4m − alternative's surplus £0 = surplus £6.6m | |
| The migrated customer (Stage 1) | none new — the C2 migration acceptance is the behaviour; at Stage 1 the released limit is at or below the existing overdraft limit, so nothing is asked beyond C2 | — | as at C2 | as at C2 | as at C2 | no case row required beyond C2's; carried unchanged |
| The unreleased customer (Stage 2) | none — a wait is not a behaviour; the limit appears when the replica opens | — | none until release | the wait, ⚠ 6–24 months (a foregone gain, not a cost incurred) | what it does today (no limit) | no row required; the wait is stated so it is not hidden |
| PRA and FCA | none new — SS1/23 is a supervisory statement, not a permission; the standardised approach needs no model approval | — | — | — | — | not an actor at C3; permissions unchanged |

---

## Actor tracks (VA-102)

| Actor | Track in the CTM v3 | Introduced | Holder of what |
|---|---|---|---|
| the business | the customer journey, four phases | C1; C2 adds migration; **C3 adds the state "limit released" between eligibility and "limit visible" for the unreleased population** | draws; accepts the receipts share; accepts or declines migration |
| the account line | account line track | C1; C2 adds migration; **C3 adds the shadow ledger row** | the flow; the shadow limit; the release flag |
| the limit engine and exception cells | limit engine track | C1; C2 adds the decline and query row; **C3 adds the back-test row** | the rule; the back-test |
| **model risk and the board risk committee** | **release track — new at C3** | **C3** | **the validation; the release decision; the band readings** |
| finance | inside the release track | C3 | the overlay |
| the pricing committee | pricing track | C2, unchanged | the price condition |
| PRA and FCA | regulator track | C1, unchanged | permissions and capital |
| the partner who brings the customer | partner track | `[REQUIRES C7]` | flagged |

No new counterparty this challenge. One new internal track (the release track); its holder exists in every UK bank (VA-92, below).

---

## BFF delta and upstream re-verification (VA-103)

| Item | At C2 | At C3 | Changed by |
|---|---|---|---|
| Made | a limit computed daily from the flow | a limit computed daily from the flow; run as a shadow and back-tested before release (path only) | SR3 (WP-5) |
| Sold | live in the account; the overdraft retired into it at migration | unchanged at scale; during the path, live only when released | SR3 (release order) |
| Delivered | one running limit; the overdraft balance a draw with a receipts share; the saving shown yearly | unchanged | — |
| Paid | a price held below the tariff (PC-1); structure `[REQUIRES C6]` | unchanged; the overlay is finance's, not the customer's | — |
| Gate | ⚠ six months of flow; the new-to-trading business excluded | unchanged at scale; during the path, the replica's release | SR3 |

**One row per earlier requirement — named checks and FIT on the BFF as it now stands:**

| Requirement | Named checks | Result on the C3 BFF | FIT |
|---|---|---|---|
| R1 (C1 record v2) | CLO stated as an operation in the delivering zone; elimination not reduction; property-holder test; existence test; R1 failure test (venture, not improvement) | **re-verified — unchanged or stronger.** The at-scale form is untouched. The failure test is stronger: the back-test compares the rule's limit with the decision the bank took, which is the evidence R1 lacked (VA-106). The release order is path, not product, and adds no operation to the delivering zone at scale | **re-verified with the SC layer populated.** Floor ⚠ 54–106 (AOM v3 section 6). On the C1 whole-book ceiling £75–120: −32.8% at the worst corner (71.25 − 106 ÷ 106), superseded for the selected customer by the C2 ceiling; non-gating in mode 3 as recorded. Nothing at C1 FAILED |
| R2 (C2 record v1) | single KMC; ToC four fields; one structural move; mutation gate; KMC admissibility; elimination coverage; credibility mechanism; pointing test; carrying check; existence test | **re-verified — unchanged.** The KMC is untouched; the migration event is the same event as Stage 1; the price condition holds at the worst corner with the new floor (142.5 ≥ 132.5, room £10.00). The C2 stress row (migrated pool alone) is now the Stage 1 count and is reported under VA-162 rather than as a stress | **re-verified: 34.4% at the worst corner at the 0.95 surplus fraction (was 35.7%); 427.8% at the best; carries true; headroom £17.50 (was £18.75).** Undiscounted 41.5% and 455.6%. PASS on the 25% gate |

**Function-gate re-run (C3 — F1 closes here).** Every earlier requirement re-run in full on the cumulative BFF: consistency audit `bank-credit-facility-consistency-audit-F1-2026-09-21.md`; verification `bank-credit-facility-verify-F1-2026-09-21.md`; counterfactual (registry F1-gate row, RD-030) `sme-fintech-models/bank-credit-facility-counterfactual.md`.

---

## Financial check — the floor on four layers, the ceiling and the carrying check

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2, WP-3, WP-4, WP-5 (new), CP-1 (amended at C2; the release state added at C3), PC-1 (condition).

**How the SC layer is populated (runner's call, tagged).** The scaling costs are one-off. The FIT verifier's four layers put scaling cost in the annual floor, so the one-offs are spread over the PCO's payback horizon (five years) and over the at-scale book. One-offs: Stage 0 ⚠ £0.3–0.8m; migration ⚠ £0.3–0.85m; readings ⚠ £0.04–0.08m; the carrying cost of the overlays at ⚠ 12–15% for the months held, ⚠ £0–10.4m. Total ⚠ £0.64–12.1m ÷ 5 ÷ £3.4–5.7bn = ⚠ £0.02–0.71 per £1,000 a year, rounded to **⚠ 0–1**. The C2 caveat "INDICATIVE — SC excluded" becomes **"complete on four layers at F1"**; the floor moves from 54–105 to **54–106**.

```
COST FLOOR — four-layer breakdown        £ per £1,000 of average drawn balance a year (all ⚠ T4)

  PVC  funding 15–30 · expected loss 20–40 · computing 2–5 · exceptions and write-off 3–8      40–83
  RC   HQ ⚠ 47 people and technology £7.2–12.8m ÷ £3.4–5.7bn                                    2–5
  SC   one-off scaling cost ⚠ £0.64–12.1m over five years ÷ £3.4–5.7bn                          0–1   ← populated at C3
  IC   capital on drawn 10.8–13.5 · capital on undrawn 1.6–3.4                                 12–17
  ─────────────────────────────────────────────────────────────────────────────────────────────────────
  COST FLOOR (four layers)                                                                    54–106   ← complete at F1

REQUIRED PRICE (25% margin — the OPERATING bar)         67.50–132.50   ← floor × 1.25
REQUIRED PRICE (capital payback — the CAPITAL bar)      26.05–43.68    ← £148.5m required year-five revenue ÷ £5.7–3.4bn (unchanged)
BINDING REQUIRED PRICE                                  67.50–132.50   ← the operating bar at every corner
PRICE CEILING (KMC — R2 = WTP_low)                      150–300        ← the standard-tariff outflow (T3), unchanged

HEADROOM (ceiling low − binding bar high)               17.50
FMOS (WTP_low − Cost_high) ÷ Cost_high                  41.5% undiscounted · 34.4% at the fit model's 0.95 surplus fraction
```

```
CARRYING CHECK — R3
kmc:                     £150–300 per £1,000 drawn a year (T3)
operatingBar:            £67.50–132.50 (floor 54–106 × 1.25)
capitalBar:              £26.05–43.68 (PCO parameters, unchanged from C2)
bindingBar:              £67.50–132.50 | which: operating
headroomOnBinding:       £17.50 at the worst corner (150 − 132.50); £232.50 at the best (300 − 67.50)
carries:                 true
floorCompleteness:       four layers populated — the bar is no longer a lower bound
```

**Working capital timing (R3's primary output, Section 7).** On the funded balance: capital out at the draw, revenue in with the next receipt, ⚠ 1–2 days; working capital per £1,000 drawn beyond the balance itself: £0. On the evidence: overlay out at release, back at the reading, 12 months (trial) and 6 months (replica); peak ⚠ £0–50m; inside the envelope at every corner. The fin-sim change is the SC line and the stage table; no annual line moves.

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C3.yaml`).** By hand, replicating the script's arithmetic at the 0.95 surplus fraction: ceiling £142.50–285; net contribution £36.50 at the worst corner; **34.4% at the worst corner; 427.8% at the best. PASS on the 25% gate; the floor is complete.** Undiscounted: 41.5% and 455.6%. **The script did not run:** `fit_margin.py` refused because the checking scripts carry two edits and one new file awaiting the principal's batched seal (verifier r3, section "Script run"). The runner does not seal and does not run a copy elsewhere. The margin figure in this record is runner-computed on the model file's declared inputs and is to be replaced by the script's output after the seal — recorded as a failed registry row below with what was decided.

**Spread count (VA-162).** The fixed layers (RC, SC) are spread over the at-scale drawn book ⚠ £3.4–5.7bn (228,000 drawn accounts) because the check is the margin of safety of the product at scale (VA-74). At the PCO's other count — Stage 1 alone, ⚠ £0.4–1.9bn — RC becomes ⚠ £3.8–32 per £1,000 and the floor ⚠ 55.8–133; the margin at the worst corner is **7.1%** (142.5 − 133 ÷ 133), 12.8% undiscounted. Stage 1 is viable on revenue against the running layer (capital path) but thin per £1,000 at its worst corner. Stated, not gating.

**Binding gate — found by driving the design across its gates (VA-84).** Gates tested, in the order the design meets them:

1. margin at the KMC ceiling on four layers — 34.4% at the worst corner; 9.4 points above the 25% gate;
2. expected loss on the flow-underwritten pool — assumed ⚠ 2.0–4.0%; with SC the 25% gate holds at the worst corner up to **4.8%** at the C3 floor (floor 114 at a 4.8% loss line; 142.5 ÷ 114 − 1 = 25.0%; at the C10 floor of 107.47 the same gate falls to 4.45% — see the C10 record and the v2 changelog row); zero margin at 7.65%; at the pivot trigger of 5% the margin is 22.8%, BORDERLINE;
3. the history the bank holds — ≥ ⚠ 3 years of daily flow in a readable form on the same accounts: retention is FACT (five years), form is ⚠ T4; if the history is shorter than ⚠ 2 years the back-test loses its power and Stage 0 becomes a forward cohort;
4. model risk's acceptance of back-test plus existing-exposure conduct for release — SS1/23 recognises both; the risk committee's appetite is ⚠ T4;
5. the trial band reading at 12 months — unmeasured by construction;
6. the replica band — a named unmeasured input until the trial reads;
7. the overlay share the auditor requires on Stage 1 — ⚠ 0–25%; at 100% the overlay is ⚠ £76m at the high corner, still inside the envelope;
8. lending capital for Stage 2 — ⚠ £0.31–0.56bn, about 1–3% of a large UK bank's common equity (T3); the bank's headroom is a red field;
9. the CCA form of the modifying agreement — standing constraint, unchanged;
10. the price condition holdable above the operating bar — 142.5 ≥ 132.5 at the worst corner, room £10.00.

**First to fail on today's evidence: (2), the loss rate.** Margin to it: 0.8 points of loss above the assumption's own high corner (4.0% → 4.8%) before the margin drops below 25% — one tenth of a point tighter than at C2, because the SC line took £1 of floor. **A margin of under one point of loss against an assumed value is the finding, unchanged since C1, and it is reported unsoftened.** Second to fail: (6), the replica band, which cannot be read until the trial reads.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  measure:      expected loss as a share of average drawn balance a year
  threshold:    4.8% at the C3 floor — the 25% margin fails above it at the worst corner; 7.65% — the margin is zero
                (C10 floor: 4.45% at £140, 4.05% at £135; zero at 7.25% — the values the trial band now carries)
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.8 points at the assumed high corner (20% of the assumed value)
  pivot:        above ⚠ 5% at the worst corner → R1's SR2 with the loss line as the brief
  read at:      the Stage 1 trial band, 12 months from migration, on ≥ ⚠ 10,000 accounts (over-sampled ten times)
```

**Independence (VA-97).** The margin of safety and the binding gate share the loss line; the margin is a transform of the gate. **NOT shown** — one financial check. Shared input (VA-160): the loss rate. An independent second check would be a count: the tariff share, the acceptance rate, or — new at C3 — the share of migrated accounts whose rule limit is at or below their existing overdraft limit (assumption 4, ⚠ 50–80%). None is public; all are the insider's or the trial's.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- CLO II named as a single operation, with capital, timing, lag and at-scale requirement stated ✓ (SR1).
- Durables identified before the diagnostic; the migration one-off and the engine build said to be too small, with the arithmetic ✓.
- Launch constraints absent from SR1–SR4 (VA-23) ✓.
- ToC — class of problem a named category ✓; theory named with researcher, year and paper ✓; context as conditions ✓; outcome as a state ✓ ("the rule is validated … before any exposure it does not").
- Strategy — exactly one structural move ✓; hypothesis with falsification and four named assumptions ✓.
- Mutation gate emitted before the strategy; four genuine mutations; justification mode false ✓.
- Cost-shifting test, new-BFF test, R1/R2 consistency test ✓.
- Stage gates, trial and replica bands, yes-threshold inside a pre-registered budget (VA-163) ✓ — the budget is £0 and says why.
- Two models stated apart, with what falls away and when ✓.
- Property-holder test (VA-71) ✓. Properties in the strategy: *proven* and *validated* — holder model risk; *appetite* — holder the board risk committee; *booked* and *released* — holder finance. Each has a row on the release track in the CTM v3. The customer holds no new property.
- Credibility mechanism (VA-81) ✓. Receiver: the board risk committee. Proposition: "the rule's loss under release equals its back-tested loss." Instrument the receiver uses today: the model validation report and the quarterly cohort loss report it reads for the bank's existing IFRS 9 models. Supplier: model risk.
- Existence test (VA-92) ✓. The holder of the release decision exists in every UK bank — SS1/23 Principle 2 places model-risk accountability with the board (FACT). An internal holder, admitted. The most the form can hand back is the wait itself: ⚠ 9–18 months.
- Pointing test ✓. The move attacks the cause of the lag (evidence bought by commitment) not the overlay as a number.
- Limit of the analogue stated ✓ (synthesis check).
- Completeness contract (VA-73) ✓. SR1–SR4 present; two models; capital path; VA-4; VA-1.
- No forward references (VA-80) ✓. C6, C7, R6, R9 by number only.
- VA-106 line present ✓. VA-103 table present, one row per earlier requirement, function-gate re-run named ✓. VA-127 table present, every non-venture behaviour priced with two arithmetic lines ✓. VA-82 items classified ✓ (below).
- Binding gate by driving ✓. Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162).
- Verdict order (VA-95) ✓ by reading. Loop-gate branch (VA-153): no FAIL, no branch. Loop-backs (VA-151): 0.
- Incremental write ✓.
- Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r3-2026-09-21.md`; F1 artefacts named in VA-103.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v3 and AOM v3 are written as documents; the model files (`bank-credit-facility-ctm-model-at-C3.yaml`, `bank-credit-facility-aom-model-at-C3.yaml`) are not, so `check_model_coverage.py` and `check_requirement_trace.py` did not run — **build item**, carried from C1 and C2, and recorded here as a FAIL disposed. Every AOM v3 activity names its flow and a driver that resolves to a named quantity, event or actor (section 0, RD-031); no cost line is a share of revenue ✓. Capacity: ⚠ 17,000 exception hours per cell a year covering ⚠ 100,000 drawn accounts; ⚠ 2.28 cells at scale, ⚠ 38,800 hours — **unchanged by R3; the replica is the cell (VA-91), and every calculation in this record uses the one figure.** The R3 rows are one-off (Stage 0, the readings) and sit at HQ, not in the cell. Role support: model risk, the risk committee and finance each have a supervisor, a trainer and a reviewer (AOM v3 section 4) ✓. Unit sizing: unchanged ✓. Component carriage: every C3 transition in the CTM v3 is carried by WP-5, the release track or a flag ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin of safety 34.4% at the worst corner, 427.8% at the best, by hand (41.5% and 455.6% undiscounted); PASS on the 25% gate on a complete floor; the script refused pending the seal. Carrying check: carries at every corner, headroom £17.50 on the operating bar. Binding gate: the loss rate, unmeasured, 0.8 points of margin at the assumed high corner. Independence NOT shown — one check. Working capital: £0 per £1,000 beyond the balance; overlay peak ⚠ £0–50m, inside the envelope. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- `fit_margin.py` refused (the toolchain awaits the principal's seal) — **build item**; owner: Tom (the seal); convergence: the script's output pasted into verifier r3 and this record's margin line replaced; the by-hand figures stand until then. FAIL on the run, disposed.
- CTM and AOM model files absent, so the coverage and trace scripts did not run — **build item**; owner: the Venture Architect seat if the run proceeds; convergence: the model files exist and both scripts pass before C4 opens. FAIL on the run, disposed.
- `check_verdict_order.py` refused (same seal) — **build item**; the order was checked by reading (R3 PROVISIONAL ≤ R2 PROVISIONAL ≤ R1 PROVISIONAL).
- The shadow ledger, the release flag on the account line and the back-test pipeline — **build items**; owner: the engine team and the account line (Case A); convergence: Stage 0 runs.
- The loss rate on the flow-underwritten pool — **unmeasured input**; owner: the insider, then the trial; convergence: the Stage 1 reading at 12 months; pivot: above ⚠ 5%.
- The trial band reading and the hypothesis (observed within ⚠ 1 point of back-tested) — **unmeasured input** by construction; owner: model risk; convergence: 12 months from migration.
- The replica band — **unmeasured input**; owner: model risk; convergence: the trial's reading.
- The history depth and its readable form — **unmeasured input**; owner: the insider; convergence: a count of accounts with ≥ 3 years of daily flow held.
- The overlay share the auditor requires on existing exposure — **unmeasured input**; owner: finance; convergence: the Stage 1 audit position.
- Lending capital headroom for Stage 2 — **unmeasured input**; owner: the treasury; convergence: the capital plan.
- The share of migrated accounts whose rule limit is at or below the existing overdraft limit (⚠ 50–80%) — **unmeasured input**; owner: the insider; convergence: the Stage 0 shadow run itself.
- C2's carried unmeasured inputs (tariff share; acceptance; revenue given up; owner-funded and deterred costs) — carried unchanged.
- The CCA form of the modifying agreement; SS1/23 validation; the 10% CCF; the Consumer Duty; IFRS 9 5.5.20 on undrawn exposure — **standing constraints**; SS1/23 is now designed for, and remains a constraint.
- New-to-trading businesses — **structural limit**, unchanged from C2; caps at PROVISIONAL with the rest.

```
GATE VERDICT — on the cumulative architecture C1 to C3
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files; coverage and trace scripts not run)
  financial limb:    PROVISIONAL     FMOS 34.4% worst corner / 427.8% best (by hand; script refused pending the seal) · binding gate the loss rate on the pool: surplus 0.8 points at the assumed high corner, unmeasured
  dispositions:      9 unmeasured inputs (4 carried from C2), 5 build items, 1 standing-constraint set, 1 structural limit (above)
  capacity figure:   17,000 exception hours per cell a year, 100,000 drawn accounts per cell = one replica — used throughout   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; an independent second check would be a count   VA-97
  gates driven:      10; first to fail on evidence: the loss rate, margin 0.8 points at the assumed high corner; second: the replica band   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r3-2026-09-21.md · bank-credit-facility-consistency-audit-F1-2026-09-21.md · bank-credit-facility-verify-F1-2026-09-21.md   VA-90
  inherited:         R2 PROVISIONAL (C2 record v1) and R1 PROVISIONAL (C1 record v2) — R3 cannot exceed them; PCO ratified by lapse 20 Sep 2026 17:00   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design; the two script refusals are build items with owner and convergence   VA-153
  launch constraints:none inside SR1–SR4 and this block   VA-23
  spread count:      the at-scale drawn book ⚠ £3.4–5.7bn (228,000 drawn accounts) — the check is the FMOS of the product at scale; at the Stage 1 count the worst-corner margin is 7.1%   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; independence reads NOT shown   VA-160
  VERDICT:           PROVISIONAL
```

**R3 failure test.** Would R3 have failed? Three conditions. First, the CLO II is the funded balance and cannot be circumvented without selling the book: it is not — the receipts share clears the balance in days; the lag is the evidence. Second, the move is cost-shifting: it is not — no third party holds anything; the rejected mutations B and C are the cost-shifting forms and are named. Third, the bank holds no usable history: unmeasured; if the history is under ⚠ 2 years, Stage 0 becomes a forward cohort and the path is the conventional one — slower, not dead. None fails today. The nearest is the third, through the readable form of the history, which is why it is gate (3).

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the price, its structure and its presentation — C6
  - the customer's conviction that the limit is real, for the unreleased population at its replica's release — C4
  - who brings the customer to the limit — C7
  - the switching cost the retired overdraft creates — R8
  - the loss history as a scarce resource — R9
  - the migrated cohort's repayment behaviour under the receipts share — R6
  - the surplus-fraction bands — R7
- **Unmeasured inputs (owner named in each case):**
  - the loss rate on the pool (the insider; then the trial at 12 months) — trigger > ⚠ 5%
  - the trial band reading and the ⚠ 1-point hypothesis (model risk)
  - the replica band (model risk; after the trial)
  - the history depth in a readable form (the insider)
  - the overlay share on existing exposure (finance)
  - lending capital headroom for Stage 2 (the treasury)
  - the share of migrated accounts with rule limit ≤ existing limit (the insider; the Stage 0 run)
  - carried from C2: the tariff share; migration and receipts-share acceptance (> ⚠ 30% decline); tariff revenue given up; owner-funded and deterred costs
  - every ⚠ figure
- **Build items:**
  - the script runs of `fit_margin.py` and `check_verdict_order.py` after the seal (owner Tom)
  - CTM and AOM model files and the coverage and trace scripts (Venture Architect seat)
  - the shadow ledger and release flag on the account line; the back-test pipeline (engine team; Case A)
  - the ledger's reclassification at migration and the saving statement (carried from C2)
- **Standing constraints:**
  - the CCA modifying agreement for sole traders under £25,000 with a receipts share
  - model-risk validation of the rule (SS1/23) — designed for at C3; still a constraint
  - the 10% credit conversion factor on undrawn limits from 1 January 2027
  - the Consumer Duty price-and-value outcome on the migrated accounts
  - IFRS 9 5.5.20 — the allowance on undrawn revolving exposure
- **Structural limit:** the new-to-trading business (no flow, no limit), bounded at 314,000 a year.
- **Unowned design defects:** none.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| CLO II names a single operation with capital, timing and lag | PASS | SR1 |
| Durables identified before the diagnostic | PASS | SR1 |
| ToC — class of problem (a named category) | PASS | SR2 block |
| ToC — theory (researcher + year + paper) | PASS | SR2 block |
| ToC — context (conditions, not situation) | PASS | SR2 block |
| ToC — outcome (a state) | PASS | SR2 block |
| Strategy — one structural move | PASS | SR3 |
| Strategy — hypothesis with falsification and named assumptions | PASS | SR3 |
| Mutation gate before the strategy; ≥ 2 genuine mutations | PASS — four | SR3 block |
| Cost-shifting test; new-BFF test; R1/R2 consistency | PASS | SR3 |
| Stage gates, two kill bands, pre-registered budget (VA-163) | PASS | SR3 table |
| Two models stated apart (rocket framing) | PASS | two-models section |
| Launch constraints absent (VA-23) | PASS | SR1; GATE VERDICT |
| Elegance line (VA-106) | PASS — R1 and R2 named with mechanisms | VA-106 |
| CTM update — traceability | PASS | CTM v3 section 4 |
| AOM — every activity ↔ a flow | PASS | AOM v3 3a–3c |
| AOM — volume drivers (resolving references, RD-031) | PASS | AOM v3 section 0 |
| AOM — no ratios | PASS | AOM v3 |
| AOM — role support | PASS | AOM v3 section 4 |
| AOM — LMU sizing | PASS — unchanged; the replica is the cell | AOM v3 section 5 |
| Fin-sim — working capital timing captured | PASS | financial check; fit model at C3 |
| FIT — margin (per-requirement, 25%) | PASS at 34.4% — **script REFUSED**, by hand | verifier r3 |
| FIT — I check | PASS | verifier r3 |
| FIT — T check | PASS | verifier r3 |
| FIT staleness — component set recorded (VA-74) | PASS | financial check |
| Loop gate (PASS or fully specified PROVISIONAL) | PASS — PROVISIONAL fully specified | close |
| Three-limb close (VA-89, VA-91) | PASS — one capacity figure | close |
| Financial halves shown independent (VA-97) | NOT shown — one check, second named; shared input declared (VA-160) | financial check |
| Spread count (VA-162) | PASS — at-scale count; the other count reported | financial check |
| Partner business case (VA-99) | not applicable — no partner at C3; C7's | VA-127 |
| Structural-limit disposition (VA-101) | PASS | close |
| Verdict composes forward (VA-95) | PASS — `check_verdict_order.py` not run (toolchain refusal); by reading | GATE VERDICT |
| Upstream re-verified (VA-103) | PASS | VA-103 tables |
| Actor business cases with two arithmetic lines (VA-127, VA-157) | PASS — no FAIL row; one PROVISIONAL row with the force named | VA-127 table |
| Existence test (VA-92) | PASS — internal holder admitted | close |
| Property-holder test (VA-71) | PASS — three holders, each on a track | close |
| Binding gate by driving (VA-84) | PASS — 10 gates | financial check |
| No parallel close (VA-85) | PASS — sequenced; C4 not opened | status file |
| Classified carried items (VA-82) | PASS | carried items |
| Independent verification artefact (VA-90) | PASS — artefact exists; its script half is queued | verifier r3 |
| No forward references (VA-80) | PASS | throughout |
| Credibility mechanism (VA-81) | PASS | close |
| Consistency audit at the function gate | PASS WITH CONDITIONS | `bank-credit-facility-consistency-audit-F1-2026-09-21.md` |
| Verification at the function gate | run — score in the artefact | `bank-credit-facility-verify-F1-2026-09-21.md` |
| **Counterfactual costed (F1 gate, RD-030)** | **PASS — written; floor unchanged; the instance's larger lines answered line by line** | `sme-fintech-models/bank-credit-facility-counterfactual.md` |
| Conventional cost line named and removed (F2) | not applicable — R4–R7 rows | — |
| Position-holding assumption (F3) | not applicable — R8–R10 rows | — |
| Mode 2 verdict form (C1) | not applicable — mode 3 | — |

**Rows that did not pass, and what was decided:** FIT — margin: the script refused; the arithmetic was done by hand and the re-run is queued behind the seal (build item, owner Tom). VA-95 order check: the same refusal; checked by reading. Operational: model files absent; coverage and trace scripts not run (build item, Venture Architect seat). Independence (VA-97): NOT shown, by construction of a lending floor in which the loss line is the largest term; the second check is named and is a count. No row FAILED on the design.

---

## Quality check

| Test | Result |
|---|---|
| Does the scaling strategy transform (not transfer) the working capital constraint? | **Yes** — the evidence is produced, not bought; no third party holds anything |
| Does it require a new BFF? | **Yes** — a rule on observed flow (C1) and existing exposure on the receipts share (C2) |
| Is Stage 1 economically viable standalone? | **Yes** on revenue against the running layer (⚠ £27–249m against ⚠ £7.2–12.8m); thin per £1,000 at its worst corner (7.1%) |
| Is the cumulative BFF internally consistent? | **Yes** — one fault line (C1's "every account" against C3's release order) resolved by the two-model statement |
| Two models stated apart; what falls away and when | ✓ |
| Kill bands per kind; budget pre-registered | ✓ — trial and replica; £0 with the reason |
| Margin by the correct formula, cost denominator, bands from the registry | ✓ — by hand; script queued |
| Named assumptions (history depth; model-risk acceptance; overlay share; limit-at-or-below share) | ✓ |
| Pivot trigger written | ✓ — loss > ⚠ 5% at the worst corner (C2's, unchanged) |
| Verdict composes forward (R1, R2 PROVISIONAL → cap) | ✓ |
| Confidence | **Medium** — the mechanism is grounded and cheap to test at Stage 0; every load-bearing input is a red field |
| No tooling vocabulary or metaphor in prose; house-style checker run | run on file save — see changelog |

---

## Sources (in addition to PCO S1–S12, C1 record C1–C12 and C2 record D1–D10)

| # | Source | Used for |
|---|---|---|
| E1 | PRA, SS1/23 *Model risk management principles for banks* (May 2023; in force 17 May 2024) | Principles 2 (governance with the board) and 4 (independent validation; outcomes analysis and back-testing as methods) — FACT |
| E2 | PRA, PS9/24 *Implementation of the Basel 3.1 standards near-final part 2* (September 2024) | 10% credit conversion factor on unconditionally cancellable commitments from 1 January 2027 — FACT |
| E3 | UK CRR Art. 111 and Art. 123 (onshored) | 0% CCF on unconditionally cancellable commitments today; 75% risk weight on regulatory retail SME — FACT |
| E4 | IFRS 9, paras 5.5.20 and B5.5.39–40 | expected credit loss on revolving facilities measured over the period of exposure, drawn and undrawn — FACT |
| E5 | PRA, letters to chief financial officers on IFRS 9 post-model adjustments (2021, 2022, 2023) | overlays on new or unproven models as a recognised practice with an expectation of a plan to remove them — T2 |
| E6 | Pisano, G. (1994), "Knowledge, Integration, and the Locus of Learning", *Strategic Management Journal* 15 (S1), 85–100 | the scaling theory of change — learning before doing where the knowledge base is deep |
| E7 | Dixit, A. and Pindyck, R. (1994), *Investment under Uncertainty*, Princeton | the option cost of committing before information that arrives anyway — supporting theory |
| E8 | Block, Inc., Form 10-K for FY2024 (SEC); Square press release "Square Capital" (May 2014) | Square Loans $5.7bn originated in 2024; loss rates under 3% historically; the offer to existing sellers repaid from a share of daily card receipts — T1 for the figures, T2 for the mechanism |
| E9 | iwoca — 2024 results as reported (City AM; company statements): 2023 revenue £143m and net profit £24m; 2024 originations £952m; headcount 369 to 432; about £4bn lent to 100,000 businesses since 2012 | the counterfactual instance — T2 |
| E10 | British Business Bank, ENABLE Guarantee programme description | mutation B — a portfolio guarantee as the cost-shifting form — T2 |
| E11 | Gompers, P. (1995), "Optimal Investment, Monitoring, and the Staging of Venture Capital", *Journal of Finance* 50 (5) | why staging alone is a financing arrangement, not an architecture |
| E12 | Money Laundering Regulations 2017 reg. 40; FCA SYSC 9 | five-year record retention on business relationships — FACT for retention; the readable form is ⚠ |
| E13 | Fabozzi, F. (2000), *The Handbook of Fixed Income Securities* (asset standardisation) | mutation C — forward-flow sale as the cost-shifting form |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v2 | 21 September 2026 | Route-back H1 of the C10 consistency audit (`bank-credit-facility-consistency-audit-C10-2026-09-21.md`). The trial band's continue line was set at 4.8% against the C3 floor (⚠ 106); at the C10 floor (⚠ 107.47) the 25% margin fails above 4.45% at the set price of £140 (4.05% at ⚠ £135), so a 4.8% reading would have released Stage 2 at a 21.2% margin. Continue re-set to ≤ ⚠ 4.45% (4.05% at £135); borderline 4.45–5.0%; kill above ⚠ 5.0% unchanged (C2's pivot). The C3-floor arithmetic in the FIT section is kept and marked as the C3 floor. A change of number, not of design. The same line is changed in the CTM v10 release track, the C10 record and the function status file. Runner-drafted, object-after to 23 September 2026 17:00. |
| v1 | 21 September 2026 | First record. Closes R3 and F1. Runner-drafted, object-after to 23 September 2026 17:00. CTM v3, AOM v3, fit model at C3, verifier r3, consistency audit F1, verification F1 and the counterfactual written alongside. `fit_margin.py` and `check_verdict_order.py` refused pending the principal's seal; margin and order by hand. House-style checker run on this file and every prose record before filing. |
