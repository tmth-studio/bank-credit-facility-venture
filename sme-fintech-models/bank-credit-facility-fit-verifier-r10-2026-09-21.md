# A business bank's credit facility line — fit verifier, pass r10 (after C10) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C10.yaml`, state at-C10. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Gate:** per requirement, 25%; Function 3 closes at this pass, so the Phase II capital gate (60%) is read as well. **What changed since r9:** PC-2 added — the pool funding term. The drawn balances of the pool's accounts are funded by the credit balances of the same pool under a signed funding term, priced at the pool's measured deposit cost and read daily; the aggregate drawn book is capped at ⚠ 10% of the pool's credit balances; and one market route (a revolving master trust on the R9 ledger as its data tape) is set up before Stage 3 and maintained without issuance. The block removed: the line's funding was priced by a transfer-price convention outside the line, which the treasury could change at a sitting.

## Independence of this pass

The floor bands were derived in the AOM v10 (sections 3a, 3c, 3e, 3k and 6) from the activity register, bottom-up; the KMC band is the TAM data object's (version 4 at C10 — R10 narrows no class and names no new block; the one change is a volume gate, the cap); the price is the C6 record's runner's call, unchanged. The verifier reads the model file and computes; it did not set any band or the price. **The one shared input (VA-97):** the drawn book ⚠ £3.4–5.7bn divides every fixed line into a per-£1,000 figure and multiplies the capital line. R10 adds a second independent input to the margin — the funding line — with its own gate (3.45%) and its own hold; it does not read the loss rate. The verifier checked that the funding line and the loss line are separate inputs (the deposit cost is set by depositors and the policy rate; the loss by borrowers and the rule) and that no line of the R10 cost reads either.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.25 | T4 ⚠ | funding 15–30 (C10: the band is what the funding term holds at the measured deposit cost ⚠ 1.5–3.0%) · expected loss 20–40 (⚠ 2–4%; the band R9's calibration holds) · computing and payments 2.02–5.12 (C10: the daily price reading and the monthly tape cut add ⚠ 0.00 at two decimals) · exception handling and write-off 3.00–8.13 (unchanged) |
| RC — recurring fixed | 2.07–5.22 | T4 ⚠ | C10 adds the treasury and ALCO time on the term (⚠ 0.3–0.6 people, ⚠ 7.6–13.55m all-people cost becomes ⚠ 9.65–16.37m in the AOM v10 3c) and the route's upkeep without issuance (⚠ £0.3–0.6m a year = 0.05–0.18); unrounded 2.07–5.22 (was 2.02–5.04 at r9) |
| SC — scaling | 0–1 | T4 ⚠ | one-off total ⚠ £1.84–15.59m (C10: the route's set-up ⚠ £1–3m and the term's signature ⚠ £1–3k added) ÷ 5 years ÷ £3.4–5.7bn = 0.07–0.92, rounded up to 0–1 |
| IC — investment and capital | 13–18 | T4 ⚠ | unchanged from r8: drawn 10.8–13.5; undrawn 2.05–4.86; unrounded 12.85–18.36. The pool funding is a liability, not capital — nothing moves here |
| **Floor** | **55.09–107.47** | | four layers; the high corner moves by 0.18 (0.09–0.36 unrounded, all in RC) |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged (TAM data object v4, KMC-OD-STD-TARIFF; the cap is a volume gate and moves no class) |
| The price (C6, unchanged) | 140.00 — band ⚠ 135.00–142.50 | T4 (runner's call with logic) | 14.0% simple a year; surplus fraction 0.933; band 0.90–0.95 |
| Operating bar (required price) | 134.34 | fixed number | floor high corner 107.47 × 1.25; does not read the ceiling |

## Script run — EXECUTED

`python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C10.yaml` — toolchain sealed 21 September 2026 19:49; the script ran without refusal.

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  model              : 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C10.yaml
  venture            : Business bank credit facility line (Case B)
  state              : at-C10
  bounded at         : GBP per 1000 of average drawn balance, per year, at-scale

  cost floor         : GBP 55.0900 to 107.4700   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9330
  price ceiling      : GBP 139.9500 to 279.9000   (key cost x fraction)
  net contribution   : GBP 32.4800 to 224.8100   (worst corner to best corner)
  MARGIN OF SAFETY   : 30.2% at the worst corner (ceiling low against floor high); 408.1% at the best corner

  required price at 60%: GBP 88.1440 to 171.9520
  required price at 25%: GBP 68.8625 to 134.3375
  required price bar : GBP 134.3400   (stated in fixed-number form)

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
      - cost_floor.layers.rc is a band 2.0700 to 5.2200 (tier T4)
      - cost_floor.layers.sc is a band 0.0000 to 1.0000 (tier T4)
      - cost_floor.layers.ic is a band 13.0000 to 18.0000 (tier T4)
      - price_ceiling.kmc is a band 150.0000 to 300.0000 (tier T3)
      - required_price is built from: cost_floor, required_profit
      - the price ceiling (low end 139.9500) clears the stated required price bar 134.3400

  gate applied       : per_requirement
  VERDICT            : PASS at 30.2% (worst corner; best corner 408.1%)
  This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.
```

Exit 0. By hand at 140.00 the worst-corner margin is 30.27%, the script's 30.22% at 139.95 — 30.3% and 30.2% at one decimal; the record carries the by-hand figure at the set price (30.3%) and names the script's beside it. **The script's best corner (408.1%) is not used**, as at r6 to r9: the customer on a £300 tariff pays 140; the best corner at the set price is (140.00 − 55.09) ÷ 55.09 = **154.1%**, by hand.

**`check_verdict_order.py`** run on the verdict record `bank-credit-facility-verdict-record.yaml` with R10 added (R1–R10, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; ten checks reached a verdict; F1 reads PROVISIONAL at R3; F2 reads PROVISIONAL at R7. Exit 0. The script reads no F3 gate — carried for WS1 from r8; F3's close is therefore read by hand in this pass (below).

**`validate_tam_model.py`** run on `bank-credit-facility-tam-model.yaml` at version 4 (the C10 version; version 3 kept beside it as `bank-credit-facility-tam-model-v3-at-C7.yaml.bak`): "TAM model v4 · 6 sub-classes · 5 KMC classes"; three declared warnings, all carried from version 3 unchanged ([L4] SC-OD-BELOW-BAND; [L4] SC-LOAN-USER; [L7] volume basis is incidence while sub-classes are defined against supplied alternatives); one note (L11, the pool at risk stated for one incumbent); **✅ valid (with declared warnings)**. Exit 0. The v4 change is one gate, G-C10-1 (the cap), which excludes no class and is booked as a volume gate.

## By hand, replicating the script's arithmetic across the price band

| Step | 135.00 (0.90) | 140.00 (0.933, the set price) | 142.50 (0.95) |
|---|---|---|---|
| cost floor, high corner = 83.25 + 5.22 + 1 + 18 | **107.47** | **107.47** | **107.47** |
| cost floor, low corner = 40.02 + 2.07 + 0 + 13 | **55.09** | **55.09** | **55.09** |
| the price | 135.00 | 140.00 | 142.50 |
| net contribution, worst = price − floor high | 27.53 | 32.53 | 35.03 |
| margin of safety, worst = net ÷ floor high | **25.6%** | **30.3%** | **32.6%** |
| net contribution, best = price − floor low | 79.91 | 84.91 | 87.41 |
| margin of safety, best = net ÷ floor low | 145.1% | 154.1% | 158.7% |
| required price at 25% = 107.47 × 1.25 | 134.34 | 134.34 | 134.34 |
| room = price − 134.34 | 0.66 | 5.66 | 8.16 |
| required price at 60% = 107.47 × 1.6 | 171.95 | 171.95 | 171.95 |

**Verdict at the worst corner: PASS at 30.3% at the set price (by hand; 30.2% by the script at 139.95); PASS at every point of the band (25.6% at 135, by hand — 0.6 points above the gate).** R10 moves the worst-corner margin by −0.21 points (30.48% → 30.27%), the largest move of Function 3 and still inside the gate at every point of the band. The verdict stays PROVISIONAL: every input is a Tier 4 band, the price is a runner's call, and the funding term's price is unread until Stage 1's first daily readings.

**The band's own threshold:** the worst-corner margin reaches 25% where the price = 134.34, f = 0.896 (13.43%). The band's low end (135) sits 0.66 above the bar: a further ⚠ 0.53 of floor at the high corner would take the band's low end under the gate at 135 while the set price still passes. Function 3 as a whole used 0.23 of the 0.89 that stood at r7.

## F3 barrier score (registry row) — HRS

The registry states the thresholds for the R10 score (≥ 5 pass; ≤ 3 NCR) and not its terms. The C10 record decomposes it, patterned on the SCIS and FIS: asset ownership (0–2) + alternative availability (0–3) + replacement time (< 12 months 2; 12–36 months 1; > 36 months 0); maximum 7. The verifier re-derived each term for the key input from the record's stated basis.

| Term | Conservative | Central | Optimistic |
|---|---|---|---|
| Asset ownership (0–2) | 2 — the pool's balances are the bank's own liabilities | 2 | 2 |
| Alternative availability (0–3) | 1 — the master trust, at a price that fails the margin | 2 — the trust and a warehouse line, both above the deposit cost | 2 |
| Replacement time (0–2) | 1 (⚠ 12–18 months from a standing start) — **2 with the design commitment** (under 12 months with the route documented and the tape maintained) | 2 | 2 |
| **HRS (max 7; ≥ 5 pass; ≤ 3 NCR)** | **4 without the commitment; 5 with it — PASS** | **6 — PASS** | **6 — PASS** |

The verifier found no term it would score differently, and one term it reads as conditional: the conservative corner passes only because of the four-part design commitment (the tape cut monthly from Stage 1; the programme documents drafted before Stage 3 and refreshed yearly; the cap holding the route's opening size under ⚠ £1bn; the quarterly trigger review). Each of the four is a build item or a standing activity in the AOM v10, so the verifier accepts the 5 as a score on the design as written, not on a design the record hopes for. The seven other supplier inputs score 4 to 7; the standard's operator scores 4 at every corner and is a standing constraint carried from C7, not a supplier with power. **The term the verifier flags for WS1:** the score is one point above the line at the conservative corner because no market lends to a bank at its own deposit cost — the alternative exists and costs more than the margin can bear. A score that passes on availability alone would hide this; the position-holding re-test below is where it shows.

## Position-holding re-test (registry F3 row) — R10's assumptions at their failure values

The registry row asks for the re-test where the score is below threshold. The score is above threshold at every corner with the commitment. The re-test is run anyway, as at r9: the funding line is the largest line of the floor, and the loss band is repeated because the loss rate is the binding input of the whole design.

| Assumption | Holds because of R10 | Failure value | Floor high at failure | Margin at 140 | Margin at 135 | Verdict |
|---|---|---|---|---|---|---|
| the funding line at the pool's measured deposit cost ⚠ 1.5–3.0% (PVC) | the line is funded inside its pool under a signed term, read daily, with the market route beside it | ⚠ 4.0% — a transfer-price convention at Bank Rate (FACT for the rate; T4 for the convention) | 117.47 | **19.2%** | 14.9% | **BORDERLINE at the set price; FAIL at the band's low end** |
| the same line, on the market route | the route is the alternative when the pool's price is overridden | ⚠ 4.6% (SONIA + 0.6%) | 123.47 | **13.4%** | 9.3% | **FAIL** |
| — | — | ⚠ 5.0% (SONIA + 1.0%) | 127.47 | **9.8%** | 5.9% | **FAIL** |
| the route's upkeep without issuance (RC) | the route is maintained, not used | ⚠ £1–2m a year with the route open — RC 2.20–5.63 | 107.88 | 29.8% | 25.1% | PASS |
| the drawn book against the pool's balances (volume) | the cap | the pool's balances fall ⚠ 20–40% and the cap binds at ⚠ £3.0–4.0bn | 107.47 (no floor change) | 30.3% | 25.6% | PASS on the margin; the PCO objective is read in the fin-sim |
| the loss band ⚠ 2–4% (PVC) — repeated from r9 at the C10 floor | R9's calibration, not R10 | ⚠ 4.5% | 112.47 | **24.5%** | 20.0% | **BORDERLINE** |
| — | — | ⚠ 5.0% | 117.47 | **19.2%** | 14.9% | **BORDERLINE at the set price; FAIL at the band's low end** |
| — | — | ⚠ 6.0% | 127.47 | **9.8%** | 5.9% | **FAIL** |

**What the re-test says, unsoftened.** The margin depends on R10 holding the funding line at the pool's deposit cost. Without it — a transfer price at Bank Rate — the design is BORDERLINE at the set price and FAIL at the band's low end; on the market route it fails at every point of the band. The market route holds the venture's existence and not its margin. The design has two independent holds on the two largest lines of the floor (R9 on the loss, R10 on the funding), and a failure of either takes the margin below the gate; a failure of both (Bank Rate and a 5.0% loss) gives a floor high of 127.47 and 9.8% — FAIL. The cap and the route's upkeep hold at their failure values. This is recorded in the C10 record as a design finding (the margin's dependence on R10), and the consistency audit reads it beside the R9 finding and the SCIS finding. The failure values are runner's calls (T4): the convergence event for the funding line is the term's first year of daily readings from Stage 1; for the loss band, the held-out cohort's loss at the first replica's 24 months.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| the price | 140.00 (band 135.00–142.50) | 140.00 — one rate for the pool |
| operating bar = floor × 1.25 | 68.86 | 134.34 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| room on the binding bar at the set price | worst: 140.00 − 134.34 = **5.66** | best: 140.00 − 68.86 = 71.14 |
| carries | **true** at every point of the band (0.66 at 135) | |
| max payable to any holder (VA-164) | 0 at the pessimistic corner (the tariff given up, C6) | 5.66 at central; paid 0 |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** the term is signed before Stage 1 (⚠ £1–3k, in SC); the route is set up before Stage 3 (⚠ £1–3m, in SC) and its upkeep runs from Stage 2 (RC); the pool funding itself is a liability at the measured deposit cost from the first release and needs no working capital. **Partner's return (VA-156):** unchanged — none paid; the treasury's business case is a saving against the wholesale alternative, not a fee. **Count line (VA-155)** as printed in the C10 record: the daily price reading (365 a year), the cap reading (12), the tape cut (12), the trigger review (4), the route's upkeep (1); gate G18 — the drawn book at ⚠ 10% of the pool's credit balances.

## The ⚠ £8 cap (RD-030), running line

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |
| R6 | nil — nothing removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.27 | ⚠ 7.73 |
| R7 | ⚠ 6–35 (broker commission, referral fees, partner marketing, a partner desk) — removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.28 | ⚠ 7.72 |
| R8 | ⚠ 5–15 (loyalty pricing, exit fees, product tie-ins, a retention desk) — removed | ⚠ 1.00 rounded (0.45–1.50 unrounded) | ⚠ 1.05–1.28 rounded (0.50–1.78 unrounded) | ⚠ 6.72 |
| R9 | ⚠ 0 (a bureau score licence, a scorecard vendor, a data-science hire) — nothing to remove | ⚠ 0.01–0.03 | ⚠ 1.05–1.29 rounded (0.51–1.81 unrounded) | ⚠ 6.71 |
| **R10** | **⚠ 1–3 (the bureau, scoring and aggregator feeds a conventional line buys as its supplier inputs; the signal ⚠ 0.1–0.3 has sat inside computing since C1) — removed by number** | **⚠ 0.05–0.18 rounded (0.09–0.36 unrounded)** | **⚠ 1.10–1.47 rounded (0.60–2.17 unrounded)** | **⚠ 6.53** |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £6.60 at the set price (0.933), £8.00 at 0.95. At the set price the R4–R10 additions use 1.47 of 6.60 rounded; 2.17 of 6.60 unrounded. **Function 3 in total** (R8–R10) added ⚠ 1.06–1.21 rounded and removed a conventional line of ⚠ 6–18. The verifier notes that R10's removal is booked by number and not by activity: the conventional line's feeds were never in this form's cost, so the removal is the difference between two designs and not a saving the bank would see in its accounts — stated so that the cap line is not read as a cash saving.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 67.47 + 10L (every other line at its high corner; 67.29 at r9).

| The price | Bar = price ÷ 1.25 | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 135.00 (band low) | 108.00 = 67.47 + 10L → **4.05%** | 135.00 → 6.75% | −0.95 points — the gate sits inside the pivot |
| **140.00 (the set price)** | 112.00 → **4.45%** | 140.00 → 7.25% | −0.55 points — the gate sits inside the pivot |
| 142.50 (band high) | 114.00 → **4.65%** | 142.50 → 7.50% | −0.35 points |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.05 points at 135, **0.45 at the set price** and 0.65 at 142.5 — each 0.02 tighter than at r9, the cost of R10's upkeep line. The loss rate remains the binding input. **The second gate, read for the first time at this pass:** at a funding cost F (per cent of drawn), the high-corner floor is 77.47 + 10F; the 25% gate at the set price is reached at F = 3.45% with the loss at its high corner (112.00 − 77.47 = 34.53); 3.05% at the band's low end and 3.65% at its top; zero margin at 6.25%. **Correction made at this pass:** the C10 record v1 first printed this gate as 3.99%, a figure that does not reproduce (funding at 39.9 gives a floor high of 117.37 and a margin of 19.3%, not 25%); the record was corrected to 3.45% before the verifier closed and the correction is entered in its changelog. The measured deposit cost ⚠ 1.5–3.0% clears the gate by ⚠ 0.45–1.95 points — at the deposit cost's high corner the same 0.45 that the loss gate leaves. Bank Rate (4.0%) fails it.

## Function 3 close and the Phase II capital gate, by hand

`check_verdict_order.py` reads no F3 gate, so the close is read here. **F3 barrier scores:** SCIS 2 · 4 · 6 (C8 — below the line at the conservative corner; design finding, not NCR); FIS 5 · 6 · 7 (C9 — PASS); HRS 5 · 6 · 6 with the commitment (C10 — PASS; 4 without). Two of three pass at every corner; the SCIS is carried as a design finding with its convergence event (the seasoning schedule's first re-fit). **F3 margin:** 30.3% at the set price; the function used 0.23 points of margin across three requirements. **F3 verdict: PROVISIONAL** (capped by R1–R9; every input Tier 4).

**Phase II capital gate (≥ 60% PASS · 25–59% BORDERLINE · < 25% FAIL), at the conservative scenario:** every layer at its high corner, the price at the set price — margin 30.3% → **BORDERLINE**. The gate is a re-reading of the same arithmetic at a higher line; nothing in the design fails it, and nothing in the design reaches it at the conservative corner. **Binding input:** the loss rate — at ⚠ 2.0% (floor high 87.47) the conservative scenario reads 60.1% and passes; at the assumed 4.0% it reads 30.3%. No other single input reaches 60% from the conservative corner: the funding line at 1.5% takes the floor high to 92.47 and the margin to 51.4%; the two together (funding 1.5%, loss ⚠ 2.6%) reach 60.2%. **At the central scenario** (floor 81.28) the margin is 72.2% — PASS. **Worst-corner margin on the Phase II line:** 30.3% − 60% = −29.7 points. What tightens the reading is the Stage 1 twelve-month loss reading on the pool; the fin-sim prints the sensitivity at 2%, 3%, 4%, 4.8%, 5%, 6% and 7.65%.

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000 plus the tape's compute (⚠ 0.00 at two decimals); the route's upkeep starts at Stage 2. Floor at Stage 1: 40.02 + 3.84 + 0 + 13 = 56.86 to 83.25 + 32.40 + 1 + 18 = 134.65. Worst-corner margin at the set price: (140.00 − 134.65) ÷ 134.65 = **4.0%**; 0.3% at the band's low end; 5.8% at its top. Stage 1 does not carry the 25% gate on its own book at the high corner, as at r3 to r9; the release order carries it to scale. At Stage 1 the drawn book is ⚠ 0.4–3.8% of the pool's balances (⚠ £50–100bn); the cap is not close to binding and the pool funds the line from the first release at the measured deposit cost.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R10 removes the block — the line's funding was priced by a convention outside the line, so the line's largest cost could be moved by a party with no stake in the line. After the move the price is a signed term read daily from the pool's own measured deposit cost, and the line is funded by the balances it sits among; the treasury's alternative use of those balances is the wholesale market, which costs more. The lock-out is structural: a rival without a deposit franchise cannot fund a facility line at a deposit cost, and a rival with one has no reason to price it to a line it does not run. What R10 does not remove: the gap between the deposit cost and the market's. The record states this as the design's finding and the verifier confirms it is not softened anywhere in the record.

**I-Cost: PASS.** The things R10 could have added and did not: a treasury desk for the line, a standing issuance programme, a rating on the route, a warehouse line drawn and paid for, a deposit product of the line's own. The activities it adds are one daily price reading inside a computation already run, one monthly tape cut from a ledger already written, one term signed once, one route set up once (⚠ £1–3m) and maintained by ⚠ 0.3–0.6 people, one quarterly review at an existing sitting, and two standing records (data protection; prudential). The verifier checked the AOM v10 3c rows and found the head-count change is inside treasury's existing function (⚠ 0.3–0.6 of a person).

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r9 chain is unchanged. R10 adds the supplier chain: when a party has made an investment specific to a relationship, the counterparty can appropriate the quasi-rent by repricing after the investment is sunk, and the remedy is to bring the transaction inside one governance (Klein, Crawford and Alchian 1978); the deposit franchise's cost advantage over wholesale money is a property of the depositors, whose rate moves less than the policy rate (Drechsler, Savov and Schnabl 2017, deposit beta below one). The funding term brings the line's funding inside one governance at the deposit cost; the cap keeps the line a net user of balances the pool already holds; the market route is the outside option that sets the ceiling on any internal price.

**T-Robustness: PASS.** The contrast — Williamson 1985's reading that a bilateral contract with safeguards, not integration, is the remedy where asset specificity is moderate — argues the term alone suffices and the route is surplus cost. The contrast fails on the counterparty: the treasury is not a bilateral counterparty but a function of the same firm that can rewrite the convention the term reads, so the safeguard must be an outside option and not a clause. Diamond and Dybvig 1983 supplies the second contrast — deposits are demandable and the funding is not stable — and it is answered by the cap: at ⚠ 10% of the pool's credit balances the line is inside the stable share of deposits under the NSFR's 90–95% weighting for retail and SME deposits, and a ⚠ 20–40% outflow binds the cap on volume without moving the margin. Both contrasts name the exact terms the design depends on rather than overturning it.

## What the pass says

1. At C10 the floor is 55.09–107.47 and the price is 140. The margin at the worst corner is 30.3% at the set price (by hand; 30.2% by the script), 25.6% at the band's low end and 32.6% at its top. R10 carries; the funding term costs ⚠ 0.05–0.18 rounded against a conventional line of ⚠ 1–3 removed by number.
2. The loss gate at the set price is 4.45%, 0.02 tighter than at r9. The loss rate is the binding input. A second gate is read for the first time: the funding line fails the 25% gate at 3.45% with the loss at its high corner (the record's first figure, 3.99%, did not reproduce and was corrected); the measured deposit cost ⚠ 1.5–3.0% clears it by 0.45–1.95 points and Bank Rate fails it.
3. HRS scores 5 / 6 / 6 with the design commitment — PASS at every corner; 4 at the conservative corner without it. The position-holding re-test was run regardless and is recorded unsoftened: 19.2% BORDERLINE at Bank Rate, 13.4–9.8% FAIL at the market; the loss band repeated at the C10 floor (24.5% / 19.2% / 9.8%).
4. The cap line stands at ⚠ 1.10–1.47 rounded of ⚠ 8.00; ⚠ 6.53 remains. Function 3 closes with the cap line unbreached.
5. Function 3 closes PROVISIONAL, read by hand because the script reads no F3 gate. The Phase II capital gate at the conservative scenario is BORDERLINE (30.3% against 60%); the binding input is the loss rate; the conservative scenario passes only at a loss of ⚠ 2.0% or below; the central scenario passes at 72.2%.
6. For WS1: the HRS terms are undefined in the registry and were set by the runner; the registry's re-test condition would again have skipped the one re-test that matters; the fit model has no field for a barrier score or a position-holding table and the runner's block is used; and `check_verdict_order.py` reads no F3 gate, so the function close is a by-hand reading in this pass.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1–r9 | 18–21 September 2026 | As in `bank-credit-facility-fit-verifier-r9-2026-09-21.md`. |
| r10 | 21 September 2026 | Pass after C10 — PASS at 30.3% at the set price (by hand; `fit_margin.py` 30.2% at 139.95), 25.6–32.6% across the band; floor 55.09–107.47. `check_verdict_order.py` IN ORDER with R10 added. `validate_tam_model.py` on version 4 — valid with three declared warnings carried from version 3. HRS 5 / 6 / 6 with the design commitment (4 without) — PASS at every corner. Position-holding re-test on the funding line: 19.2% BORDERLINE at Bank Rate, 13.4% / 9.8% FAIL at the market; loss band repeated at the C10 floor. Loss gate 4.45%; funding gate 3.45% (the record's first figure 3.99% corrected at this pass). Cap line: R10 ⚠ 0.05–0.18; cumulative ⚠ 1.10–1.47; remaining ⚠ 6.53. F3 closes PROVISIONAL by hand; Phase II gate BORDERLINE at the conservative scenario, binding input the loss rate. |
