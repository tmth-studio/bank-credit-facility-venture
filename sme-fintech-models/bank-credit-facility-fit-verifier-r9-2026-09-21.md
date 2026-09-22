# A business bank's credit facility line — fit verifier, pass r9 (after C9) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C9.yaml`, state at-C9. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Gate:** per requirement, 25%. **What changed since r8:** WP-6 added — the outcome ledger and the calibration. Every daily limit is written with the multiple in force and every funded event with its clearance, stall or write-off, by cohort; once a year the base multiple by flow band and the seasoning schedule are re-fitted from the ledger alone, validated on a held-out cohort under SS1/23 and approved at the release-track sitting. No external score enters the rule. The floor effect is ⚠ 0.01–0.03 per £1,000 unrounded: computing 2.02–5.11 → 2.02–5.12; SC unrounded 0.72 → 0.74 inside 0–1. The price is unchanged at 140 (band ⚠ 135–142.5). This pass carries the F3 barrier score (FIS) and the position-holding re-test; the re-test is run even though the score passes, because the first assumption is the binding gate.

## Independence of this pass

The floor bands were derived in the AOM v9 (sections 3a, 3c, 3e, 3j and 6) from the activity register, bottom-up; the KMC band is the TAM data object's (version 3, unchanged at C9 — R9 narrows no class and names no new block); the price is the C6 record's runner's call, unchanged. The verifier reads the model file and computes; it did not set any band or the price. **The one shared input (VA-97):** the drawn book ⚠ £3.4–5.7bn divides every fixed line into a per-£1,000 figure and multiplies the capital line. R9 adds no shared input: the calibration run is a fixed yearly cost and the ledger build a one-off; neither reads the loss rate, the funding rate or the undrawn ratio. What R9 does change is the *status* of the loss band — from an assumed band to a band the calibration holds the pool inside — and that is the subject of the re-test below, not of the arithmetic.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.25 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%; from C9 the band the calibration holds) · computing and payments 2.02–5.12 (C9: the outcome row inside the daily recompute, storage ⚠ £2–8k; the yearly calibration run ⚠ £15–50k — together ⚠ 0.00–0.01) · exception handling and write-off 3.00–8.13 (unchanged: no new query class) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | unchanged from r8: the held-out validation (⚠ 200–400 hours) sits inside model risk's 10 people and absorbs the C8 seasoning review; the approval is one item at an existing sitting; the data-protection record sits inside the existing function |
| SC — scaling | 0–1 | T4 ⚠ | one-off total ⚠ £0.84–12.59m (C9: the ledger build ⚠ £100–300k added) ÷ 5 years ÷ £3.4–5.7bn = 0.03–0.74, rounded up to 0–1 |
| IC — investment and capital | 13–18 | T4 ⚠ | unchanged from r8: drawn 10.8–13.5; undrawn 2.05–4.86; unrounded 12.85–18.36 |
| **Floor** | **55.04–107.29** | | four layers; the high corner moves by ⚠ 0.01 (0.01–0.03 unrounded) |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged (TAM data object v3, KMC-OD-STD-TARIFF) |
| The price (C6, unchanged) | 140.00 — band ⚠ 135.00–142.50 | T4 (runner's call with logic) | 14.0% simple a year; surplus fraction 0.933; band 0.90–0.95 |
| Operating bar (required price) | 134.11 | fixed number | floor high corner 107.29 × 1.25; does not read the ceiling |

## Script run — EXECUTED

`python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C9.yaml` — toolchain sealed 21 September 2026 19:49; the script ran without refusal.

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  model              : 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C9.yaml
  venture            : Business bank credit facility line (Case B)
  state              : at-C9
  bounded at         : GBP per 1000 of average drawn balance, per year, at-scale

  cost floor         : GBP 55.0400 to 107.2900   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9330
  price ceiling      : GBP 139.9500 to 279.9000   (key cost x fraction)
  net contribution   : GBP 32.6600 to 224.8600   (worst corner to best corner)
  MARGIN OF SAFETY   : 30.4% at the worst corner (ceiling low against floor high); 408.5% at the best corner

  required price at 60%: GBP 88.0640 to 171.6640
  required price at 25%: GBP 68.8000 to 134.1125
  required price bar : GBP 134.1100   (stated in fixed-number form)

  checks reaching a verdict : 31
      - cost_floor.layers.pvc evidence tier vs its form (point or band)
      - cost_floor.layers.pvc band low is not above band high
      - cost_floor.layers.pvc unit vs bounding unit
      - cost_floor.layers.pvc period vs bounding period
      - cost_floor.layers.pvc scale state vs bounding scale state
      - cost_floor.layers.rc evidence tier vs its form (point or band)
      - cost_floor.layers.rc band low is not above band high
      - cost_floor.layers.rc unit vs bounding unit
      - cost_floor.layers.rc period vs bounding period
      - cost_floor.layers.rc scale state vs bounding scale state
      - cost_floor.layers.sc evidence tier vs its form (point or band)
      - cost_floor.layers.sc band low is not above band high
      - cost_floor.layers.sc unit vs bounding unit
      - cost_floor.layers.sc period vs bounding period
      - cost_floor.layers.sc scale state vs bounding scale state
      - cost_floor.layers.ic evidence tier vs its form (point or band)
      - cost_floor.layers.ic band low is not above band high
      - cost_floor.layers.ic unit vs bounding unit
      - cost_floor.layers.ic period vs bounding period
      - cost_floor.layers.ic scale state vs bounding scale state
      - price_ceiling.kmc evidence tier vs its form (point or band)
      - price_ceiling.kmc band low is not above band high
      - price_ceiling.kmc unit vs bounding unit
      - price_ceiling.kmc period vs bounding period
      - price_ceiling.kmc scale state vs bounding scale state
      - customer surplus fraction is between 0 and 1
      - required_price does not read the price ceiling
      - required_price unit vs bounding unit
      - required_price period vs bounding period
      - required_price scale state vs bounding scale state
      - cost floor is greater than zero
  notes:
      - derived_from.operating_model resolves
      - derived_from.customer_model resolves
      - header date 2026-09-21 is within 24 hours of the last edit on disk
      - cost_floor.layers.pvc is a band 40.0200 to 83.2500 (tier T4)
      - cost_floor.layers.rc is a band 2.0200 to 5.0400 (tier T4)
      - cost_floor.layers.sc is a band 0.0000 to 1.0000 (tier T4)
      - cost_floor.layers.ic is a band 13.0000 to 18.0000 (tier T4)
      - price_ceiling.kmc is a band 150.0000 to 300.0000 (tier T3)
      - required_price is built from: cost_floor, required_profit
      - the price ceiling (low end 139.9500) clears the stated required price bar 134.1100

  gate applied       : per_requirement
  VERDICT            : PASS at 30.4% (worst corner; best corner 408.5%)
  This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.
```

Exit 0. By hand at 140.00 the worst-corner margin is 30.48%, the script's 30.45% at 139.95 — both 30.5%. **The script's best corner (408.5%) is not used**, as at r6 to r8: the customer on a £300 tariff pays 140; the best corner at the set price is (140.00 − 55.04) ÷ 55.04 = **154.4%**, by hand.

**`check_verdict_order.py`** run on the verdict record `bank-credit-facility-verdict-record.yaml` with R9 added (R1–R9, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; nine checks reached a verdict; F1 reads PROVISIONAL at R3; F2 reads PROVISIONAL at R7. Exit 0. The script reads no F3 gate — carried for WS1 from r8.

**`validate_tam_model.py`** — not run at r9: the TAM data object is unchanged at C9 (version 3 stands; version 4 is written at C10 per the brief). The r7 run (valid, three declared warnings) is the standing result.

## By hand, replicating the script's arithmetic across the price band

| Step | 135.00 (0.90) | 140.00 (0.933, the set price) | 142.50 (0.95) |
|---|---|---|---|
| cost floor, high corner = 83.25 + 5.04 + 1 + 18 | **107.29** | **107.29** | **107.29** |
| cost floor, low corner = 40.02 + 2.02 + 0 + 13 | **55.04** | **55.04** | **55.04** |
| the price | 135.00 | 140.00 | 142.50 |
| net contribution, worst = price − floor high | 27.71 | 32.71 | 35.21 |
| margin of safety, worst = net ÷ floor high | **25.8%** | **30.5%** | **32.8%** |
| net contribution, best = price − floor low | 79.96 | 84.96 | 87.46 |
| margin of safety, best = net ÷ floor low | 145.3% | 154.4% | 158.9% |
| required price at 25% = 107.29 × 1.25 | 134.11 | 134.11 | 134.11 |
| room = price − 134.11 | 0.89 | 5.89 | 8.39 |
| required price at 60% = 107.29 × 1.6 | 171.66 | 171.66 | 171.66 |

**Verdict at the worst corner: PASS at 30.5% at the set price (script and by hand); PASS at every point of the band (25.8% at 135, by hand — 0.8 points above the gate).** R9 moves the worst-corner margin by −0.01 points at two decimals (30.50% → 30.48%), invisible at one decimal. The verdict stays PROVISIONAL: every input is a Tier 4 band, the price is a runner's call, and the calibration's loss gain (⚠ 0.5–1.0 points on the uplift's drawn share) is unmeasured until the first replica's 24-month reading against the held-out cohort.

**The band's own threshold:** the worst-corner margin reaches 25% where the price = 134.11, f = 0.894 (13.41%), unchanged from r8 at three decimals. The band's low end (135) sits 0.89 above the bar: a further ⚠ 0.71 of floor at the high corner would take the band's low end under the gate at 135 while the set price still passes.

## F3 barrier score (registry row) — FIS

| Term | Conservative | Central | Optimistic |
|---|---|---|---|
| Compound rate (0–3) | 2 | 2 | 3 |
| Replication lag (< 12 months 0 · 12–36 months 1 · > 36 months 2) | 1 (⚠ 27 months) | 2 (⚠ 39 months) | 2 (⚠ 54 months) |
| Capital independence (0–2) | 2 | 2 | 2 |
| **FIS (max 7; ≥ 5 pass; ≤ 3 NCR)** | **5 — PASS** | **6 — PASS** | **7 — PASS** |

The verifier re-derived each term from the C9 record's stated basis and found no term it would score differently. The conservative corner is one point above the line; the term that carries it is capital independence, which the record supports by the lag itself — money buys the engine, the people and the feed, not the months. The verifier accepts this as logic, not as evidence: the lag is Tier 4 and its convergence event is the first rival announcement of a comparable ledger, which has not occurred (desk check, T2).

## Position-holding re-test (registry F3 row) — R9's assumptions at their failure values

The registry row asks for the re-test where the score is below threshold. The score is above threshold at every corner. The re-test is run anyway, because the first assumption is the loss band and the loss rate is the binding input of the whole design: a check that skips it because a score passed would be a check on the score, not on the margin.

| Assumption | Holds because of R9 | Failure value | Floor high at failure | Margin at 140 | Margin at 135 | Verdict |
|---|---|---|---|---|---|---|
| the loss band ⚠ 2–4% (PVC) | the parameters are re-fitted yearly to the rule's own outcomes | ⚠ 4.5% | 112.29 | **24.7%** | 20.2% | **BORDERLINE** |
| — | — | ⚠ 5.0% | 117.29 | **19.4%** | 15.1% | **BORDERLINE** |
| — | — | ⚠ 6.0% | 127.29 | **10.0%** | 6.1% | **FAIL** |
| the seasoned uplift ⚠ 15–30% (IC) | the schedule's figures are fitted at the first run | ⚠ 0–10% — IC 12–17 | 106.29 | 31.7% | 27.0% | PASS |
| validation inside existing people (RC) | model risk validates under SS1/23 | external ⚠ £0.2–0.5m a year — RC +0.04–0.15 | 107.44 | 30.3% | 25.6% | PASS |

**What the re-test says, unsoftened.** The margin depends on R9 holding. Without the calibration — a generic rule on Stage 0 parameters applied to a pool that has seasoned and grown for three years — the design is BORDERLINE at the failure band's midpoint and FAIL at its top, at the set price; at the band's low end it is BORDERLINE from 4.5% and FAIL from 6.0%. The other two assumptions hold at failure. This is recorded in the C9 record as a design finding (the margin's dependence on R9) and is the reason the verifier will re-test the loss band again at r10 regardless of the R10 score. The failure band itself is a runner's call (T4): its convergence event is the held-out cohort's loss at the first replica's 24 months, which measures the drift a fixed-parameter rule shows against the re-fitted one.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| the price | 140.00 (band 135.00–142.50) | 140.00 — one rate for the pool |
| operating bar = floor × 1.25 | 68.80 | 134.11 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| room on the binding bar at the set price | worst: 140.00 − 134.11 = **5.89** | best: 140.00 − 68.80 = 71.20 |
| carries | **true** at every point of the band (0.89 at 135) | |
| max payable to any holder (VA-164) | 0 at the pessimistic corner (the tariff given up, C6) | 5.89 at central; paid 0 |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** the ledger build is spent before Stage 0 (⚠ £100–300k, in SC); the calibration run is a yearly cost after the first year of Stage 1 rows. **Partner's return (VA-156):** unchanged — none paid. **Count line (VA-155)** as printed in the C9 record: ⚠ 0.7–2.7m outcome rows a year across ⚠ 30–60 cohort cells; gate G17 — ⚠ 500 rows per cell before a cell's parameter moves.

## The ⚠ £8 cap (RD-030), running line

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |
| R6 | nil — nothing removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.27 | ⚠ 7.73 |
| R7 | ⚠ 6–35 (broker commission, referral fees, partner marketing, a partner desk) — removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.28 | ⚠ 7.72 |
| R8 | ⚠ 5–15 (loyalty pricing, exit fees, product tie-ins, a retention desk) — removed | ⚠ 1.00 rounded (0.45–1.50 unrounded) | ⚠ 1.05–1.28 rounded (0.50–1.78 unrounded) | ⚠ 6.72 |
| **R9** | **⚠ 0 (a bureau score licence, a scorecard vendor, a data-science hire) — nothing to remove: the rule never carried an external score** | **⚠ 0.01–0.03** | **⚠ 1.05–1.29 rounded (0.51–1.81 unrounded)** | **⚠ 6.71** |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £6.60 at the set price (0.933), £8.00 at 0.95. At the set price the R4–R9 additions use 1.29 of 6.60. R9 is the cheapest requirement so far and the first whose conventional line is nil by construction rather than by choice: a form that never bought a score has no score to stop buying. The verifier notes the asymmetry — R9 gets no credit for a removal it did not make, and none is claimed.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 67.29 + 10L (every other line at its high corner; 67.28 at r8).

| The price | Bar = price ÷ 1.25 | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 135.00 (band low) | 108.00 = 67.29 + 10L → **4.07%** | 135.00 → 6.77% | −0.93 points — the gate sits inside the pivot |
| **140.00 (the set price)** | 112.00 → **4.47%** | 140.00 → 7.27% | −0.53 points — the gate sits inside the pivot |
| 142.50 (band high) | 114.00 → **4.67%** | 142.50 → 7.52% | −0.33 points |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.07 points at 135, **0.47 at the set price** and 0.67 at 142.5 — unchanged from r8 at two decimals. The loss rate remains the binding input. R9 is the requirement that acts on it: the calibration's claimed loss gain (⚠ 0.5–1.0 points on the uplift's drawn share, ⚠ 0.05–0.30 points on the pool) would widen the 0.47 if it holds, and the verifier does not book it — the gain is a hypothesis with a falsification condition (< 0.2 points at the first replica's 24 months), not an input.

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000. Floor at Stage 1: 40.02 + 3.84 + 0 + 13 = 56.86 to 83.25 + 32.38 + 1 + 18 = 134.63. Worst-corner margin at the set price: (140.00 − 134.63) ÷ 134.63 = **4.0%**; 0.3% at the band's low end; 5.8% at its top. Stage 1 does not carry the 25% gate on its own book at the high corner, as at r3 to r8; the release order carries it to scale. At Stage 1 the ledger holds ⚠ 2,300–28,000 rows per cell across ⚠ 30–60 cells (C9 record, G17): the first calibration run is at the end of Stage 1's first year, and no parameter moves in a cell below ⚠ 500 rows.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R9 removes the block — the rule's parameters were set from outside its own outcomes, so a rival with the same public parameters and the same feed could set the same limit. After the move the parameters are set from the outcome ledger, whose outcome column exists in no external feed (the CMA Order 2017 and PSRs reg. 69 give a rival the transactions, not what the bank's limit did on them). The lock-out is structural: the resource cannot be bought, and building it takes the ⚠ 27–54 months of the form's own release order.

**I-Cost: PASS.** The three things R9 could have added and did not: a bureau score licence, a scorecard vendor, a data-science hire. The activities it adds are two fields written inside a computation already run, one batch run a year (⚠ £15–50k), one validation inside model risk's existing cycle, one approval item at an existing sitting, one data-protection record inside the existing function, and one build (⚠ £100–300k once). No new people. The verifier checked the AOM v9 3c rows and found no head-count change.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r8 chain is unchanged. R9 adds the resource chain: an asset built by accumulation over time cannot be bought at any price in the period a rival wants it (Dierickx and Cool 1989 — time compression diseconomies), and its precision rises with its own size (asset mass efficiencies); the knowledge is a by-product of the activity itself (Arrow 1962). The calibration ledger makes the accumulation a rule input that a rival's ledger, starting later, cannot match until it has run for as long.

**T-Robustness: PASS.** The contrast — Barney 1991's resource conditions read together with the Open Banking premise that account data is portable — argues that a data resource on a bank account is not inimitable because the data moves with the customer. The contrast fails on the outcome column: what moves under the CMA Order is the transaction, not the limit the bank set on it or what that limit did. The contrast names the exact field the design depends on rather than overturning it, and the C9 record carries that field as its first named assumption (the outcome column is not reconstructible from the transaction feed).

## What the pass says

1. At C9 the floor is 55.04–107.29 and the price is 140. The margin at the worst corner is 30.5% at the set price (script and by hand), 25.8% at the band's low end and 32.8% at its top. R9 carries; the resource costs ⚠ 0.01–0.03 against a conventional line of ⚠ 0.
2. The loss gate at the set price is 4.47%, unchanged from r8. The loss rate is the binding input; R9 is the requirement that holds it inside its band, and the re-test shows the design BORDERLINE at 4.5–5.0% and FAIL at 6.0% without R9.
3. FIS scores 5 / 6 / 7 — PASS at every corner. The position-holding re-test was run regardless and is recorded unsoftened.
4. The cap line stands at ⚠ 1.05–1.29 rounded of ⚠ 8.00; ⚠ 6.71 remains for R10.
5. For WS1: the registry row's condition for the re-test (score below threshold) would have skipped the one re-test that matters at C9; the runner's call is to run it at every F3 requirement whose assumptions include the binding input.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1–r8 | 18–21 September 2026 | As in `bank-credit-facility-fit-verifier-r8-2026-09-21.md`. |
| r9 | 21 September 2026 | Pass after C9 — PASS at 30.5% at the set price (`fit_margin.py`), 25.8–32.8% across the band (by hand); floor 55.04–107.29. `check_verdict_order.py` IN ORDER with R9 added. FIS 5 / 6 / 7 — PASS at every corner. Position-holding re-test on the loss band: 24.7% BORDERLINE at 4.5%, 19.4% BORDERLINE at 5.0%, 10.0% FAIL at 6.0% — recorded as the design's dependence on R9. Loss gate 4.47%. Cap line: R9 ⚠ 0.01–0.03; cumulative ⚠ 1.05–1.29; remaining ⚠ 6.71. |
