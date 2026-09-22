# A business bank's credit facility line — fit verifier, pass r2 (after C2) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C2.yaml`, state at-C2. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Reference volume:** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1 standing limit, WP-2 the draw, WP-3 receipts share, WP-4 migration, CP-1 the limit statement as amended, PC-1 the price condition. **Gate applied:** per-requirement (PASS ≥ 25% · BORDERLINE 15–24% · FAIL < 15%). **Mode-3 rule at C2 (RD-024 (e)):** the ceiling is now the R2 key monetizable cost — the cash outflow the selected customer pays today on a standard-tariff overdraft. The margin gates R2 through the carrying check.

## Independence of this pass

The floor bands were derived in the AOM v2 (section 6) from the activity register, bottom-up; the KMC band was derived in the TAM data object v2 from published representative overdraft rates. The verifier reads the model file and computes; it did not set either band. **The one shared line (VA-97):** expected loss sits inside the PVC band and is also the binding gate named in the C2 record. The margin and the binding gate are therefore not two independent checks — they are one financial check read twice. This pass reports one financial check. An independent second check would be a count, not a rate: the share of the bank's overdraft accounts on the standard tariff (the population the margin applies to) or the share of overdraft holders who accept migration. Neither is a public figure; both are the insider's.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40–83 | T4 ⚠ | funding 15–30 (deposit cost ⚠ 1.5–3.0%) · expected loss 20–40 (⚠ 2–4%; held, not lowered, for the observed-conduct migrated pool) · computing and payments 2–5 (the saving statement adds ⚠ 0.003) · exception handling and write-off 3–8 (2.3 cells at ⚠ 17,000 hours, ⚠ £1.8–2.4m, plus write-off administration ⚠ 3–7) |
| RC — recurring fixed | 2–5 | T4 ⚠ | ⚠ 47 HQ people and technology £7.2–12.8m ÷ £3.4–5.7bn (AOM v2 3c; the v1 double count of the exception cells removed) |
| SC — scaling | excluded | — | not designed until C3; the one-off migration cost (⚠ £0.1–0.5m notices; ⚠ 5,300–8,200 handler hours) is recorded there by number |
| IC — investment and capital | 12–17 | T4 ⚠ | 75% risk weight × ⚠ 12% capital × ⚠ 12–15% cost of equity on drawn = 10.8–13.5 · undrawn limits ⚠ 1.5–2.5 per £1 drawn × 10% credit conversion factor = 1.6–3.4 |
| **Floor** | **54–105** | | unchanged from C1 — R2 adds no annual line that survives rounding |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | published representative EARs 14.54–15.62% on unsecured business overdrafts up to £25,000 (HSBC UK; Lloyds Bank; Bank of Scotland; read 21 Sep 2026) · fees ⚠ 1–2% of the limit at 47% utilisation · high corner ⚠ 30% (top of tariff; non-bank receipts-share rate) |
| Customer surplus fraction | 0.95 | judged | the fee element discounted a twentieth; the fraction must be strictly below one (method gap logged 16 Sep 2026) |
| Operating bar (required price) | 131.25 | fixed number | floor high corner 105 × 1.25; does not read the ceiling (RB-V-025) |

## Script run — REFUSED, and why

Command: `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C2.yaml`

```
REFUSED: the toolchain does not match its manifest:
    - test_pool_at_risk.py is present and not in the manifest — an unlisted script in the toolchain directory
    - validate_model.py does not match its recorded digest — it has been edited since the last seal
    - validate_tam_model.py does not match its recorded digest — it has been edited since the last seal
  [the instruction to re-seal, omitted here — the seal is the principal's]
Nothing was computed. There is no margin of safety to quote.
exit 2
```

The refusal is not about this model. The checking scripts carry two additions from the R&D register (RD-031 driver discipline, staged 18 September 2026 as patch 4) and one new test file. The seal that records them is the principal's, batched (publication rule, 16 September 2026). The runner does not seal and does not run a copy of the scripts elsewhere — a copy is what the guard exists to refuse. **What was done about it:** the arithmetic below is done by hand on the same inputs, step by step. The script run is queued to be repeated after the seal. Until then the margin figure is runner-computed, not script-computed, and the C2 record says so.

## By hand, replicating the script's arithmetic (surplus fraction 0.95)

| Step | Low corner | High corner |
|---|---|---|
| cost floor = pvc + rc + ic | 40 + 2 + 12 = **54** | 83 + 5 + 17 = **105** |
| price ceiling = KMC × 0.95 | 150 × 0.95 = **142.50** | 300 × 0.95 = **285.00** |
| net contribution | worst: 142.50 − 105 = **37.50** | best: 285.00 − 54 = **231.00** |
| margin of safety | worst: 37.50 ÷ 105 = **35.7%** | best: 231.00 ÷ 54 = **427.8%** |
| required price at 60% | 54 × 1.6 = 86.40 | 105 × 1.6 = 168.00 |
| required price at 25% | 54 × 1.25 = 67.50 | 105 × 1.25 = 131.25 |
| operating bar 131.25 against ceiling low 142.50 | clears by 11.25 | — |

**Verdict at the worst corner: PASS at 35.7% (≥ 25%).** The verdict is INDICATIVE: one cost layer (SC) is excluded, so the margin is optimistic. This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.

## By hand, on the undiscounted price

- Worst corner: (150 − 105) ÷ 105 = **42.9%**.
- Best corner: (300 − 54) ÷ 54 = **455.6%**.
- The carrying check in the C2 record uses these undiscounted figures, as the challenge skill's block does; the fit model's discounted figures are the gate.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| operating bar = floor × 1.25 | 67.50 | 131.25 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| headroom on the binding bar | worst: 150 − 131.25 = **18.75** | best: 300 − 67.50 = 232.50 |
| carries | **true** at every corner | |

**Floor completeness:** three of four layers declared from activities (PVC, RC, IC); SC excluded by rule until C3. **PCO estimate against derived:** the PCO carried no KMC estimate in mode 3. The C1 ceiling (75–120, the price paid on the whole book) stood in for it. The derived C2 ceiling is 2.0–2.5× higher for the selected customer. Selection holds.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** The key monetizable cost is the tariff's cash outflow. The design removes its cause, not its effect. The overdraft product is retired from the account (WP-4), so the renewal and its fee event stop existing. The balance sits on a limit whose exposure is set by a rule from observed flow, not by a per-facility decision priced for information the bank lacks. The price condition (PC-1) is the recorded consequence — the customer's outflow falls because the bank's cost of holding the exposure fell at C1.

**I-Cost: PASS.** The C2 components add no per-account annual activity that survives rounding (AOM v2 section 6). The one-off migration cost is recorded and carried to C3 by number.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** Cause: the standard tariff prices adverse selection and the lender's information cost on a customer it cannot observe cheaply (Stiglitz and Weiss 1981, *American Economic Review* 71(3); Petersen and Rajan 1994, *Journal of Finance* 49(1)). Mechanism: the account's flow is that observation, and the bank already holds it (Berger and Udell 2006, *Journal of Banking and Finance* 30 — transactions lending on hard information). A limit set from the flow and repaid from receipts removes the information premium and the collection cost (FinRegLab 2019 and 2025 — cash-flow variables predict small-business default). Outcome: the price the customer pays can fall below the tariff while the bank's margin holds (the margin above). Each step is named; none is asserted without a source.

**T-Robustness: PASS.** None of the theories named is on the fragile-findings list (ego depletion, power posing, social priming, growth mindset, stereotype threat, money priming, the IAT). Stiglitz and Weiss 1981 and Petersen and Rajan 1994 are replicated foundations of credit rationing and relationship lending; FinRegLab's cash-flow results have been repeated across lenders in 2019 and 2025.

## What the pass says

1. At C2 the selected customer's KMC clears the C1 floor with a 35.7% margin at the worst corner and 18.75 per £1,000 of headroom over the operating bar. R2 carries.
2. The margin rests on the loss line. The 25% gate holds at the worst corner up to a loss rate of 4.9% (floor 105 − 40 + 49 = 114; 142.5 ÷ 114 − 1 = 25.0%). The margin reaches zero at 7.75%. At the pivot trigger of 5% the margin is 23.9%, BORDERLINE. The insider's loss rate on a flow-underwritten, observed-conduct pool is the one figure that moves the verdict.
3. The population the margin applies to is ⚠ 40–70% of the bank's overdraft accounts — assumed with its logic stated, not measured. It does not move the per-£1,000 margin; it moves the size of the prize.
4. The script did not run. The figures above are the runner's arithmetic on the model file's declared inputs and are to be replaced by the script's output after the principal's seal.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. Source correction on the KMC band recorded. I check and T check added. |
