# A business bank's credit facility line — function 1–3 status · 21 September 2026 (F1 closed; F2 closed; F3 closed PROVISIONAL at C10 — the architecture complete, Phase II gate BORDERLINE)

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. Unnamed in every file; internal figures as red fields. **Path:** C, mode 3 (just show me). **Entry:** `../bank-deposits-lending-pco-v1-2026-09-18.md`, runner-drafted, object-after to 20 September 2026 17:00 — **ratified by lapse, 20 September 2026 17:00; no objection recorded.** Every C1–C7 document is runner-drafted and object-after (derived-work rule, 1 September 2026).

| Requirement | Sub-requirements | CTM | AOM | Fin-sim | FIT | Verdict |
|---|---|---|---|---|---|---|
| R1 — at-scale cost bottleneck (v2, CLO in the delivering zone) | 5 of 5 filled | v1 written (document; model file a build item) | v1 written (document; model file a build item) | fit model at-C1, script run | −32.1% / 111.1% by script; non-gating in mode 3 | **PROVISIONAL** — the PCO cap is lifted (ratified by lapse); the verdict stands on its own build item and unmeasured inputs; binding gate the loss rate (unmeasured) |
| R2 — customers' value bottleneck (v1, closed 21 Sep 2026) | SR1–SR5 filled after the rerun; KMC = the standard-tariff overdraft cash outflow £150–300 per £1,000 drawn a year (T3) | v2 written (document; model file a build item) | v2 written (document; capacity 17,000 h per cell; v1 double count removed) | fit model at-C2 written; **script REFUSED** (toolchain awaits the principal's seal) — arithmetic by hand | 35.7% worst / 427.8% best by hand (42.9% / 455.6% undiscounted); PASS ≥ 25%, INDICATIVE; carries true, headroom £18.75 | **PROVISIONAL** — cannot exceed R1's PROVISIONAL (VA-95); binding gate the loss rate (holds to 4.9%; pivot > ⚠ 5%) |
| R3 — scaling cost bottleneck (v2, closed 21 Sep 2026; v2 = H1 route-back, trial band re-set) | SR1–SR4 filled; CLO II = releasing a standing limit under a rule whose loss rate has not been observed; the one move = release in order of existing exposure (shadow limit, back-test, migrated accounts first, replicas against pre-registered bands) | v3 written (WP-5; the release track; path-only rows marked) | v3 written (section 3e scaling stages; SC populated 0–1; floor 54–106 complete on four layers; capacity unchanged) | fit model at-C3 written; **three scripts REFUSED** (seal awaited) — arithmetic by hand | 34.4% worst / 427.8% best by hand (41.5% / 455.6% undiscounted); PASS ≥ 25%; carries true, headroom £17.50 | **PROVISIONAL** — cannot exceed R1's (VA-95); binding gate the loss rate (gate 4.8%; pivot > ⚠ 5%; zero at 7.65%) |
| **F1 gate** (21 Sep 2026) | consistency audit: **PASS WITH CONDITIONS** (0 hard, 2 soft; one condition — Stage 2 opens within ⚠ 24 months or the capital bar is re-driven on the Stage 1 book) · verification: **93.4 SOUND**, validation-maturity pre-operational (completeness 92.9 · consistency 90 · discipline 90.6 · synthesis 100) · counterfactual: written; floor unchanged; the conventional R4–R10 additions must fall to ⚠ £8 per £1,000 or less at the high corner | — | — | — | — | **F1 closed PROVISIONAL**; C4 may open on the record as it stands |

**Files.**
- C1 record: `../bank-credit-facility-c1-v2-2026-09-18.md` (v1 retained: first diagnosis)
- CTM v1: `bank-credit-facility-ctm-v1-2026-09-18.md`
- AOM v1: `bank-credit-facility-aom-v1-2026-09-18.md`
- Fit model: `bank-credit-facility-fit-model-at-C1.yaml`
- Verifier r1: `bank-credit-facility-fit-verifier-r1-2026-09-18.md`
- Evidence object (14 Sep 2026): `bank-conventional-model-object.yaml`
- C2 run note (19 Sep 2026, diagnosis and rerun; now superseded by the record): `../bank-credit-facility-c2-run-note-2026-09-19.md`
- **C2 record: `../bank-credit-facility-c2-v1-2026-09-21.md`**
- TAM data object v2 (at-C2-close, validated): `bank-credit-facility-tam-model.yaml`
- CTM v2: `bank-credit-facility-ctm-v2-2026-09-21.md`
- AOM v2: `bank-credit-facility-aom-v2-2026-09-21.md`
- Fit model at C2: `bank-credit-facility-fit-model-at-C2.yaml`
- Verifier r2: `bank-credit-facility-fit-verifier-r2-2026-09-21.md`
- **C3 record: `../bank-credit-facility-c3-v1-2026-09-21.md`**
- CTM v3: `bank-credit-facility-ctm-v3-2026-09-21.md`
- AOM v3: `bank-credit-facility-aom-v3-2026-09-21.md`
- Fit model at C3: `bank-credit-facility-fit-model-at-C3.yaml`
- Verifier r3: `bank-credit-facility-fit-verifier-r3-2026-09-21.md`
- Consistency audit F1: `../bank-credit-facility-consistency-audit-F1-2026-09-21.md`
- Verification F1: `../bank-credit-facility-verify-F1-2026-09-21.md`
- Counterfactual (F1 gate, RD-030): `bank-credit-facility-counterfactual.md`

## Function 2 — the want, use, buy and access blocks (C4–C7)

**The number F2 must hit (counterfactual, RD-030):** the conventional R4–R10 additions, ⚠ 15–63 per £1,000 a year, must fall to ⚠ £8 or less at the high corner at a surplus fraction of 0.95. Tom's rule (16 September 2026): R4–R7 remove the blocks the conventional form pays for; a booked acquisition cost is a failed R4. Every F2 record therefore names the conventional line, removes it, and books only what the one move costs.

| Gate | Block and the one move | Conventional line (removed) | Cost added ⚠ | Cumulative ⚠ | Remaining of ⚠ 8.00 | Floor ⚠ | FMOS worst corner (0.90 · 0.95 · 1.00; from C6: band low · set price · band high) | Verdict |
|---|---|---|---|---|---|---|---|---|
| C3 (F1 close, baseline) | — | — | — | — | 8.00 | 54–106 | — · 34.4% · — | PROVISIONAL |
| C4 | credibility gap → the limit as its own verifiable history, placed at the shortfall (CP-2) | R4 2–8, marketing and outreach | 0.03–0.20 | 0.03–0.20 | 7.80 | 54.03–106.20 | 27.1% · 34.2% · 41.2% | **PROVISIONAL** |
| C5 | routine disruption the C1 form itself introduced (the draw as a customer act at a cue with no act) → default funding on an accepted term (WP-2 amended; draw ahead retained; switch-off) | R5 1–2, onboarding, help content, a support line | 0.02–0.06 | 0.05–0.26 | 7.74 | 54.04–106.26 | 27.0% · 34.1% · 41.2% | PROVISIONAL |
| C6 | timing mismatch the conventional form pays for (the calendar debit; the fee as a lump) → the charge as the first slice of the receipts share — 14.0% simple a year on the daily drawn balance, no fee, no charging date (PC-1 resolved; WP-3 amended) | R6 nil — nothing removed | 0.00–0.01 | 0.05–0.27 | 7.73 | 54.04–106.27 | 27.0% (135) · **31.7% (140, the set price)** · 34.1% (142.5) | **PROVISIONAL** |
| C7 | the access block — the limit absent from the seat where a connected customer's shortfall is first foreseen (the platform's cash forecast) → the released limit published as the account's pre-agreed credit line by the public account-information standard, receipt splits as transaction lines (PP-1; no fee, no agreement) | R7 6–35, partner fees, integration and partner management | 0.00–0.01 | 0.05–0.28 | 7.72 | 54.04–106.28 | 27.0% (135) · **31.7% (140, the set price)** · 34.1% (142.5) | **PROVISIONAL** |

| Requirement | Sub-requirements | CTM | AOM | FIT | Verdict |
|---|---|---|---|---|---|
| R4 — customers' want block (v1, closed 21 Sep 2026) | SR1–SR5 filled; three beliefs named; the key efficacy doubt = a credibility gap (a bank's number is not money until a person has decided); Attraction ToC on Milgrom 1981 and Hoch and Deighton 1989; mutation gate A adopted, B–F rejected by name; category entry point = the shortfall | v4 written (Phase 1 Conviction; CP-2; the conduct row; six traceability rows) | v4 written (Selling stream 3f; capacity 19,500 h per cell, 13 handlers band 12–14; productive hours band 1,400–1,600; floor 54.03–106.20) | fit model at-C4 written; surplus fraction as a band 0.90–1.00 (F-1 closed); **script REFUSED** (seal awaited) — by hand 27.1% / 34.2% / 41.2% worst, 427.5% best at the convention; PASS ≥ 25% at every point of the band; loss gate 4.2% / 4.8% / 5.4% | **PROVISIONAL** — cannot exceed R1–R3's; one FAIL row (the account line's unpaid-item fees foregone, ⚠ £0.9–24m a year) disposed as a mode-3 standing constraint and an input to C6 by number |
| R5 — customers' use block (v1, closed 21 Sep 2026) | SR1–SR5 filled; eight-step use routine; the Key Learning Block = routine disruption at step 5 (the draw) and step 3 (notice) — created by the C1 form, not by the market; Adoption ToC on Madrian and Shea 2001 and Wood and Neal 2007 (contrast Carroll et al. 2009; robustness Jachimowicz et al. 2019); mutation gate A adopted (default funding), B–F rejected by name; incumbent test read on the cumulative form (a WS1 question) | v5 written (Phase 2 Activation; WP-2 v2; acceptance, draw-ahead, switch-off, reversal, notice rows; the loss-gap reading; the arranged-not-unarranged desk position) | v5 written (Using stream 3g; e.funded_event, e.funding_query, e.term_drafting; cell at 14 handlers, 20,400 h; floor 54.04–106.26) | fit model at-C5; verifier r5 — PASS at 34.1% on the convention (`fit_margin.py` run after the seal), 27.0% at the band's low end; cap line 0.05–0.26 of 8.00 | PROVISIONAL |
| R6 — customers' buy block (v1, closed 21 Sep 2026) | SR1–SR5 filled; two interim-value lifecycles (the customer, six stages; the account line, four) with inline diagrams; Critical Value Threshold per party (acceptance for the migrated customer, the first funded-event notice for the never-borrowed, Stage 2 opening for the bank); buy block type = timing mismatch (lumpiness secondary), not price sensitivity; Amortisation ToC on Prelec and Loewenstein 1998 (contrast Gourville and Soman 1998; robustness Thaler 1985, Soman 2001); mutation gate A adopted, B–E rejected by name; payment trigger = the receipt; price 14.0% (band ⚠ 13.5–14.25%) with three fixed points (150 ceiling, 132.84 bar, 14.54% lowest published EAR); representative APR ⚠ 14.0–14.9%; gateway partner = the account line (internal); R3 flagged and its model updated (receivable cycle ⚠ 1–3 days) | v6 written: PC-1 resolved; WP-3 v2; CP-1 v5; five Phase 3 rows; four track rows; six traceability rows | v6 written: five events; the accrual and split rows; charge queries inside the C5 headroom; floor 54.04–106.27 | PASS 31.7% at the set price (`fit_margin.py`, 31 checks); 27.0–34.1% across the band by hand; best corner 159.1% at the set price by hand (the script's 417.9% is a band artefact, recorded); loss gate 4.57% at the set price; `check_verdict_order.py` IN ORDER with R6 | **PROVISIONAL** — object-after to 23 September 2026 17:00 |
| R7 — partner (access) block (v1, closed 21 Sep 2026) | SR1–SR5 filled; two access routines (connected ⚠ 45–70%, unconnected); affordability screen before any candidate (7.15 above the operating bar at the central corner, 0 at the pessimistic; paid 0); existence test on the class, not a name; eight candidates by loss and gain side (VA-147), the class of account-information readers present collectively (VA-155 third case), aggregate form (VA-165); coordination ToC on Farrell and Saloner 1985 (contrast Christensen and Raynor 2003; customer side Sharp 2010); mutation gate A adopted, B–E rejected by name; hypothesis ≥ 2 of 3 largest platforms display the line at the first replica's six months (G15); desk position: account information under PSRs 2017 reg 69, not a CONC 3 promotion; four unattended calls a day (SCA-RTS art 36(5)) | v7 written (PP-1; partner track with six holder rows; five traceability rows; no flag remains — F2 complete in the map) | v7 written (Selling stream 3h — access; `e.balance_call`, `e.display_query`, `e.conformance_test`, `e.field_build`, `e.field_position`; SC total ⚠ £0.72–12.25m; computing 2.02–5.11; floor 54.04–106.28) | fit model at-C7 written; **script PASS 31.7%** at the worst corner, 31 checks pass; verdict record R7 IN ORDER; TAM v3 valid with three declared warnings | **PROVISIONAL** (capped by VA-95: the model files are a carried build item); by hand 27.0 / 31.7 / 34.1; best corner at the set price 159.1 |
| **F2 gate** (21 Sep 2026) | consistency audit: **PASS WITH CONDITIONS** (0 hard, 3 soft — S1 the published line on a switched-off account; S2 the C5 headroom reused as a recurring line; S3 two presentations of "available"; one condition — the room above the operating bar is 7.15 at the central corner and 0 at the pessimistic, and every F2 cost sits inside it) · verification: **93.1 SOUND**, validation-maturity pre-operational (completeness 90.0 · consistency 85 · discipline 97.4 · synthesis 100); registry 81 rows by this count — 59 applied, 17 not applicable, 5 lacking the element; seven faults, none needing Tom | `../bank-credit-facility-consistency-audit-F2-2026-09-21.md` | `../bank-credit-facility-verify-F2-2026-09-21.md` | — | verdict record: F2 reads PROVISIONAL at R7 (VA-95) | **PASSED — proceed to C8** with the F1 and F2 conditions carried as critical assumptions |

**F2 files (as written).**
- **C4 record: `../bank-credit-facility-c4-v1-2026-09-21.md`**
- CTM v4: `bank-credit-facility-ctm-v4-2026-09-21.md`
- AOM v4: `bank-credit-facility-aom-v4-2026-09-21.md`
- Fit model at C4: `bank-credit-facility-fit-model-at-C4.yaml`
- Verifier r4: `bank-credit-facility-fit-verifier-r4-2026-09-21.md`
- **C5 record: `../bank-credit-facility-c5-v1-2026-09-21.md`** (v1.1)
- CTM v5: `bank-credit-facility-ctm-v5-2026-09-21.md`
- AOM v5: `bank-credit-facility-aom-v5-2026-09-21.md`
- Fit model at C5: `bank-credit-facility-fit-model-at-C5.yaml`
- Verifier r5: `bank-credit-facility-fit-verifier-r5-2026-09-21.md`
- **C6 record: `../bank-credit-facility-c6-v1-2026-09-21.md`**
- CTM v6: `bank-credit-facility-ctm-v6-2026-09-21.md`
- AOM v6: `bank-credit-facility-aom-v6-2026-09-21.md`
- Fit model at C6: `bank-credit-facility-fit-model-at-C6.yaml`
- Verifier r6: `bank-credit-facility-fit-verifier-r6-2026-09-21.md`
- **C7 record: `../bank-credit-facility-c7-v1-2026-09-21.md`**
- CTM v7: `bank-credit-facility-ctm-v7-2026-09-21.md`
- AOM v7: `bank-credit-facility-aom-v7-2026-09-21.md`
- Fit model at C7: `bank-credit-facility-fit-model-at-C7.yaml`
- Verifier r7: `bank-credit-facility-fit-verifier-r7-2026-09-21.md`
- Verdict record (for `check_verdict_order.py`, R1–R7): `bank-credit-facility-verdict-record.yaml`
- TAM data object, version 3 at C7 (narrowed by the named block "price"; `validate_tam_model.py` valid with three declared warnings): `bank-credit-facility-tam-model.yaml` (version 2 kept as `bank-credit-facility-tam-model-v2-at-C2.yaml.bak`)
- Consistency audit F2: `../bank-credit-facility-consistency-audit-F2-2026-09-21.md`
- Verification F2: `../bank-credit-facility-verify-F2-2026-09-21.md`

## Function 3 — the store of value, the lock-out and the supplier hold (C8–C10)

**What F3 must do (Tom, 16 September 2026):** R8–R10 make the at-scale price and cost hold. Price is set at C6 (£140 per £1,000 drawn a year; band ⚠ 135–142.5) and F3 does not reprice. R10 is what the venture can replace if a supplier turns adversarial; cost-shifting is not architecture. Each F3 record carries a barrier score (SCIS at C8, FIS at C9, HRS at C10 — pass ≥ 5, NCR ≤ 3) and a position-holding table re-tested at every failure value.

| Gate | Block and the one move | Conventional line (removed) | Cost added ⚠ | Cumulative ⚠ | Remaining of ⚠ 8.00 | Floor ⚠ | FMOS worst corner (135 · 140 set · 142.5) | Barrier score (conservative · central · optimistic) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| C7 (F2 close, baseline) | — | — | — | 0.05–0.28 | 7.72 | 54.04–106.28 | 27.0% · 31.7% · 34.1% | — | PROVISIONAL |
| C8 | the C7 openness itself — a published limit is a reconstructible one → the seasoned limit: the multiple rises on the account's own cleared events (WP-1 v2); the store is the record, which the customer owns and exports | R8 5–15, loyalty pricing, exit fees, product tie-ins, a retention desk | 1.00 rounded (0.45–1.50) | 1.05–1.28 (0.50–1.78) | 6.72 | 55.04–107.28 | 25.8% · 30.5% · 32.8% | SCIS 2 · 4 · 6 — **below the line at the conservative corner; design finding, not softened** | PROVISIONAL |
| C9 | a rival who copies the rule gets the same parameters → the outcome ledger and a yearly re-fit on it (parameter, not rule); the outcome column is not in any consented feed | R9 0 — a bureau licence, a scorecard vendor, a data-science hire: the rule never carried an external score | 0.01–0.03 | 1.05–1.29 (0.51–1.81) | 6.71 | 55.04–107.29 | 25.8% · 30.5% · 32.8% | FIS 5 · 6 · 7 | PROVISIONAL |
| C10 | funding is the largest floor line and its supplier is treasury → PC-2, the levelled-line funding: the pool's drawn balances funded by the pool's own credit balances under a signed term at the measured deposit cost, read daily; cap ⚠ 10% of pool balances; standby revolving master trust on the R9 ledger, set up before Stage 3, never issued | R10 1–3, the bureau, scoring and aggregator feeds a conventional line buys | 0.05–0.18 (0.09–0.36) | **1.10–1.47 (0.60–2.17)** | **6.53** | **55.09–107.47** | **25.6% · 30.3% · 32.6%** | HRS 4 → 5 with the design commitment · 6 · 6 | **PROVISIONAL — F3 closes** |

| Requirement | Sub-requirements | CTM | AOM | FIT | Verdict |
|---|---|---|---|---|---|
| R8 — store of value (v1, closed 21 Sep 2026) | SR1–SR5 filled; the cleared event (⚠ 90-day cut) and the seasoned multiple; customer-ownership test passed; ToC on Sharpe 1990 (contrast Rajan 1992); mutation gate A of five; the uplift lands in the undrawn commitment (IC 13–18), not the drawn book; seasoning-query rate ⚠ 0.5–1.5% books the 15th handler at the high corner (closes F2 audit S2) | v8 written (WP-1 v2; seasoning as a published parameter; down-seasoning symmetrical in what it counts) | v8 written (seasoning input in the engine; IC 13–18; floor 55.04–107.28) | script PASS 30.5% at the set price (`fit_margin.py`); 25.8–32.8% by hand; loss gate 4.47% | PROVISIONAL (VA-95) |
| R9 — lock-out (v1, closed 21 Sep 2026) | SR1–SR5 filled; the outcome column (the multiple in force, cleared-or-lost) as the asset stock; replication lag ⚠ 27–54 months; ToC on Dierickx and Cool 1989 and Arrow 1962 (contrast Barney 1991); yearly re-fit, held-out cohort, cohort minimum ⚠ 500 rows (G17); compute ⚠ £5–30k a run; ledger pseudonymised (UK GDPR Art 4(5), Recital 26); FIS 5 · 6 · 7 | v9 written (the ledger and the calibration run; the exception desk answers the schedule question) | v9 written (floor 55.04–107.29) | script PASS 30.4% (30.5% by hand at 140); loss gate 4.47% unchanged; position-holding re-test: without the calibration the design is BORDERLINE at 140, FAIL at 135 | PROVISIONAL (VA-95) |
| R10 — supplier hold (v1 with same-day correction, closed 21 Sep 2026) | SR1–SR5 filled; funding as the key input (⚠ 1.5–3.0% deposit cost, the largest floor line); ToC on Klein, Crawford and Alchian 1978 and Drechsler, Savov and Schnabl 2017 (contrasts Williamson 1985; Diamond and Dybvig 1983); PC-2 with mutation gate A of six; the at-scale test — cap used ⚠ 3.4–11.4%, binds only at the worst corner of the pool (⚠ £5.0bn against £5.7bn, a 12% cut, a volume effect); HRS 4 without the commitment / 5 with it / 6 / 6; existence test — the route agents are commodity vendors, upkeep ⚠ £0.3–0.6m a year, set-up one-off ⚠ £1.84–15.59m; **the funding gate first printed as 3.99% did not reproduce and was corrected to 3.45% the same day (changelog row)** | v10 written (treasury track, six states: the daily price, the cap reading, the tape cut, the trigger review, the route's upkeep and set-up) | v10 written (§3k; RC +0.05–0.18; SC +0.04–0.18 unrounded; floor 55.09–107.47) | script PASS 30.2% at 139.95, 30.3% by hand at 140; 25.6–32.6% across the band; best 154.1% at the set price; bar 134.34, room 5.66; loss gate 4.45% (4.05 at 135; zero margin 7.25%); funding gate 3.45% (3.05–3.65 across the band; zero margin 6.25%); position-holding re-test: at Bank Rate BORDERLINE (19.2% / 14.9%), at the market FAIL (13.4% / 9.3%; 9.8% / 5.9%) — printed unsoftened, carried as a design finding | **PROVISIONAL — F3 closes PROVISIONAL** |
| **F3 gate** (21 Sep 2026) | consistency audit C10 (whole architecture C1–C10): **COHERES — one route-back, four soft items, one condition.** H1 (hard, of number): the C3 trial band's continue line ⚠ 4.8% is above the 4.45% gate at the C10 floor (21.2% at 4.8) — routed back to the C3 record for re-setting (continue ≤ ⚠ 4.45 at the set price; borderline 4.45–5.0; kill > ⚠ 5.0 unchanged), not patched. **H1 closed 21 Sep 2026:** C3 record v2, CTM v10.1 release-track row and this file carry the C10 value. **S1, S2, S4 closed 21 Sep 2026:** S1 the funding gate added as a quarterly reading (CTM v10.1 treasury track); S2 the ⚠ 1.06 named as a reserve against the assumed people count (AOM v10.1 RC row); S4 the C10 spread count re-stated on the AOM v10 fixed layer (Stage 1 2.8% at the set price; simulation −1.2%). S3 stands as a named tension, no change by design. S1 the funding gate absent from the quarterly sitting; S2 the recurring fixed layer carried ⚠ 1.06 per £1,000 above the activities (RD-031); S3 the R7–R8 tension resolved at R9; S4 two Stage 1 figures. Moat test PASS — every VA-106 line names ≥ 2 other requirements (counts 4, 3, 4, 6, 5, 6, 7, 5, 4, 5); the moat is R9 + R10 with R8 as the store they protect; SCIS 2 named as the weak barrier. Analogue for the whole architecture: Square Financial Services (Block's Utah industrial bank, 2021) funding Square Loans beside the sellers' deposits — stops at the cap and the standby route, and Square is the acquirer not the account holder · verification: **87.7 SOUND**, validation-maturity pre-operational (completeness 90.0 · consistency 65 · discipline 95.8 · synthesis 100); registry 81 rows — 61 applied, 15 not applicable, 5 lacking the element; ten faults, none needing Tom; three premature details (the 90-day cut, the yearly run, the before-Stage-3 date) to recast as convergence items | `../bank-credit-facility-consistency-audit-C10-2026-09-21.md` | `../bank-credit-facility-verify-C10-2026-09-21.md` | verdict record R1–R10 IN ORDER (`check_verdict_order.py`, ten checks; the script reads no F3 gate) | **F3 CLOSED PROVISIONAL** — the ten requirements are designed; the next event that moves any verdict is a measurement (Stage 0's back-test) |

### The Phase II capital gate — the financial simulation at C10

`bank_credit_facility_fin_sim.py` → `bank-credit-facility-fin-sim-outputs.json` → `../bank-credit-facility-fin-sim-2026-09-21.md`. At-scale and scaling-stage models separated; every one of the twelve C10 figures reproduced; no point estimates.

| Reading | Conservative | Central | Optimistic |
|---|---|---|---|
| At-scale book (drawn) | ⚠ £3.4bn | ⚠ £4.55bn | ⚠ £5.7bn |
| Floor per £1,000 drawn a year | 107.47 | 81.28 | 55.09 |
| Margin at the set price (140) | **30.3% — PASS ≥ 25**; Phase II gate **BORDERLINE** against 60% (−29.7 points) | 72.2% — PASS | 154.1% — PASS |
| Loss rate at which the 25% margin fails (at 140) | 4.45% (4.05 at 135; 4.65 at 142.5); zero margin 7.25% | — | — |
| Loss rate at which the Phase II gate (60%) passes at the conservative corner | ⚠ 2.00% (the band's low end) alone; or funding 1.5% with loss ⚠ 2.6%; funding 1.5% alone gives 51.4% | — | — |
| Peak venture capital on the path (deepest operating deficit + overlay held) | ⚠ £50.0m at month 13 (the replica overlay, held six months; the largest cash shortfall is £1.8m at month 1, £1.3m of it Stage 0; operating cash positive from month 6) | ⚠ £25.0m at month 13 | ⚠ £0.5m at month −1 |
| Lending capital at scale (funding, not venture capital; 75% RW × 12% × (drawn + 10% undrawn)) | ⚠ £0.36–0.70bn (the AOM's ⚠ £0.31–0.56bn is the two-replica figure) | | |
| At scale reached (month) | 43 | 35 | 27 |
| Cumulative operating cash at month 60 | ⚠ £1,098.9m | ⚠ £1,341.2m | ⚠ £1,420.8m |
| Stage 1 margin on its own book (below the gate at every corner; the release order carries it) | −1.2% (the record's 4.0% on ⚠ £12.95m of people; the simulation on ⚠ £13.55m with the seasoning call — audit S4) | 59.6% | 142.6% |
| Cap at the worst corner of the pool | drawn ⚠ £5.0bn against ⚠ £5.7bn — a 12% cut; net contribution still ≈ 3.7× the PCO's required profit (£29.7m at year five) | not binding | not binding |

**Phase II gate verdict:** BORDERLINE at the conservative scenario (30.3% against 60%; band 25.6–32.6% across the price band); PASS at central and optimistic. **Binding input:** the loss rate on the flow-underwritten pool (⚠ 2–4%; every point moves the floor high by 10); second input the measured deposit cost (⚠ 1.5–3.0%; gate 3.45%). **What tightens the gate:** the loss band moving to its low end at Stage 0's back-test, or the deposit cost reading at the band's low end under the signed term. The kill line (5.0%) reads BORDERLINE on the 25% gate at 140 and FAIL at 135; the C3 continue line (4.8%) reads BORDERLINE — the H1 route-back above.

### The business case — the two files a reader in another company receives (22 September 2026)

Built to `Forge/WS1/business-case-standard.md` v0.3 from one model data file, under the model data file specification v1.2 (the `book` block added for this run: the balance each transaction carries and the share of it the venture funds with capital). Runner-drafted; **object-after Tom by 24 September 2026 17:00**. The bank is not named in any of the three; every bank-held figure is a ⚠ band.

| File | Digest (first 13) | What it is |
|---|---|---|
| `sme-fintech-models/bank-credit-facility-model.yaml` | `c48405f480fb1` | the model data file — every load-bearing input a band with its source and tier; one transaction = £1,000 of drawn balance for one month; one operating unit = one exception cell; head office = the bank's own teams at no margin |
| `sme-fintech-models/bank-credit-facility-business-case-evidence.xlsx` | `d376d0f879421` | the evidence workbook — tabs 1–12 the IFC model, 13–14 the year-one sales and cash flow with the 10% stress, 15–18 the five-year roll-out, profit and loss, cash flow and balance sheet (loans to customers, deposits and the capital held against the book carried), 19 the checks. Recalculated independently: ALL CHECKS PASS; the balance sheet balances in all five years; 146 named cells agree with the model |
| `sme-fintech-models/bank-credit-facility-business-case-evidence-cells.md` | `e888a69896aeb` | the cell index — every name the document cites |
| `../bank-credit-facility-business-case.html` | f06784a673a05 (v1.0, 22 September 2026; cite checker and house-style checker both clean) | the business case document — seven sections in the GOV.UK order, summary panel first, appendix "Where each number lives" |

**Reconciliation to the simulation above (base scenario against the central corner):**

| Reading | Workbook, scenario 1 | Simulation, central | Difference and its cause |
|---|---|---|---|
| Cost floor per £1,000 drawn a year | £84.60 (7.05 a month × 12) | £81.28 | +£3.32: the workbook charges corporation tax at 25% on the return required on the capital held against the book (£3.87 per £1,000 a year); the simulation applied the 12–15% cost of equity with no tax on it. Before that tax the workbook's floor is £80.72 — within £1 of the simulation |
| Margin at the set price | 65.5% (73.4% before the tax on the return) | 72.2% | the same cause |
| Worst corner | 14.5% — every banded input at its adverse end at once, **including the price at £135**, the accounts with no flow at 25%, the balances at £15k, the one-offs spread over 36 months and the reserve in full | 30.3% conservative at £140 (25.6% at £135) | a stricter definition: the simulation's conservative corner moves the cost lines and the book, not the price, the flow coverage or the spreading period |
| Binding input | the expected credit loss on the drawn balance (a move to 4% takes the margin to 48.0%) | the loss rate (gate 4.45%) | the same input |
| Cash the venture needs in year one | £3.7m base, £4.8m under the 10% stress; £5m equity set in year one | £1.8m largest shortfall at month 1 (central) | the workbook pays the one-offs in month one in full (£8.76m including the ⚠ £5.2m carrying cost of the pool overlays, held as a charge); the simulation holds the overlays as capital and spreads the one-offs |
| Profit after tax, years one to five | £43.5m · £234.2m · £258.2m · £258.2m · £258.2m; cash at year five £1,143m, retained | cumulative operating cash at month 60 ⚠ £1,341m | the P&L charges tax and the one-offs; the simulation's figure is before tax |

**A reading for Tom to rule — the tax on the return on capital.** The workbook's rule (finance standard: tax on the investment return) is right if the 12–15% cost of equity is an after-tax target, which is how a bank states its return on tangible equity. On that reading the design record's margins are about five points too high: conservative 30.3% → 25.0% (the tax adds 4.50 to the floor: 111.97; exactly on the 25% gate), central 72.2% → 64.4%, optimistic 154.1% → 140.0%. The price stays £140; the verdicts at central and optimistic stay PASS; the conservative reading moves from 5.3 points above the 25% gate to the line, and the Phase II reading stays BORDERLINE. Derived, not a new commitment — object-after with the files.

### Cost progression C3 → R10 (the floor's high corner, per £1,000 drawn a year)

| Point | Floor ⚠ | Added at the high corner | Cumulative R4–R10 | Remaining of ⚠ 8.00 | Margin at 140, worst corner |
|---|---|---|---|---|---|
| C3 (F1 close) | 54–106 | — | — | 8.00 | 34.4% (at the convention) |
| C4 | 54.03–106.20 | 0.20 | 0.20 | 7.80 | 34.2% |
| C5 | 54.04–106.26 | 0.06 | 0.26 | 7.74 | 34.1% |
| C6 (price set at 140) | 54.04–106.27 | 0.01 | 0.27 | 7.73 | 31.7% |
| C7 (F2 close) | 54.04–106.28 | 0.01 | 0.28 | 7.72 | 31.7% |
| C8 | 55.04–107.28 | 1.00 | 1.28 | 6.72 | 30.5% |
| C9 | 55.04–107.29 | 0.01 | 1.29 | 6.71 | 30.5% |
| **C10 (F3 close)** | **55.09–107.47** | **0.18** | **1.47** | **6.53** | **30.3%** |

Seven requirements added ⚠ 1.47 of the ⚠ 8.00 the counterfactual allows at the high corner (0.60–2.17 unrounded) and removed conventional lines that sum to ⚠ 15–63. The margin fell 4.1 points from C3, of which 2.7 were the price set below the C2 ceiling at C6 and 1.4 the F2–F3 costs.

**F3 files (as written).**
- **C8 record: `../bank-credit-facility-c8-v1-2026-09-21.md`**
- CTM v8: `bank-credit-facility-ctm-v8-2026-09-21.md` · AOM v8: `bank-credit-facility-aom-v8-2026-09-21.md` · fit model at C8: `bank-credit-facility-fit-model-at-C8.yaml` · verifier r8: `bank-credit-facility-fit-verifier-r8-2026-09-21.md`
- **C9 record: `../bank-credit-facility-c9-v1-2026-09-21.md`**
- CTM v9: `bank-credit-facility-ctm-v9-2026-09-21.md` · AOM v9: `bank-credit-facility-aom-v9-2026-09-21.md` · fit model at C9: `bank-credit-facility-fit-model-at-C9.yaml` · verifier r9: `bank-credit-facility-fit-verifier-r9-2026-09-21.md`
- **C10 record: `../bank-credit-facility-c10-v1-2026-09-21.md`** (v1 with the funding-gate correction and the function-gate re-run rows in the changelog)
- CTM v10: `bank-credit-facility-ctm-v10-2026-09-21.md` · AOM v10: `bank-credit-facility-aom-v10-2026-09-21.md` · fit model at C10: `bank-credit-facility-fit-model-at-C10.yaml` · verifier r10: `bank-credit-facility-fit-verifier-r10-2026-09-21.md`
- Verdict record R1–R10: `bank-credit-facility-verdict-record.yaml`
- TAM data object, version 4 at C10 (gate G-C10-1, the cap — a volume gate that excludes no class; valid with three declared warnings): `bank-credit-facility-tam-model.yaml` (version 3 kept as `bank-credit-facility-tam-model-v3-at-C7.yaml.bak`)
- Financial simulation: `bank_credit_facility_fin_sim.py` · `bank-credit-facility-fin-sim-outputs.json` · `../bank-credit-facility-fin-sim-2026-09-21.md`
- Consistency audit C10: `../bank-credit-facility-consistency-audit-C10-2026-09-21.md`
- Verification C10: `../bank-credit-facility-verify-C10-2026-09-21.md`
- Architecture summary for Tom: `../bank-credit-facility-architecture-summary-2026-09-21.md`

**House-style checker (`.scripts/check-house-style.py`), run 21 September 2026:** C8, C9, C10 records, verifiers r8–r10, fin-sim document, consistency audit C10, verification C10, this file, the architecture summary — all ✅ clean (sentence-length warnings only, which do not fail).

## The answer in mode 3

**Could the bank adopt this without changing its architecture?** No. The bank's roadmap (pre-approved limits at scale, digital fulfilment, extension to new joiners — insider-confirmed 18 September 2026) already makes the decision cheap. The seed removes what the roadmap leaves standing: the fixed, secured, scheduled exposure, and with it security, annual review and collections; it replaces a fixed exposure held against a balance sheet with a variable exposure that follows the flow and repays from receipts. Risk governance, the people employed, the risk object and the object sold all change. **A new form is required: venture, not improvement.** The honest tension: the bank could build the limit engine as a feature behind its pre-assessed limit; it could not run it as the form without removing the operations above.

**At F1 close.** Floor ⚠ 54–106 per £1,000 drawn a year, complete on four layers; the selected customer's ceiling ⚠ 150–300 clears it by 34.4 per cent at the worst corner. The scaling path adds ⚠ 0–1 to the floor because the first release is against exposure the bank already carries: no whole-book overlay, no forward cohorts. Peak overlay ⚠ £0–50m; ⚠ 27–42 months to at-scale; lending capital for the replicas ⚠ £0.31–0.56bn, about 1–3 per cent of a large UK bank's CET1.

**At F2 close.** Floor ⚠ 54.04–106.28 per £1,000 drawn a year. The four customer-facing and partner requirements added ⚠ 0.05–0.28 of the ⚠ £8 the counterfactual allows, and removed conventional lines that sum to ⚠ 9–45. Price 14.0 per cent simple a year on the daily drawn balance (£140 per £1,000 drawn; band ⚠ 135–142.5), no fee, collected as the first slice of each receipts share; 31.7 per cent above the floor at the worst corner. The loss gate at the set price is 4.57 per cent. Nothing in R4–R7 has a partner fee, a marketing budget, an onboarding line or a charging date; the four blocks were removed by the form, not paid for.

**At F3 close.** Floor ⚠ 55.09–107.47 per £1,000 drawn a year. The three barrier requirements added ⚠ 1.10–1.47 of the ⚠ 8.00 (6.53 remains) and removed conventional lines of ⚠ 6–18. Price unchanged at 140; 30.3 per cent above the floor at the worst corner, 25.6 at the band's low end. The moat is not a switching cost (SCIS 2 at the conservative corner, by design — R7 published the limit): it is the outcome ledger and the parameters fitted on it (R9), which no consented feed carries and which a rival needs ⚠ 27–54 months to match, and the deposit franchise (R10), which no rival without a current-account pool can price against. The two largest lines of the floor — the loss (gate 4.45%) and the funding (gate 3.45%) — each hold on one of those two requirements, and neither is measured. The Phase II capital gate reads BORDERLINE at the conservative scenario until Stage 0's back-test moves the loss band.

**The C1 number, reported and not gating.** Floor ⚠ 54–105 per £1,000 drawn a year against a price paid today of ⚠ 75–120 and a roadmap-form floor of ⚠ 57–133: the fixed-per-facility delivering lines fall ⚠ 75–80%, expected loss and undrawn capital rise, the net floor falls ⚠ 5–21%. The first thing the insider corrects is the loss rate on a flow-underwritten pool; at 4.8% the central margin is zero.

## Open items, by owner

| Item | Owner | Convergence |
|---|---|---|
| PCO — ratified by lapse 20 September 2026 17:00 | closed | — |
| Toolchain seal — **closed 21 September 2026 19:49** (re-sealed, not by the runner). `fit_margin.py` re-run on the C3, C4 and C5 fit models: 34.4% · 34.2% · 34.1%, matching the hand figures in r3, r4 and r5. `check_verdict_order.py` on the verdict record: IN ORDER. `fit_margin.py` on the C6 and C7 fit models: 31.7% · 31.7%, matching r6 and r7. `validate_tam_model.py` on the TAM data object version 3: valid with three declared warnings (two L4 vocabulary, one L7 incidence basis). | closed | — |
| **Business case — model data file, evidence workbook, cell index, document (22 September 2026) — object-after** | Tom | 24 September 2026 17:00 |
| Tax on the return on the capital held against the book — after-tax cost of equity (workbook, margins five points lower) or pre-tax (simulation) | Tom | a ruling; the price and the central/optimistic verdicts do not move either way |
| C2 record, TAM v2, CTM v2, AOM v2, fit model, verifier r2 — object-after | Tom | 23 September 2026 17:00 (48 hours from filing) |
| **C3 record, CTM v3, AOM v3, fit model at C3, verifier r3, consistency audit F1, verification F1, counterfactual — object-after** | Tom | 23 September 2026 17:00 |
| Depth of readable transaction history for the back-test (assumed ⚠ 3–5 years; MLR retention sets the ceiling) | the insider | the years the data platform holds per account |
| Share of migrated accounts whose rule limit is at or below the existing overdraft limit (assumed ⚠ 50–80%) | the back-test (Stage 0) | the back-test output |
| Overlay share finance and the auditor require on the unproven model (assumed ⚠ 0–25% on Stage 1) | finance and the external auditor | their view before Stage 1 release |
| Lending capital headroom for the replicas (⚠ £0.31–0.56bn) against the bank's own plan | treasury and ALCO | the capital plan |
| Trial and replica bands (continue ≤ ⚠ 4.45% at the set price of £140, 4.05% at ⚠ £135; borderline 4.45–5.0%; kill > 5.0%; replica = trial ± 1 point, provisional — re-set at the C10 floor per H1, C3 record v2) | the board risk committee | pre-registration before Stage 1; the 12-month and 6-month readings |
| F1 condition: Stage 2 opens within ⚠ 24 months of Stage 1, or the capital bar is re-driven on the Stage 1 book | the runner, at the C3 record's next regeneration | a dated line in the capital path |
| Share of the bank's overdraft accounts on the standard tariff at ≥ 15% EAR all-in (assumed ⚠ 40–70%) | the insider | the count by tariff band |
| Tariff revenue on the migrated pool against Reading D (VA-147) | the insider | the bank's overdraft revenue by tariff band and its attrition to non-bank lenders |
| Loss rate on the flow-underwritten pool | the insider | the bank's loss by account-conduct band; pivot trigger > ⚠ 5% |
| Size and loss of the flow-eligible pool with no facility today (SC-DETERRED and SC-OWNER-FUNDED in the TAM data object — recorded, unpriced; Tom, 22 September 2026: the opportunity cost of not getting capital is their KMC) — count accounts with ≥ ⚠ 6 months of flow, a shortfall history and no facility, and read their clearance rate against the tariff pool's | the Stage 0 back-test (no customer, no cost beyond the run) | the count and the two clearance rates; a second selected customer with a priced ceiling if the loss sits inside the band |
| Share of accounts with ≥ ⚠ 6 months of flow here or at a previous mandated provider | the insider | the count by account age and monthly receipts; switchers' history via open banking |
| Every ⚠ cost line | the insider | the bank's cost by function |
| Customer acceptance of migration and the receipts share | the insider (a pilot cohort — no fieldwork by the venture) | decline share; trigger > ⚠ 30% |
| CTM and AOM model files, script runs | Venture Architect seat, if the run proceeds | coverage script passes before C4 |
| Verification faults F-1 and F-2 — **closed at C4**: the surplus fraction is a band ⚠ 0.90–1.00 (fit model at C4) and the productive hours a band ⚠ 1,400–1,600 with ONS and WTR sources (AOM v4 section 0) | closed | — |
| **C4 record, CTM v4, AOM v4, fit model at C4, verifier r4 — object-after** | Tom | 23 September 2026 17:00 |
| **C5 record (v1.1), CTM v5, AOM v5, fit model at C5, verifier r5, verdict record — object-after** | Tom | 23 September 2026 17:00 |
| **C6 record, CTM v6, AOM v6, fit model at C6, verifier r6, verdict record (R6) — object-after** | Tom | 23 September 2026 17:00 |
| **C7 record, CTM v7, AOM v7, fit model at C7, verifier r7, verdict record (R7), TAM version 3, consistency audit F2, verification F2 — object-after** | Tom | 23 September 2026 17:00 |
| Loss gap between the default-funded pool and the drawn-ahead pool (hypothesis ⚠ ≤1 point; above it default funding falls to opt-in by flow band) | the Stage 1 reading (model risk) | the two pools' loss rates at twelve months |
| Switch-off share (⚠ ≤10%; falsified above 25%) and reversal-within-three-days share (⚠ ≤5%; falsified above 15%) at ⚠ 10,000 accounts | the Stage 1 reading | the account line's counts |
| Funding-query rate (⚠ 0.05–0.2% of funded events; threshold 0.5%, above which the cell needs a 15th handler) | the first replica at six months | the cell's query log |
| Channel mix of payments that exceed the balance (instant majority assumed; UK Finance 2025 for the market) | the Stage 0 back-test | the count by channel on the selected pool |
| Unpaid-item fees foregone — restated at C5 to ⚠ £3.6–45m a year; **priced at C6**: the default-funded book's contribution at the set price is ⚠ £5.7–74m a year — covers the fee at the central case, not at the pessimistic corner; inside the pricing-committee row, not recovered by the rate | the pricing committee; the insider for the count | the bank's unpaid-item fee income on the selected pool |
| CONC 5.2A creditworthiness assessment timing under default funding (design position: at acceptance, on the rule's limit; what a ruling would settle) | the bank's conduct function | the signed term |
| Unpaid-item fees the account line gives up when the limit covers a shortfall (⚠ £0.9–24m a year, VA-127 FAIL row at C4) — **superseded by the C5 restatement and the C6 pricing above** | closed into the row above | — |
| Share of released accounts with at least one shortfall in twelve months (assumed ⚠ 30–70%; below ⚠ 30% the placement reaches too few) | the Stage 0 back-test | the back-test count |
| Whether the limit amount alone is a financial promotion under CONC 3 (design position: no rate shown at C4, so no representative example under CONC 3.5.5R) — **the rate arrives at C6 and the representative example is drafted there** (⚠ 14.0–14.9% APR; the APR basis and whether the collection term is a "charge" are what a ruling would settle) | the bank's conduct function | the signed template and example |
| CCA form for a variable-repayment running account under £25,000, now including the modifying agreement at migration (s.82) | the bank's conduct function | a form of agreement signed off |
| The rate — 14.0% simple a year (band ⚠ 13.5–14.25%), a runner's call: threshold 13.28% (the 25% margin) and 14.5% (the lowest published EAR); decline share with "the rate" as reason > ⚠ 30% moves it toward the band's low end | the pricing committee | Stage 1 acceptance |
| Migrated book size and tariff mix — the pricing-committee row FAILS at the pessimistic corner (−£234m) and passes at the central (+£156m); force = the mode-3 decision and the pool at risk | the pricing committee; the insider | the bank's overdraft revenue by tariff band; the Stage 2 opening reading |
| Charge-query rate (⚠ 0.2–0.5% of drawn accounts; threshold 1.5%, above which the C5 headroom is used up) and the no-receipt accrued-charge count (⚠ ≤ 2%) | the first replica at six months; the stage reading | the cell's query log; the accrued-charge ledger by days outstanding |
| Receipts per active drawn account (⚠ 300 a year; sets the split's frequency only) | the account line | the bank's receipt counts |
| Fixed rate against a Bank Rate–linked rate — the funding line moves with Bank Rate; a carried question, not a structural item | the pricing committee | the first yearly review |
| TAM narrowing by the named block "price" — **done at C7**: version 3 excludes SC-OD-BELOW-BAND and SC-LOAN-USER by gate G-C6-1; surviving volume unchanged; pool at risk sized; `validate_tam_model.py` valid with three declared warnings (the L4 pair is a vocabulary gap for WS1: excluded by the venture's own price with a live comparison rate) | closed | — |
| Connected share of released accounts (assumed ⚠ 45–70%; below ⚠ 30% routine A reaches too few and R7 adds nothing) | the bank's account-information consent count | the count at Stage 1 |
| Platforms displaying the pre-agreed line (hypothesis ≥ 2 of 3 largest at the first replica's six months; falsified at 0 of 3) | the first replica at six months (G15) | the platforms' rendering, read by the account-information team |
| Display-query rate (⚠ 0.1–0.3% of connected drawn accounts a year; threshold 1%, above which the C5 headroom is used up) | the first replica at six months | the cell's query log |
| Conformance-test hours (⚠ 100–200 across six counterparties) and field build (⚠ 400–800 hours), field position (⚠ 40–80 hours) | the account-information team | the estimate before the build |
| Published line on a switched-off account (audit S1; switched-off share ⚠ ≤ 10%) — design position: publish, because the limit is drawable by draw ahead | the runner, at the C7 record's next regeneration; the account-information team | the display-query rate |
| C5 headroom (⚠ 0–425 hours a cell) restated as a first-year line and a recurring line (audit S2) | the runner, AOM v8 | the three query rates at the first replica's six months |
| Two presentations of "available" — the app's one figure against the feed's booked balance plus a credit line marked not included (audit S3) | the runner, at the C7 record's next regeneration; the conduct desk position | the platforms' rendering at the first replica |
| Verification faults F-5 and F-6 — the six-counterparty scope and `Included = false` fixed ahead of the evidence | the runner, at the C7 record's next regeneration | recast as convergence items |
| `fit_margin.py` best corner read over the whole ceiling band regardless of the set price (417.9% reported; 159.1% by hand at the set price) | Head of R&D (WS1) | a script change |
| **C8 record, CTM v8, AOM v8, fit model at C8, verifier r8, verdict record (R8) — object-after** | Tom | 23 September 2026 17:00 |
| **C9 record, CTM v9, AOM v9, fit model at C9, verifier r9, verdict record (R9) — object-after** | Tom | 23 September 2026 17:00 |
| **C10 record (with the same-day correction), CTM v10, AOM v10, fit model at C10, verifier r10, verdict record (R10), TAM version 4, financial simulation, consistency audit C10, verification C10, architecture summary — object-after** | Tom | 23 September 2026 17:00 |
| **H1 — the C3 trial band re-set** (continue ≤ ⚠ 4.45% at the set price, 4.05 at 135; borderline 4.45–5.0; kill > ⚠ 5.0 unchanged) — the F2 audit's remark, now a contradiction of number | the runner, at the C3 record's next regeneration; the CTM release track | the board risk committee's pre-registration before Stage 1 |
| Loss rate on the flow-underwritten pool (⚠ 2–4%; gate 4.45%; Phase II passes at ⚠ 2.0%) — the binding input of every verdict | Stage 0's back-test on the bank's own history; then the 12-month Stage 1 reading | the back-test output; the trial band's reading |
| Measured deposit cost under the funding term (⚠ 1.5–3.0%; gate 3.45%; failure values 4.0% at Bank Rate, 4.6–5.0% at the market) | treasury, at the term's signing; then the first year of daily readings | the transfer-pricing reading |
| Pool credit balances (⚠ £50–100bn) and the cap's use (⚠ 3.4–11.4%; binds only at ⚠ £5.7bn drawn against £50bn) | treasury and ALCO | the bank's balance sheet at the term's signing |
| The four-part design commitment at C10 (the tape cut monthly from Stage 1; the programme documents drafted before Stage 3; the agents named; the yearly refresh) — HRS 4 → 5 at the conservative corner rests on it | the treasury; the engine team for the tape | the first tape; the documents |
| Seasoning schedule (⚠ 8–24 months to each step) and the cleared-event cut (⚠ 90 days — verification F-6, to recast as a band) | Stage 0's back-test | the distribution of clearance times |
| Seasoning-query rate (⚠ 0.5–1.5% of drawn accounts a year; the 15th handler booked at the high corner) | the first replica at six months | the cell's query log |
| Undrawn commitment per £1 drawn (⚠ 1.9–3.6; IC 13–18) | the 12-month Stage 1 reading | the undrawn count |
| Calibration frequency (yearly — verification F-7, to recast as a band settled by the first held-out reading), cohort minimum (⚠ 500 rows), compute (⚠ £5–30k a run) | the runner at the C9 record's next regeneration; the engine team; the data platform | the first held-out reading; the platform's quote |
| Standby route set-up date (before Stage 3 — verification F-8, to recast as a trigger on the deposit-cost reading) and cost (⚠ £1.84–15.59m one-off; ⚠ £0.3–0.6m a year) | the runner at the C10 record's next regeneration; the treasury | the agents' quotes |
| Audit S1 — the funding gate (3.45%) added to the quarterly trigger review's readings | the runner, CTM v11 | one reading at the sitting |
| Audit S2 — the recurring fixed layer's ⚠ 1.06 per £1,000 above the activities: carry the derived line or declare the reserve (RD-031) | the runner, AOM v11 | the next regeneration |
| Audit S4 — the C10 record's Stage 1 people figure (⚠ £12.95m) brought to the AOM v10's (⚠ £13.55m) | the runner, C10 record | the next regeneration |
| F2 verification F-3, F-4, F-5, F-6 (the switched-off line; two presentations of "available"; the conformance scope; `Included = false`) — still open | the runner, at the C7 record's next regeneration | unchanged |
| WS1 — the HRS has thresholds and no terms in the registry; the checks-run table asks "printed" not "reproduces from the floor" (the 3.99% error); the fit model has no field for a barrier score or a position-holding table; `check_verdict_order.py` reads no F3 gate; `validate_tam_model.py` has no vocabulary for a volume gate or a class excluded by the venture's own price | Head of R&D (WS1) — see the WS1 feedback log, F3 section | script and registry changes |
