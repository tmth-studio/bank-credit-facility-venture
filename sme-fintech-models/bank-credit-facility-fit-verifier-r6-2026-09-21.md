# A business bank's credit facility line — fit verifier, pass r6 (after C6) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C6.yaml`, state at-C6. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Gate:** per requirement, 25%. **What changed since r5:** the price is set — PC-1 resolved to the charge, 14.0% simple a year on the daily drawn balance, no fee, collected from receipts as the first slice of the receipts share. The surplus fraction is the set price (0.933 = 140 ÷ 150), replacing the 0.95 convention; the band 0.90–0.95 is the pricing committee's room. R6 adds ⚠ 0.00–0.01 to the floor's high corner (the accrual ledger). Every figure below is Tier 4 unless marked.

## Independence of this pass

The floor bands were derived in the AOM v6 (sections 3a, 3b, 3c, 3g and 6) from the activity register, bottom-up; the KMC band is the TAM data object v2's, unchanged; the price is the C6 record's runner's call, inside the band, with its threshold and convergence stated there. The verifier reads the model file and computes; it did not set any band or the price. **The one shared input (VA-97):** the loss rate, which sits in the floor and is the binding gate; the margin is a transform of it. **The price is a second shared input at C6:** it sets where on the loss line the gate sits, and it is a runner's call — the verifier reports the gate at the set price and at both ends of the band so that neither the number nor its author is hidden.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.23 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2.02–5.10 (C6: the accrual ledger adds ⚠ 0.00–0.01) · exception handling and write-off 3.00–8.13 (C6: charge queries inside the C5 headroom, no addition) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | unchanged from r5: the rate review sits in the pricing committee's existing sittings |
| SC — scaling | 0–1 | T4 ⚠ | unchanged from r3; the representative example (⚠ £10–20k once) sits inside the band |
| IC — investment and capital | 12–17 | T4 ⚠ | unchanged from r2: the accrued charge is not exposure |
| **Floor** | **54.04–106.27** | | four layers; the high corner moves by ⚠ 0.01; the low corner does not move |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged from r2 (TAM data object v2, KMC-OD-STD-TARIFF) |
| The price (C6) | 140.00 — band ⚠ 135.00–142.50 | T4 (runner's call with logic) | 14.0% simple a year; surplus fraction 0.933; band 0.90–0.95 |
| Operating bar (required price) | 132.84 | fixed number | floor high corner 106.27 × 1.25; does not read the ceiling |

## Script run — EXECUTED

Command, run 21 September 2026 from the vault root:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C6.yaml`

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  state              : at-C6
  cost floor         : GBP 54.0400 to 106.2700   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9330
  price ceiling      : GBP 139.9500 to 279.9000   (key cost x fraction)
  net contribution   : GBP 33.6800 to 225.8600   (worst corner to best corner)
  MARGIN OF SAFETY   : 31.7% at the worst corner (ceiling low against floor high); 417.9% at the best corner
  required price at 60%: GBP 86.4640 to 170.0320
  required price at 25%: GBP 67.5500 to 132.8375
  required price bar : GBP 132.8400   (stated in fixed-number form)
  checks reaching a verdict : 31   (all pass)
  notes: derived_from.operating_model resolves · derived_from.customer_model resolves · the price ceiling (low end 139.9500) clears the stated required price bar 132.8400
  gate applied       : per_requirement
  VERDICT            : PASS at 31.7% (worst corner; best corner 417.9%)
```

Exit 0. The script's ceiling at 0.933 is 139.95 (the fraction is a three-decimal reading of 140 ÷ 150); by hand at 140.00 the worst-corner margin is 31.74%, the script's 31.69% — both 31.7%. **The script's best corner (417.9%) is not used:** it multiplies the KMC band's high corner (300) by the fraction, but the customer on a £300 tariff pays the same 140; the best corner at the set price is (140.00 − 54.04) ÷ 54.04 = **159.1%**, by hand. This is a limit of the model's shape (a KMC band × one fraction) once a single price is set, recorded for WS1; it does not affect the worst-corner verdict.

**`check_verdict_order.py`** run on the verdict record `bank-credit-facility-verdict-record.yaml` with R6 added (R1–R6, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; six checks reached a verdict; function gate F1 reads PROVISIONAL at R3. Exit 0.

## By hand, replicating the script's arithmetic across the price band

The script reports the set price (0.933). The two ends of the band are computed by hand.

| Step | 135.00 (0.90) | 140.00 (0.933, the set price) | 142.50 (0.95) |
|---|---|---|---|
| cost floor, high corner = 83.23 + 5.04 + 1 + 17 | **106.27** | **106.27** | **106.27** |
| cost floor, low corner = 40.02 + 2.02 + 0 + 12 | **54.04** | **54.04** | **54.04** |
| the price | 135.00 | 140.00 | 142.50 |
| net contribution, worst = price − floor high | 28.73 | 33.73 | 36.23 |
| margin of safety, worst = net ÷ floor high | **27.0%** | **31.7%** | **34.1%** |
| net contribution, best = price − floor low | 80.96 | 85.96 | 88.46 |
| margin of safety, best = net ÷ floor low | 149.8% | 159.1% | 163.7% |
| required price at 25% = 106.27 × 1.25 | 132.84 | 132.84 | 132.84 |
| room = price − 132.84 | 2.16 | 7.16 | 9.66 |
| required price at 60% = 106.27 × 1.6 | 170.03 | 170.03 | 170.03 |

**Verdict at the worst corner: PASS at 31.7% at the set price (script and by hand); PASS at every point of the band (27.0% at 135, by hand).** The fall from 34.1% (r5) to 31.7% is the set price (0.933 against the 0.95 convention), not a cost: R6's addition to the floor is ⚠ 0.01 and would have moved the margin by less than 0.01 points at the convention. The verdict stays PROVISIONAL: every input the verdict depends on is a Tier 4 band, and the price is a runner's call.

**The band's own threshold:** the worst-corner margin reaches 25% where the price = 132.84, f = 0.886 (13.28%). The set price sits 0.047 above it; the band's low corner 0.014 above it.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| the price | 140.00 (band 135.00–142.50) | 140.00 — one rate for the pool |
| operating bar = floor × 1.25 | 67.55 | 132.84 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| room on the binding bar at the set price | worst: 140.00 − 132.84 = **7.16** | best: 140.00 − 67.55 = 72.45 |
| carries | **true** at every point of the band (2.16 at 135) | |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** changed at C6 and stated — the charge is cash with each receipt; the accrued-charge receivable cycle is ⚠ 1–3 days against ⚠ 30 under a monthly debit; interest cash arrives ⚠ 27 days earlier on average, worth ⚠ £0.9–2m a year at the funding line; the capital bar is unchanged (on the drawn balance); the gain is stated in the AOM v6 section 2 and not credited to the floor. **Below-tariff check:** 140 against a KMC low corner of 150 before fees and against the lowest published EAR (14.54%, £145.40): the price is lower for every migrated customer on a published standard tariff, by 10.00 at the KMC low corner and by 5.40 against HSBC's EAR alone; above 14.5% the claim fails.

## The ⚠ £8 cap (RD-030), running line

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |
| R6 | nil (the counterfactual books no cost against the price structure) — nothing removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.27 | ⚠ 7.73 |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £6.60 at the set price (0.933), £8.00 at 0.95. At the set price the R4–R6 additions use 0.27 of 6.60. The line is carried to C7. R7's conventional line is ⚠ 6–35: R7 is the requirement that can spend the cap.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 66.27 + 10L (every other line at its high corner). The gate now sits at a set price rather than at a convention.

| The price | Bar = price ÷ 1.25 | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 135.00 (band low) | 108.00 = 66.27 + 10L → **4.17%** | 135.00 → 6.87% | −0.83 points — the gate sits inside the pivot |
| **140.00 (the set price)** | 112.00 → **4.57%** | 140.00 → 7.37% | −0.43 points — the gate sits inside the pivot |
| 142.50 (band high) | 114.00 → **4.77%** | 142.50 → 7.62% | −0.23 points |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.17 points at 135, **0.57 at the set price** and 0.77 at 142.5. The C5 default-funded gap (⚠ 1 point on a ⚠ 30–50% default-funded share = 0.3–0.5 points on the pool rate) sits inside the 0.57 at the set price and outside the 0.17 at the band's low end. The design's answer is C5's fallback (opt-in by flow band at a 1-point gap), not the rate: the C6 record rules that the rate does not move on the loss reading — the limit rule does (C3's overlay). **At every point of the band the 25% gate sits below the ⚠ 5% pivot**, so the margin fails before the pivot is reached; that has been true since r4 and the set price does not change it.

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000. Floor at Stage 1: 40.02 + 3.84 + 0 + 12 = 55.86 to 83.23 + 32.38 + 1 + 17 = 133.61. Worst-corner margin at the set price: (140.00 − 133.61) ÷ 133.61 = **4.8%**; (135.00 − 133.61) ÷ 133.61 = **1.0%** at the band's low end; (142.50 − 133.61) ÷ 133.61 = **6.7%** at its top. Stage 1 does not carry the 25% margin at any point of the band, as at r3–r5; the stage order and the F1 condition (Stage 2 within ⚠ 24 months) are the design's answer. The bank's Critical Value Threshold (C6 record, SR2) is that same event.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R6 removes the charging date. The charge exists only as a fraction of money that has arrived; arrears on it, a returned debit for it and a draw to pay it cannot occur. No instalment plan, reminder, collections step or fee-waiver process is added because there is no charging event to manage.

**I-Cost: PASS.** The one thing R6 could have added and did not: a collections and arrears line on the charge (which the C1 form removed as an operation and a monthly debit would have brought back). The activities it adds are one ledger line per drawn account per day inside the daily batch (⚠ £8k a year), one more split rule on an event WP-3 already acts on (£0), a yearly sitting the pricing committee already holds, one document drafted once, and a query type inside the C5 headroom. None scales with the customer's use beyond the accrual, which is ⚠ 0.00 per £1,000.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r5 chain is unchanged for value, scaling, conviction and activation. R6 adds the payment chain. A payment coupled to the benefit it pays for and made from the money the benefit produced is felt least; a payment decoupled in time from the benefit is felt as a loss, and a decoupled instalment on a debt is the most painful case (Prelec and Loewenstein 1998, *Marketing Science* 17(1)). The charge taken from each receipt is coupled to the trade the draw financed; the monthly debit is the decoupled instalment. The at-scale claim rests on the split being arithmetic on an existing event, not on any behaviour.

**T-Robustness: PASS.** The coupling result is one of the founding results of mental accounting (Thaler 1985, *Marketing Science* 4(3)) and is consistent with the field evidence on payment transparency (Soman 2001, *Journal of Consumer Research* 27(4)). The contrast theory — payment depreciation (Gourville and Soman 1998) — argues for the advance fee where consumption follows a sunk payment; here the benefit's timing is unknown at acceptance, so the advance fee is felt in full at the worst moment, and the contrast theory names why mutation B is rejected rather than overturning the design. The direction is used, not the size; the size is read at the first replica (the charge-query and rate-reason decline shares).

## What the pass says

1. At C6 the floor is 54.04–106.27 and the price is set at 140. The margin at the worst corner is 31.7% at the set price (script and by hand), 27.0% at the band's low end and 34.1% at its top. R6 carries; the payment structure costs ⚠ 0.00–0.01 against a conventional line of nil.
2. The loss gate at the set price is 4.57%: 0.57 points above the assumed high corner (4.0%), of which the C5 default-funded gap may consume 0.3–0.5. At the band's low end the gap would consume the whole tolerance. The rate is not the lever on the loss line; the limit rule is.
3. The cap line is open: ⚠ 7.73 of ⚠ 8.00 remains for R7–R10 at the high corner (0.27 of 6.60 at the set price); R7 is the one that can spend it.
4. The model's best-corner figure (417.9%) is an artefact of a KMC band multiplied by one fraction once a single price is set; the best corner at the set price is 159.1%. Recorded for WS1: the fit model wants a `price` field that replaces the ceiling band once C6 sets one.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. |
| r3 | 21 September 2026 | Pass after C3 — PASS at 34.4% (by hand; three scripts refused), floor complete on four layers, PROVISIONAL on evidence. |
| r4 | 21 September 2026 | Pass after C4 — PASS at 34.2% on the convention, 27.1–41.2% across the surplus band (by hand; script refused). Cap line opened: R4 ⚠ 0.03–0.20 of ⚠ 8.00. |
| r5 | 21 September 2026 | Pass after C5 — PASS at 34.1% on the convention (`fit_margin.py`, run after the 19:49 seal), 27.0–41.2% across the band (by hand). Re-runs at C3 and C4 confirm r3 and r4. `check_verdict_order.py` IN ORDER on the new verdict record. Cap line: R5 ⚠ 0.02–0.06; cumulative ⚠ 0.05–0.26. |
| r6 | 21 September 2026 | Pass after C6 — PASS at 31.7% at the set price (`fit_margin.py` at a surplus fraction of 0.933), 27.0–34.1% across the price band (by hand). The best corner reported by hand at the set price (159.1%); the script's band figure recorded as a model-shape limit. `check_verdict_order.py` IN ORDER with R6 added. Loss gate at the set price 4.57%. Cap line: R6 ⚠ 0.00–0.01; cumulative ⚠ 0.05–0.27; remaining ⚠ 7.73. |
