# A business bank's credit facility line — consistency audit at C10 (the F3 gate and the whole architecture) · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Span audited:** C8 (record v1), C9 (record v1), C10 (record v1, with the funding-gate correction of the same day), read against the PCO and C1–C7, with the CTM v10, the AOM v10, the fit model at C10, the verifier r10, the TAM data object version 4 and the financial simulation at C10. **Auditor:** the runner, as an independent pass on the record — a re-reading of the ten records for places where a later element uses a figure, a population or a rule an earlier element set, and says something different. **Method:** the F1 and F2 audits' structure, applied to the F3 span and then once across the whole architecture C1–C10, as the C10 record's close asks (the function-gate re-run). The F1 and F2 findings are re-read where an F3 element touches them, and where the financial simulation now answers one.

**Path C, mode 3.** The C10 set is object-after to 23 September 2026 17:00. The seal of 21 September 2026 19:49 is the principal's, not the runner's; the four checking scripts ran after it and their outputs are recorded in the verifier r10.

## Verdict: COHERES — one route-back, four soft items, one condition

The ten moves are one product read cold, with one central mechanism (a standing limit that is a property of the account, funded as a property of the pool) and no structural contradiction. One number in an earlier record is made false by the later floor and is routed back to that record for re-setting; this audit does not patch it.

| Item | Class | Where | Registry row | Re-enters |
|---|---|---|---|---|
| H1 — the C3 trial band's continue line (⚠ 4.8%) is stated as the point where "the 25% margin holds"; at the C10 floor the 25% margin fails above 4.45% at the set price (4.05% at the band's low end). The continue line now sits on the fail side of the gate | **hard — of number, not of structure** | C3 record, kill-band table (trial band row); C10 record, BINDING GATE block; verifier r10, binding-input table | Kill band stated per stage (C3); Binding gate printed at every challenge | **routed back to the C3 record** — re-set continue ≤ ⚠ 4.45% at the set price, borderline 4.45–5.0%, kill above ⚠ 5.0% (C2's pivot, unchanged); the F2 audit's remark of the same day foresaw this and asked the F3 audit to read it |
| S1 — the C6 price is reviewed yearly on the funding term; the funding term is read daily; the funding gate (3.45%) is not among the quarterly trigger review's readings | soft | C6 record, rate review; C10 record, trigger and the G-funding line; CTM v10 treasury track | Standing constraints named with a reading | add the funding gate as a reading at the quarterly trigger review — CTM v10 treasury track at the next regeneration |
| S2 — the recurring fixed layer is carried at 2.07–5.22 per £1,000 (the C1 band rounded up plus the route's upkeep) while the AOM 3c derives ⚠ £7.9–14.15m a year, which is 1.39–4.16 per £1,000; the floor holds ⚠ 1.06 per £1,000 of RC above the activities at the conservative corner | soft | AOM v10 §6 RC row; financial simulation §1; RD-031 (every line traces resource → activity → driver → volume) | Cost lines derived ABC, bottom-up | AOM at the next regeneration: either carry the derived £ line or state the ⚠ 1.06 as a named reserve with its reason; the margin is not read as tighter than the activities make it until then |
| S3 — R7 opens the limit to third-party readers under a public standard; R8's store of value is the seasoned multiple, and the limit it produces is exactly what R7 publishes. The two pull against each other and the C8 SCIS reads 2 at the conservative corner for that reason | soft — a named tension, not a contradiction | C7 record SR4; C8 record SCIS table; C9 record (the outcome column is not in the feed) | VA-106 read across lines; F3 barrier scores | no change: the design resolves it at R9, where the thing that does not move with the customer is the outcome column and the parameters fitted on it. Stated so that the moat is read as R9 + R10, not R8 |
| S4 — the C10 record's spread count carries the C3 people figure (⚠ £12.95m) for Stage 1 and prints 4.0%; the AOM v10 3c figure is ⚠ £13.55m and the simulation, with the seasoning call, prints −1.2% after the cost of capital at the conservative corner | soft | C10 record, spread count (VA-162); financial simulation §2 | Fixed-cost spread count stated once (VA-162) | the C10 record at the next regeneration carries the AOM v10 figure; both readings say Stage 1 does not carry the gate |

**The condition (a critical assumption for the record, not a process note):** the whole architecture's margin at the worst corner is 30.3% at the set price, and it rests on two independent holds on the two largest lines of the floor: R9 on the loss (⚠ 2–4%, gate 4.45%) and R10 on the funding (⚠ 1.5–3.0%, gate 3.45%). Neither is measured. A failure of either takes the design below the 25% gate; a failure of both takes it to 9.8%. The Phase II capital gate reads BORDERLINE at the conservative scenario (30.3% against 60%) on the same unmeasured loss rate. Until Stage 0's back-test and Stage 1's twelve-month reading replace the loss band, and the funding term's first year of daily readings replaces the deposit-cost band, every verdict in the ten records is PROVISIONAL on those two numbers and on nothing else of the same size.

## 1 · What this audit covers

The F3 dependencies the skill lists that exist at C10 are three. R7 openness → R8 store of value → R9 lock-out: what is published, what accumulates and what a rival cannot reconstruct. R9 ledger → R10 tape: the same object with a second use. R10 funding → R1 floor → R2 price condition: the largest cost line's reference. Beyond the listed pairs, the audit checked every place where an F3 element uses a figure, a population or a rule set by the PCO or C1–C7, and then read the ten VA-106 lines together, the three barrier scores together, and the financial simulation against the records.

## 2 · Dependency matrix

| Dependency | What the earlier element requires | What the later element says | Status |
|---|---|---|---|
| PCO job sentence → C10 | the customer still gets working money against the account, from the same bank, under the same permissions | the customer sees nothing at C10; the funding and the route are inside the bank; the term and the cap are treasury's | 🟢 consistent |
| C1 standing limit, no per-account act → C8, C9, C10 | no requirement reintroduces a per-account decision or a customer act | C8 the multiple steps on a cleared event the split already writes; C9 the parameters are re-fitted by cohort; C10 nothing touches the account | 🟢 consistent |
| C1 cost floor → C10 floor, re-checked at the set price | the C6 price still clears the floor as finally designed | 140 against 107.47: 30.3% at the worst corner; 25.6% at 135; 32.6% at 142.5; the operating bar 134.34 sits 5.66 under the price | 🟢 consistent |
| C1 binding gate (loss ⚠ 2–4%; pivot above ⚠ 5) → C10 loss line | the gate sits on the same input and the same numbers | floor high 67.47 + 10L; the gate at 4.45% at the set price; the pivot unchanged at 5.0%; the C3 trial band's continue line 4.8% now above the gate | 🔴 **H1** — routed back to C3 |
| C1 funding line ⚠ 1.5–3.0% (a deposit-cost assumption) → C10 funding term | the funding figure is unchanged and its reference is named | 15–30 unchanged; the reference is fixed as the measured deposit cost under a signed term; the failure values (4.0%; 4.6–5.0%) are in the position-holding table | 🟢 consistent — an assumption became a term |
| C2 KMC → C6 set price → TAM v4 | a price or a gate set later narrows the TAM only by a named block | TAM v4 adds gate G-C10-1 (the cap), a volume gate that excludes no class; the surviving volume is unchanged | 🟢 consistent |
| C2 price condition PC-1 (the operating bar inside the ceiling) → C10 | the room stays positive at every point of the band | 5.66 at 140; 0.66 at 135; 8.16 at 142.5 | 🟢 consistent |
| C3 release order and stage readings → C8 seasoning → C10 cap | the stage readings read the cohorts by the same axes the later elements add | C8 adds seasoning as a second axis of the cohort reading; C10 adds the cap reading to the release track's sitting; release pauses at the cap without any limit cut | 🟢 consistent |
| C3 at-scale count and its date (F1 audit S1: undated) → financial simulation | the at-scale count is reached at a stated month, as a band | the simulation reaches the at-scale book at month 27 (optimistic), 35 (central), 43 (conservative) on the runner's seasoning call | 🟢 **closes F1 S1** |
| C3 overlay and capital envelope → financial simulation | peak venture capital inside the ⚠ £100m envelope | ⚠ £50m at the conservative corner (the replica overlay at month 13, held six months), £25m central, £0.5m optimistic | 🟢 consistent |
| C5 handler headroom (⚠ 0–425 hours a cell; F2 audit S2) → C8 seasoning queries | recurring query loads sit inside a stated capacity | C8 books ⚠ 500–1,500 seasoning queries a cell and adds the 15th handler at the high corner (3.00–8.15, inside the rounded band) | 🟢 **closes F2 S2** |
| C6 yearly rate review → C10 daily funding term | the price reprices on the funding term at a stated frequency | yearly on the term (C10 VA-106 R2); the funding gate is not a quarterly reading | 🟡 **S1** |
| C6 fixed-against-variable question (carried) → C10 | the mechanism that would answer it is named | the daily funding term is the mechanism; the question stays with C6; the at-scale price hold across a rate cycle is printed in C10 | 🟢 consistent, carried |
| C7 open publication → C8 store of value → C9 outcome column | what R7 publishes is not what R8–R9 hold | R7 publishes the limit; R8 raises it on the account's own cleared events; R9 fits the parameters on an outcome column the feed does not carry | 🟡 **S3** — a named tension, resolved at R9 |
| C8 seasoned uplift raises undrawn (IC 13–18) → C10 cap on the drawn book | the cap counts drawn only | the cap is on the aggregate drawn book; the undrawn commitment is a capital figure and not a funding one (C10 re-verification of R8) | 🟢 consistent |
| C9 outcome ledger (pseudonymised; UK GDPR Art 4(5), Recital 26) → C10 tape | the tape carries no personal data the ledger does not | the tape is the ledger's monthly cut; the vehicle's agents are processors under Art 28; no new field | 🟢 consistent |
| C9 yearly calibration → C10 route | the route's data history is as long as the form's | the tape is produced monthly from WP-6 from Stage 1 (design commitment part i) | 🟢 consistent |
| C9 FIS and its re-test → C10 HRS and its re-test | the loss band is re-tested at every F3 requirement regardless of the score | re-tested at the C10 floor: 24.5% / 19.2% / 9.8% | 🟢 consistent |
| AOM v10 §6 RC (carried band) → fit model → floor | every line traces resource → activity → driver → volume (RD-031) | the band is the C1 rounded band plus the route; the derived £ line is lower by ⚠ 1.06 per £1,000 at the high corner | 🟡 **S2** |
| C10 spread count (Stage 1) → financial simulation | the Stage 1 figures agree or the difference is stated | the record 4.0% on ⚠ £12.95m; the simulation −1.2% on ⚠ £13.55m with seasoning | 🟡 **S4** |
| C10 funding gate 3.99% (v1 as first written) → verifier r10 | the gate reproduces by arithmetic | it did not; corrected to 3.45% the same day; the changelog carries the correction | 🟢 corrected before this audit |
| C10 cap at the worst corner → AOM q.drawn_book_gbp → PCO objective | the at-scale book band is unchanged and the cut is stated | the band is unchanged; the cut (⚠ 12% at £5.7bn against a £50bn pool) is a structural limit; the net contribution for the book falls in proportion and clears the PCO's required profit by 3.7× at the conservative corner | 🟢 consistent |
| CTM v10 treasury track (six states) → AOM v10 §3k → fit model RC and SC | every state has an activity and every activity a cost line | six states; the daily price, the cap reading, the tape cut, the trigger review, the route's upkeep and set-up each have a row; RC +0.05–0.18, SC +0.04–0.18 unrounded | 🟢 consistent |

## 3 · Hard contradictions

**H1 — one, of number.** The C3 record's trial band says "continue at or below ⚠ 4.8% (the 25% margin holds)". At the C3 floor that was true. Seven requirements later the floor high is 107.47 and the 25% margin at the set price fails above 4.45% (4.05% at the band's low end); at 4.8% the margin is 21.2% — BORDERLINE. The later element (the accumulated floor) makes the earlier element's stated reason false. The C10 record prints the gate at every challenge and the F2 audit's remark named the drift; neither re-set the band. This audit does not patch it: the trial band is C3's object and is re-set at the next regeneration of the C3 record — continue ≤ ⚠ 4.45% at the set price (4.05% at 135), borderline 4.45–5.0%, kill above ⚠ 5.0% (C2's pivot, unchanged). No structural element depends on the number; the release order, the overlay and the readings are unchanged.

No other F3 element states a figure, a population or a rule that an earlier element makes false.

## 4 · Soft items

### S1 — the funding gate is not a quarterly reading

C6 reviews the price yearly on the funding term; C10 reads the term daily and reviews the trigger quarterly; the trigger is the transfer price against the market's. The funding gate (3.45% with the loss at its high corner) is a third reading and belongs at the same quarterly sitting, so that a within-year rise in the measured deposit cost is read against the margin and not only against the market. One line in the CTM v10 treasury track.

### S2 — the recurring fixed layer holds a reserve the activities do not derive

Stated in the matrix. The reserve is conservative and does not weaken any verdict; it breaches RD-031's rule that every line traces to an activity. Two ways to close it, both the AOM's: carry the derived line (which raises the margin at the conservative corner to about 31.5%) or name the reserve and its reason. The audit prefers the second: a reserve declared is a design choice; a reserve undeclared is a defect.

### S3 — R7 and R8 pull against each other; R9 resolves it

Stated in the matrix. Recorded so that the moat test (section 7) is read correctly: the switching cost R8 creates is low by design (SCIS 2 at the conservative corner) because R7 published the limit; the lock-out is R9's and the supplier hold is R10's.

### S4 — two Stage 1 figures

Stated in the matrix. Both say Stage 1 does not carry the gate on its own book and the release order carries it to scale. The C10 record carries the AOM v10 people figure at its next regeneration.

## 5 · Additional tensions checked (skill step 3)

- **Scale and friction across F3:** none of R8–R10 adds a customer act or a query class the C5 headroom does not cover once the 15th handler is booked (C8). R10 adds nothing the customer sees.
- **Cost-shifting (VA-148), re-read at C8–C10:** R8's rejected mutations bought retention with price; R9's bought a score; R10's would have bought funding at the market or held a locked sweep against the customer. Each adopted move moves no cost onto a third party or onto the pricing room.
- **The shared input (VA-160):** the margin and the binding gate both move on the loss rate; R9 acts on it; R10 adds a second independent input (the funding line) with its own gate and its own hold. Two inputs, two readings, no transform of one into the other. Consistent with F1 and F2.
- **Existence test (VA-92) at R10 with the affordability screen first:** the maximum payable to any holder is 5.89 ÷ 1.25 = 4.71 per £1,000 (⚠ £16–27m); the route costs ⚠ 0.09–0.36; the agents are commodity vendors and no business case is owed. Consistent with C7's screen (VA-164).
- **The cap against R3's release order:** the cap binds only at the worst corner of the pool (⚠ £5.0bn against £5.7bn); at Stage 1 the drawn book is ⚠ 0.4–3.8% of the pool's balances. The release order reaches the cap, if at all, at the last tranche; release pauses, no limit is cut. Consistent.
- **Regulatory positions across the ten:** SS1/23 (C3, C9), PSRs 2017 reg. 69 (C7), UK GDPR (C9, C10), the Regulated Covered Bonds Regulations and the UK Securitisation Regulation (C10 — the covered bond route unavailable; the master trust with 5% retention available), CRR NSFR (C10). No position taken at one requirement is contradicted at another.

## 6 · Phase 5 process notes (skill step 3b) — not conditions

- The trial band's re-set (H1) is a one-line change in the C3 record and a one-line change in the kill-band row of the CTM's release track; it is not a design change.
- The funding gate's addition to the quarterly sitting (S1) is one reading; the CTM's treasury track gains one state input.
- The tape's production from WP-6 (C10 design commitment i) is the calibration's monthly cut with the route's field order; a data-design choice for the engine team.
- The route's programme documents (commitment ii) are drafted before Stage 3 and refreshed yearly by the agents; a procurement the treasury runs.

## 7 · VA-106 synergy count — read across the ten lines the run wrote

| Requirement | Other requirements its VA-106 line names | Count |
|---|---|---|
| C1 | R3, R4, R6, R8 (later, by number) | 4 |
| C2 | R3, R6, R8 (later, by number) | 3 |
| C3 | R1, R2 (earlier, with mechanism); R6, R9 (later, by number) | 4 |
| C4 | R1, R2, R3 (earlier, with mechanism); R5, R8, R10 (later, by number) | 6 |
| C5 | R1, R2, R4 (earlier, with mechanism); R6, R8 (later, by number) | 5 |
| C6 | R1, R2, R3, R4, R5 (earlier, with mechanism); R8 (later, by number) | 6 |
| C7 | R1, R2, R3, R4, R5, R6 (earlier, with mechanism); R8 (later, by number) | 7 |
| C8 | R1, R3, R4, R5, R7 (earlier, with mechanism); R2, R6 no, with reasons | 5 |
| C9 | R1, R3, R6, R8 (earlier, with mechanism); R2, R4, R5, R7 no, with reasons | 4 |
| C10 | R1, R2, R3, R6, R9 (earlier, with mechanism); R4, R5, R7, R8 no, with reasons | 5 |

**The moat test (Phase 3):** at least one line names two or more other requirements — every line does; seven of ten name three or more with a mechanism. **PASS.** Read across the ten: R1 is served with a mechanism by every later requirement (C3–C10, eight lines) — the standing limit is the object every move acts on, which is what "one product read cold" means. R3 is served by six. R8 is named by number at C1, C2, C4–C7 and served with a mechanism at C9; it is the most anticipated requirement and, by its own score, the weakest barrier (SCIS 2 at the conservative corner). The moat the ten lines describe is therefore not a switching cost: it is a lock-out (R9 — the outcome column and the parameters fitted on it, which move with no customer) and a supplier hold (R10 — the deposit franchise, which no rival without one can price against), with R8 as the store the two protect. The three barrier scores read together say the same: SCIS 2 · 4 · 6, FIS 5 · 6 · 7, HRS 5 · 6 · 6 with the commitment. Two of three pass at every corner; the one that does not is the one the other two make unnecessary. Recorded as a design finding, not softened into a pass.

## 8 · Real-business analogue for the whole architecture (VA-1)

**Square (Block, Inc.) — Square Loans originated by Square Financial Services, Block's own Utah industrial bank (opened March 2021), alongside Square Checking and Square Savings.** Read against the ten moves: a limit computed from the seller's own observed receipts with no application (R1); the price as a fixed fee below the seller's alternative (R2); cohorts scaled on the platform's own data before a bank charter (R3); the offer placed inside the seller's own dashboard (R4); no-act draw and repayment as a share of each card receipt (R5); the charge taken first from each settlement (R6); the line shown in the tool the seller already uses (R7); renewal offers that grow with repayment history (R8); underwriting calibrated on Square's own repayment outcomes, which no bureau carries (R9); and, since 2021, loans originated and held inside Block's own bank beside the deposits of the same sellers, where before they were funded through Celtic Bank and warehouse lines — the market route this design keeps as its standby (R10). Sources: Block, Inc. annual reports 2021–2024 (T2). **Where the analogue stops:** Square sees the receipts because it processes them, not because it holds the current account; the deposit franchise is small against the loan book, so no cap of the design's kind is published; and a standby master trust is not disclosed. Where it stops is exactly where this design's R10 goes further — a bank's own current-account pool is large against its facility line (⚠ 3.4–11.4%), so the cap is available and the funding is cheaper than any market route. One analogue, its stopping point named.

## 9 · Convergence routing

The parts have cohered: one analogue for the whole architecture with its stopping point named; no structural contradiction; one number routed back; ten synergy lines that pass the moat test; three barrier scores read together with the weak one named. **Routing:** Function 3 closes PROVISIONAL at the C10 record. H1 re-enters the C3 record at its next regeneration; S1 the CTM; S2 the AOM; S4 the C10 record. The condition above is carried as the architecture's critical assumption into the verification pass and the status file. The next event that moves any verdict is a measurement, not a design change: Stage 0's back-test on the bank's own history.

## 10 · Remarks, not findings

- The F2 audit remarked that the C6 price bought 2.5 per £1,000 of margin and that the trial band had drifted onto the fail side of the gate. F3 spent a further 0.23 of margin (30.5% → 30.3%) and the drift is now a contradiction (H1). The pattern — each requirement's small addition read as small — is why the cap line (RD-030) is printed at every challenge; the cap line holds at ⚠ 1.10–1.47 of ⚠ 8.00.
- The financial simulation's peak venture capital (⚠ £50m at the conservative corner) is an overlay held for six months, not money spent; the venture's operating cash is positive from month 6 at the conservative corner and from month 1 at the others. The C3 record's envelope reading (⚠ £1–50m) is reproduced.
- Four script findings for WS1, all carried from r7–r9 and one new: `fit_margin.py` reads the best corner over the whole ceiling band; `validate_tam_model.py` has no vocabulary for a class excluded by the venture's own price or for a volume gate; `check_verdict_order.py` reads no F3 gate; and, new, the fit model has no field for a barrier score or a position-holding table.
- The funding gate as first written (3.99%) was an arithmetic error caught by the verifier r10 before this audit. The verifier's check — every gate re-derived from the floor by hand — is the one that caught it; the record's own checks-run table did not, because the table asked whether the gate was printed and not whether it reproduced.

## What I did not do

- I did not re-audit the F1 and F2 pairs except where an F3 element or the simulation touches them (five rows above).
- I did not read the CTM and AOM model files (the structured data form); they are a carried build item. The audit read the written v-documents.
- I did not patch H1. I did not run the seal. I did not name the bank. I did not write any internal count.
