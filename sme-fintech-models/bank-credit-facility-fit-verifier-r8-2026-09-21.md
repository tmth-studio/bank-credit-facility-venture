# A business bank's credit facility line — fit verifier, pass r8 (after C8; Function 3 opens) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C8.yaml`, state at-C8. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Gate:** per requirement, 25%. **What changed since r7:** WP-1 amended to v2 — the seasoned limit. The rule's multiple of flow rises on a published schedule with the account's own cleared events, so the limit an account carries after two years of use is one no rival can offer on the first day. The only floor effect is capital on the larger undrawn commitment: undrawn per £1 drawn ⚠ 1.5–2.5 → 1.9–3.6; IC 12–17 → 13–18. The price is unchanged at 140 (band ⚠ 135–142.5). This pass adds two things the F2 passes did not carry: the barrier score (SCIS) with its verdict, and the position-holding re-test at the failure value of the assumption R8 holds.

## Independence of this pass

The floor bands were derived in the AOM v8 (sections 3a, 3b, 3c, 3e, 3i and 6) from the activity register, bottom-up; the KMC band is the TAM data object's (version 3, unchanged at C8 — R8 narrows no class and names no new block); the price is the C6 record's runner's call, unchanged. The verifier reads the model file and computes; it did not set any band or the price. **The one shared input (VA-97):** the drawn book ⚠ £3.4–5.7bn divides every fixed line into a per-£1,000 figure and multiplies the capital line; a smaller book raises RC and SC per £1,000 and does not move IC. R8 adds a second shared input — the undrawn-to-drawn ratio — which moves IC only; the loss rate and the funding rate do not read it. The two are independent: a higher ratio at the same loss rate raises capital, not loss.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.24 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2.02–5.11 (C8: the seasoning field and the cleared event add ⚠ £1–3k a year — 0.00) · exception handling and write-off 3.00–8.13 (C8: seasoning queries ⚠ 125–375 hours per cell inside the C5 headroom at the central corner; the 15th handler at the high corner adds 0.02 inside the rounded band) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | unchanged from r7: the yearly seasoning validation (⚠ 100–200 hours) sits inside model risk's 10 people; the schedule's term line inside existing conduct people |
| SC — scaling | 0–1 | T4 ⚠ | one-off total ⚠ £0.74–12.29m (C8: the seasoning build ⚠ £20–40k added) ÷ 5 years ÷ £3.4–5.7bn = 0.03–0.72, rounded up to 0–1 |
| IC — investment and capital | 13–18 | T4 ⚠ | drawn 10.8–13.5 unchanged; undrawn 2.05–4.86 (C8: was 1.6–3.4 — undrawn per £1 drawn ⚠ 1.9–3.6 × 10% CCF × 75% × 12% × 12–15%); unrounded 12.85–18.36 |
| **Floor** | **55.04–107.28** | | four layers; both corners move by ⚠ 1.00 in the rounded IC layer (0.45–1.50 unrounded) |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged (TAM data object v3, KMC-OD-STD-TARIFF) |
| The price (C6, unchanged) | 140.00 — band ⚠ 135.00–142.50 | T4 (runner's call with logic) | 14.0% simple a year; surplus fraction 0.933; band 0.90–0.95 |
| Operating bar (required price) | 134.10 | fixed number | floor high corner 107.28 × 1.25; does not read the ceiling |

## Script run — EXECUTED

Command, run 21 September 2026 from the vault root:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C8.yaml`

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  state              : at-C8
  cost floor         : GBP 55.0400 to 107.2800   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9330
  price ceiling      : GBP 139.9500 to 279.9000   (key cost x fraction)
  net contribution   : GBP 32.6700 to 224.8600   (worst corner to best corner)
  MARGIN OF SAFETY   : 30.5% at the worst corner (ceiling low against floor high); 408.5% at the best corner
  required price at 60%: GBP 88.0640 to 171.6480
  required price at 25%: GBP 68.8000 to 134.1000
  required price bar : GBP 134.1000   (stated in fixed-number form)
  checks reaching a verdict : 31   (all pass)
  notes: derived_from.operating_model resolves · derived_from.customer_model resolves · header date 2026-09-21 is within 24 hours of the last edit on disk · the price ceiling (low end 139.9500) clears the stated required price bar 134.1000
  gate applied       : per_requirement
  VERDICT            : PASS at 30.5% (worst corner; best corner 408.5%)
```

Exit 0. By hand at 140.00 the worst-corner margin is 30.50%, the script's 30.45% at 139.95 — both 30.5%. **The script's best corner (408.5%) is not used**, as at r6 and r7: the customer on a £300 tariff pays 140; the best corner at the set price is (140.00 − 55.04) ÷ 55.04 = **154.4%**, by hand.

**`check_verdict_order.py`** run on the verdict record `bank-credit-facility-verdict-record.yaml` with R8 added (R1–R8, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; eight checks reached a verdict; F1 reads PROVISIONAL at R3; F2 reads PROVISIONAL at R7. Exit 0. The script reads no F3 gate — F3 closes at R10 and the script's gate list ends at F2; recorded for WS1.

**`validate_tam_model.py`** — not run at r8: the TAM data object is unchanged at C8 (version 3 stands; version 4 is written at C10 per the brief). The r7 run (valid, three declared warnings) is the standing result.

## By hand, replicating the script's arithmetic across the price band

| Step | 135.00 (0.90) | 140.00 (0.933, the set price) | 142.50 (0.95) |
|---|---|---|---|
| cost floor, high corner = 83.24 + 5.04 + 1 + 18 | **107.28** | **107.28** | **107.28** |
| cost floor, low corner = 40.02 + 2.02 + 0 + 13 | **55.04** | **55.04** | **55.04** |
| the price | 135.00 | 140.00 | 142.50 |
| net contribution, worst = price − floor high | 27.72 | 32.72 | 35.22 |
| margin of safety, worst = net ÷ floor high | **25.8%** | **30.5%** | **32.8%** |
| net contribution, best = price − floor low | 79.96 | 84.96 | 87.46 |
| margin of safety, best = net ÷ floor low | 145.3% | 154.4% | 158.9% |
| required price at 25% = 107.28 × 1.25 | 134.10 | 134.10 | 134.10 |
| room = price − 134.10 | 0.90 | 5.90 | 8.40 |
| required price at 60% = 107.28 × 1.6 | 171.65 | 171.65 | 171.65 |

**Verdict at the worst corner: PASS at 30.5% at the set price (script and by hand); PASS at every point of the band (25.8% at 135, by hand — 0.8 points above the gate).** R8 moves the worst-corner margin by −1.2 points (31.7% → 30.5%), the first move above one decimal since C4. The verdict stays PROVISIONAL: every input is a Tier 4 band, the price is a runner's call, and the seasoning schedule's three inputs (uplift, cleared-event frequency, the undrawn ratio) are unmeasured until the first replica's 24-month reading.

**The band's own threshold:** the worst-corner margin reaches 25% where the price = 134.10, f = 0.894 (13.41%). Was 0.886 at r7. The band's low end (135) now sits 0.90 above the bar: a further ⚠ 0.72 of floor at the high corner would take the band's low end under the gate at 135 while the set price still passes.

## Position-holding re-test (registry F3 row) — R8's assumptions at their failure values

The C8 record scores the barrier: **SCIS 2 (conservative) · 4 (central) · 6 (optimistic)** — magnitude from the switching-cost ratio (⚠ 0.17 / 0.63 / 1.51: the seasoned uplift's value against a 40-day cash buffer's cost), portability (partially — the flow history is readable by a rival under CMA Order 2017; the seasoning under the schedule is not), trajectory (compounds to ⚠ 36 months). **The conservative corner is 2, which is at or below the NCR threshold of 3 — FAIL, recorded.** What the C8 record does about it: the design commitment is the schedule itself and the first replica's 24-month switch-out reading (G16); no repair is available inside R8 because the magnitude term is the customer's cash-buffer cost, an input of the world.

Where the score is below threshold the verifier re-tests the margin at the failure value:

| Assumption | Holds at | Fails to | Effect on the floor at the high corner | Worst-corner margin at 140 |
|---|---|---|---|---|
| switch-out rate | ≤ 4% of drawn accounts a year (CMA 2016) | ⚠ 10–15% | the release-scaling share of RC (⚠ 5–8%) × churn ratio 12.5 ÷ 4 → RC 5.04 → ⚠ 5.58–5.90; SC unrounded 0.72 → 0.84, inside 0–1; floor high 107.82–108.14 | **29.5%** at 108.14 (29.8% at 107.82) — PASS |
| seasoned uplift | ⚠ 15–30% | 0% | IC returns to 12–17; floor high 106.28; the store of value is absent — R8 loops to SR1 | 31.7% — the margin passes, the requirement does not |
| loss rate on the uplift | ⚠ 2–4% (the pool's own band) | ⚠ 4–5% on ⚠ 10% of drawn-days | expected loss +0–1 per £1,000; floor high 107.28–108.28 | 29.3% at 108.28 — PASS; the loss gate (4.47%, below) is the earlier limit |

**The re-test holds at every failure value: the lowest margin is 29.3%, 4.3 points above the gate.** The re-test is arithmetic on declared failure values; the failure values are Tier 4 and the first replica's readings at 12 and 24 months converge them.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| the price | 140.00 (band 135.00–142.50) | 140.00 — one rate for the pool |
| operating bar = floor × 1.25 | 68.80 | 134.10 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| room on the binding bar at the set price | worst: 140.00 − 134.10 = **5.90** | best: 140.00 − 68.80 = 71.20 |
| carries | **true** at every point of the band (0.90 at 135) | |
| max payable to any holder (VA-164) | 0 at the pessimistic corner (the tariff given up, C6) | 5.90 at central; paid 0 |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** the larger undrawn commitment is capital held, not cash out; the seasoned limit funds nothing until drawn, and a draw is funded as at C5. **Partner's return (VA-156):** unchanged — none paid. **Count line (VA-155)** as printed in the C8 record: ⚠ 0.7–2.7m cleared events a year; seasoned share at scale ⚠ 60–80% of drawn accounts.

## The ⚠ £8 cap (RD-030), running line — Function 3 opens

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |
| R6 | nil — nothing removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.27 | ⚠ 7.73 |
| R7 | ⚠ 6–35 (broker commission, referral fees, partner marketing, a partner desk) — removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.28 | ⚠ 7.72 |
| **R8** | **⚠ 5–15 (loyalty pricing, exit fees, product tie-ins, a retention desk) — removed** | **⚠ 1.00 rounded (0.45–1.50 unrounded)** | **⚠ 1.05–1.28 rounded (0.50–1.78 unrounded)** | **⚠ 6.72** |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £6.60 at the set price (0.933), £8.00 at 0.95. At the set price the R4–R8 additions use 1.28 of 6.60. R8 is the first requirement whose addition is visible at one decimal, and it is capital on a larger promise, not an activity: the form pays for the store of value in equity held against undrawn commitment, ⚠ £1.5–8.4m a year on the book.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 67.28 + 10L (every other line at its high corner; 66.28 at r7).

| The price | Bar = price ÷ 1.25 | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 135.00 (band low) | 108.00 = 67.28 + 10L → **4.07%** | 135.00 → 6.77% | −0.93 points — the gate sits inside the pivot |
| **140.00 (the set price)** | 112.00 → **4.47%** | 140.00 → 7.27% | −0.53 points — the gate sits inside the pivot |
| 142.50 (band high) | 114.00 → **4.67%** | 142.50 → 7.52% | −0.33 points |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.07 points at 135, **0.47 at the set price** and 0.67 at 142.5 — each 0.10 tighter than r7. The C5 default-funded gap (0.3–0.5 points) now sits at the edge of the 0.47 at the set price: at the top of that gap and the top of the loss band the margin is 25.0%. This is the first pass at which a carried unmeasured input, at its own high corner, reaches the gate exactly. The loss rate remains the binding input; R9's move is designed against it.

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000. Floor at Stage 1: 40.02 + 3.84 + 0 + 13 = 56.86 to 83.24 + 32.38 + 1 + 18 = 134.62. Worst-corner margin at the set price: (140.00 − 134.62) ÷ 134.62 = **4.0%**; 0.3% at the band's low end; 5.9% at its top. Stage 1 does not carry the 25% gate on its own book at the high corner, as at r3–r7; the release order carries it to scale. At Stage 1 the seasoning is nil — no account has a cleared event under the form on day one — so the Stage 1 undrawn ratio is the C7 ratio (1.5–2.5) and IC at Stage 1 is 12–17 by construction; the 4.0% is stated at the C8 band for the spread count's convention, and is 4.8% at the Stage 1 ratio.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R8 removes the block — nothing accumulates in the relationship that a rival cannot supply on day one. After the move the seasoned limit is a property of the account's own record under the form; a rival reading the flow history under CMA Order 2017 can compute the unseasoned limit and cannot compute the seasoning, which exists only under the schedule.

**I-Cost: PASS.** The four things R8 could have added and did not: loyalty pricing, an exit fee, a product tie-in, a retention desk — the conventional line of ⚠ 5–15. The activities it adds are one field read inside a computation already run, one event recognised on a ledger already written, one build (⚠ £20–40k once), one yearly validation inside existing people, and one query type inside the C5 headroom at the central corner. The capital line is not an activity: it is the cost of the larger promise, and it is the whole of R8's floor effect.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r7 chain is unchanged. R8 adds the store-of-value chain: a lender that observes a borrower's repayment over time acquires information the borrower cannot transfer to a rival at the same cost (Sharpe 1990); the lender's terms improve with the relationship's length because the information does (Petersen and Rajan 1994; Ioannidou and Ongena 2010 on the reversal when the borrower switches). The seasoned limit makes that information a term the customer can see — the schedule — rather than a discount the rival cannot see.

**T-Robustness: PASS.** The contrast theory — Rajan 1992 on the hold-up cost of an informed lender — argues the informed lender extracts rent as the relationship lengthens; here the price is one rate for the pool (PC-1) and the schedule is published, so the rent the contrast predicts has no instrument to act through. The contrast names why the loyalty-pricing mutation is rejected rather than overturning the design.

## What the pass says

1. At C8 the floor is 55.04–107.28 and the price is 140. The margin at the worst corner is 30.5% at the set price (script and by hand), 25.8% at the band's low end and 32.8% at its top. R8 carries; the store of value costs ⚠ 1.00 rounded (0.45–1.50 unrounded) against a conventional line of ⚠ 5–15.
2. The loss gate at the set price is 4.47%, 0.10 tighter than r7; the C5 default-funded gap at its high corner now reaches the gate exactly. The loss rate is the binding input.
3. SCIS scores 2 / 4 / 6; the conservative corner FAILS the NCR threshold and is disposed to G16. The position-holding re-test at every failure value holds — lowest margin 29.3%.
4. The cap line stands at ⚠ 1.05–1.28 rounded of ⚠ 8.00; ⚠ 6.72 remains for R9–R10.
5. Two script findings for WS1: `check_verdict_order.py` reads no F3 gate; the fit model has no field for a barrier score or a position-holding re-test, so both are carried in a block the script does not read.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1–r7 | 18–21 September 2026 | As in `bank-credit-facility-fit-verifier-r7-2026-09-21.md`. |
| r8 | 21 September 2026 | Pass after C8 — PASS at 30.5% at the set price (`fit_margin.py`), 25.8–32.8% across the band (by hand); floor 55.04–107.28. `check_verdict_order.py` IN ORDER with R8 added. SCIS 2 / 4 / 6 — conservative corner FAIL, disposed. Position-holding re-test: 29.3–29.5% at the failure values. Loss gate 4.47%. Cap line: R8 ⚠ 1.00 rounded; cumulative ⚠ 1.05–1.28; remaining ⚠ 6.72. |
