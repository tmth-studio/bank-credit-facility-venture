# A business bank's credit facility line — design-integrity verification at the F3 gate (C10) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Source records:** C8 v1, C9 v1, C10 v1 with its same-day correction (all 21 Sep 2026), read against PCO v1 and C1–C7; CTM v10, AOM v10, fit model at C10, verifier r10, TAM data object version 4, verdict record R1–R10, financial simulation at C10, consistency audit C10 — all 21 Sep 2026. **Verifier:** the runner, as an independent pass on the record, one reader. **Scored:** the F3 span (R8–R10) on the four passes; the F1 and F2 spans are not re-scored and their conditions are carried; the whole-architecture reading is the consistency audit's and is read here, not re-done.

**Path C, mode 3.** The C10 set is object-after to 23 September 2026 17:00. The four checking scripts ran after the seal of 21 September 2026 19:49 (the principal's, not the runner's); their outputs are in the verifier r10 and are read here, not re-run.

## Verdict

**SOUND (verification) · validation-maturity: pre-operational.** The three requirements are solved to the method's standard, the form factor changed at every challenge, and one real business shares the mechanism across all ten moves and is named where it stops. The score is held below the F2 score by one hard contradiction of number (an earlier record's trial band made false by the accumulated floor, routed back and not patched), four soft items, one carried build item and three details fixed ahead of the evidence that would settle them. The architecture's margin rests on two unmeasured inputs; that is reported as maturity, not as integrity.

| Sub-score | Score | Derivation |
|---|---|---|
| Completeness | 90.0 | 12 complete + 0.5 × 3 partial, over 15 sub-requirements |
| Consistency | 65 | 100 − 15 × 1 hard − 5 × 4 soft |
| Discipline | 95.8 | (33 earned + 0.5 × 3 premature) over 36 specified details; 0 unjustified; no justification mode, so no cap |
| Synthesis | 100 | a named analogue for the whole architecture with its stopping point, and three of three VA-106 lines name earlier requirements with the mechanism |
| **Overall** | **87.7** | the four at 25 per cent each; no cap applies |

**Registry coverage (the count).** 81 rows by the F2 count (the F1 verify counted 82; the one-row difference is a counting difference, named and not resolved). **61 were applied. 15 were not applicable**, each with a reason in section 6. **5 could not be applied because the record lacks the element they test** — the five Phase 1 rows, as at F1 and F2.

## Four-pass scorecard

| Pass | Status | Finding |
|---|---|---|
| Completeness | 🟢 | 3 of 3 requirements complete on their worst sub-requirement, at Partial: each SR5 row (the model files are a carried build item) |
| Consistency | 🟡 | 1 hard (of number — the C3 trial band's continue line against the C10 floor), 4 soft — see the consistency audit C10 |
| Discipline | 🟢 | 3 premature, 0 unjustified; no justification mode — the form changed at C8, C9 and C10, and every mutation gate rejected the alternatives by name |
| Synthesis | 🟢 | Square Financial Services and Square Loans read against all ten moves; the stopping point (the cap and the standby route) named; VA-106 counts 5, 4, 5 |

## Validation-maturity readout — reported beside the score, never inside it

| Parameter | Evidence method | Tag | Convergence event |
|---|---|---|---|
| loss rate on the flow-underwritten pool (⚠ 2–4 per cent; gate 4.45 at the set price; pivot 5.0) | test | emergent | Stage 0 back-test on the bank's own history, then the 12-month loss on ≥ 10,000 Stage 1 accounts — carried from F1 and F2 |
| measured deposit cost under the funding term (⚠ 1.5–3.0 per cent; gate 3.45) | examination | elicitable | treasury's transfer-pricing reading at the term's signing; then the first year of daily readings (C10) |
| pool credit balances (⚠ £50–100bn) and cap use (⚠ 3.4–11.4 per cent) | examination | elicitable | the bank's own balance sheet at the term's signing (C10) |
| seasoning schedule (months to each step, ⚠ 8–24 in the simulation) and the cleared-event cut (⚠ 90 days) | test | emergent | Stage 0 back-test on the bank's own history; the first cohort year at Stage 1 (C8) |
| seasoning-query rate (⚠ 0.5–1.5 per cent of drawn accounts a year) | test | emergent | the first replica's six months (C8) |
| undrawn commitment per £1 drawn (⚠ 1.9–3.6; IC 13–18) | test | emergent | the twelve-month Stage 1 reading (C8, re-read at C10) |
| replication lag (⚠ 27–54 months) | analysis | elicitable | no event moves it; re-read if a rival publishes a comparable outcome ledger (C9) |
| calibration cohort minimum (⚠ 500 outcome rows a cell) and the held-out cohort | test | emergent | the first yearly run on the Stage 0 history (C9) |
| calibration compute (⚠ £5–30k a run) | examination | elicitable | the bank's data-platform quote before the first run (C9) |
| standby route set-up (⚠ £1.84–15.59m one-off) and upkeep (⚠ £0.3–0.6m a year) | examination | elicitable | the agents' fee quotes before Stage 3 (C10) |
| price band (⚠ 135–142.5; set 140) | analysis | elicitable | the pricing committee's reading — carried from F2 |

**Overall maturity: pre-operational.** No operational evidence exists and none could at F3. Every emergent parameter names a test event; every elicitable one names who holds the figure. That is the correct state at this gate and reduces no sub-score. Two of the eleven — the loss rate and the deposit cost — carry the whole margin between them; the consistency audit's condition says so.

## Pass 1 — Completeness

Criteria from `verify-balm-custom`; the at-scale check applied; the FIT-staleness check (VA-74) run per requirement.

| Requirement · SR | Status | Note |
|---|---|---|
| R8 SR1 — the store of value | complete | the cleared event and the seasoned multiple; the customer-ownership test; what does not move with the customer named |
| R8 SR2 — the block | complete | the C7 openness itself: a published limit is a reconstructible one |
| R8 SR3 — theory of change | complete | Sharpe 1990 on the incumbent's learned information; Rajan 1992 as contrast; the Open Banking premise stated |
| R8 SR4 — strategy and hypothesis | complete | WP-1 v2, the seasoned limit; mutation gate; SCIS 2 · 4 · 6 printed unsoftened; falsification stated |
| R8 SR5 — CTM, AOM, FIT | partial | v8 documents; model files a build item; 30.4 per cent at the worst corner |
| R9 SR1 — the outcome ledger | complete | the outcome column; replication lag as a band; what the feed does not carry |
| R9 SR2 — the block | complete | the rule's parameters are the same for a rival who copies the rule |
| R9 SR3 — theory of change | complete | Dierickx and Cool 1989 on asset stocks and time compression; Arrow 1962 on learning by doing; Barney 1991 as contrast |
| R9 SR4 — strategy and hypothesis | complete | yearly re-fit on the ledger; parameter not rule; held-out cohort; G17; FIS 5 · 6 · 7; falsification stated |
| R9 SR5 — CTM, AOM, FIT | partial | v9 documents; model files a build item; 30.4 per cent at the worst corner |
| R10 SR1 — the key input | complete | funding as the largest floor line; the pool and its balances; the position-holding table re-tested at every failure value |
| R10 SR2 — supplier-power theory | complete | Klein, Crawford and Alchian 1978; Drechsler, Savov and Schnabl 2017; Williamson 1985 and Diamond and Dybvig 1983 as contrasts |
| R10 SR3 — strategy and hypothesis | complete | PC-2, the levelled-line funding with the cap and the standby route; mutation gate A of six; HRS 4 → 5 with the commitment, 6, 6; the at-scale test; falsification stated |
| R10 SR4 — productised in the architecture | complete | the treasury track's six states; the tape as the ledger's second use; nothing the customer sees |
| R10 SR5 — CTM, AOM, FIT | partial | v10 documents; model files a build item; script PASS at 30.2 per cent at the ceiling read, 30.3 by hand at the set price |

**FIT staleness (VA-74).** The fit model at C10 lists the component set the CTM v10 carries, PC-2 included; the floor it reads (55.09–107.47) is the AOM v10 floor. Not stale. The fit models at C8 and C9 each matched their own CTM and AOM at the time and each was superseded in order (verdict record: IN ORDER, ten checks).

**At-scale check.** The margin is read at the at-scale count. Stage 1 on its own reads 4.0 per cent at the worst corner in the record (VA-162: 4.0 / 0.3 / 5.8) and −1.2 per cent in the simulation with the seasoning call — both below the gate, as at F1 and F2; the F1 condition on the at-scale count is carried, and the simulation now dates it (month 43 at the conservative corner). The loss gate sits at 4.45 at the set price; the funding gate at 3.45.

## Pass 2 — Consistency

Read from the consistency audit C10: 1 hard (H1 — the C3 trial band's continue line, ⚠ 4.8 per cent, stated as the point where the 25 per cent margin holds; at the C10 floor the margin at 4.8 is 21.2 per cent; routed back to the C3 record for re-setting, not patched), 4 soft (S1 the funding gate absent from the quarterly sitting; S2 the recurring fixed layer carried above the activities by ⚠ 1.06 per £1,000; S3 the R7–R8 tension resolved at R9; S4 two Stage 1 figures). Score 65. Each has a fix, an owner and a convergence event in the audit. The hard item is of number, not structure: no release step, overlay or reading changes when the band is re-set.

## Pass 3 — Discipline

### 3a — Premature-design audit (VA-2)

Thirty-six specified details across the three records (C8 11, C9 10, C10 15). Thirty-three are earned: each is needed for the form to work as designed, or is a band with a tag and a convergence event. The three below are fixed ahead of the evidence that would settle them.

| Detail | Where | Class | Why |
|---|---|---|---|
| the cleared-event cut at ⚠ 90 days without receipts | C8 record §0 and WP-1 v2 (down-seasoning) | premature | a single value where Stage 0's back-test on the bank's own history would give the distribution of clearance times; the runner's reason (a stalled draw must not season) earns a cut, not this cut |
| the calibration run yearly | C9 record SR4 | premature | the frequency is fixed before the first held-out reading says how fast the parameters drift; quarterly-to-yearly is the band the evidence would narrow |
| the standby route set up before Stage 3 | C10 record SR3, design commitment ii | premature | the timing is fixed before the funding term's first year says whether treasury will ever want to issue; the cost lines are bands, so the defect is the date, not the figures |

None is unjustified: each carries its reasoning and its owner. All three convert to convergence items at the next regeneration.

### 3b — Justification-mode tell (VA-3)

Not present. The form changed at each of the three challenges (WP-1 v2; the ledger and the yearly run; PC-2 with the cap and the standby route). Each mutation gate rejected the alternatives by name and by test — five at C8, five at C9, six at C10 — and the rejected ones included the moves a justification would have reached for: a retention discount (C8), a score sold to the customer (C9), market funding or a locked sweep (C10). The SCIS at C8 was printed at 2 at the conservative corner and carried as a design finding rather than raised. The C10 record's own funding gate was found wrong by the verifier r10 and corrected in the record with a changelog row rather than left. No detail was added to make an earlier choice look right.

## Pass 4 — Synthesis

Square Loans, carried from C3 and named at C7 as stopping at R7, is re-read at C10 as Square Financial Services — Block's own Utah industrial bank, funding the loans beside the sellers' own deposits since 2021 — and the analogue then covers all ten moves. Its stopping point is named: the cap and the standby master trust are not published, and Square sees receipts as an acquirer, not as the account holder. Three of three VA-106 lines name earlier requirements with the mechanism (counts 5, 4, 5 — the audit's section 7), and the moat test across the ten lines passes with the weak barrier (SCIS) named. Score 100.

## 6 · Registry coverage — the rows

**Applied, 61.** TPM standard: all four (three premature details found, section 3a). Phase 2, 45 rows. The generation rows: diagnosis, ToC class, theory, context (one scorer — a limit of the check, recorded), outcome, design choice, hypothesis. The model rows: CTM update (on the document), AOM ops map, volume drivers (every driver resolves to section 0, RD-031 — with the S2 reserve as the one exception, scored under consistency), no ratios, role support, LMU sizing. The verification rows: the margin of safety (PASS at every corner at every requirement; 30.3 per cent at the set price), FIT I check, FIT T check, VA-106 synergy, loop gate, the three-check close (VA-89, VA-91), VA-97, VA-100, VA-99, VA-101, VA-95, VA-103 (nine rows at C10), VA-127, VA-147, VA-162, VA-164 (re-run at R10), VA-153, VA-156, VA-155, VA-92 (R10), VA-84, VA-85, VA-148 (cost-shifting, at each F3 mutation gate), VA-160 (the shared input, R9 and R10). **Newly applicable at F3:** the position-holding assumption (R10 — re-tested at every failure value, BORDERLINE and FAIL printed) and the F3 barrier scores (SCIS, FIS, HRS — each printed at three corners; SCIS below the line at one). The carried-forward rows: VA-83 (TAM re-versioned at C10; validated with three declared warnings), excluded population, capital bar (26.05–43.68, not binding), VA-82, VA-90, VA-80, VA-81, conventional cost line named and removed (R8, R9, R10). Phase 3: all four (the moat test at section 7 of the audit). Phase 4: nine of nine.

**Not applicable, 15.** Phase 0: all eight (closed at F1; nothing in F3 re-opens the frame). Phase 1: CLO statement (closed at F1). Phase 2: VA-149 (R1), VA-163 (R3), mode 2 verdict form (C1). Counterfactual costed (F1 gate) — exists; read as the source of the cap line, not re-applied. Phase 5: PCO confirmation and expert sign-off (human).

**Could not apply because the record lacks the element, 5.** The five Phase 1 rows, as at F1 and F2.

**Scored on rules the run was never told.** One new at F3: the HRS row states thresholds and no terms, so the C10 record scored itself on a decomposition it wrote (asset ownership, alternative availability, replacement time). This verification applied the same decomposition and did not dock the record for the registry's gap; the gap is WS1's (fault F-9).

## 7 · The faults found, ranked

| Fault | Item | Pass | Fix | Owner |
|---|---|---|---|---|
| F-1 · the C3 trial band's continue line sits on the fail side of the gate | audit H1 | 2 | re-set in the C3 record and the CTM release track: continue ≤ ⚠ 4.45 at the set price (4.05 at 135); borderline 4.45–5.0; kill above ⚠ 5.0 unchanged | the runner, C3 record at its next regeneration |
| F-2 · the model files do not exist | CTM and AOM model files, carried from C1; a partial on every SR5 row | 1 | build the files from the v10 documents; re-run the four scripts on them | the Venture Architect seat |
| F-3 · the recurring fixed layer holds ⚠ 1.06 per £1,000 the activities do not derive | audit S2 | 2 | carry the derived line or declare the reserve with its reason | the runner, AOM v11 |
| F-4 · the funding gate is not a quarterly reading | audit S1 | 2 | one reading added to the trigger review's sitting | the runner, CTM v11 |
| F-5 · two Stage 1 figures | audit S4 | 2 | the C10 record carries the AOM v10 people figure | the runner, next regeneration |
| F-6 · the cleared-event cut fixed at ⚠ 90 days | C8 §0 | 3a | recast as a band settled by Stage 0's back-test | the runner, next regeneration |
| F-7 · the calibration frequency fixed at yearly | C9 SR4 | 3a | recast as a band settled by the first held-out reading | the runner, next regeneration |
| F-8 · the standby route's set-up date fixed before Stage 3 | C10 SR3 | 3a | recast as a trigger: set up when the term's first-year readings put the deposit cost within ⚠ 0.5 points of the gate, or before Stage 3, whichever first | the runner, next regeneration |
| F-9 · the HRS has thresholds and no terms in the registry | criteria registry, F3 barrier scores | 6 | add the three terms and their scales, or adopt the record's decomposition | Head of R&D (WS1) |
| F-10 · a gate figure was printed that did not reproduce (3.99, corrected to 3.45) | C10 record v1 as first written; caught by the verifier r10 | process | the challenge skill's checks-run table asks "printed"; it should ask "reproduces from the floor" | Head of R&D (WS1) |

Carried from the F2 verification and not re-scored: F2 F-3 (the published line on a switched-off account), F2 F-4 (two presentations of "available"), F2 F-5 and F-6 (the conformance-test scope and `Included = false`) — open, owners unchanged; F2 F-2 (the C5 headroom as a recurring line) is closed by the 15th handler at C8; F2 F-7 (the fit script's best corner) is repeated at r10 and stays with WS1.

## 8 · The three things that most raise the score

1. Re-set the trial band in the C3 record — closes F-1 and lifts Consistency by 15 (overall +3.75).
2. Write the four soft items' lines (the reserve, the quarterly reading, the Stage 1 figure; S3 needs no change but a sentence in C8) — closes F-3 to F-5 and lifts Consistency to 100 (overall +5).
3. Build the model files — closes F-2 and lifts Completeness to 100 (overall +2.5).

All three together put the score at 99 on the F3 span (the three premature details hold 1 point); none needs Tom.

## Recommended next session

Nothing in this list needs Tom. F-1, F-3 to F-8 are one regeneration each of the C3, C8, C9, C10 records, the CTM and the AOM. F-2 is the Venture Architect seat's build. F-9 and F-10 are method questions for WS1. Function 3 closes PROVISIONAL on the record as it stands, with three conditions carried as critical assumptions into the status file: the F1 condition (the at-scale count, now dated by the simulation), the F2 condition (the room at the set price, 5.66 at the worst corner) and the F3 condition (two unmeasured inputs carry the margin; the Phase II gate reads BORDERLINE at the conservative scenario until the loss band moves). The next event that moves any verdict is a measurement: Stage 0's back-test.

## What I did not do

I did not re-derive any band or re-run any design step. I did not re-run the checking scripts; I read their outputs from the verifier r10. I did not re-score the F1 or F2 spans. I did not re-do the whole-architecture reading; I read it from the consistency audit C10. I scored with one reader where the registry's rubric rows want two. I did not run the seal, name the bank or write any internal count.
