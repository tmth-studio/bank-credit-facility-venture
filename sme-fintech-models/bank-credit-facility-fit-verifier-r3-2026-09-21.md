# A business bank's credit facility line — fit verifier, pass r3 (after C3) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C3.yaml`, state at-C3. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Reference volume:** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2, WP-3, WP-4, WP-5, CP-1 (amended), PC-1 (condition) — the C3 set. **What changed since r2:** the SC layer is populated; nothing else in the model moved.

## Independence of this pass

The floor bands were derived in the AOM v3 (sections 3e and 6) from the activity register, bottom-up; the KMC band is the TAM data object v2's, unchanged. The verifier reads the model file and computes; it did not set either band. **The one shared line (VA-97):** expected loss sits inside the PVC band and is also the binding gate named in the C3 record. The margin and the gate are therefore not independent on that one line; the verifier states this and does not claim they are. The SC layer shares nothing with the gate: its largest item (the overlay's carrying cost) is a function of the overlay share, not the loss rate.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40–83 | T4 ⚠ | unchanged from r2: funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2–5 (the shadow-limit field sits inside) · exception handling and write-off 3–8 |
| RC — recurring fixed | 2–5 | T4 ⚠ | unchanged from r2: ⚠ 47 HQ people and technology £7.2–12.8m ÷ £3.4–5.7bn; the stage readings are hours inside model risk's 10, not new people |
| SC — scaling | 0–1 | T4 ⚠ | AOM v3 3e: one-off ⚠ £0.64–12.1m (back-test and validation 0.3–0.8; migration 0.3–0.85; three stage readings 0.045–0.135; the overlay's carrying cost 0–10.4) ÷ 5 years ÷ £3.4–5.7bn = 0.02–0.71, rounded up |
| IC — investment and capital | 12–17 | T4 ⚠ | unchanged from r2: drawn 10.8–13.5 · undrawn 1.6–3.4 |
| **Floor** | **54–106** | | complete on four layers; the high corner moves by £1 |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged from r2 (TAM data object v2, KMC-OD-STD-TARIFF) |
| Customer surplus fraction | 0.95 | judged | unchanged from r2 |
| Operating bar (required price) | 132.50 | fixed number | floor high corner 106 × 1.25; does not read the ceiling |

## Script run — REFUSED, and why

Commands, run 21 September 2026:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C3.yaml`
- `python3 .claude/skills/shared/generators/check_verdict_order.py 04-Projects/Product_Strategy/bank-credit-facility-c3-v1-2026-09-21.md`
- `python3 .claude/skills/shared/generators/validate_tam_model.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-tam-model.yaml`

```
REFUSED: the toolchain does not match its manifest:
    - test_pool_at_risk.py is present and not in the manifest — an unlisted script in the toolchain directory
    - validate_model.py does not match its recorded digest — it has been edited since the last seal
    - validate_tam_model.py does not match its recorded digest — it has been edited since the last seal
  [the instruction to re-seal, omitted here — the seal is the principal's]
Nothing was computed. There is no margin of safety to quote.
exit 2
```

The second and third commands refused with the same three lines ("Nothing was ordered" and "Nothing was validated"). The refusal is not about this model or this record. The state is the one r2 recorded: the checking scripts carry the RD-031 additions and one new test file, and the seal that records them is the principal's, batched (publication rule, 16 September 2026). The runner does not seal and does not run a copy of the scripts elsewhere. **Queued re-run:** all three commands, after the seal; the by-hand figures below are to be replaced by the scripts' output, and the FAIL/PASS lines in the C3 record's checks table updated from "by hand" to "script".

## By hand, replicating the script's arithmetic (surplus fraction 0.95)

| Step | Low corner | High corner |
|---|---|---|
| cost floor = pvc + rc + sc + ic | 40 + 2 + 0 + 12 = **54** | 83 + 5 + 1 + 17 = **106** |
| price ceiling = KMC × 0.95 | 150 × 0.95 = **142.50** | 300 × 0.95 = **285.00** |
| net contribution | worst: 142.50 − 106 = **36.50** | best: 285.00 − 54 = **231.00** |
| margin of safety | worst: 36.50 ÷ 106 = **34.4%** | best: 231.00 ÷ 54 = **427.8%** |
| required price at 60% | 54 × 1.6 = 86.40 | 106 × 1.6 = 169.60 |
| required price at 25% | 54 × 1.25 = 67.50 | 106 × 1.25 = 132.50 |
| operating bar 132.50 against ceiling low 142.50 | clears by 10.00 | — |

**Verdict at the worst corner: PASS at 34.4% (≥ 25%).** The verdict is no longer INDICATIVE on floor completeness: all four layers are declared from activities. It stays PROVISIONAL on evidence: every input the verdict depends on is Tier 4, and the loss rate is unmeasured. This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.

## By hand, on the undiscounted price

- Worst corner: (150 − 106) ÷ 106 = **41.5%**.
- Best corner: (300 − 54) ÷ 54 = **455.6%**.
- The carrying check in the C3 record uses these undiscounted figures, as the challenge skill's block does; the fit model's discounted figures are the gate.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| operating bar = floor × 1.25 | 67.50 | 132.50 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| headroom on the binding bar | worst: 150 − 132.50 = **17.50** | best: 300 − 67.50 = 232.50 |
| carries | **true** at every corner | |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** the C3 record's timing check finds no working capital beyond the drawn balance itself; the receipts share returns cash with each receipt (⚠ 1–2 days). The path's working capital is the overlay, costed as carrying cost in SC. **PCO estimate against derived:** unchanged from r2 — selection holds.

## Binding input and its threshold

The expected-loss line is the only input that can move the verdict on its own. At a loss rate L (per cent of drawn), the high-corner floor is 66 + 10L (every other line at its high corner). Against the discounted ceiling of 142.50:

| Loss rate | Floor | Margin | Reading |
|---|---|---|---|
| 4.0% (the band's high corner) | 106 | 34.4% | PASS |
| **4.8%** | **114** | **25.0%** | **the 25% gate — the trial band's continue line** |
| 5.0% (the pivot trigger) | 116 | 22.8% | BORDERLINE — 0.8 points inside the pivot |
| 7.65% | 142.5 | 0% | zero margin |

The 0.8-point gap between the gate (4.8%) and the pivot (5.0%) is the whole tolerance the design has on its one unmeasured input. It is stated, not hidden. The trial band in the C3 record is set on these three numbers.

## Stage 1 spread count (VA-162), by hand

At Stage 1 the RC layer is carried by the migrated book alone (⚠ £0.4–1.9bn drawn): £7.2–12.8m ÷ £0.4–1.9bn = 3.8–32 per £1,000. Floor at Stage 1: 40 + 3.8 + 0 + 12 = 55.8 to 83 + 32 + 1 + 17 = 133. Worst-corner margin: (142.5 − 133) ÷ 133 = **7.1%** discounted; (150 − 133) ÷ 133 = **12.8%** undiscounted. Stage 1 clears its cost but not the 25% gate on its own. The C3 record names this: Stage 1 is viable standalone (positive contribution), and Stage 2 must open for the margin to reach the gate. The at-scale figure is the FIT input; the Stage 1 figure is the path's.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** Unchanged from r2: the overdraft's renewal and fee event stop existing at migration (WP-4); the price condition (PC-1) records the consequence.

**I-Cost: PASS.** R3 adds no per-account annual activity. The path's costs are one-off and sit in SC at 0–1. The shadow limit is the same computation with one extra field. The stage readings are hours inside an existing function. The one thing R3 could have added and did not: a per-cohort underwriting or review step. The release is by stage against a band, not by account.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r2 chain (Stiglitz and Weiss 1981; Petersen and Rajan 1994; Berger and Udell 2006; FinRegLab 2019 and 2025) is unchanged for the value side. R3 adds the scaling chain. The constraint on scale is where the learning happens (Pisano 1994, *Strategic Management Journal* 15). Learning before doing is available where the underlying process is well understood, and the bank's own history is such a process. The value of waiting for the loss signal before committing capital is the option value of staged commitment (Dixit and Pindyck 1994). Mechanism: the back-test converts history into evidence before any release; existing exposure makes the first release capital-free; each replica's band converts observed loss into the next release. Outcome: the overlay falls from whole-book to stage-sized, and the time to scale falls from ⚠ 36–60 months (forward cohorts) to ⚠ 27–42.

**T-Robustness: PASS.** Neither Pisano 1994 nor Dixit and Pindyck 1994 is on the fragile-findings list; both are replicated foundations of learning-curve and real-options work. The value-side theories are as r2.

## What the pass says

1. At C3 the floor is complete on four layers at 54–106. The selected customer's KMC clears it with a 34.4% margin at the worst corner and 17.50 per £1,000 of headroom over the operating bar. R3 carries; F1 is arithmetically closed.
2. The margin rests on the loss line. The gate holds up to 4.8%; the pivot is 5.0%; the margin is zero at 7.65%. One unmeasured Tier 4 input decides the verdict, and the design's tolerance on it is 0.8 points.
3. The SC layer is small because the one move (release by existing exposure) makes the first stage capital-free and the later stages replica-sized. If the overlay share the auditor requires is above 25% on Stage 1, the SC layer rises: at 100% of the modelled allowance (⚠ £228m at the top of the whole-book case) the carrying cost is ⚠ £27–34m a year, and SC rises to ⚠ 1–2 — still inside the margin. The SC layer does not decide the verdict at any overlay share the runner can find a precedent for.
4. The scripts did not run. The figures above are the runner's arithmetic on the model file's declared inputs and are to be replaced by the scripts' output after the principal's seal.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. Source correction on the KMC band recorded. I check and T check added. |
| r3 | 21 September 2026 | Pass after C3 — PASS at 34.4% (by hand; three scripts refused pending the principal's seal), floor complete on four layers, PROVISIONAL on evidence. Binding-input table, Stage 1 spread count and the scaling theory chain added. |
