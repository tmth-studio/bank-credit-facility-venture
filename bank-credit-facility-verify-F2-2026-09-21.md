# A business bank's credit facility line — design-integrity verification at the F2 gate · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Source records:** C4 v1, C5 v1, C6 v1, C7 v1 (all 21 Sep 2026), read against PCO v1 and C1–C3; CTM v7, AOM v7, fit model at C7, verifier r7, TAM model version 3 (at C7), verdict record R1–R7, consistency audit F2 — all 21 Sep 2026. **Verifier:** the runner, as an independent pass on the record, one reader. **Scored:** the F2 span (R4–R7) on the four passes; the F1 span is not re-scored, and its condition is carried.

**Path C, mode 3.** The C7 set is object-after to 23 September 2026 17:00. The three checking scripts ran after the seal of 21 September 2026 19:49 (the principal's, not the runner's); their outputs are in the verifier r7 and are read here, not re-run.

## Verdict

**SOUND (verification) · validation-maturity: pre-operational.** The four requirements are solved to the method's standard, the record contradicts itself nowhere, the form factor changed at every challenge, and one real business shares the mechanism up to R6 and is named as stopping there. The score is held below 100 by one carried build item (the model files, a partial on every SR5 row), three soft items from the consistency audit, and two details fixed ahead of the evidence that would settle them.

| Sub-score | Score | Derivation |
|---|---|---|
| Completeness | 90.0 | 16 complete + 0.5 × 4 partial, over 20 sub-requirements |
| Consistency | 85 | 100 − 15 × 0 hard − 5 × 3 soft |
| Discipline | 97.4 | (36 earned + 0.5 × 2 premature) over 38 specified details; 0 unjustified; no justification mode, so no cap |
| Synthesis | 100 | a named analogue with its stopping point, and four of four VA-106 lines name earlier requirements with the mechanism |
| **Overall** | **93.1** | the four at 25 per cent each; no cap applies |

**Registry coverage (the count).** By this count the registry has 77 rows in its six phase tables plus the four TPM-standard rows: 81. (The F1 verify counted 82; the one-row difference is a counting difference, named here and not resolved.) **59 were applied. 17 were not applicable**, each with a reason in section 6. **5 could not be applied because the record lacks the element they test** — the five Phase 1 rows, as at F1.

## Four-pass scorecard

| Pass | Status | Finding |
|---|---|---|
| Completeness | 🟢 | 4 of 4 requirements complete on their worst sub-requirement, at Partial: each SR5 row (the model files are a carried build item) |
| Consistency | 🟢 | 0 hard, 3 soft — see the consistency audit F2 |
| Discipline | 🟢 | 2 premature, 0 unjustified; no justification mode — the form factor changed at C4, C5, C6 and C7, and every mutation gate rejected the alternatives by name |
| Synthesis | 🟢 | Square Loans carried and re-read at each requirement; the analogue's stopping point (R7) named; VA-106 counts 6, 5, 6, 7 |

## Validation-maturity readout — reported beside the score, never inside it

| Parameter | Evidence method | Tag | Convergence event |
|---|---|---|---|
| loss rate on the flow-underwritten pool (⚠ 2–4 per cent; gate 4.57 at the set price; pivot 5.0) | test | emergent | 12-month loss on ≥ 10,000 Stage 1 accounts (trial band) — carried from F1 |
| surplus fraction (⚠ 0.90–1.00) | analysis | elicitable | the first cell year's waiver count (C4) |
| handler productive hours (⚠ 1,400–1,600 a year) | examination | elicitable | the bank's own contact-centre figure (C4) |
| switch-off share (⚠ ≤ 10 per cent) | test | emergent | the first replica's six months (C5) |
| funding-query rate (first-year peak) | test | emergent | the first replica's six months (C5) |
| charge-query rate | test | emergent | the first replica's six months (C6) |
| price band (⚠ 135–142.5; set 140) | analysis | elicitable | the pricing committee's reading of the band against the C2 KMC (C6) |
| connected share of released accounts (⚠ 45–70 per cent) | examination | elicitable | the bank's account-information consent count at Stage 1 (C7) |
| platforms displaying the line (hypothesis: ≥ 2 of 3 largest) | test | emergent | the first replica's six months (C7, G15) |
| display-query rate (⚠ 0.1–0.3 per cent; threshold 1 per cent) | test | emergent | the first replica's six months (C7) |
| conformance-test hours (⚠ 100–200) and field build (⚠ 400–800) | examination | elicitable | the account-information team's estimate before the build (C7) |

**Overall maturity: pre-operational.** No operational evidence exists and none could at F2. Every emergent parameter names a test event; every elicitable one names who holds the figure. That is the correct state at this gate and reduces no sub-score.

## Pass 1 — Completeness

Criteria from `verify-balm-custom`; the at-scale check applied; the FIT-staleness check (VA-74) run per requirement.

| Requirement · SR | Status | Note |
|---|---|---|
| R4 SR1 — the want, the beliefs | complete | three beliefs; the key efficacy doubt named as a credibility gap |
| R4 SR2 — the block | complete | one block: a bank's number is not money until a person has decided |
| R4 SR3 — theory of change | complete | Milgrom 1981; Hoch and Deighton 1989; context, outcome, substitution test |
| R4 SR4 — strategy and hypothesis | complete | CP-2, the limit as its own verifiable history at the shortfall; mutation gate A of six; falsification stated |
| R4 SR5 — CTM, AOM, FIT | partial | v4 documents written; model files a build item; fit model at C4 by hand 27.1 per cent, script confirms after the seal |
| R5 SR1 — the use routine | complete | eight steps; the cue with no act |
| R5 SR2 — the block | complete | routine disruption at steps 3 and 5, created by the C1 form itself |
| R5 SR3 — theory of change | complete | Madrian and Shea 2001; Wood and Neal 2007; contrast and robustness named |
| R5 SR4 — strategy and hypothesis | complete | default funding on an accepted term; draw ahead; switch-off; mutation gate A of six |
| R5 SR5 — CTM, AOM, FIT | partial | v5 documents; model files a build item; 27.0 per cent at the worst corner |
| R6 SR1 — interim value and the CVT | complete | two lifecycles; a Critical Value Threshold per party |
| R6 SR2 — the block | complete | timing mismatch (the calendar debit; the fee as a lump); price sensitivity rejected as the type |
| R6 SR3 — theory of change | complete | Prelec and Loewenstein 1998; Gourville and Soman 1998; Thaler 1985; Soman 2001 |
| R6 SR4 — strategy and hypothesis | complete | the charge as the first slice of the receipts share; 14.0 per cent simple a year; band; three fixed points; mutation gate A of five |
| R6 SR5 — CTM, AOM, FIT | partial | v6 documents; model files a build item; 31.7 per cent at the set price |
| R7 SR1 — the access routine | complete | two routines (connected, unconnected); connected share as a band |
| R7 SR2 — the enumeration | complete | affordability screen before any candidate; existence test on the class; eight candidates by loss and gain side; presence third case; aggregate form; hours per close as the conformance test |
| R7 SR3 — the coordination problem and theory | complete | Farrell and Saloner 1985; Christensen and Raynor 2003 as contrast; Sharp 2010 on the customer side |
| R7 SR4 — strategy and hypothesis | complete | PP-1, the published pre-agreed line by the public standard; mutation gate A of five; hypothesis (a)(b)(c) with falsification; five assumptions tagged |
| R7 SR5 — CTM, AOM, FIT | partial | v7 documents; model files a build item; script PASS at 31.7 per cent |

**FIT staleness (VA-74).** The fit model at C7 lists the component set the CTM v7 carries, PP-1 included; the floor it reads (54.04–106.28) is the AOM v7 floor. Not stale. The fit models at C4, C5 and C6 each matched their own CTM and AOM at the time, and each was superseded by the next, in order (verdict record: IN ORDER).

**At-scale check.** The margin is read at the at-scale count. Stage 1 on its own reads 1.0 per cent at the worst corner (VA-162: 4.8 / 1.0 / 6.6), below the gate, as at F1. The F1 condition on the at-scale count is carried unchanged. The loss gate now sits at 4.57 at the set price.

## Pass 2 — Consistency

Read from the consistency audit F2: 0 hard, 3 soft (S1 the published line on a switched-off account; S2 the C5 headroom reused as a recurring line; S3 two presentations of "available"). Score 85. Each has a fix, an owner and a convergence event in the audit.

## Pass 3 — Discipline

### 3a — Premature-design audit (VA-2)

Thirty-eight specified details across the four records. Thirty-six are earned: each is needed for the form to work as designed, or is a band with a tag and a convergence event. The two below are fixed ahead of the evidence that would settle them.

| Detail | Where | Class | Why |
|---|---|---|---|
| the conformance-test scope of six counterparties (three aggregators, three platforms) | C7 record SR2; CTM v7 partner track; AOM v7 `e.conformance_test` | premature | the count is a design choice made before the existence test's first-replica result says which readers matter; the cost line (⚠ 100–200 hours) is a band, so the defect is the scope, not the figure |
| the credit line served with `Included = false` | C7 record SR4 (runner's call) | premature | the right value depends on how the platforms render a separate line against a merged figure, which is read at the first replica; the audit's S3 is the tension it created |

Neither detail is unjustified: each carries its reasoning and its owner. Both convert to convergence items at the next regeneration.

### 3b — Justification-mode tell (VA-3)

Not present. The form changed at each of the four challenges (CP-2; WP-2 amended; WP-3 amended and PC-1 resolved; PP-1). Each mutation gate rejected four or five alternatives by name and by test. The C6 record set a price below the C2 ceiling rather than at it; the C7 record chose the form that adds no partner fee over the form that names a platform. No detail was added to make an earlier choice look right.

## Pass 4 — Synthesis

Square Loans named at C3, carried and re-read at C4, C5 and C6 with the shared mechanism stated each time, and named at C7 as the point where the analogue stops. Four of four VA-106 lines name earlier requirements with the mechanism (counts 6, 5, 6, 7 — the audit's section 7). Score 100.

## 6 · Registry coverage — the rows

**Applied, 59.** TPM standard: all four (two premature details found, section 3a). Phase 2, 43 rows, listed as the registry orders them. The generation rows: diagnosis, ToC class, theory, context (one scorer — a limit of the check, recorded), outcome, design choice, hypothesis. The model rows: CTM update (on the document), AOM ops map, volume drivers (every driver resolves to section 0, RD-031), no ratios, role support, LMU sizing. The verification rows: the margin of safety (PASS at every corner at every requirement; 31.7 per cent at the set price), FIT I check, FIT T check, VA-106 synergy, loop gate, the three-check close (VA-89, VA-91), VA-97, VA-100, VA-99 (every enabler carries the business-case fields), VA-101 (two structural-limit decisions: the accountant row and the pricing-committee row at the pessimistic corner), VA-95, VA-103 (six rows at C7), VA-127, VA-147 (eight candidates, two classes), VA-162, VA-164 (R4, and re-run at R7), VA-153, VA-156 (R7: partner return nil), VA-155 (R7: count line with G15), VA-92 (R7), VA-84, VA-85. The carried-forward rows: VA-83 (TAM re-versioned at C7; validated), excluded population (R2, re-sized at C7 by the price gate), capital bar, VA-82, VA-90, VA-80, VA-81, conventional cost line named and removed (R4, R5, R6, R7). Phase 3: all four. Phase 4: eight of nine.

**Not applicable, 17.** Phase 0: all eight (closed at F1; nothing in F2 re-opens the frame). Phase 1: CLO statement (closed at F1 on C1 SR2). Phase 2: VA-149 (R1), VA-163 (R3), position-holding assumption (F3), mode 2 verdict form (C1). Counterfactual costed (F1 gate) — exists; read as the source of the cap line, not re-applied. Phase 4: F3 barrier scores (F3 not designed). Phase 5: PCO confirmation and expert sign-off (human).

**Could not apply because the record lacks the element, 5.** The five Phase 1 rows (structural class, cross-domain analogues, filtered candidates, candidate score, workaround seed): Path C entered from the levelled line into C1 without a Phase 1 pass, as at F1.

**Scored on rules the run was never told.** None new at F2. The TPM rows, applied at F1 on rules the challenge skills do not state, were applied again; the F2 records wrote bands with tags throughout, so nothing was docked on them this time.

## 7 · The faults found, ranked

| Fault | Item | Pass | Fix | Owner |
|---|---|---|---|---|
| F-1 · the model files do not exist | CTM and AOM model files, carried from C1; a partial on every SR5 row | 1 | build the files from the v7 documents; re-run the three scripts on them | the Venture Architect seat |
| F-2 · the C5 headroom is now a recurring line | audit S2 | 2 | split the headroom into a first-year line and a recurring line, each with its driver | the runner, AOM v8 |
| F-3 · the published line on a switched-off account has no written position | audit S1 | 2 | one line in the C7 record naming the position and the reading | the runner, next regeneration |
| F-4 · two presentations of "available" | audit S3 | 2 | a one-line reconciliation in the C7 record; the conduct desk owns the app wording | the runner; the conduct desk position |
| F-5 · the conformance-test scope is fixed ahead of the evidence | six counterparties | 3a | recast as a convergence item: the scope is set at the first replica from the existence test's reading | the runner, next regeneration |
| F-6 · `Included = false` is fixed ahead of the evidence | the runner's call at C7 SR4 | 3a | recast as a convergence item with the platform rendering as the reading | the runner, next regeneration |
| F-7 · the fit script's best corner is an artefact | 417.9 per cent reported; 159.1 by hand at the set price | verifier r7 | the script should read the best corner at the set price once one exists | Head of R&D (WS1) |

## 8 · The three things that most raise the score

1. Build the model files — closes F-1 and lifts Completeness to 100 (overall +2.5).
2. Write the S1 and S3 lines and split the headroom — closes F-2, F-3 and F-4 and lifts Consistency to 100 (overall +3.75).
3. Recast the two premature details as convergence items — closes F-5 and F-6 and lifts Discipline to 100 (overall +0.7).

All three together put the score at 100 on the F2 span; none needs Tom.

## Recommended next session

Nothing in this list needs Tom. F-2 to F-6 are one regeneration of the C7 record and the AOM. F-1 is the Venture Architect seat's build. F-7 is a method question for WS1. C8 can open on the record as it stands, with the F1 condition (the at-scale count) and the F2 condition (the 7.15 of room at the central corner, 0 at the pessimistic corner) carried as critical assumptions.

## What I did not do

I did not re-derive any band or re-run any design step. I did not re-run the checking scripts; I read their outputs from the verifier r7. I did not re-score the F1 span. I did not score F3 rows. I scored with one reader where the registry's rubric rows want two. I did not run the seal, name the bank or write any internal count.
