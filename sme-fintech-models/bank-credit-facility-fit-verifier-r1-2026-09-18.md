# A business bank's credit facility line — fit verifier, pass r1 (after C1) · 18 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C1.yaml`, state at-C1. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Reference volume:** `[average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1 standing limit, WP-2 the draw, WP-3 receipts share. **Gate applied:** per-requirement (PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%). **Mode-3 rule (RD-024 (e)):** the margin is measured against the price the borrower pays today and does not gate; the R1 failure test gates.

## Independence of this pass

The floor bands were derived in the AOM (section 6) from the activity register, bottom-up; the price bands were derived in the fit model from the Bank of England effective rate and public overdraft pricing. The verifier reads the model file and computes; it did not set either band. The one shared line is expected loss: it sits inside the PVC band and is also the binding gate named in the C1 record. That sharing is declared, not hidden.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40–83 | T4 ⚠ | funding 15–30 (deposit cost ⚠ 1.5–3.0%) · expected loss 20–40 (⚠ 2–4%) · computing and payments 2–5 · exception handling and write-off 3–8 |
| RC — recurring fixed | 2–5 | T4 ⚠ | ⚠ 70 people and technology £8.5–14.5m ÷ £3.4–5.7bn (AOM 3c) |
| SC — scaling | excluded | — | not designed until C3 |
| IC — investment and capital | 12–17 | T4 ⚠ | 75% risk weight × ⚠ 12% capital × ⚠ 12–15% cost of equity on drawn = 10.8–13.5 · undrawn limits ⚠ 1.5–2.5 per £1 drawn × 10% credit conversion factor = 1.6–3.4 |
| **Floor** | **54–105** | | |
| KMC — the price paid today | 75–120 | T4 ⚠ (rate band FACT; blend ⚠) | Bank of England effective rate on new SME loans 6.18–7.00% (2025) · overdrafts ⚠ 10–15% · fees ⚠ 1–2% · blended ⚠ 7.5–12% |
| Customer surplus fraction | 0.95 | judged | the fee element discounted a twentieth; the fraction must be strictly below one (method gap logged 16 Sep 2026) |

## Script output, pasted

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  model              : 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C1.yaml
  venture            : Business bank credit facility line (Case B)
  state              : at-C1
  bounded at         : GBP per 1000 of average drawn balance, per year, at-scale

  cost floor         : GBP 54.0000 to 105.0000   (layers pvc, rc, ic)
  layers excluded    : sc
  key cost           : GBP 75.0000 to 120.0000
  surplus fraction   : 0.9500
  price ceiling      : GBP 71.2500 to 114.0000   (key cost x fraction)
  net contribution   : GBP -33.7500 to 60.0000   (worst corner to best corner)
  MARGIN OF SAFETY   : -32.1% at the worst corner (ceiling low against floor high); 111.1% at the best corner

  required price at 60%: GBP 86.4000 to 168.0000
  required price at 25%: GBP 67.5000 to 131.2500

  checks reaching a verdict : 22
  notes:
      - derived_from.operating_model resolves
      - derived_from.customer_model resolves
      - header date 2026-09-18 is within 24 hours of the last edit on disk
      - cost_floor.layers.pvc is a band 40.0000 to 83.0000 (tier T4)
      - cost_floor.layers.rc is a band 2.0000 to 5.0000 (tier T4)
      - cost_floor.layers.sc excluded: C3
      - cost_floor.layers.ic is a band 12.0000 to 17.0000 (tier T4)
      - price_ceiling.kmc is a band 75.0000 to 120.0000 (tier T4)

  gate applied       : per_requirement
  VERDICT            : FAIL at -32.1% (worst corner; best corner 111.1%)
  ** The verdict is INDICATIVE. 1 cost layer(s) are excluded, so the margin is optimistic. **
  This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.
```

## By hand, on the undiscounted price

- Worst corner: (75 − 105) ÷ 105 = **−28.6%**.
- Best corner: (120 − 54) ÷ 54 = **122%**.
- Centre of both bands: floor 79.5, price 97.5 → (97.5 − 79.5) ÷ 79.5 = **22.6%** (BORDERLINE band). The script's centre, with the fraction applied, is 16.5%.
- Conventional form on the same unit (AOM 6: ⚠ 60–154): worst corner (75 − 154) ÷ 154 = −51%; best corner (120 − 60) ÷ 60 = 100%.

## What the pass says

1. The margin is not a verdict on the design in mode 3; it is the report the rule asks for. The shape — negative at the worst corner, wide at the best — is the same in the conventional form, because funding and capital are ⚠ 25–44 of every floor that lends.
2. The worst corner of the new form is the high-loss pool (expected loss at ⚠ 4%, funding at ⚠ 3%). The worst corner of the conventional form is the small facility. The design moves the binding constraint from the facility's size to the pool's loss rate.
3. What most changes the figure: the loss rate. At the central price (97.5) and the central non-loss floor (49.5), the floor equals the price at a loss of 4.8% of drawn balance. The assumed high corner (4.0%) leaves 0.8 points. This is an unmeasured input; the bank's own loss by account-conduct band is not public.
4. The pass converges when the loss line is replaced by the bank's figure and the ⚠ cost lines by the bank's cost by function. Until then: **PROVISIONAL, non-gating, reported.**

## Note added after the baseline correction (18 September 2026, C1 v2)

The computed margin is unchanged: the new form's floor and the price paid today did not move. What moved is the comparison. The bank's roadmap form (pre-approved, digitally fulfilled) has a floor of ⚠ 57–133 on the pre-approved segment; its margin against the same price is −44% at the worst corner and 111% at the best. The drop from roadmap form to new form is ⚠ 5–21% at the blended book (v1 measured ⚠ 10–32% against the older application form). The same-shape comparison stands: the roadmap form's negative corner is the small facility; the new form's is the high-loss pool.

## Changelog

| Pass | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | First pass, after C1. |
| r1.1 | 18 September 2026 | Comparison re-cut against the roadmap form after the insider's baseline correction; computed margin unchanged. |
