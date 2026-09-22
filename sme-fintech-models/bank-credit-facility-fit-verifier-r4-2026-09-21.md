# A business bank's credit facility line — fit verifier, pass r4 (after C4) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility of a large UK SME bank (unnamed; every internal figure a red field). **Model:** `bank-credit-facility-fit-model-at-C4.yaml`, state at-C4. **Unit:** £ per £1,000 of average drawn balance, per year, at scale. **Reference volume:** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2, WP-3, WP-4, WP-5, CP-1 (amended C2 and C4), CP-2 (new), PC-1 (condition) — the C4 set. **What changed since r3:** the Selling stream's activities are added inside the PVC and RC layers (⚠ 0.03–0.20); the surplus fraction and the productive hours are bands, not points; the operating bar moves from 132.50 to 132.75. The KMC is unchanged.

## Independence of this pass

The floor bands were derived in the AOM v4 (sections 3a, 3b, 3c, 3f and 6) from the activity register, bottom-up; the KMC band is the TAM data object v2's, unchanged. The verifier reads the model file and computes; it did not set either band. **The one shared line (VA-97):** expected loss sits inside the PVC band and is also the binding gate named in the C4 record. The margin and the gate are not independent on that line; the verifier states this and does not claim they are. The C4 additions share nothing with the gate: the history, the reviewer and the queries are counts of accounts, templates and questions, not of losses.

## The four layers

| Layer | Band (£ per £1,000 a year) | Tier | Derived from |
|---|---|---|---|
| PVC — per-unit variable | 40.01–83.16 | T4 ⚠ | funding 15–30 · expected loss 20–40 (⚠ 2–4%) · computing and payments 2.01–5.07 (C4: the limit history adds ⚠ 0.01–0.07) · exception handling and write-off 3.00–8.09 (C4: the limit-query handlers add ⚠ 0.00–0.09) |
| RC — recurring fixed | 2.02–5.04 | T4 ⚠ | ⚠ 48 HQ people and technology £7.3–12.95m ÷ £3.4–5.7bn (C4: +1 conduct reviewer, ⚠ 0.02–0.04) |
| SC — scaling | 0–1 | T4 ⚠ | unchanged from r3 |
| IC — investment and capital | 12–17 | T4 ⚠ | unchanged from r2: drawn 10.8–13.5 · undrawn 1.6–3.4 |
| **Floor** | **54.03–106.20** | | four layers; the high corner moves by ⚠ 0.20 |
| KMC — the standard-tariff overdraft cash outflow | 150–300 | T3 (low corner T1; high corner ⚠) | unchanged from r2 (TAM data object v2, KMC-OD-STD-TARIFF) |
| Customer surplus fraction | 0.90–1.00 (0.95 convention) | T3 | C4: a band, was a point — verify-F1 fault F-1 closed |
| Operating bar (required price) | 132.75 | fixed number | floor high corner 106.20 × 1.25; does not read the ceiling |

## Script run — REFUSED, and why

Command, run 21 September 2026 from the vault root:

- `python3 .claude/skills/shared/generators/fit_margin.py 04-Projects/Product_Strategy/sme-fintech-models/bank-credit-facility-fit-model-at-C4.yaml`

```
REFUSED: the toolchain does not match its manifest:
    - test_pool_at_risk.py is present and not in the manifest — an unlisted script in the toolchain directory
    - validate_model.py does not match its recorded digest — it has been edited since the last seal
    - validate_tam_model.py does not match its recorded digest — it has been edited since the last seal
  [the instruction to re-seal, omitted here — the seal is the principal's]
Nothing was computed. There is no margin of safety to quote.
exit 2
```

The state is the one r2 and r3 recorded. The seal is the principal's, batched (publication rule, 16 September 2026). The runner does not seal and does not run a copy of the scripts elsewhere. **Queued re-run:** the command above, plus `check_verdict_order.py` on the C4 record, after the seal; the by-hand figures below are to be replaced by the scripts' output.

## By hand, replicating the script's arithmetic

The surplus fraction is a band, so the worst corner is computed three times. The convention (0.95) is the reporting centre; the two ends bound it.

| Step | 0.90 | 0.95 (convention) | 1.00 |
|---|---|---|---|
| cost floor, high corner = 83.16 + 5.04 + 1 + 17 | **106.20** | **106.20** | **106.20** |
| cost floor, low corner = 40.01 + 2.02 + 0 + 12 | **54.03** | **54.03** | **54.03** |
| price ceiling, low corner = 150 × fraction | 135.00 | 142.50 | 150.00 |
| price ceiling, high corner = 300 × fraction | 270.00 | 285.00 | 300.00 |
| net contribution, worst = ceiling low − floor high | 28.80 | 36.30 | 43.80 |
| margin of safety, worst = net ÷ floor high | **27.1%** | **34.2%** | **41.2%** |
| net contribution, best = ceiling high − floor low | 215.97 | 230.97 | 245.97 |
| margin of safety, best = net ÷ floor low | 399.7% | 427.5% | 455.2% |
| required price at 25% = 106.20 × 1.25 | 132.75 | 132.75 | 132.75 |
| headroom = ceiling low − 132.75 | 2.25 | 9.75 | 17.25 |
| required price at 60% = 106.20 × 1.6 | 169.92 | 169.92 | 169.92 |

**Verdict at the worst corner: PASS at 34.2% on the convention; PASS at every point of the surplus band (27.1% at 0.90).** The margin against r3 falls by 0.2 points (34.4% → 34.2%) — the whole of the R4 addition. The verdict stays PROVISIONAL on evidence: every input the verdict depends on is Tier 4, and the loss rate is unmeasured. This verdict is arithmetic on declared inputs. It is not evidence that any input is true of the world.

**The band's own threshold:** the worst-corner margin reaches 25% where 150 × f = 132.75, f = 0.885. The low corner 0.90 sits 0.015 above it. Below 0.885 the verdict is BORDERLINE with no change to the floor. This is the first number C6 must read: the price it sets inside the band decides whether the design keeps the 25% margin or spends it.

## Carrying check (challenge skill section 8), by hand

| Item | Low corner | High corner |
|---|---|---|
| KMC | 150 | 300 |
| operating bar = floor × 1.25 | 67.54 | 132.75 |
| capital bar = PCO capital parameters ÷ drawn book | £148.5m ÷ £5.7bn = 26.05 | £148.5m ÷ £3.4bn = 43.68 |
| binding bar | operating at both corners | |
| headroom on the binding bar (undiscounted) | worst: 150 − 132.75 = **17.25** | best: 300 − 67.54 = 232.46 |
| carries | **true** at every corner | |

**Floor completeness:** four of four layers declared from activities. **Working capital timing:** unchanged from r3; R4 adds no cash timing — the history is a read, not a payment. **PCO estimate against derived:** unchanged — selection holds.

## The ⚠ £8 cap (RD-030), running line

| Requirement | Conventional line | Added by this form | Cumulative | Remaining at the high corner |
|---|---|---|---|---|
| R4 | ⚠ 2–8 (marketing and outreach) — removed | ⚠ 0.03–0.20 | ⚠ 0.03–0.20 | ⚠ 7.80 |

The cap is the number the counterfactual set: R4–R10 additions at the high corner must stay at or below ⚠ £8 per £1,000 at a surplus fraction of 0.95. The cap itself moves with the fraction — ⚠ £2.00 at 0.90, £8.00 at 0.95, £14.00 at 1.00 — because it is the headroom the ceiling leaves over the operating bar. At 0.90 the R4 addition of 0.20 uses a tenth of the cap. The line is carried to C7.

## Binding input and its threshold

The expected-loss line is the only input that can move the verdict on its own. At a loss rate L (per cent of drawn), the high-corner floor is 66.20 + 10L (every other line at its high corner). The 25% gate and the zero-margin line are read at each corner of the surplus band:

| Surplus fraction | Ceiling (low corner) | Loss rate at the 25% gate | Loss rate at zero margin | Margin to the ⚠ 5.0% pivot |
|---|---|---|---|---|
| 0.90 | 135.00 | 108.00 = 66.20 + 10L → **4.2%** | 135.00 → 6.9% | −0.8 points — the gate sits inside the pivot |
| 0.95 (convention) | 142.50 | 114.00 → **4.8%** | 142.50 → 7.6% | 0.2 points |
| 1.00 | 150.00 | 120.00 → **5.4%** | 150.00 → 8.4% | 0.4 points beyond the pivot |

Two readings of the same line, both used. Against the assumed high corner of the loss band (4.0%), the gate leaves 0.2 points at 0.90, 0.8 at 0.95 and 1.4 at 1.00 — the "0.2–1.4 points" the C4 record prints. Against the pivot, at the convention the gap between the gate (4.8%) and the pivot (5.0%) is 0.2 points — r3 wrote 0.8 by rounding 4.78 to the gate line and 5.0 to the pivot; the arithmetic here uses the unrounded gate, and the tolerance is smaller than r3 stated. At the low corner of the surplus band the pivot is outside the gate: a design priced at 0.90 of the tariff with a 5.0% loss rate is BORDERLINE, not PASS. The trial band in the C4 record is set on these numbers.

## Stage 1 spread count (VA-162), by hand

At Stage 1 the RC layer is carried by the migrated book alone (⚠ £0.4–1.9bn drawn): £7.3–12.95m ÷ £0.4–1.9bn = 3.84–32.38 per £1,000. Floor at Stage 1: 40.01 + 3.84 + 0 + 12 = 55.85 to 83.16 + 32.38 + 1 + 17 = 133.54. Worst-corner margin: (142.50 − 133.54) ÷ 133.54 = **6.7%** at the convention; (135.00 − 133.54) ÷ 133.54 = **1.1%** at 0.90; (150 − 133.54) ÷ 133.54 = **12.3%** undiscounted. Stage 1 clears its cost at every point of the band and reaches the 25% gate at none. Unchanged reading from r3: Stage 1 is viable standalone; Stage 2 must open for the margin to reach the gate.

## I check — is the cost driver removed at the design level?

**I-Value: PASS.** The overdraft's renewal and fee event stop existing at migration (WP-4); unchanged from r2. R4 adds a second removal: the want block is removed by placing the bank's own record beside the limit, not by a message. There is no campaign to run and no message that could be un-run.

**I-Cost: PASS.** R4 adds no acquisition activity. The one thing R4 could have added and did not: a marketing or outreach line (the conventional ⚠ 2–8). The three activities it adds are a read of a ledger the bank holds (per account, automated), one sign-off role, and a query type inside a cell that exists. None of them scales with the number of customers to be convinced; the history scales with accounts, and the query rate is bounded by the release count.

## T check — is the theory chain explicit and robust?

**T-Chain: PASS.** The r3 chain is unchanged for the value and scaling sides. R4 adds the conviction chain. A claim the receiver can verify against a record is believed; a claim they cannot verify is discounted as talk (Milgrom 1981, *Bell Journal of Economics* 12 — verifiable disclosure; Crawford and Sobel 1982, *Econometrica* 50 — the contrast: cheap talk is discounted). Evidence the receiver draws from their own experience is weighted above evidence supplied by the seller (Hoch and Deighton 1989, *Journal of Marketing* 53). Mechanism: the limit is shown beside twelve months of the customer's own shortfalls, each one dated, with the balance and the limit on that day; the customer reads a record they already trust, at the moment the shortfall recurs. Outcome: the credibility gap closes without a message, and the draw is the customer's act.

**T-Robustness: PASS.** Milgrom 1981 is a foundational result in disclosure theory, replicated across the persuasion-game literature; Hoch and Deighton 1989 is a conceptual paper whose central claim (self-generated evidence outweighs supplied evidence) is supported by the later work on the self-generation effect. Neither is on the fragile-findings list. The one theory set aside, Samuelson and Zeckhauser 1988 (status quo bias), is not on the list either; the record sets it aside because inertia is not the block, not because the finding is fragile.

## What the pass says

1. At C4 the floor is 54.03–106.20. The selected customer's KMC clears it with a 34.2% margin at the worst corner on the convention and 27.1% at the low corner of the surplus band. R4 carries; the conviction activities cost ⚠ 0.03–0.20 against a conventional line of ⚠ 2–8.
2. The margin rests on two inputs now, not one. The loss line still decides the verdict on its own; the surplus fraction decides how much tolerance the loss line has. At 0.95 the tolerance is 0.2 points; at 0.90 it is gone. C6 sets the fraction, and the C6 record must show the loss-gate line at the price it chooses.
3. The cap line is open: ⚠ 7.80 of ⚠ 8.00 remains for R5–R10 at the high corner.
4. The scripts did not run. The figures above are the runner's arithmetic on the model file's declared inputs and are to be replaced by the scripts' output after the principal's seal.

## Changelog

| Version | Date | Change |
|---|---|---|
| r1 | 18 September 2026 | Pass after C1 — FAIL at −32.1% on the whole-book price, INDICATIVE. |
| r2 | 21 September 2026 | Pass after C2 — PASS at 35.7% (by hand; script refused pending the principal's seal), INDICATIVE. |
| r3 | 21 September 2026 | Pass after C3 — PASS at 34.4% (by hand; three scripts refused), floor complete on four layers, PROVISIONAL on evidence. |
| r4 | 21 September 2026 | Pass after C4 — PASS at 34.2% on the convention, 27.1–41.2% across the surplus band (by hand; script refused). Surplus fraction and productive hours as bands. Loss-gate line read at three corners; the r3 tolerance of 0.8 points corrected to 0.2. Cap line opened: R4 ⚠ 0.03–0.20 of ⚠ 8.00. |
| r4.1 | 21 September 2026 | Queued re-run executed after the seal of 19:49 (not the runner's): `fit_margin.py` PASS at 34.2% on the at-C4 model — matches the hand table above. A colon-space in the model file's PVC source text stopped the file from being read; changed to a dash, no number changed. |
