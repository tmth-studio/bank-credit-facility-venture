# A business bank's credit facility line — financial simulation at C10 · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every figure only the bank holds is a red field (⚠) and a band. **Runner:** Function 3 runner, Path C mode 3; propose-and-confirm, object-after to 23 September 2026 17:00. **Script:** `sme-fintech-models/bank_credit_facility_fin_sim.py` → `bank-credit-facility-fin-sim-outputs.json`; this document is written by the script from the outputs file. **Reads:** the fit model at C10 (four layers, KMC band, price, cap line) and the TAM data object version 4. **Edits:** nothing.

**Verdict, first.** At scale the design carries: the floor is 55.09–107.47 per £1,000 of drawn balance a year against a price of 140, a margin of 30.3% at the worst corner (25.6% at the band's low end; 154.1% at the best corner). The Phase II capital gate at the conservative scenario reads **BORDERLINE** — 30.3% against the 60% line, 29.7 points short — and the input that closes the gap is the loss rate: the conservative scenario passes 60% only at a loss of ⚠ 2.0% or below with every other line at its high corner. On the path, the venture's own capital peaks at £50.0m at the conservative corner (month 13), £25.0m at central and £0.5m at optimistic — inside the PCO's £100m envelope at every corner; the lending capital on the book (£0.36bn–£0.70bn at scale) is the bank's and is funded by the pool, so it is shown as funding and not as venture capital. Every C10 figure the simulation was asked to reproduce is reproduced (section 6). No figure in this document is a point estimate of the world: each is a corner of a declared band, and the inputs register names the source and tier of every band.

## 0 · Defined terms

- **Corner** — conservative: every cost line at its high corner and the book at its small corner (£3.4bn); optimistic: every cost line at its low corner and the book at £5.7bn; central: the midpoint of each band.
- **Floor** — PVC + RC + SC + IC per £1,000 of average drawn balance a year, the fit model's four layers.
- **Margin** — (price − floor) ÷ floor. Per-requirement gate 25%; Phase II capital gate 60% (25–59% BORDERLINE; below 25% FAIL).
- **Venture capital on the path** — the deepest cumulative operating deficit plus the overlay held in the same month; what the venture needs from the bank beyond the balances it lends.
- **Lending capital** — regulatory capital on the drawn and undrawn exposure: 75% risk weight × ⚠ 12% total capital × (drawn + 10% × undrawn). The bank's, not the venture's.
- **Operating cash** — revenue less funding, expected loss, computing, exceptions, the fixed layer and the one-offs in the month; before the cost of capital.

## 1 · The at-scale model — the P&L per £1,000 and for the book

| Line (£ per £1,000 drawn a year) | Conservative | Central | Optimistic |
|---|---|---|---|
| revenue — the set price (14.0% simple) | 140.00 | 140.00 | 140.00 |
| funding at the measured deposit cost (⚠ 3.0 / 2.25 / 1.5%) | 30.00 | 22.50 | 15.00 |
| expected loss (⚠ 4.0 / 3.0 / 2.0%) | 40.00 | 30.00 | 20.00 |
| computing and payments | 5.12 | 3.57 | 2.02 |
| exceptions and write-off handling | 8.13 | 5.57 | 3.00 |
| recurring fixed (the HQ layer and the route's upkeep) | 5.22 | 3.64 | 2.07 |
| scaling one-offs spread over five years | 1.00 | 0.50 | 0.00 |
| **contribution before the cost of capital** | 50.53 | 74.22 | 97.91 |
| cost of capital (IC) | 18.00 | 15.50 | 13.00 |
| **net contribution above the floor** | 32.53 | 58.72 | 84.91 |
| **floor** | **107.47** | **81.28** | **55.09** |
| **margin at 140** | **30.3%** | **72.2%** | **154.1%** |
| margin at 135 / 142.5 | 25.6% / 32.6% | 66.1% / 75.3% | 145.1% / 158.7% |
| operating bar (floor × 1.25); room at 140 | 134.34; 5.66 | 101.60; 38.40 | 68.86; 71.14 |

**For the book (⚠ £3.4bn conservative · £4.55bn central · £5.7bn optimistic), £m a year at scale.** The conservative column pairs the high cost lines with the large book (£5.7bn), and the optimistic column the low lines with the small book (£3.4bn) — the table's pairing, kept because the per-£1,000 margin does not depend on it. The record's worst corner for the margin is the high cost lines alone; the worst corner for the £m contribution would pair the high lines with the small book, and reads £110.6m before the cost of capital and £49.4m after it. Neither pairing is a claim that book and cost lines move together.

| Line (£m a year) | Conservative | Central | Optimistic |
|---|---|---|---|
| revenue | 798.0 | 637.0 | 476.0 |
| funding | 171.0 | 102.4 | 51.0 |
| expected loss | 228.0 | 136.5 | 68.0 |
| computing and payments | 29.2 | 16.2 | 6.9 |
| exceptions and write-off | 46.3 | 25.3 | 10.2 |
| recurring fixed | 29.8 | 16.6 | 7.0 |
| one-offs spread | 5.7 | 2.3 | 0.0 |
| **contribution before the cost of capital** | 288.0 | 337.7 | 332.9 |
| cost of capital | 102.6 | 70.5 | 44.2 |
| **net contribution** | 185.4 | 267.2 | 288.7 |
| lending capital on the book (the bank's; funded by the pool) | 698 | 522 | 364 |
| the pool's credit balances ⚠; the book's share; the cap at 10% | £100.00bn; 5.7%; £10.00bn | £75.00bn; 6.1%; £7.50bn | £50.00bn; 6.8%; £5.00bn |

**The cap's worst corner** is not a corner of this table: it is the large book against the small pool — £5.70bn against £50.00bn, a share of 11.4%. There the cap (£5.00bn) binds and cuts the book by 12.3%; the per-£1,000 margin is unchanged and the net contribution for the book falls in proportion. At the three corners of the table the cap does not bind.

**Against the PCO's objective.** The PCO's required-revenue line is £148.5m a year at year five (£100m ⚠ ASSUMED at 30%, at an assumed 20% margin — a required profit of £29.7m). The design's revenue at scale is 798–476m and its net contribution above the floor, after the cost of capital, is 185–289m — 6.2× the required profit at the conservative corner. The objective is not what binds; the 60% line is (section 4).

**The recurring fixed layer, two readings.** The fit model carries RC at 2.07–5.22 per £1,000 (the C1 band, rounded up, plus the route's upkeep). The AOM v10 3c derives the HQ layer's all-people cost at ⚠ £7.6–13.55m a year, which with the route's ⚠ £0.3–0.6m is ⚠ £7.9–14.15m — 1.39–4.16 per £1,000 across the corners. The at-scale table uses the carried band, so it reproduces the record; the monthly path uses the £ line, because a fixed cost on a path is a sum of money and not a rate. The difference is ⚠ 1.06 per £1,000 at the conservative corner: the floor carries that much more RC than the activities derive. It is headroom, held on purpose since C1, and it is named here so that the margin is not read as tighter than the activities make it.

## 2 · The scaling-stage model — the monthly path

**The path (C3 record):** Stage 0, the back-test, months −6 to −1. Stage 1, the migrated overdraft accounts, released at month 1 and read at month 12 (the trial band); overlay ⚠ £0–19m held for 12 months. Stage 2, replica 1 released at month 13 and read at month 18; replica 2 released at month 19 and read at month 24; overlay ⚠ £0–50m on each for 6 months. Stage 3, at scale, when the last tranche's drawn balances have seasoned. The HQ layer runs from month 1 at its full cost (the C3 record's finding: the fixed layer runs for the whole ramp); the route's upkeep runs from replica 2's release, when the route is set up. **Runner's calls on the path, each a red field:** a released tranche's drawn balance starts at ⚠ 80% of its seasoned level and reaches it over ⚠ 8–24 months (the seasoning); Stage 1's share of the at-scale book is the C3 band ⚠ £0.4–1.9bn against the book at the same corner; the two replicas split the rest equally.

| Path reading | Conservative | Central | Optimistic |
|---|---|---|---|
| Stage 1's share of the at-scale book | 7.0% | 25.3% | 50.0% |
| seasoning months per tranche | 24 | 16 | 8 |
| at scale reached | month 43 | month 35 | month 27 |
| **peak venture capital on the path** | £50.0m | £25.0m | £0.5m |
| in | month 13 | month 13 | month -1 |
| cumulative operating cash turns positive | month 6 | month 1 | month 1 |
| cumulative operating cash at month 60 (the PCO's window) | £1,098.9m | £1,341.2m | £1,420.8m |
| lending capital at scale (the bank's; shown as funding) | £697.7m | £522.1m | £364.1m |
| Stage 1 floor per £1,000 on its own book (year 1, excluding one-offs) | 141.66 | 87.71 | 57.71 |
| Stage 1 margin at the set price | -1.2% | 59.6% | 142.6% |

**Peak venture capital, read plainly.** The peak on every path is an overlay held, not money spent. At the conservative corner the venture's operating cash is negative for the first 5 months after launch (the migration one-off and the full HQ layer against a small, unseasoned migrated book — the largest cash shortfall is £1.8m at month 1, of which £1.3m is the Stage 0 work) and positive from month 6; the peak need is the replica overlay ⚠ £50m at month 13, when replica 1 is released, with cumulative cash already positive. At central the peak is the replica overlay at its midpoint (£25m); at optimistic the overlays are nil and the peak is the Stage 0 work alone (£0.5m). The PCO's £100m envelope is not approached on any path; the overlay is released at each reading, so the peak is held for six months and returned. What the path does not show and the record does: the lending capital on the book (£0.36bn–£0.70bn at scale), which the bank holds against the exposure and which the C3 record names as an unmeasured input (the bank's headroom).

**Stage 1 on its own book.** At the conservative corner Stage 1 does not cover its floor after the cost of capital: -1.2% on a year-one average drawn balance of £0.34bn (the migrated book at ⚠ 80% seasoning), with the HQ layer at the AOM v10 3c figure (⚠ £13.55m) and the cost of capital at 18 per £1,000. The C10 record's spread count printed 4.0% on the full ⚠ £0.4bn and the C3 people figure (⚠ £12.95m). The two readings say the same thing — Stage 1 does not carry the gate; the release order does — and differ by the seasoning call and ⚠ £0.6m of people cost. Operating cash before the cost of capital is positive from month 2 at every corner.

**Year by year, conservative corner (£m).**

| Year | Average drawn (£bn) | Revenue | Funding | Expected loss | Computing | Exceptions | Fixed | One-offs | Operating cash | Cost of capital | Contribution after capital |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.34 | 47.4 | 10.2 | 13.5 | 1.7 | 2.8 | 13.6 | 0.9 | 4.8 | 6.2 | -1.4 |
| 2 | 3.71 | 519.0 | 111.2 | 148.3 | 19.0 | 30.1 | 13.8 | 3.1 | 193.4 | 68.1 | 125.4 |
| 3 | 5.28 | 739.3 | 158.4 | 211.2 | 27.0 | 42.9 | 14.2 | 0.0 | 285.5 | 96.9 | 188.6 |
| 4 | 5.66 | 792.6 | 169.8 | 226.5 | 29.0 | 46.0 | 14.2 | 0.0 | 307.1 | 103.9 | 203.2 |
| 5 | 5.70 | 798.0 | 171.0 | 228.0 | 29.2 | 46.3 | 14.2 | 0.0 | 309.3 | 104.7 | 204.7 |

**Year by year, central and optimistic corners (£m, contribution after the cost of capital).**

| Year | Central: average drawn (£bn) | Central: operating cash | Central: contribution after capital | Optimistic: average drawn (£bn) | Optimistic: operating cash | Optimistic: contribution after capital |
|---|---|---|---|---|---|---|
| 1 | 1.00 | 67.1 | 51.7 | 1.57 | 149.3 | 129.1 |
| 2 | 3.32 | 247.4 | 195.9 | 2.85 | 276.4 | 239.8 |
| 3 | 4.43 | 336.5 | 267.8 | 3.39 | 331.5 | 287.9 |
| 4 | 4.55 | 345.5 | 275.1 | 3.40 | 332.0 | 288.3 |
| 5 | 4.55 | 345.5 | 275.1 | 3.40 | 332.0 | 288.3 |

**Monthly funding path, conservative corner — the months that matter (£m).** The full monthly table for every corner is in the outputs file.

| Month | Stage | Drawn (£bn) | Operating cash | Cumulative | Overlay held | Venture capital need |
|---|---|---|---|---|---|---|
| -6 | Stage 0 begins | 0.00 | -0.2 | -0.2 | 0.0 | 0.2 |
| -1 | Stage 0 ends | 0.00 | -0.3 | -1.3 | 0.0 | 1.3 |
| 1 | Stage 1 — migration | 0.32 | -0.5 | -1.8 | 19.0 | 20.8 |
| 12 | Stage 1 reading | 0.36 | 0.5 | 3.5 | 19.0 | 19.0 |
| 13 | replica 1 released | 2.48 | 10.6 | 14.1 | 50.0 | 50.0 |
| 18 | replica 1 reading | 2.61 | 11.2 | 68.8 | 50.0 | 50.0 |
| 19 | replica 2 released; route set-up begins | 4.75 | 20.8 | 89.6 | 50.0 | 50.0 |
| 24 | replica 2 reading; route set up | 4.99 | 21.9 | 196.9 | 50.0 | 50.0 |
| 36 | year 3 | 5.52 | 24.9 | 482.4 | 0.0 | 0.0 |
| 43 | at scale (conservative) | 5.70 | 25.8 | 660.7 | 0.0 | 0.0 |
| 60 | the PCO's window ends | 5.70 | 25.8 | 1,098.9 | 0.0 | 0.0 |

## 3 · Loss-rate sensitivity — the conservative corner, every other line at its high corner

| Loss rate | Floor high | Margin at 140 | Margin at 135 | 25% gate | Phase II 60% | Year-five contribution after capital (£m) | Peak venture capital (£m) | Cash turns positive |
|---|---|---|---|---|---|---|---|---|
| ⚠ 2.00% | 87.47 | 60.1% | 54.3% | PASS | PASS | 318.7 | 50.0 | month 3 |
| ⚠ 3.00% | 97.47 | 43.6% | 38.5% | PASS | BORDERLINE | 261.7 | 50.0 | month 4 |
| ⚠ 4.00% | 107.47 | 30.3% | 25.6% | PASS | BORDERLINE | 204.7 | 50.0 | month 6 |
| ⚠ 4.80% | 115.47 | 21.2% | 16.9% | BORDERLINE | FAIL | 159.1 | 50.0 | month 10 |
| ⚠ 5.00% | 117.47 | 19.2% | 14.9% | BORDERLINE | FAIL | 147.7 | 50.0 | month 12 |
| ⚠ 6.00% | 127.47 | 9.8% | 5.9% | FAIL | FAIL | 90.7 | 50.0 | month 13 |
| ⚠ 7.65% | 143.97 | -2.8% | -6.2% | FAIL | FAIL | -3.4 | 55.8 | month 15 |

**Reading.** The 25% gate at the set price falls between 4.0% and 4.8% — at 4.45% (the C10 record's 4.45%). The C3 trial band's continue line (⚠ 4.8%) is already past the gate at the set price: at 4.8% the design is BORDERLINE (the record's C3 line was set on the C3 floor; the floor has since risen by the R4–R10 additions). The kill line (⚠ 5.0%) reads BORDERLINE at 140 and FAIL at 135. Zero margin at 7.25%; at 7.65% (a figure carried from the C3 record's zero-margin reading on the C3 floor) the design loses money on every £1,000. The year-five contribution stays positive to 6% because the fixed layer is small against the book; the margin gate fails long before the cash does — which is the point of the gate.

## 4 · The Phase II capital gate — Function 3 close

| Reading | Value |
|---|---|
| conservative scenario margin at the set price | **30.3%** |
| band across the price (135 → 142.5) | 25.6% → 32.6% |
| the line | 60% (25–59% BORDERLINE; below 25% FAIL) |
| **verdict** | **BORDERLINE** |
| worst-corner margin to the line | -29.7 points |
| binding input | the loss rate on the flow-underwritten pool (⚠ 2–4%, unmeasured; C1) |
| loss rate at which the conservative scenario reaches 60% at 140 | ⚠ 2.00% (floor high 87.50) |
| the same at 135 | ⚠ 1.69% |
| the funding line at 1.5% with the loss at 4.0% | 51.4% — does not reach 60% alone |
| funding at 1.5% and the loss at | ⚠ 3.50% — reaches 60% |
| central scenario | 72.2% — PASS |
| optimistic scenario | 154.1% — PASS |

**What tightens the reading.** One measurement: the Stage 1 twelve-month loss on the migrated pool under the receipts share (the C3 trial band; on ≥ ⚠ 10,000 accounts). If it reads at or below ⚠ 2.0% the conservative scenario passes the 60% line as the book stands; between 2.0% and 4.0% the gate stays BORDERLINE and the design stays inside the 25% requirement gate; above 4.45% the requirement gate itself fails at the set price. The second input, the funding line, cannot close the gap alone: at its low corner (1.5%) with the loss at 4.0% the margin is 51.4%. No design change inside R1–R10 moves the reading — the ten moves have already removed the conventional lines (⚠ 6–18 across F2 and F3) and the ⚠ £8 cap line stands at ⚠ 1.10–1.47 used. **The gate is BORDERLINE on an unmeasured input, not on a design defect**: the design's conservative corner assumes a loss rate at the top of a band that the bank's own records will replace at Stage 0's back-test before any capital is committed.

## 5 · Per-segment penetration (TAM data object, version 4)

**The bank's own volume (⚠, the AOM's proxy):** own base 950,000 business current accounts; 760,000 with six months of flow carry a limit (80%); 228,000 drawn at any time (30%). **The market proxy** (surviving volume, the standard-tariff overdraft users across UK banks): low 250,800–387,600; central 344,850–532,950; high 438,900–678,300. The classes overlap and are not added.

| Sub-class | Addressable | Accounts at the bank ⚠ (public incidence × own base) | Limit carried at scale | Drawn reading |
|---|---|---|---|---|
| SC-OD-STD-TARIFF — current overdraft user on the standard tariff, paying 15–30% EAR all-in, with observable flow | addressable | 41,800–113,050 | 100% at Stage 1 (migrated; the tariff overdraft retired into the limit) | ⚠ 100% of the migrated drawn balance, £0.4–1.9bn |
| SC-OD-BELOW-BAND — current overdraft user on negotiated or secured pricing below 15% EAR | not | 31,350–96,900 | the limit is offered beside the negotiated overdraft (excluded by G-C6-1 as the selected customer; the account still carries a limit) | ⚠ 0–30% — draws only where the limit is cheaper than the negotiated price on the day |
| SC-LOAN-USER — SME with a bank term loan and observable flow | not | 28,500–85,500 | the limit sits beside the loan for new draws | ⚠ unmeasured — the loan continues to its schedule |
| SC-OWNER-FUNDED — SME that had to inject personal money and has observable flow | partly | 167,200–167,200 | carried where the flow gate is met (80%) | ⚠ unmeasured — the C1 offer reaches it; no KMC priced |
| SC-DETERRED — would-be seeker with observable flow who did not apply | partly | 38,000–38,000 | carried where the flow gate is met (80%) | ⚠ unmeasured — foregone return unpriced |
| SC-NO-FLOW-HISTORY — new-to-trading SME with no account-flow history anywhere | not | 190,000–190,000 | none — excluded by G-C1-1 (no flow) | nil |

**Reading.** The selected customer (SC-OD-STD-TARIFF) is fully penetrated at Stage 1 by construction — the tariff overdraft is retired into the limit at migration (C2, WP-4), so penetration is the migration acceptance (⚠ 90%, e.migration_decline at 10%) and not a sales result. Every other class with flow carries a limit at scale and draws on it at a rate the design does not price: the drawn book ⚠ £3.4–5.7bn is 228,000 drawn accounts × ⚠ £15–25k, of which the migrated tariff accounts are ⚠ £0.4–1.9bn; the balance is drawn by accounts that today hold a negotiated overdraft, a loan, personal money or nothing. That share of the book (⚠ 67–88%) is the design's largest unmeasured volume input after the loss rate, and Stage 0's shadow run reads it before release.

## 6 · Reproduction of the C10 figures

| C10 figure | The simulation | Reproduced |
|---|---|---|
| floor 55.09–107.47 | 55.09–107.47 | yes |
| margin at the set price, worst corner 30.3% | 30.3% | yes |
| margin at 135 / 142.5: 25.6% / 32.6% | 25.6% / 32.6% | yes |
| best corner 154.1% | 154.1% | yes |
| operating bar 134.34; room 5.66 | 134.34; 5.66 | yes |
| central floor 81.28; margin 72.2% | 81.28; 72.2% | yes |
| loss gate 4.45% at 140 (4.05 / 4.65 at the band's ends); zero margin 7.25% | 4.45% (4.05 / 4.65); 7.25% | yes |
| funding gate 3.45% at 140 (corrected from 3.99%) | 3.45% | yes |
| IC unrounded 12.85–18.36 | 12.85–18.36 | yes |
| Phase II: 60% at loss ⚠ 2.0% (floor high 87.47) | loss 2.00% | yes |
| cap binds at the worst corner: ⚠ £5.0bn against £5.7bn, 12% cut | £5.0bn against £5.7bn, 12% cut | yes |
| cap line cumulative ⚠ 1.10–1.47; remaining 6.53 | 1.1–1.47; 6.53 | yes |

## 7 · The inputs register

| Input | Band | Tier | Source |
|---|---|---|---|
| book_gbp | 3,400,000,000.0 – 5,700,000,000.0 | T4 ⚠ | AOM v10 §0 q.drawn_book_gbp — 228,000 drawn accounts × ⚠ £15–25k |
| funding_pct | 1.5 – 3.0 | T4 ⚠ | AOM v10 §6 PVC-funding — the measured deposit cost under the funding term (C10) |
| loss_pct | 2.0 – 4.0 | T4 ⚠ | AOM v10 §6 PVC-loss — the flow-underwritten pool; the binding input |
| computing_per_1000 | 2.02 – 5.12 | T4 ⚠ | AOM v10 §6 PVC-computing |
| exceptions_per_1000 | 3.0 – 8.13 | T4 ⚠ | AOM v10 §6 PVC-exceptions and write-off |
| rc_people_gbp | 7,600,000.0 – 13,550,000.0 | T4 ⚠ | AOM v10 §3c all-people cost of the HQ layer (before the route) |
| route_upkeep_gbp | 300,000.0 – 600,000.0 | T2/T4 ⚠ | AOM v10 §3c the standby route's upkeep without issuance (C10) |
| undrawn_per_drawn | 1.9 – 3.6 | T4 ⚠ | AOM v10 §0 q.undrawn_per_drawn (C8) |
| risk_weight | 0.75 – 0.75 | T1 | regulatory retail SME, standardised — FACT |
| total_capital | 0.12 – 0.12 | T4 ⚠ | ⚠ 12% total capital ratio — AOM v10 §6 IC |
| ccf_undrawn | 0.1 – 0.1 | T1 | Basel 3.1, PRA PS9/24, from 1 January 2027 — FACT |
| cost_of_equity | 0.12 – 0.15 | T4 ⚠ | AOM v10 §6 IC — ⚠ 12–15% |
| pool_credit_balances | 50,000,000,000.0 – 100,000,000,000.0 | T2/T4 ⚠ | AOM v10 §0 q.pool_credit_balances (C10) |
| cap_share | 0.1 – 0.1 | runner's call ⚠ | C10 record, gate G18 — the cap at ⚠ 10% of the pool's credit balances |
| stage1_book_gbp | 400,000,000.0 – 1,900,000,000.0 | T4 ⚠ | C3 record — the migrated overdraft accounts' drawn balance |
| seasoning_months | 8 – 24 | T4 ⚠ | runner's call — months a released tranche takes to reach its at-scale drawn balance (C8: seasoned share ⚠ 30–50% at 24 months); convergence: the first replica's 24-month reading |
| unseasoned_drawn_share | 0.8 – 0.8 | T4 ⚠ | runner's call — a released account's drawn balance at release as a share of its seasoned level (the seasoned uplift ⚠ 15–30% on limits, C8) |
| overlay_stage1_gbp | 0 – 19,000,000.0 | T4 ⚠ | AOM v10 §3e — the overlay on Stage 1, held 12 months |
| overlay_replica_gbp | 0 – 50,000,000.0 | T4 ⚠ | AOM v10 §3e — the overlay on each replica, held 6 months |
| one-off: back-test and its validation (Stage 0) | £0.300m – £0.800m, months -6 to -1 | T4 ⚠ | C3 record; AOM v10 §3e |
| one-off: the outcome ledger build (C9) | £0.100m – £0.300m, months -6 to -1 | T4 ⚠ | AOM v10 §3e e.ledger_build |
| one-off: the seasoning build (C8) | £0.020m – £0.040m, months -3 to -1 | T4 ⚠ | AOM v10 §3e |
| one-off: the credit-line element build and conformance test (C7) | £0.050m – £0.100m, months -3 to -1 | T4 ⚠ | AOM v10 §3e |
| one-off: the term drafting (C5), the representative example (C6), the funding term's signature (C10) | £0.026m – £0.053m, months -2 to -1 | T4 ⚠ | AOM v10 §3e |
| one-off: migration notices and handler time (C2) | £0.300m – £0.850m, months 1 to 1 | T4 ⚠ | C3 record; AOM v10 §3e |
| one-off: stage readings, three (C3) | £0.045m – £0.135m, months 12 to 24 | T4 ⚠ | AOM v10 §3e e.stage_reading — ⚠ £15–45k each at months 12, 18 and 24 |
| one-off: the standby route's set-up (C10) | £1.000m – £3.000m, months 19 to 24 | T4 ⚠ | AOM v10 §3e e.route_setup — before Stage 3 |
| release months | Stage 1 at 1; replica 1 at 13; replica 2 at 19; readings at [12, 18, 24] | C3 record | the trial band at 12 months; the replica band at 6 months |
| PCO | capital £100m ⚠; 30%; required revenue £148.5m at year five | ⚠ ASSUMED | bank-deposits-lending-pco-v1-2026-09-18.md — capital £100m ⚠ ASSUMED; 30%; required-revenue line £148.5m at year five at a 20% margin |

**One-offs, summed:** £1.84–5.28m before the overlays' carrying cost; the AOM v10 3e total of ⚠ £1.84–15.59m includes the overlays' carrying cost at ⚠ 12–15% cost of equity (⚠ £0–10.3m). The simulation holds the overlays as capital (section 2) and does not spend the carrying cost, so the two totals differ by that line and by nothing else.

## 8 · What is not in this simulation

- The HRS, FIS and SCIS scores — read in the C8–C10 records and the verifiers; not arithmetic on the floor.
- The bank's headroom for the lending capital (⚠ £0.36–0.70bn at scale) — an unmeasured input owned by the treasury (C3).
- The seasoning curve — a runner's call (⚠ 80% at release; ⚠ 8–24 months); the first replica's 24-month reading replaces it.
- Tax, transfer pricing between the line and the account line, and the bank's own cost of the deposits it would otherwise hold — outside the venture's unit.
- A rate cycle — the price is 14.0% simple and the funding is the measured deposit cost; the C10 record reads the at-scale price across a rate cycle and the daily funding term carries it.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.1 | 22 September 2026 | Section 1 prose corrected: it said the conservative £m column paired the high cost lines with the small book; the table pairs them with the large book (revenue 798 = £5.7bn × 140). The small-book pairing is now printed beside it (£110.6m before capital, £49.4m after). No number in any table changed. |
| v1 | 21 September 2026 | Created at the Function 3 close by the runner. At-scale P&L per £1,000 and for the book at three corners; monthly path Stage 0 → Stage 1 → replica 1 → replica 2 → at scale with peak venture capital; loss-rate sensitivity at seven values; Phase II gate BORDERLINE at the conservative scenario (30.3% against 60%; loss ⚠ 2.0% closes it); per-segment penetration from TAM v4; twelve C10 figures reproduced. |
