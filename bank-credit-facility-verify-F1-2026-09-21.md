# A business bank's credit facility line — design-integrity verification at the F1 gate · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Source records:** PCO v1 (18 Sep), C1 v2 (18 Sep), C2 v1 (21 Sep), C3 v1 (21 Sep); CTM v3, AOM v3, fit model at C3, verifier r3, consistency audit F1, counterfactual — all 21 Sep 2026. **Verifier:** the runner, as an independent pass on the record. **Loaded before scoring:** `va-design-discipline.md` and the criteria registry (82 rows). `va-design-evidence.md` was not read. **Format:** the challenge skill names this file; the skill's HTML form is deferred to the function-gate regeneration.

## Verdict

**SOUND (verification) · validation-maturity: pre-operational.** The three requirements are solved to the method's standard, the record contradicts itself nowhere, the form factor changed at every challenge, and one real business shares the mechanism. The score is held below 100 by two build items (model files; the checking scripts' run) and two figures stated as bare points where the method wants bands.

| Sub-score | Score | Derivation |
|---|---|---|
| Completeness | 92.9 | 12 complete + 0.5 × 2 partial, over 14 sub-requirements |
| Consistency | 90 | 100 − 15 × 0 hard − 5 × 2 soft |
| Discipline | 90.6 | (28 earned + 0.5 × 2 premature) over 32 specified details; no justification mode, so no cap |
| Synthesis | 100 | a named analogue, and three of three VA-106 lines name another requirement |
| **Overall** | **93.4** | the four at 25 per cent each; no cap applies |

**Registry coverage (the count).** The registry has 82 rows. **62 were applied. 15 were not applicable**, each with a reason in section 6. **5 could not be applied because the record lacks the element they test** — the five Phase 1 rows (structural class, cross-domain analogues, filtered candidates, candidate score, workaround seed): the run entered Path C from the PCO's levelled line into C1 directly, and no architecture-generator artefact exists. The CLO statement row was applied on C1 SR2.

## Four-pass scorecard

| Pass | Status | Finding |
|---|---|---|
| Completeness | 🟢 | 3 of 3 requirements complete on their worst sub-requirement, at Partial: R1 SR5 (model files a build item), R2 SR3 (the TAM file exists; its validation run is refused by the toolchain) |
| Consistency | 🟢 | 0 hard, 2 soft — see the consistency audit F1 |
| Discipline | 🟢 | 2 premature, 2 unjustified (both TPM-standard defects: a bare point on a load-bearing figure); no justification mode — the form factor changed at C2 and C3 |
| Synthesis | 🟢 | cohered — Square Loans (Block), with the shared mechanism and the differences named |

## Validation-maturity readout — reported beside the score, never inside it

| Parameter | Evidence method | Tag | Convergence event |
|---|---|---|---|
| loss rate on the flow-underwritten pool (⚠ 2–4 per cent; gate 4.8; pivot 5.0) | test | emergent | 12-month loss on ≥ 10,000 Stage 1 accounts (trial band) |
| overlay share the auditor requires (⚠ 0–25 per cent) | examination | elicitable | finance and auditor's view before Stage 1 release |
| share of migrated accounts with the rule limit ≤ the existing limit (⚠ 50–80 per cent) | analysis | elicitable | the back-test at Stage 0 |
| years of readable history (⚠ 3–5) | examination | elicitable | the data extraction at Stage 0 |
| standard-tariff share of overdraft accounts (⚠ 40–70 per cent) | examination | elicitable | the insider's figure |
| KMC high corner (⚠ 300) | examination | elicitable | the tariff's top band, read from the bank's own tariff |
| replica band (provisional = trial ± 1 point) | test | emergent | the first replica reading at 6 months |
| deposit cost, capital ratio, cost of equity (⚠ bands) | examination | elicitable | treasury's figures |

**Overall maturity: pre-operational.** No operational evidence exists and none could at F1. Every emergent parameter names a test event; every elicitable one names who holds the figure. That is the correct state at this gate and reduces no sub-score.

## Pass 1 — Completeness

Criteria from `verify-balm-custom`; the at-scale check applied; the FIT-staleness check (VA-74) run per requirement.

| Requirement | Sub-requirement | Status | Note |
|---|---|---|---|
| R1 | SR1 conventional form | ✅ | made · sold · delivered · paid; single-case check; the roadmap form as the baseline (v1.1 correction) |
| R1 | SR2 limiting operation | ✅ | the per-application decision, stated as an operation; cost evidenced (T3 benchmark and judged UK figure) |
| R1 | SR3 theory of change | ✅ | class, named theories with year and source, context as conditions, outcome as a state |
| R1 | SR4 workaround strategy | ✅ | one move; hypothesis with a falsification condition; five candidates considered |
| R1 | SR5 business form factor | ⚠️ | stated; CTM and AOM written as documents; model files a build item with a convergence event (before C4); the scripts refused pending the principal's seal |
| R2 | SR1 high-import outcome | ✅ | outcome as a state; the selected customer named |
| R2 | SR2 attendant routines | ✅ | routines across the four rows; the autopilot named |
| R2 | SR3 key monetizable cost | ⚠️ | money, foregone; sized per £1,000; the TAM data object exists (VA-83) but its validation run is refused by the toolchain — not failed, not run |
| R2 | SR4 efficacy ToC and strategy | ✅ | theories named; mutation gate with candidates and rejections |
| R2 | SR5 business form factor C1–C2 | ✅ | cumulative; reads as one product |
| R3 | SR1 limiting operation II | ✅ | an operation ("releasing a standing limit under a rule whose loss rate has not been observed"); the diagnostic run on the unit; the CLO II diagnostic translated to a bank's working capital and the translation stated |
| R3 | SR2 scaling ToC | ✅ | class (a locus-of-learning problem); Pisano 1994 with Dixit and Pindyck 1994; four conditions; outcome as a state; falsifiable |
| R3 | SR3 scaling strategy | ✅ | one move; four mutations with rejections; cost-shifting, new-form and R1–R2 consistency tests; VA-163 bands with a pre-registered £0 budget; two-model statement; capital path by stage |
| R3 | SR4 business form factor C1–C3 | ✅ | cumulative; completes F1; VA-103 table with the function-gate re-run named |

**Count: 12 complete, 2 partial, 0 open. Completeness = (12 + 1) / 14 = 92.9.**

**FIT-staleness (VA-74).** Verifier r1: WP-1, WP-2, WP-3, CP-1. r2: adds WP-4, CP-1 amended, PC-1. r3: adds WP-5. CTM v3 section 4 records the same set at C3. Not stale.

**At-scale check.** Every strategy is designed at the incumbent's volume (⚠ 228,000 drawn accounts, ⚠ £3.4–5.7bn). The C3 record separates the at-scale model from the scaling model and marks every path-only element. Passes.

## Pass 2 — Consistency

From the consistency audit F1: no hard contradiction; two soft items (S1 — the at-scale count has no date; S2 — a CTM v2 forward flag that named a change R3 did not make, corrected in v3). One condition carried: Stage 2 opens within ⚠ 24 months of Stage 1, or the capital bar is re-driven on the Stage 1 book. **Consistency = 100 − 10 = 90.**

## Pass 3 — Discipline

### 3a — Premature-design audit (VA-2)

Thirty-two specified details inventoried across the three records and the two models. The ones that need attention:

| Detail | Verdict | The open question it hides |
|---|---|---|
| the customer surplus fraction, 0.95, a judged point | 🔴 | what band the fee element of the tariff is waived in; the margin moves from 41.5 to 34.4 on it. Load-bearing, no band, no V/Val tag |
| productive hours per handler, 1,500, a point (T3, "the runner's seat judgement") | 🔴 | VA-135: the available-hours figure is a named input with a source and a date; here it has neither. Load-bearing on capacity (⚠ 17,000 hours per cell), not on the margin |
| the SC amortisation period, 5 years | 🟡 | the method states no period for one-off scaling cost; the runner chose one with its logic. The open question is the method's (routed to WS1 feedback) |
| the receipt and draw frequencies (⚠ 300 and ⚠ 3 a year), points | 🟡 | drive the computing line, which is rounded up to a band; not load-bearing on the margin |

Everything else — 28 details — is earned: each traces to the challenge that required it (the standing limit, the receipts share and the deposit funding to C1; the migration, the statement, the price condition and the selected customer to C2; the shadow limit, the release order, the back-test, the bands, the replica and the overlay to C3). **Traceability = (28 + 1) / 32 = 90.6.**

### 3b — Justification-mode tell (VA-3)

The form factor at C1: a standing limit from observed flow, repaid from receipts. At C2: the overdraft retired into that limit for the selected customer, with a price condition. At C3: the limit released in order of existing exposure, under a back-tested rule, in replicas against bands. Each challenge changed the organism. Each recorded three to five candidate mutations and the reason each rejected one was rejected. **No justification mode.** No cap.

## Pass 4 — Synthesis

**Cohered.** Square Loans (Block, Inc.) — a limit pre-computed from receipts the lender observes, shown without an application, repaid as a share of each receipt. The record names what is not Square's: the balance sheet and the release order. The three VA-106 lines name other requirements (C1: four; C2: three; C3: four, two of them earlier with a mechanism). **Synthesis = 100.**

## 6 · Registry coverage — the rows

**Applied, 62.** TPM standard: all four (two defects found, section 3a). Phase 0: investment parameters, PCO statement, research firewall, levelling record (pass; the PCO is provisionally ratified by the object-after rule, deadline 20 Sep 17:00 passed). Phase 1: CLO statement (pass, on C1 SR2).

Phase 2, 40 rows, listed as the registry orders them. Diagnosis, ToC class, theory, context (one scorer — a limit of the check, recorded), outcome, design choice, hypothesis, CTM update (on the document), AOM ops map, volume drivers (every driver resolves to section 0, RD-031), no ratios, role support, LMU sizing (Q1 pass; Q2 pass — replica = cell), FIT margin (34.4 per cent by hand; scripts refused), I check, T check, VA-106, loop gate, three-check close, VA-97 (NOT shown, the shared input named — VA-160), VA-99 (actor cases in VA-127 form), VA-101 (the new-to-trading structural limit), VA-95, VA-103, VA-127, VA-162, VA-149 (the CCA form as a statutory residue, driver and basis stated), VA-153 (no FAIL to branch; applied, trivially), VA-163, VA-92, VA-84 (ten gates driven), VA-85 (sequential), VA-83 (file exists; validation not run — partial), excluded population sized, capital bar stated, VA-82, VA-90 (r1–r3 exist), VA-80 (no later actor in C3's cells), VA-81 (the back-test as the instrument model risk already uses), counterfactual (pass).

Phase 3: all four. Phase 4: eight of nine. Phase 5: PCO confirmation (provisional, object-after).

**Not applicable, 15.** Phase 0: core functionality, right-sized problem, use cases, loss-to-price ratio (Path C mode 3 enters on a line; RD-023, RD-024). Phase 2: VA-147, VA-156, VA-155 (R7), VA-164 (R4), conventional cost line (F2), position-holding (F3), mode 2 verdict form (mode 3 clears at the incumbent's volume), VA-100 (no rule ratified by the run). Phase 4: F3 barrier scores. Phase 5: expert sign-off (after R10). Methodology note: F3 financial simulation.

**Could not apply because the record lacks the element, 5.** The Phase 1 rows named in the verdict.

**Scored on rules the run was never told.** By search of the challenge skills for R1–R3, the PCO skill and the fit verifier skill: the four TPM rows, VA-135 and VA-138 appear in none of them. Items docked on them: the surplus fraction and the productive hours (section 3a). The run wrote bands and tiers on every other figure, so it read the registry's spirit; the two points are still defects under the rule. The list routes to the Head of R&D as a defect in the method's skills, not in the venture.

## 7 · The faults found, ranked

| Fault | Item | Pass | Fix | Owner |
|---|---|---|---|---|
| F-1 · the surplus fraction is a judged point | 0.95 with no band | 3a | state it as a band with the waiver share it rests on and a V/Val tag; report the margin at both corners | the runner, next regeneration |
| F-2 · the hours figure has no source or date | 1,500 productive hours per handler | 3a | name a source (a published contact-centre utilisation figure) and a date; carry it in the AOM section 0 | the runner, next regeneration |
| F-3 · the model files do not exist; three checking scripts refused | CTM and AOM model files; fit margin, verdict order, TAM validation | 1 | build the files; re-run the scripts after the principal's seal | the VA seat; the principal (seal) |
| F-4 · the TAM data object's validation has not run | same refusal | 1 | queued behind the seal | the principal |
| F-5 · the at-scale count has no date | audit item S1 | 2 | one dated line in the C3 capital path | the runner |
| F-6 · the SC amortisation period is the runner's choice | 5 years | 3a | a method rule (WS1 feedback, R3 section) | Head of R&D |

## 8 · The three things that most raise the score

1. Build the model files and run the scripts after the seal — closes the third and fourth faults and lifts Completeness to 100.
2. Band the surplus fraction and source the hours figure — closes the first two faults and lifts Discipline to about 97.
3. Date the at-scale count — closes the fifth fault and lifts Consistency to 95.

## Recommended next session

Nothing in this list needs Tom. The first, second and fifth faults are one regeneration of the C3 record and the AOM. The third and fourth wait on the seal. The sixth is a method question. C4 can open on the record as it stands, with the F1 condition carried as a critical assumption.

## What I did not do

I did not re-derive any band or re-run any design step. I did not read `va-design-evidence.md`. I did not run the checking scripts (refused; the seal is the principal's). I did not score F2 or F3 rows. I scored with one reader where the registry's rubric rows want two.
