# A business bank's credit facility line — consistency audit at the F2 gate · 21 September 2026

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every internal figure is a red field `⚠`. **Span audited:** C4 (record v1), C5 (record v1), C6 (record v1), C7 (record v1), read against PCO and C1–C3, with the CTM v7, the AOM v7, the fit model at C7, the verifier r7 and the TAM model version 3 (at C7). **Auditor:** the runner, as an independent pass on the record — a re-reading of the four records for places where a later element uses a figure, a population or a rule an earlier element set, and says something different. **Method:** the F1 audit's structure, applied to the F2 span; the F1 findings are not re-audited except where an F2 element touches them.

**Path C, mode 3.** The C7 set is object-after to 23 September 2026 17:00. The seal of 21 September 2026 19:49 is the principal's, not the runner's; the three checking scripts ran after it and their outputs are recorded in the verifier r7.

## Verdict: PASS WITH CONDITIONS — no hard contradiction, three soft items, one condition

| Item | Class | Where | Registry row | Re-enters |
|---|---|---|---|---|
| S1 — a switched-off account (C5) still shows the published pre-agreed line (C7); a platform's cash forecast may show a shortfall covered when the payment would be returned | soft | C5 record, switch-off row; C7 record SR1 routine A and assumption 5; CTM v7 partner track | Use routine at the cue (VA-155 presence third case); actor table, effect on own book (VA-127) | C7 record — a design position line at the next regeneration; the display-query rate reads it |
| S2 — the C5 handler headroom (⚠ 0–425 hours a cell) was booked against a first-year funding-query peak; C6 and C7 now draw recurring query loads from it (87–300 hours at the high corners) | soft | AOM v5 §0 `f.cell_min_people`; AOM v6 §3b charge queries; AOM v7 §3b display queries and §0 note | ABC cost line with a resolving driver (RD-031); capacity band stated (VA-165) | AOM v8 — restate the headroom as a recurring line; convergence at the first replica's six months |
| S3 — two presentations of "available": the bank's app shows one available figure (C5); the account-information feed serves the booked balance plus a credit line marked not included (C7) | soft | C5 record use routine step 3; C7 record SR4 integration strategy, runner's call on `Included = false` | Integration strategy stated; conduct row (CONC 3 / PSRs reg 69 desk position) | C7 record — a one-line reconciliation at the next regeneration; the conduct desk position owns the wording |

**The condition (a critical assumption for the record, not a process note):** the F2 design's margin is read at the set price of £140 per £1,000 drawn (C6) and at the at-scale count. The C6 price sits 2.5 below the C2 fixed point of 142.5 and 7.15 above the operating bar at the C7 floor high (132.85). Every F2 requirement added cost inside that 7.15 of room, and the room is what a paid partner would have been bought from; R7 bought none. Until the first replica reads the loss rate, the funding-query rate and the display-query rate, the design's whole tolerance is the 7.15 at the central corner and 0 at the pessimistic corner. The C7 record's affordability screen (VA-164) states this; the audit carries it as the condition on the F2 verdict.

## 1 · What this audit covers

The F2 dependencies the skill lists that exist at C7 are four. R1 form → R6 price structure: the charge on the daily drawn balance is a term of the same limit. R4 placement → R5 routine → R7 seat: the same shortfall, seen in three places. R6 price → R7 affordability: what a partner could be paid from. R2 KMC → R6 set price → the TAM narrowing by the named block "price". R7 → R8 (openness and lock-in) is designed on one side only and is read for the F3 audit. Beyond the listed pairs, the audit checked every place where an F2 element uses a figure, a population or a rule set by PCO or C1–C6.

## 2 · Dependency matrix

| Dependency | What the earlier element requires | What the later element says | Status |
|---|---|---|---|
| PCO job sentence → C7 | the customer still gets working money against the account, from the same bank, under the same permissions | the published line is account information under PSRs 2017 regulation 69; no new permission; the limit is the C1 limit | 🟢 consistent |
| C1 standing limit, no per-account act → C7 element | no requirement reintroduces a per-account decision or a customer act to obtain the line | the feed publishes a limit the rule already set; the account-information team runs one conformance test per counterparty class, not per account | 🟢 consistent |
| C1 cost floor → C7 floor, re-checked at the set price | the C6 price still clears the floor as finally designed | 140 against 106.28: 31.7 per cent at the worst corner; 27.0 at the band low; 34.1 at the band high (verifier r7, by hand and by script) | 🟢 consistent (non-gating) |
| C1 binding gate (loss rate ⚠ 2–4 per cent; pivot above ⚠ 5) → C7 loss line | the gate sits on the same input and the same numbers | floor high 66.28 + 10L; the gate crosses 25 per cent at 4.57 at the set price (4.17 at the band low, 4.77 at the band high). The C1 pivot now sits 0.43 points on the fail side of the gate, against 0.8 at C3. The record names the narrowing | 🟢 consistent, tension re-named with the new number |
| C2 KMC (the rate the customer compares against) → C6 set price → TAM v3 | a price set at C6 may narrow the TAM only by a named block | TAM v3 gate G-C6-1, named block "price"; SC-OD-BELOW-BAND and SC-LOAN-USER move to not addressable with `excluded_by` stated; surviving volume unchanged; `validate_tam_model.py` valid with three declared warnings | 🟢 consistent |
| C2 ceiling (139.95–279.90; fixed point 142.50) → C6 price band | the set price and its band sit inside the ceiling band | 140, band ⚠ 135–142.5; the band high equals the C2 fixed point; nothing above it | 🟢 consistent |
| C3 release flag → C7 element | the feed shows a line only where C3 has released one | the published line is present for released accounts and absent otherwise; an unreleased account shows no credit line resource, not a zero | 🟢 consistent |
| C4 CP-2 placed at the shortfall → C7 seat | the history is placed where the shortfall is first seen | for a connected customer the shortfall is first foreseen in the platform's cash forecast, not in the bank's app; C7 completes the placement for that share (⚠ 45–70 per cent) rather than moving it | 🟢 consistent — C7 is the completion of C4's placement rule, stated as such in the C7 record |
| C4 credibility gap (a bank's number is not money until a person has decided) → C7 | the same belief mechanism, not a second one | the feed puts the number in the tool where the person plans; Milgrom 1981 read across; C7 names R4 in its VA-106 line with the mechanism | 🟢 consistent |
| C5 default funding and draw ahead → C7 published line | the line the feed publishes is drawable by the same rules | drawable by default funding or by draw ahead; a switched-off account is drawable by draw ahead only — the platform cannot tell the two apart | 🟡 soft (S1) |
| C5 use routine step 5 (no act) → C7 routine A | the connected customer's routine keeps the no-act property | routine A adds no act: the forecast reads the line; the funded event is unchanged; routine B is the C5 routine unchanged | 🟢 consistent |
| C5 handler headroom (⚠ 0–425 hours a cell) → C6 charge queries → C7 display queries | the headroom is a first-year peak allowance | C6 and C7 book recurring loads of 87–300 hours at the high corners from the same headroom; at the 20,400-account cell the sum fits; a first-year peak plus recurring loads may not | 🟡 soft (S2) |
| C5 app screen (one available figure) → C7 feed (booked balance plus a credit line marked not included) | one representation of the limit to the customer | the Open Banking balance resource carries both balance types; the runner's call on `Included = false` keeps the platform's forecast honest but differs from the app's one figure | 🟡 soft (S3) |
| C6 charge as the first slice of the receipts share → C7 receipt splits as transaction lines | the feed's split lines are the C6 slices and nothing else | two lines per receipt where a balance is drawn: the charge slice and the repayment slice; the C6 representative example is reproduced line for line in the C7 record | 🟢 consistent |
| C6 pricing-committee actor row (FAIL at the pessimistic corner, disposed) → C7 affordability screen (VA-164) | both read the same room above the operating bar | C6: 7.15 central, 0 pessimistic; C7: 7.15 central, 0 pessimistic, paid partner return 0 — the same number, the same corner | 🟢 consistent |
| C6 no fee, no charging date → C7 no fee, no agreement | R7 adds no price term | partner return nil (VA-156); no agreement; the conformance test is the only cost | 🟢 consistent |
| C3 at-scale count → C7 connected count | the connected count derives from the released count by a stated share | `q.connected_accounts` 342,000–532,000 = the released count × ⚠ 45–70 per cent; the share is T4 with its source | 🟢 consistent |
| VA-160 shared input (loss rate) → C7 | no F2 element moves the loss rate | C4–C7 each state the loss rate unchanged; the C7 loss line moves by price only | 🟢 consistent |
| Verdict record R1–R7 → the F2 gate reading | verdicts compose forward (VA-95) | `check_verdict_order.py`: IN ORDER; F2 reads PROVISIONAL at R7 | 🟢 consistent |
| RD-030 cap line → C4–C7 additions | cumulative additions ≤ ⚠ £8 per £1,000 at the high corner | R4 0.03–0.20; R5 0.02–0.06; R6 0.00–0.01; R7 0.00–0.01; cumulative ⚠ 0.05–0.28; remaining 7.72 | 🟢 consistent |

## 3 · Hard contradictions

None found. No F2 element states a figure, a population or a rule that an earlier element makes false.

## 4 · Soft items

### S1 — the published line on a switched-off account

C5 lets a customer switch default funding off. The limit stays; a draw then needs the customer's act (draw ahead). C7 publishes the limit to the platform for every released connected account, switched off or not, because the limit is drawable either way. The platform's forecast then shows the shortfall covered. For a switched-off account the payment would be returned unless the customer draws ahead. **Design position (runner's call, tagged):** publish for switched-off accounts too, because the standard has no field for "drawable only on request" and a line that appears and disappears with a switch would be the routine disruption C5 removed. The switched-off share is ⚠ ≤ 10 per cent (C5, T4). The account-information team owns it; the display-query rate is the reading that would show it. **Fix:** one line in the C7 record at its next regeneration, naming the position and the reading.

### S2 — the C5 headroom is now a recurring line

The C5 AOM booked ⚠ 0–425 hours a cell of handler headroom against a first-year peak of funding queries. C6 drew charge queries from it and C7 drew display queries from it; both are recurring, not first-year. At the high corners the recurring draws sum to 87–300 hours, inside the 425. The first-year peak plus the recurring draws is not summed anywhere. **Fix:** at the next AOM regeneration, split the headroom into a first-year line and a recurring line, each with its own driver resolving to section 0 (RD-031). **Convergence:** the first replica's six months, when the three query rates are read.

### S3 — two presentations of "available"

The bank's app (C5) shows one available figure: the booked balance plus the limit. The feed (C7) serves the booked balance and, as a separate resource, the credit line with `Included = false`, so that the platform adds it in its own forecast logic. Both are permitted by the standard. A customer who reads both may see two different "available" figures. **Position (runner's call, tagged):** the feed's form is the correct one for a forecast, because a platform that receives one merged figure cannot show the customer how much of it is borrowing. The app is a display; the feed is data. **Fix:** a one-line reconciliation in the C7 record, and the conduct desk position owns the wording the app uses.

## 5 · Additional tensions checked (skill step 3)

- **Openness and lock-in (R7 → R8):** R7 opens the limit to third-party readers; the reading is by a public standard, so no reader is locked in. What R8 would count as a switching cost is the presence of the line in the customer's own tools: a rival bank's limit is not in the platform unless that bank publishes one too. C7 names this as an R8 signal by number and designs nothing for it. Noted for the F3 audit.
- **Scale and friction:** R7 adds no customer friction — the customer connects an account once (already done for the connected share) and sees a line appear. Four unattended calls a day per account (SCA-RTS article 36(5)) is the platform's load, not the customer's.
- **Cost-shifting (VA-148, re-read at C7):** mutation B (a paid integration with a named platform) was rejected because it moves cost onto the pricing room; mutation A moves none.
- **The shared input (VA-160):** the margin and the binding gate both move on the loss rate. No F2 element touches it. Consistent with F1.
- **Partner class, not partner name (VA-92):** C7 names a class of readers and runs the existence test on the class; no partner is named, so no `kmc` sits on a partner. Consistent.

## 6 · Phase 5 process notes (skill step 3b) — not conditions

- The conformance test pack for the six counterparties (three platforms, two aggregators, one accountant-software provider) — what the account-information team runs and records. A process the bank designs.
- The app's wording where the feed's line and the app's figure differ (S3). A handbook item for the conduct desk.
- The migration script for the connected share: whether the customer is told the line will appear in the platform before it does. A handbook item.
- The display-query rate's definition: a query is counted when the customer asks the bank about a figure they saw in a third-party tool. A data-design choice.

## 7 · VA-106 synergy count — read from the lines the run wrote

| Requirement | Other requirements its VA-106 line names | Count |
|---|---|---|
| C4 | R1, R2, R3 (earlier, with mechanism); R5, R8, R10 (later, by number) | 6 |
| C5 | R1, R2, R4 (earlier, with mechanism); R6, R8 (later, by number) | 5 |
| C6 | R1, R2, R3, R4, R5 (earlier, with mechanism); R8 (later, by number) | 6 |
| C7 | R1, R2, R3, R4, R5, R6 (earlier, with mechanism); R8 (later, by number) | 7 |

Every F2 line names two or more other requirements, and every line names at least one earlier requirement with the mechanism: **PASS** on the moat test as far as F2 reaches. The count rises by one at each requirement because each F2 form is placed on the form before it; that is what Tom's rule for R4–R7 (16 September 2026) asks for.

## 8 · Real-business analogue (VA-1)

Square Loans (Block, Inc.), carried from C3 and re-read at each F2 requirement. Three mechanisms are shared: the placement of the offer inside the seller's own dashboard (R4), the no-act draw and repayment from receipts (R5), and the charge as a share of receipts with no calendar debit (R6). R7 is where the analogue ends. Square shows the limit in its own dashboard, which its sellers already use. The bank's customers plan in third-party tools, so the C7 form publishes the limit by a public standard rather than by owning the dashboard. The C7 record states the shared mechanism and the difference. **PASS.**

## 9 · Convergence routing

The parts have cohered: one analogue with its stopping point named, no contradiction, four synergy lines that name earlier requirements with the mechanism. **Routing:** proceed to C8 after the F2 gate closes. The condition above is carried as a critical assumption. S1 and S3 are added as lines at the next regeneration of the C7 record. S2 is taken at the next AOM regeneration.

## 10 · Remarks, not findings

- The C1 pivot trigger (above ⚠ 5 per cent) and the loss gate at the set price (4.57 per cent) are now 0.43 points apart, against 0.8 at C3. The C6 price bought this: 2.5 per £1,000 of margin was spent on setting the price below the ceiling. The trial band (continue ≤ 4.8) now sits on the fail side of the gate at the set price. The C7 record names this; the F3 audit should ask whether the band moves to 4.57.
- The audit ran after the seal of 21 September 2026 19:49 (the principal's). Three script findings for WS1. `fit_margin.py` reports a best corner of 417.9 per cent, read over the whole ceiling band regardless of the set price; by hand the best corner at the set price is 159.1. `validate_tam_model.py` has no vocabulary for a segment excluded by the venture's own price while its comparison rate stays live; two L4 warnings were declared, not forced to KMC-0. `check_verdict_order.py` reads both function gates correctly.
- A platform's own rendering may word the credit line as an "overdraft". That is the platform's communication, not the bank's; C7 carries it as assumption 5 with the conduct desk as owner. Not a tension between elements: C5's desk position is that the limit is an arranged facility, and "arranged overdraft" is a true description.

## What I did not do

- I did not re-audit the F1 pairs except where an F2 element touches them (three rows above).
- I did not read the CTM and AOM model files (the structured data form); they are a carried build item. The audit read the written v-documents.
- I did not run the seal. I did not name the bank. I did not write any internal count.
