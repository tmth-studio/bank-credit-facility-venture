# A business bank's credit facility line — fit verifier, pass r5 (after C5) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C5.yaml`, state at-C5. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Reference volume:** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2 (amended C5), WP-3, WP-4, WP-5, CP-1 (amended C2, C4 and C5), CP-2, PC-1 (condition) — the C5 set. **What changed since r4:** the Using stream's activation activities are added inside the existing layers — the funded-event notice (computing +0.00–0.02) and the funding-query handlers (exceptions +0.00–0.04); the one-off term drafting sits inside SC. The conventional R5 line (⚠ 1–2, onboarding and support for the first draws) is not booked. The drawn-book rise under default funding is not credited.

## Independence of this pass

The floor bands were derived in the AOM v5 (sections 3a, 3b, 3c, 3g and 6) from the activity register, bottom-up; the KMC band is the TAM data object v2's, unchanged. The verifier reads the model file and computes; it did not set either band. **The one shared line (VA-97):** expected loss sits inside the PVC band and is also the binding gate named in the C5 record. The margin and the gate are not independent on that line; the verifier states this and does not claim they are. **A second shared line opens at C5:** default funding raises the drawn book and may raise the loss rate on the default-funded pool (the loss gap, ⚠ ≤1 point hypothesis). The gap is not in the floor — the band 2.0–4.0% is held — so the margin below does not read it; the loss-gate table shows how much of the tolerance it could consume.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.02–83.22 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2.02–5.09 (C5: the notice adds ⚠ 0.00–0.02) · exception handling and write-off 3.00–8.13 (C5: the funding-query handlers add ⚠ 0.00–0.04) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | unchanged from r4: ⚠ 48 HQ people and technology £7.3–12.95m ÷ £3.4–5.7bn |
| SC — scaling | 0–1 | T4 ⚠ | unchanged from r3; the term drafting (⚠ £15–30k once) sits inside the band |
| IC — investment and capital | 12–17 | T4 ⚠ | unchanged from r2: drawn 10.8–13.5 · undrawn 1.6–3.4 |
| **Floor** | **54.04–106.26** | | four layers; the high corner moves by ⚠ 0.06; the low corner by 0.01 |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged from r2 (TAM data object v2, KMC-OD-STD-TARIFF) |
| Customer surplus fraction | 0.90–1.00 (0.95 convention) | T3 | unchanged from r4 |
| Operating bar (required price) | 132.83 | fixed number | floor high corner 106.26 × 1.25; does not read the ceiling |

## Script run — EXECUTED

At r2, r3 and r4 the script refused because the toolchain did not match its manifest. The manifest at `04-Projects/TMTH_Venture_Studio/Forge/WS1/toolchain-manifest.txt` was re-sealed at 19:49 on 21 September 2026 — not by the runner, who did not run `seal` (the seal is the principal's). `toolchain_guard.py verify` now reports PASS on 20 scripts. The queued re-run was executed. One defect in the model files was found and fixed first: the at-C4 and at-C5 files carried a colon-space inside the PVC source text, which the file format reads as a new field; the script stopped on it before computing. The text was changed to a dash; no number changed.

Command, run 21 September 2026 from the vault root:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C5.yaml`

```
Financial margin of safety — computed, not read   (fit_margin 1.1.0 (16 September 2026))
  model              : 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C5.yaml
  venture            : Business bank credit facility line (Case B)
  state              : at-C5
  bounded at         : GBP per 1000 of average drawn balance, per year, at-scale

  cost floor         : GBP 54.0400 to 106.2600   (layers pvc, rc, sc, ic)
  key cost           : GBP 150.0000 to 300.0000
  surplus fraction   : 0.9500
  price ceiling      : GBP 142.5000 to 285.0000   (key cost x fraction)
  net contribution   : GBP 36.2400 to 230.9600   (worst corner to best corner)
  MARGIN OF SAFETY   : 34.1% at the worst corner (ceiling low against floor high); 427.4% at the best corner

  required price at 60%: GBP 86.4640 to 170.0160
  required price at 25%: GBP 67.5500 to 132.8250
  required price bar : GBP 132.8300   (stated in fixed-number form)

  checks reaching a verdict : 31
  notes:
      - derived_from.operating_model resolves
      - derived_from.customer_model resolves
      - header date 2026-09-21 is within 24 hours of the last edit on disk
      - the price ceiling (low end 142.5000) clears the stated required price bar 132.8300

  gate applied       : per_requirement
  VERDICT            : PASS at 34.1% (worst corner; best corner 427.4%)
  This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.
```

Exit 0. The 31 checks that reached a verdict are the layer, unit, period, scale-state, tier-form, fraction and required-price checks; all pass.

**Re-runs on the earlier models, same command:** at-C3 PASS at 34.4% (matches r3 by hand); at-C4 PASS at 34.2% (matches r4 by hand). The by-hand figures in r3 and r4 stand.

**`check_verdict_order.py`** run on the new verdict record `bank-credit-facility-verdict-record.yaml` (R1–R5, each PROVISIONAL, covering C1 to C[n]): **IN ORDER — every verdict is at most the worst beneath it**; function gate F1 reads PROVISIONAL at R3. Exit 0.

## By hand, replicating the script's arithmetic across the surplus band

The script reports the convention (0.95). The two ends of the band are computed by hand.

| Step | 0.90 | 0.95 (convention) | 1.00 |
|---|---|---|---|
| cost floor, high corner = 83.22 + 5.04 + 1 + 17 | **106.26** | **106.26** | **106.26** |
| cost floor, low corner = 40.02 + 2.02 + 0 + 12 | **54.04** | **54.04** | **54.04** |
| price ceiling, low corner = 150 × fraction | 135.00 | 142.50 | 150.00 |
| price ceiling, high corner = 300 × fraction | 270.00 | 285.00 | 300.00 |
| net contribution, worst = ceiling low − floor high | 28.74 | 36.24 | 43.74 |
| margin of safety, worst = net ÷ floor high | **27.0%** | **34.1%** | **41.2%** |
| net contribution, best = ceiling high − floor low | 215.96 | 230.96 | 245.96 |
| margin of safety, best = net ÷ floor low | 399.6% | 427.4% | 455.1% |
| required price at 25% = 106.26 × 1.25 | 132.83 | 132.83 | 132.83 |
| headroom = ceiling low − 132.83 | 2.17 | 9.67 | 17.17 |
| required price at 60% = 106.26 × 1.6 | 170.02 | 170.02 | 170.02 |

**Verdict at the worst corner: PASS at 34.1% on the convention (script); PASS at every point of the surplus band (27.0% at 0.90, by hand).** The margin against r4 falls by 0.1 points (34.2% → 34.1%) — the whole of the R5 addition. The verdict stays PROVISIONAL on evidence: every input is Tier 4 and the loss rate is unmeasured. The C5 record's first draft printed the floor's low corner as 54.05; the script computes 54.04 (40.02 + 2.02 + 12); the record is corrected at v1.1.

**The band's own threshold:** the worst-corner margin reaches 25% where 150 × f = 132.83, f = 0.886 (was 0.885 at r4). The low corner 0.90 sits 0.014 above it.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| operating bar = floor × 1.25 | 67.55 | 132.83 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| headroom on the binding bar (undiscounted) | worst: 150 − 132.83 = **17.17** | best: 300 − 67.55 = 232.45 |
| carries | **true** at every corner | |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** default funding moves the draw's timing from the customer's act to the payment's authorisation; the receipts share repays as before; no new cash timing for the bank beyond the drawn-book rise (unmeasured, not credited). **PCO estimate against derived:** unchanged — selection holds.

## The ⚠ £8 cap (RD-030), running line

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |
| R5 | ⚠ 1–2 (onboarding, help content, a support line) — removed | ⚠ 0.02–0.06 | ⚠ 0.05–0.26 | ⚠ 7.74 |

The cap moves with the fraction — ⚠ £2.00 at 0.90, £8.00 at 0.95, £14.00 at 1.00. At 0.90 the R4 and R5 additions together use 0.26 of 2.00. The line is carried to C7. R6's conventional line is 0 and R7's is ⚠ 6–35: R7 is the requirement that can spend the cap.

## Binding input and its threshold

At a loss rate L (per cent of drawn), the high-corner floor is 66.26 + 10L (every other line at its high corner).

| Surplus fraction | Ceiling (low corner) | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 0.90 | 135.00 | 108.00 = 66.26 + 10L → **4.2%** | 135.00 → 6.9% | −0.8 points — the gate sits inside the pivot |
| 0.95 (convention) | 142.50 | 114.00 → **4.8%** | 142.50 → 7.6% | 0.2 points |
| 1.00 | 150.00 | 120.00 → **5.4%** | 150.00 → 8.4% | 0.4 points beyond the pivot |

Against the assumed high corner of the loss band (4.0%), the gate leaves 0.2 points at 0.90, 0.8 at 0.95 and 1.4 at 1.00. **New at C5:** the default-funded pool may carry a higher loss rate than the drawn-ahead pool; the C5 hypothesis bounds the gap at ⚠ 1 point, with opt-in by flow band as the fallback above it. A gap of 1 point at the pool's whole weight would consume the entire tolerance at 0.95 (0.8 points) and most of it at 1.00; the C5 record's estimate that the gap consumes 0.3–0.5 points of the tolerance assumes the default-funded share of the drawn book is ⚠ 30–50% (T4). C6 must show the loss-gate line at the price it chooses, with the gap included.

## Stage 1 spread count (VA-162), by hand

RC at Stage 1 on the migrated book alone (⚠ £0.4–1.9bn drawn): 3.84–32.38 per £1,000. Floor at Stage 1: 40.02 + 3.84 + 0 + 12 = 55.86 to 83.22 + 32.38 + 1 + 17 = 133.60. Worst-corner margin: (142.50 − 133.60) ÷ 133.60 = **6.7%** at the convention; (135.00 − 133.60) ÷ 133.60 = **1.0%** at 0.90; (150 − 133.60) ÷ 133.60 = **12.3%** undiscounted. Unchanged reading: Stage 1 is viable standalone and reaches the 25% gate at no point of the band; Stage 2 must open.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** R5 removes the draw as a customer act. The routine steps notice–decide–move do not exist after the move; the account authorises against balance plus limit as an arranged overdraft already does. No support, prompt or onboarding activity is added because there is nothing for the customer to learn.

**I-Cost: PASS.** The one thing R5 could have added and did not: an onboarding and support line (the conventional ⚠ 1–2). The activities it adds are an authorisation rule the account line already runs (£0), a notice per funded event (automated), a query type inside a cell that exists, and one term drafted once. None scales with the number of customers to be activated.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r4 chain is unchanged for value, scaling and conviction. R5 adds the activation chain. A default is taken up at a rate far above an equivalent opt-in because the default requires no act and the act is what the routine lacks (Madrian and Shea 2001, *Quarterly Journal of Economics* 116(4): 401(k) participation 49% → 86% under automatic enrolment). A behaviour that is cued by the environment and needs no decision persists without support (Wood and Neal 2007, *Psychological Review* 114). Contrast: Carroll, Choi, Laibson, Madrian and Metrick 2009 (*QJE* 124) — active choice raises participation above opt-in but below a default; this is why the design is a default with switch-off and not an active choice at each shortfall. Mechanism: the payment is met at authorisation for every channel; the customer's routine is the routine they had under the arranged overdraft. Falsification: the switch-off share above 25% or the reversal share above 15% at ⚠ 10,000 accounts.

**T-Robustness: PASS.** Madrian and Shea 2001 is replicated across the automatic-enrolment literature and in the UK by the Pensions Regulator's auto-enrolment evaluation (opt-out ⚠ 9–10%); the default effect is one of the most robust findings in behavioural economics (Jachimowicz, Duncan, Weber and Johnson 2019, *Behavioural Public Policy* 3 — meta-analysis, d = 0.68 across 58 studies). Wood and Neal 2007 is a review, not a single finding. Neither is on the fragile-findings list. The intention–behaviour gap (Sheeran 2002) supports the choice of a default over a prompt and the verdict does not depend on it.

## What the pass says

1. At C5 the floor is 54.04–106.26. The KMC clears it with a 34.1% margin at the worst corner on the convention (script) and 27.0% at the low corner of the surplus band (by hand). R5 carries; the activation activities cost ⚠ 0.02–0.06 against a conventional line of ⚠ 1–2.
2. The loss line now has a second reader: the default-funded pool's gap. At 0.95 the tolerance is 0.8 points against the assumed high corner and 0.2 against the pivot; a 1-point gap on a ⚠ 30–50% default-funded share consumes 0.3–0.5 of it. C6 must price with the gap shown.
3. The cap line is open: ⚠ 7.74 of ⚠ 8.00 remains for R6–R10 at the high corner; R7 is the one that can spend it.
4. The scripts ran. `fit_margin.py` and `check_verdict_order.py` agree with the hand arithmetic; the hand slip of 0.01 at the floor's low corner in the C5 record is corrected.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. |
| r3 | 21 September 2026 | Pass after C3 — PASS at 34.4% (by hand; three scripts refused), floor complete on four layers, PROVISIONAL on evidence. |
| r4 | 21 September 2026 | Pass after C4 — PASS at 34.2% on the convention, 27.1–41.2% across the surplus band (by hand; script refused). Cap line opened: R4 ⚠ 0.03–0.20 of ⚠ 8.00. |
| r5 | 21 September 2026 | Pass after C5 — PASS at 34.1% on the convention (`fit_margin.py`, run after the 19:49 seal), 27.0–41.2% across the band (by hand). Re-runs at C3 and C4 confirm r3 and r4. `check_verdict_order.py` IN ORDER on the new verdict record. Model-file colon defect fixed at C4 and C5. Cap line: R5 ⚠ 0.02–0.06; cumulative 0.05–0.26; remaining 7.74. |
