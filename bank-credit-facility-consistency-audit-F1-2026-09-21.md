# A business bank's credit facility line — consistency audit at the F1 gate · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Span audited:** PCO, C1 (record v2), C2 (record v1), C3 (record v1), with the CTM v3, the AOM v3, the fit model at C3 and the verifier r3. **Auditor:** the runner, as an independent pass on the record — a re-reading against the dependency matrix, not a re-run of the design. **Format:** the challenge skill names this file; the audit skill's HTML form is deferred to the function-gate regeneration so that the record set stays in one format.

**Path C, mode 3.** The C3 set is object-after to 23 September 2026 17:00.

## Verdict: PASS WITH CONDITIONS — no hard contradiction, two soft items, one condition

| Item | Class | Where | Registry row | Re-enters |
|---|---|---|---|---|
| S1 — the at-scale margin is read on the at-scale count; Stage 1 on its own does not clear the gate, and the record does not date when the at-scale count is reached | soft | C3 record, capital path and spread count (VA-162); verifier r3 Stage 1 line | Fixed-cost spread count stated once (VA-162); Capital bar stated | C3 capital path — a dated line; the condition below |
| S2 — the CTM v2 flagged Phase 3 (Paying) as "the phase R3 changes"; R3 changed nothing in it | soft | CTM v2 section 2 heading; CTM v3 corrects it | CTM update (traceability) | corrected in CTM v3; no further action |

**The condition (a critical assumption for the record, not a process note):** the design's margin is stated at the at-scale count (⚠ 228,000 drawn accounts). The path reaches that count only when Stage 2 is released, which depends on the trial band reading at 12 months on the Stage 1 pool. Until then the venture runs at a Stage 1 margin of ⚠ 7.1 per cent (discounted) — positive, below the gate. The condition: **Stage 2 opens within ⚠ 24 months of Stage 1, or the record re-drives the capital bar on the Stage 1 book.** This passes the step 3b test as a condition: it depends on an observed loss rate, which the venture does not control.

## 1 · What this audit covers

The F1 dependencies the skill lists that exist at C3: R1 cost structure → R2 value ceiling, re-checked with the C3 floor. R1 BFF → R6 and R3 → R8 are not designed and are not audited. Beyond the listed pairs, the audit checked every place where a later element uses a figure, a population or a rule an earlier element set.

## 2 · Dependency matrix

| Dependency | What the earlier element requires | What the later element says | Status |
|---|---|---|---|
| PCO job sentence → C1 | the customer still gets working money against the account, from the same bank, under the same permissions | the standing limit on the account line; PRA and FCA permissions unchanged | 🟢 consistent |
| PCO excluded delivery (asset and invoice finance, PCO 2d) → C1–C3 | no requirement reintroduces the excluded delivery | C1 mutation C (lend on the receivable) rejected on that ground; C3's four mutations are all on the release of the same limit | 🟢 consistent |
| C1 CLO (the per-application decision, eliminated) → C3 release order | the release must not reintroduce a per-account decision | release is by stage against a pre-registered band; the account-level act is a flag change | 🟢 consistent |
| C1 "no annual review" → C3 SS1/23 monitoring | the removed activity is the review of each facility | what SS1/23 monitors is the rule as a model; the stage readings are readings of the rule, not of accounts | 🟢 consistent |
| C1 cost floor → C2 ceiling, re-checked with the C3 floor | the ceiling still clears the floor as finally designed | 142.50 against 106: 34.4 per cent at the worst corner (verifier r3, by hand) | 🟢 consistent (non-gating) |
| C1 binding gate (loss rate ⚠ 2–4 per cent; pivot above ⚠ 5 per cent) → C3 trial band | the band must sit on the same input and the same numbers | continue ≤ 4.8; borderline 4.8–5.0; kill > 5.0. The gate crosses 25 per cent at 4.8, so the C1 pivot sits 0.8 points on the fail side of the gate. The record names the gap and the band holds it | 🟢 consistent, tension named |
| C1 whole-book ceiling (FAIL at r1) → C3 VA-103 row | the FAIL stays recorded and non-gating | −32.8 per cent at the C3 floor, non-gating; the selected customer's ceiling is the gate | 🟢 consistent |
| C2 selected customer (standard-tariff overdraft accounts ⚠ 41,800–113,050) → C3 Stage 1 population (all migrated overdraft accounts ⚠ 104,500–161,500) | the trial population must contain the population the saving is measured on | the tariff accounts are a subset of the migrated accounts; the C3 VA-106 R2 line states the two pools converge on one cohort | 🟢 consistent |
| C2 price condition PC-1 (price below the tariff; the operating bar inside the ceiling) → C3 floor +£1 | the room between bar and ceiling stays positive | 142.50 − 132.50 = 10.00 (was 11.25) | 🟢 consistent |
| C2 saving statement (annual, from migration) → C3 CP-1 release-time note | for the selected customer the statement timing must not move | migration and release are the same event at Stage 1; the note binds the unreleased population only | 🟢 consistent |
| C2 migration one-off (⚠ £0.1–0.5m; ⚠ 5,300–8,200 hours) → C3 SC layer | the figure carried by number is the figure used | AOM v3 3e uses ⚠ £0.3–0.85m in all, the same two components | 🟢 consistent |
| C3 SC amortisation (5 years) → path length (⚠ 27–42 months) and MLR retention (5 years) | the period must contain the path and have a stated basis | both stated in AOM v3 section 6 | 🟢 consistent |
| C3 replica (⚠ 333,000 accounts, ⚠ 100,000 drawn) → AOM section 5 cell (100,000 drawn) | the scaling unit and the operating unit must be one object or the difference stated | one object; the 30 per cent drawn share is the C1 quantity | 🟢 consistent |
| C3 stage-reading and back-test hours → AOM 3c headcount (unchanged) | the added hours must fit inside the existing functions | ⚠ 450–900 reading hours inside model risk's ⚠ 15,000; ⚠ 1,500–3,000 back-test hours inside the engine team's ⚠ 37,500; ⚠ 800–1,500 validation hours inside model risk | 🟢 consistent |
| C3 overlay share ⚠ 0–25 per cent (assumption 3) → verifier r3 sensitivity | the assumption must be stated with what happens if it is wrong | at 100 per cent SC rises to ⚠ 1–2; the verdict does not move | 🟢 consistent |
| VA-23 (no launch constraints in the at-scale design) → C3 two-model statement | the scaling path must not enter the at-scale form | the at-scale model carries no shadow limit, no release flag, no band; the CTM v3 marks every path row "path only" | 🟢 consistent, tension named (the release order is a scaling model, not a launch constraint — the record says so and mutation D was rejected as one) |
| C3 at-scale margin (34.4 per cent) → C3 Stage 1 margin (⚠ 7.1 per cent) → the capital bar | the count the margin is read on is the at-scale count, with the date it is reached | the count is stated once with its reason (VA-162); the date is not | 🟡 S1 |
| CTM v2 Phase 3 flag → CTM v3 | a forward flag names a change the later requirement makes | R3 made no change to the customer's paying rows | 🟡 S2 (corrected) |
| R1 → R6 · R3 → R8 · all F2 and F3 pairs | — | not designed | not applicable at F1 |

## 3 · Hard contradictions

None. Every figure a later element uses was traced to the element that set it, and none was found changed on the way. The two places a reader might expect a contradiction — "no annual review" against SS1/23 monitoring, and "no per-application decision" against a staged release — resolve on what is reviewed (the rule, not the facility) and what is released (a stage, not an account).

## 4 · Soft items

### S1 — the at-scale count has no date

The C3 record reads the margin at ⚠ 228,000 drawn accounts and states why that is the at-scale count. It also prints the Stage 1 margin (⚠ 7.1 per cent discounted, 12.8 undiscounted) and says Stage 1 is viable standalone. What it does not say is when the at-scale count is reached, in months from Stage 1, as a band. The path length (⚠ 27–42 months) is stated; the point at which the RC layer is spread over the full book is not. The capital bar (⚠ 26.05–43.68) is derived from the PCO's required year-five revenue, so the year matters. **Resolution:** one dated line in the capital path — "the at-scale count is reached at ⚠ month 27–42, inside year five" — and the condition above. No BFF change.

### S2 — a forward flag that named a change R3 did not make

CTM v2's Phase 3 heading read "the phase R3 changes; the price is C6". R3 changed the bank's working-capital structure, not the customer's paying rows. CTM v3 corrects the heading. The defect is in the v2 record, which is retained unchanged as the C2 record; the correction is carried in v3's changelog. **Resolution:** done.

## 5 · Additional tensions checked (skill step 3)

- **Openness and lock-in (R3 → R8):** not designed. Noted for the F3 audit: the release order opens nothing to a partner; the rule and the history stay inside the bank.
- **Scale and friction:** the release order adds no customer friction — the customer sees a limit appear. Nothing here for R8 to lose.
- **Cost-shifting (VA-148 at R1, re-read at R3):** the C3 record runs the test on each mutation; B (guarantee) and C (forward-flow sale) fail it and are rejected. Consistent with the C1 answer.
- **The shared input (VA-160):** the margin and the binding gate both move on the loss rate. The verifier and the record both say NOT shown. Consistent.

## 6 · Phase 5 process notes (skill step 3b) — not conditions

- The stage-reading pack: what the board risk committee sees at each reading (loss by cohort against the band, conduct sample, overlay position). A process the bank designs.
- The shadow-limit field's retention after Stage 3 (dropped, or kept for the validation record). A data-design choice.
- The migration-decline script and the release-time statement for the unreleased population. Handbook items.

## 7 · VA-106 synergy count — read from the lines the run wrote

| Requirement | Other requirements its VA-106 line names | Count |
|---|---|---|
| C1 | R3, R4, R6, R8 (later, by number) | 4 |
| C2 | R3, R6, R8 (later, by number) | 3 |
| C3 | R1, R2 (earlier, with mechanism); R6, R9 (later, by number) | 4 |

At least one line names two or more other requirements: **PASS** on the moat test as far as F1 reaches. The C3 line is the first to name earlier requirements with a mechanism, which is the test's purpose.

## 8 · Real-business analogue (VA-1)

Square Loans (Block, Inc.), stated at C3 with its limits: the mechanism (a limit pre-computed from observed receipts, repaid as a share of each receipt, no application) is shared; the balance sheet (a bank's deposits and capital, not a partner bank's) and the release order (existing exposure first) are not Square's. The analogue is named, the shared mechanism is named, the differences are named. **PASS.**

## 9 · Convergence routing

The parts have cohered: one analogue, no contradiction, a synergy line that names earlier requirements. **Routing:** proceed to C4 after the F1 gate closes — with the condition above carried as a critical assumption and the S1 dated line added at the next regeneration of the C3 record.

## 10 · Remarks, not findings

- The C1 pivot trigger (above ⚠ 5 per cent) and the C3 gate crossing (4.8 per cent) are 0.8 points apart. The trial band holds the gap as a borderline zone. A reader should know that the design's whole tolerance on its one unmeasured input is that zone.
- The audit could not run `check_verdict_order.py` (toolchain refused; the seal is the principal's). The verdict order in the three records was read by eye: verdict first, then the checks. No defect found.

## What I did not do

I did not re-derive any band. I did not read `va-design-evidence.md`. I did not run the checking scripts. I did not audit F2 or F3 pairs, which are not designed.
