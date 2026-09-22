# A business bank's credit facility line — fit verifier, pass r7 (after C7; the Function 2 gate) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C7.yaml`, state at-C7. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Gate:** per requirement, 25%. **What changed since r6:** PP-1 — the released standing limit published as the account's pre-agreed credit line in the balance response the bank already serves to every account-information reader, and the receipt splits as transaction lines. No partner is paid. R7 adds ⚠ 0.00–0.01 to the floor's high corner (the element in ⚠ 0.50–0.78bn balance calls a year) and ⚠ £50–100k of one-offs inside the SC band. The price and its band are unchanged. This pass also closes Function 2: the cap line R4–R7 is complete. Every figure below is Tier 4 unless marked.

## Independence of this pass

The floor bands were derived in the AOM v7 (sections 3a, 3b, 3c, 3e, 3h and 6) from the activity register, bottom-up; the KMC band is the TAM data object's (version 3 at C7 — the band is unchanged from version 2); the price is the C6 record's runner's call, unchanged at C7. The verifier reads the model file and computes; it did not set any band or the price. **The one shared input (VA-97):** the loss rate, which sits in the floor and is the binding gate; the margin is a transform of it. **The price is the second shared input** (from C6): it sets where on the loss line the gate sits. R7 adds no shared input: the partner's return is nil under both readings (VA-156), so no partner figure enters the floor or the ceiling.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.24 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2.02–5.11 (C7: the credit-line element adds ⚠ 0.00–0.01) · exception handling and write-off 3.00–8.13 (C7: display queries inside the C5 headroom, no addition) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | unchanged from r6: the desk position sits inside the existing conduct people; the account-information team adds no people |
| SC — scaling | 0–1 | T4 ⚠ | one-off total ⚠ £0.72–12.25m (C7: the element's population rule ⚠ £40–80k and the conformance test ⚠ £10–20k added) ÷ 5 years ÷ £3.4–5.7bn = 0.03–0.72, rounded up to 0–1 |
| IC — investment and capital | 12–17 | T4 ⚠ | unchanged from r2: nothing published is exposure |
| **Floor** | **54.04–106.28** | | four layers; the high corner moves by ⚠ 0.01; the low corner does not move |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged (TAM data object v3, KMC-OD-STD-TARIFF) |
| The price (C6, unchanged) | 140.00 — band ⚠ 135.00–142.50 | T4 (runner's call with logic) | 14.0% simple a year; surplus fraction 0.933; band 0.90–0.95 |
| Operating bar (required price) | 132.85 | fixed number | floor high corner 106.28 × 1.25; does not read the ceiling |

## Script run — EXECUTED

Command, run 21 September 2026 from the vault root:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C7.yaml`

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  state              : at-C7
  cost floor         : GBP 54.0400 to 106.2800   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9330
  price ceiling      : GBP 139.9500 to 279.9000   (key cost x fraction)
  net contribution   : GBP 33.6700 to 225.8600   (worst corner to best corner)
  MARGIN OF SAFETY   : 31.7% at the worst corner (ceiling low against floor high); 417.9% at the best corner
  required price at 60%: GBP 86.4640 to 170.0480
  required price at 25%: GBP 67.5500 to 132.8500
  required price bar : GBP 132.8500   (stated in fixed-number form)
  checks reaching a verdict : 31   (all pass)
  notes: derived_from.operating_model resolves · derived_from.customer_model resolves · header date 2026-09-21 is within 24 hours of the last edit on disk · the price ceiling (low end 139.9500) clears the stated required price bar 132.8500
  gate applied       : per_requirement
  VERDICT            : PASS at 31.7% (worst corner; best corner 417.9%)
```

Exit 0. By hand at 140.00 the worst-corner margin is 31.73%, the script's 31.69% at 139.95 — both 31.7%. **The script's best corner (417.9%) is not used**, as at r6: it multiplies the KMC band's high corner by the fraction, but the customer on a £300 tariff pays 140; the best corner at the set price is (140.00 − 54.04) ÷ 54.04 = **159.1%**, by hand.

**`check_verdict_order.py`** run on the verdict record `bank-credit-facility-verdict-record.yaml` with R7 added (R1–R7, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; seven checks reached a verdict; function gate F1 reads PROVISIONAL at R3; **function gate F2 reads PROVISIONAL at R7**. Exit 0.

**`validate_tam_model.py`** run on the TAM data object, version 3 at C7 (`bank-credit-facility-tam-model.yaml`): **✅ valid (with declared warnings)**; exit 0. Three warnings, each read:

- [L4] ×2 — SC-OD-BELOW-BAND and SC-LOAN-USER are marked not addressable but carry a live KMC (KMC-LOAN-RATE). *Read:* the script's model of "not addressable" is elimination by a supplied alternative (KMC → KMC-0). Here the KMC is live — the class does pay a loan rate — and the venture cannot address it because its set price (140) exceeds that KMC (75–90): a block named "price", not an elimination. The warning is correct on the script's model and does not apply on the design's; recorded for WS1 as a gap in the script's vocabulary (a class can be excluded by the venture's price while its cost stays live).
- [L7] — volume.basis is 'incidence' while sub-classes are defined against supplied alternatives. *Read:* carried from version 2; no segment share in any record is quoted against the incidence volume — the own-volume note (41,800–113,050) is the denominator every record uses.
- L11 note — pool at risk stated for one incumbent (INC-BANK-TARIFF-OD). *Read:* the block the script asked for at r6 is now present; the venture is mode 3, so the one incumbent is the bank's own tariff line.

## By hand, replicating the script's arithmetic across the price band

| Step | 135.00 (0.90) | 140.00 (0.933, the set price) | 142.50 (0.95) |
|---|---|---|---|
| cost floor, high corner = 83.24 + 5.04 + 1 + 17 | **106.28** | **106.28** | **106.28** |
| cost floor, low corner = 40.02 + 2.02 + 0 + 12 | **54.04** | **54.04** | **54.04** |
| the price | 135.00 | 140.00 | 142.50 |
| net contribution, worst = price − floor high | 28.72 | 33.72 | 36.22 |
| margin of safety, worst = net ÷ floor high | **27.0%** | **31.7%** | **34.1%** |
| net contribution, best = price − floor low | 80.96 | 85.96 | 88.46 |
| margin of safety, best = net ÷ floor low | 149.8% | 159.1% | 163.7% |
| required price at 25% = 106.28 × 1.25 | 132.85 | 132.85 | 132.85 |
| room = price − 132.85 | 2.15 | 7.15 | 9.65 |
| required price at 60% = 106.28 × 1.6 | 170.05 | 170.05 | 170.05 |

**Verdict at the worst corner: PASS at 31.7% at the set price (script and by hand); PASS at every point of the band (27.0% at 135, by hand).** No figure moved at one decimal from r6; R7's addition to the floor is ⚠ 0.01 at the high corner. The verdict stays PROVISIONAL: every input the verdict depends on is a Tier 4 band, the price is a runner's call, and the partner mechanism (the platforms' display of the element) is unmeasured.

**The band's own threshold:** the worst-corner margin reaches 25% where the price = 132.85, f = 0.886 (13.28%). Unchanged.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| the price | 140.00 (band 135.00–142.50) | 140.00 — one rate for the pool |
| operating bar = floor × 1.25 | 67.55 | 132.85 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| room on the binding bar at the set price | worst: 140.00 − 132.85 = **7.15** | best: 140.00 − 67.55 = 72.45 |
| carries | **true** at every point of the band (2.15 at 135) | |
| max payable to any holder (VA-164) | 0 at the pessimistic corner (the tariff given up, C6) | 7.15 at central; paid 0 |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** unchanged from r6 — nothing published moves money. **Partner's return (VA-156):** neither fee-in-the-floor nor share-of-surplus; the unit margin is 31.7% under either reading because both are zero. **Count line (VA-155)** as printed in the C7 record: ⚠ 437,000 connected accounts at central; ⚠ 342,000–532,000 at scale; the PCO screen 760,000 accounts with a limit; the objective £148.5m at year five = ⚠ 42,000–71,000 drawn accounts against 228,000 at scale; G15 gate ≥ 2 of 3 platforms displaying, margin one.

## The ⚠ £8 cap (RD-030), running line — Function 2 complete

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |
| R6 | nil (the counterfactual books no cost against the price structure) — nothing removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.27 | ⚠ 7.73 |
| R7 | ⚠ 6–35 (broker commission, platform referral fees, partner marketing, a partner desk) — removed | ⚠ 0.00–0.01 | ⚠ 0.05–0.28 | ⚠ 7.72 |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £6.60 at the set price (0.933), £8.00 at 0.95. At the set price the R4–R7 additions use 0.28 of 6.60. **Function 2 closes with ⚠ 0.05–0.28 of the ⚠ £8 used; the conventional lines removed sum to ⚠ 9–45 per £1,000** — on a £4.5bn book, ⚠ £40–200m a year the conventional form spends on the four blocks this form removes for ⚠ £0.3–1.3m. The line is carried to R8–R10 (counterfactual R8 5–15, R9 0, R10 1–3) with ⚠ 7.72 remaining.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 66.28 + 10L (every other line at its high corner; 66.27 at r6).

| The price | Bar = price ÷ 1.25 | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 135.00 (band low) | 108.00 = 66.28 + 10L → **4.17%** | 135.00 → 6.87% | −0.83 points — the gate sits inside the pivot |
| **140.00 (the set price)** | 112.00 → **4.57%** | 140.00 → 7.37% | −0.43 points — the gate sits inside the pivot |
| 142.50 (band high) | 114.00 → **4.77%** | 142.50 → 7.62% | −0.23 points |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.17 points at 135, **0.57 at the set price** and 0.77 at 142.5 — unchanged from r6 at two decimals. The C5 default-funded gap (0.3–0.5 points) sits inside the 0.57 at the set price. R7 adds a gate with no floor effect (G15 — the platforms' display; a failed G15 loops R7 back to SR2, it does not move the margin) and one query rate with a threshold (display queries ⚠ 0.1–0.3%, threshold 1%, above which a handler is added and the R7 line rises to ⚠ 0.05).

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000. Floor at Stage 1: 40.02 + 3.84 + 0 + 12 = 55.86 to 83.24 + 32.38 + 1 + 17 = 133.62. Worst-corner margin at the set price: (140.00 − 133.62) ÷ 133.62 = **4.8%**; (135.00 − 133.62) ÷ 133.62 = **1.0%** at the band's low end; (142.50 − 133.62) ÷ 133.62 = **6.6%** at its top. Stage 1 does not carry the 25% margin at any point of the band, as at r3–r6; the stage order and the F1 condition (Stage 2 within ⚠ 24 months) are the design's answer.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R7 removes the access block — the limit's absence from the seat where a connected customer's shortfall is first foreseen. After the move the limit is present at every seat that reads the account; no partner decision remains for the block to depend on. The unconnected account has no seat outside the bank; C4's placement holds it, and the record names this as a bounded limit.

**I-Cost: PASS.** The four things R7 could have added and did not: a broker commission, a platform referral fee, a partner desk, an accountant programme — the conventional line of ⚠ 6–35. The activities it adds are one element in a response already served (⚠ £5–8k a year), two one-offs (⚠ £50–100k) inside the SC band, a desk position inside existing conduct hours, and a query type inside the C5 headroom. None scales with a count of partners; the one driver that scales (`q.connected_accounts`) scales with the customer's consents, and its cost is ⚠ 0.00 per £1,000.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r6 chain is unchanged for value, scaling, conviction, activation and payment. R7 adds the access chain. Where an installed base already reads a compatibility standard, an actor carries a compatible feature without a decision: the cost of carrying it is the conformance already paid, and the benefit is its own product's compatibility with what the rest of the base shows (Farrell and Saloner 1985, *RAND Journal of Economics* 16(1)). The limit is published into an element every conforming reader already parses; each reader's own product — the forecast, the ledger — is correct with the element and wrong without it. The at-scale claim rests on the standard, not on any reader's behaviour toward the venture.

**T-Robustness: PASS.** The contrast theory — asymmetric motivation (Christensen and Raynor 2003) — argues that a fee-paid partner's motivation shrinks as the product substitutes for its core; here no fee is paid and the platform's core is served, not substituted, so the contrast names why the display-agreement mutation is rejected rather than overturning the design. The customer-side theory is physical availability (Sharp 2010; Romaniuk and Sharp 2016): the product is present where the customer looks. The Farrell and Saloner result is a model, not a field finding; the direction is used, and the hypothesis (≥ 2 of 3 large platforms displaying the element at the first replica's six months with no bank contact) measures the display, not the theory.

## What the pass says

1. At C7 the floor is 54.04–106.28 and the price is 140. The margin at the worst corner is 31.7% at the set price (script and by hand), 27.0% at the band's low end and 34.1% at its top. R7 carries; the access mechanism costs ⚠ 0.00–0.01 against a conventional line of ⚠ 6–35.
2. The loss gate at the set price is 4.57%, unchanged at two decimals. R7 adds no floor-moving gate; G15 (the platforms' display) loops the requirement, it does not move the margin.
3. Function 2 closes with the cap line at ⚠ 0.05–0.28 of ⚠ 8.00 used; ⚠ 7.72 remains for R8–R10. Every F2 requirement removed the block the conventional form pays for; none paid for it.
4. Three script findings for WS1: the fit model's best-corner artefact (r6, unchanged); the TAM script's "not addressable" vocabulary has no case for a class excluded by the venture's price while its cost stays live (L4 ×2); the verdict-order script now reads F2 at R7 without a change to the record's shape.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. |
| r3 | 21 September 2026 | Pass after C3 — PASS at 34.4% (by hand; three scripts refused), floor complete on four layers, PROVISIONAL on evidence. |
| r4 | 21 September 2026 | Pass after C4 — PASS at 34.2% on the convention, 27.1–41.2% across the surplus band (by hand; script refused). Cap line opened: R4 ⚠ 0.03–0.20 of ⚠ 8.00. |
| r5 | 21 September 2026 | Pass after C5 — PASS at 34.1% on the convention (`fit_margin.py`, run after the 19:49 seal), 27.0–41.2% across the band (by hand). Re-runs at C3 and C4 confirm r3 and r4. `check_verdict_order.py` IN ORDER on the new verdict record. Cap line: R5 ⚠ 0.02–0.06; cumulative ⚠ 0.05–0.26. |
| r6 | 21 September 2026 | Pass after C6 — PASS at 31.7% at the set price (`fit_margin.py` at a surplus fraction of 0.933), 27.0–34.1% across the price band (by hand). The best corner reported by hand at the set price (159.1%); the script's band figure recorded as a model-shape limit. `check_verdict_order.py` IN ORDER with R6 added. Loss gate at the set price 4.57%. Cap line: R6 ⚠ 0.00–0.01; cumulative ⚠ 0.05–0.27; remaining ⚠ 7.73. |
| r7 | 21 September 2026 | Pass after C7 — PASS at 31.7% at the set price (`fit_margin.py`), 27.0–34.1% across the band (by hand); floor 54.04–106.28. `check_verdict_order.py` IN ORDER with R7 added; F2 reads PROVISIONAL at R7. `validate_tam_model.py` on the data object v3 at C7: valid with three declared warnings (L4 ×2 read as a vocabulary gap; L7 carried), the pool-at-risk block present. Cap line: R7 ⚠ 6–35 removed, ⚠ 0.00–0.01 added; cumulative ⚠ 0.05–0.28; remaining ⚠ 7.72. Function 2 closed. |
