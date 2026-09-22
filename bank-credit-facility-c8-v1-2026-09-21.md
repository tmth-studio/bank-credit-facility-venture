# A business bank's credit facility line — challenge eight (R8) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R8 opens Function 3. The block is that nothing in the form as it stands at C7 accumulates: the limit reads the flow, and the flow is readable by any authorised provider through the same bank feed R7 opened. A rival that reads the account can copy the limit on day one. The one move gives the limit rule a second input — the account's own record on the limit: funded events cleared through the receipts share. The multiple of flow rises with cleared events, so a limit that has been used and repaid on this account is larger than a limit computed from flow alone. The record is the customer's (shown in the limit history, exportable) and the seasoned limit exists only on the account whose receipts fund the share; a rival can read the record but cannot honour the seasoned limit without the receipts. Component: WP-1 v2 — the seasoned limit. The verdict cannot exceed R1–R7's PROVISIONAL (VA-95). The move adds ⚠ 0.45–1.46 per £1,000 drawn a year to the floor before rounding (capital on the larger undrawn commitment), booked as a rise of the IC layer from 12–17 to 13–18 by the whole-number convention; the conventional R8 line (⚠ 5–15 — loyalty pricing, tie-ins, exit fees, a retention desk) is removed; cumulative conventional additions used ⚠ 1.05–1.28 of ⚠ £8 (RD-030) on the rounded layers (⚠ 0.50–1.74 unrounded). Floor ⚠ £55.04–107.28. Margin at the worst corner **30.5% at the set price**; 25.8% at the band's low end; 32.8% at its top. Binding gate unchanged: the loss rate on the flow-underwritten pool — the 25% margin fails above ⚠ 4.47% at the set price; the assumed high corner is 4.0%. **One registry row does not pass:** the switching-cost score (SCIS) is 2 at the conservative corner, 4 at central and 6 at the optimistic — below the pass line of 5 at central and an NCR at the conservative corner. The switching cost is genuine and too small: the annual spend it is measured against is ⚠ £2,100–3,500 an account. What is done about it: the fit verifier r8 re-tests the margin at the position-holding failure value (switch-out ⚠ 10–15% a year) and it holds at 29.5%. What holds position is the margin, not the lock. The record says so and does not soften it.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c7-v1-2026-09-21.md` (R7, PROVISIONAL, object-after to 23 September 2026 17:00), and the C6 to C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3; F2 closed PROVISIONAL at C7 (audit PASS WITH CONDITIONS; verification 93.1 SOUND). **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F3 rule this record works under (Tom, 16 September 2026).** R8 to R10 make the at-scale price and cost hold. R8 does it without an artificial barrier: value accumulated in the relationship, in the account's own record. The conventional R8 line is ⚠ 5–15 per £1,000 in the counterfactual (RD-030): loyalty pricing, exit fees, product tie-ins and the retention desk that runs them. This record names what the conventional bank buys with that line, replaces it with accumulation the customer owns, and books only what the one move costs.

**F3 ordering (challenge skill).** Identify the resource or store of value first; the strategy and the theory follow from it. The store of value is named at SR1 before any theory is chosen.

**Customer of record (VA-154).** The business owner who holds the account (the migrated overdraft user and the never-borrowed customer with enough flow — one customer of record, one payer). The routine positioned in: the customer's extended use of the limit across years — the funded events, the receipts that clear them, and the point at which the customer weighs moving the account. One run. No supplier binds at launch (the C10 shelf check is R10's by number).

**Sections in this record.** Defined terms. SR1 to SR3 with the mutation gate. Productizing. Cumulative business form factor (C1–C8). Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C7. Financial check with the position-holding table and the switching-cost score. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

- **Store of value** — what accumulates on the account through use of the limit that a customer would lose by moving the account, and that no rival can supply on day one.
- **Funded event** — a payment that exceeded the balance and was met from the limit under the accepted term (WP-2 v2, C5), or a draw ahead.
- **Cleared event** — a funded event whose drawn balance has returned to zero through the receipts share (WP-3 v2, C6), with no receipt-free accrual older than ⚠ 90 days at the point of clearance. *Runner's call* — the 90-day cut keeps a stalled draw out of the count.
- **Seasoning** — the count of cleared events on the account and the months since the first, read by the limit engine as the rule's second input.
- **Seasoned limit (WP-1 v2)** — the standing limit computed from the flow (C1) and from the account's seasoning: the multiple of flow rises with cleared events, from the base multiple at six months of flow to a full multiple at ⚠ 36 months and ⚠ 12 cleared events. The rise is published in the limit history (CP-2) and through the pre-agreed credit line (PP-1) like any other limit change.
- **Seasoning schedule** — the rule that maps seasoning to the multiple: ⚠ two-thirds of the full uplift by ⚠ 12 cleared events; the full uplift by ⚠ 36 months; the average uplift across the at-scale book ⚠ 15–30% of the flow-only limit. Every figure T4 and calibrated on the bank's own history (R9 by number).
- **Switch-out** — the account leaving the bank through the Current Account Switch Service (CASS) or by closure; CMA 2016 put SME switching at about 4% a year (T1 for the market; ⚠ for this pool).
- **SC ratio** — the switching cost divided by the customer's annual spend with the bank on the line (Klemperer 1987; Farrell and Klemperer 2007): the magnitude term in the SCIS.

---

## SR1 — Extended product use routine and key store of value

*Customer of record: the business owner who holds the account; the routine positioned in: the extended use of the limit across years.*

**The extended routine — what happens on the account after the first funded event, in the order it happens.**

1. A payment exceeds the balance; the limit funds it (C5). The account is drawn.
2. Receipts arrive; the split (C6) takes the charge first and then the drawn balance until it is zero. The event is cleared. Time to clear ⚠ 5–40 days at the flow bands in the pool (T4, from the C5 use routine: a shortfall of ⚠ 10–30% of monthly receipts cleared at the receipts rate).
3. Steps 1 and 2 repeat ⚠ 3–12 times a year on a drawn account (T4, from the C4 share of accounts with at least one shortfall in twelve months, ⚠ 30–70%, and the C5 event count).
4. The limit is recomputed daily from the flow (C1). Today the flow is the only input: a good year raises the limit, a weak quarter lowers it, and the account's record of having drawn and cleared changes nothing.
5. At some point the customer weighs moving the account — a rival's offer, a change of accountant, a new director, a bad experience elsewhere in the bank. What the customer weighs is the balance they hold, the payments set up, and the facility. At C7 the facility weighs nothing in that decision that a rival cannot match on day one: the rival reads the same flow through the same feed and computes the same limit.

**The block, named as one operation.** The limit rule's single input. Everything the rule reads is readable by a rival; nothing the customer does on this account changes what this account's limit is beyond what any account with the same flow would get. The C1 VA-106 line said the limit lives where the flow lives; that is the starting context and it is not enough, because at C7 the flow lives wherever a bank feed points.

**Store of value type: data accumulation.** What accumulates: the account's own record on the limit — funded events and their clearance through the receipts share, by date, amount and days to clear. It is a record of realised conduct on this facility, not of flow. Flow is a property of the business and travels with it; clearance through the receipts share is a property of the relationship between this account and this limit, and it is created only by using the limit here.

**Why this is not the other two types.** *Integration depth* — the payments, mandates and feeds tied to the account — is Case A's store (the account line's own R8) and the CASS redirection service was built to make it portable in seven days. *Relationship capital* — a manager who knows the business — is the conventional relationship-lending form the C1 design removed. The store here is a record, and it is the only one of the three the C1 form creates by itself.

**The customer-ownership test.** The record is shown to the customer in the limit history (CP-2, C4) as its own line — each funded event, its clearance, the multiple it earned — and it is exportable with the history. The customer owns the record. What the customer cannot take is the position the record earns: a seasoned limit funded from the receipts of this account. A rival can read the exported record and choose to match the seasoned figure; it then holds a limit on receipts it does not see, repaid by a direct debit it must chase — a different loss model at a different price. *Runner's call:* that asymmetry is the switching cost, and it is genuine because it comes from where the money flows, not from a term.

**Switching cost trajectory.** Nil at release (no cleared events). Material when the seasoned multiple exceeds what a rival's flow-only rule gives: ⚠ two-thirds of the uplift by ⚠ 12 cleared events — on a drawn account, ⚠ 12–36 months after release; full by ⚠ 36 months. On the never-borrowed account with no funded events the trajectory is flat: the store accumulates only through use. That is by design — a switching cost on an unused limit would be a term, not a record.

---

## SR2 — Lock-in theory of change

**Parameter the store of value rests on.** Realised conduct on the facility is private to the lender that funded it, even when the flow that predicts it is public. The bank knows what this account did when it was drawn; a rival knows what the flow says it might do.

**Theory.** Sharpe, S. A. (1990), "Asymmetric Information, Bank Lending, and Implicit Contracts: A Stylized Model of Customer Relationships", *Journal of Finance* 45(4). An incumbent lender learns a borrower's quality by lending to it; outside lenders cannot see what it learned, so the incumbent can offer terms an outside lender would only match by risking a winner's curse. The consequence in the model is informational capture — a customer that has proven itself to one lender is worth more to that lender than to any other, and the lender can pass part of that value back as better terms. Supported by Petersen and Rajan (1994), *Journal of Finance* 49(1): availability of credit rises with the length of the lending relationship in US small-firm data; and by Ioannidou and Ongena (2010), *Journal of Finance* 65(5): firms that switch banks receive a lower rate at first and see it rise as the new bank learns — the outside lender's offer prices in what it cannot see. Not on the fragile-findings list.

**Contrast.** Rajan (1992), *Journal of Finance* 47(4): informational capture lets the incumbent hold the borrower up, and borrowers respond by keeping a second lender. Open Banking has changed the premise both models share — the flow is no longer private. What stays private is the realised conduct on the facility. The mechanism here therefore rests on the record's realisation, not on hiding the flow: the seasoned limit is a better term earned on private conduct, published openly, and the hold-up Rajan names is bounded by the C6 price (one rate, the same for all) and the C4 history (the customer sees what they earned). *Runner's call:* the design takes Sharpe's mechanism and removes Rajan's cost by publishing the terms.

**Context in which the mechanism holds.** The customer draws and clears on this account (steps 1–3 of the routine). The account has enough flow to be selected (C1). The seasoned uplift is visible to the customer before any rival's offer arrives (C4, C7).

**Outcome.** A customer weighing a move sees a seasoned limit here and a flow-only limit there, with the difference shown in their own history. Moving the account costs the difference until the rival's facility has seasoned in turn — ⚠ 12–36 months. The outcome is a lower switch-out rate on seasoned accounts than on unseasoned ones, and a book whose average limit is ⚠ 15–30% larger than flow alone would give, on accounts that have shown they clear.

**Hypothesis (falsifiable).** Accounts with ≥ 24 months on the limit and ≥ ⚠ 12 cleared events switch out at half the rate or less of accounts with < 6 months on the limit, read at the first replica's 24 months on the CASS and closure counts. Falsified if the ratio is ≥ 0.8. **Falsification condition on the theory:** if seasoned accounts switch out at the same rate as unseasoned, realised conduct is not private in the sense the theory needs — a rival's flow-only rule matches the seasoned limit — and the store of value is not a store.

**Named assumptions.** (1) A rival's limit rule reads flow only, or reads the exported record but does not fund from this account's receipts — T4, from the mechanism; (2) the uplift's loss rate is at or below the pool average, because it accrues only on accounts that have cleared — T4, from the definition of a cleared event; (3) switching a business account for a facility alone is rare below ⚠ £25,000 of limit — T3, CMA 2016 (SME switching about 4% a year for all reasons).

---

## SR3 — Lock-in strategy

**The strategy in one sentence.** Make the account's own record on the limit the rule's second input, so that a limit which has been used and repaid here is larger than any limit computed from flow alone, and show the customer what they earned.

```
MUTATION GATE — R8
baseline: the limit is computed daily from the flow alone (C1); any authorised reader of the account can compute the same limit from the same feed (C7); nothing the customer does on this account changes its limit beyond what the flow says, so the facility carries no weight in a decision to move the account.
mutation_A: the seasoned limit — the rule reads a second input, the account's cleared events, and the multiple of flow rises with them on a published schedule; the uplift is shown in the limit history and exists only on the account whose receipts fund the share | reason_considered: it is the one store the C1 form creates by itself, it is the customer's, and a rival cannot honour it without the receipts | verdict: adopted | reason_verdict: genuine accumulation; passes the customer-ownership test; a rival matching the figure off-account carries a different loss model; costs capital on the larger undrawn commitment and nothing else
mutation_B: integration depth — tie the limit to the account's mandates, standing orders and feeds so that moving the account means rebuilding them | reason_considered: the largest switching cost in business banking today | verdict: rejected | reason_verdict: it is the account line's own R8 (Case A) and the CASS redirection service was built to remove it; the venture would be borrowing a barrier it does not own and the CMA has already priced at seven days
mutation_C: publish the account's cleared-event record to third parties as a trade-credit signal, so that suppliers extend terms on it | reason_considered: raises the value of staying by making the record worth something outside the bank | verdict: rejected | reason_verdict: a conduct and data-protection question the design does not need (the record leaves the customer's control); it also makes the record portable, which removes the store
mutation_D: the exportable limit history as the store — the customer keeps a full record they can show a rival | reason_considered: passes the customer-ownership test outright | verdict: folded into A | reason_verdict: the export already exists in CP-2 (C4); alone it is a portability device, not a store — a rival that reads it still cannot fund from the receipts
mutation_E: loyalty pricing — the rate falls with tenure | reason_considered: the conventional R8 line; simple to state | verdict: rejected | reason_verdict: contractual, not structural; it reprices (C6 set the price and F3 does not move it); it costs margin the cap cannot carry; and it is copied by any rival with a spreadsheet
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: mutation_A — the seasoned limit (WP-1 v2)
evolvedBFF: a bank whose credit facility is a standing property of every business account with enough flow — computed daily from the flow and from the account's own record of drawing and clearing, so that a limit used and repaid here is larger than any limit computed from flow alone; priced below the tariff, released in stages, believed on its history, used without an act, paid from receipts, published wherever the account is read, and now seasoned by use.
synthesisCheck: a trade-credit account with a supplier for business lending, because the credit line a supplier extends rises with the invoices the customer has paid on time — a record the supplier holds and the customer can show but a new supplier cannot fund against on day one.
```

**Switching cost test.** Genuine accumulation. The record is created by the customer's own use of the limit; nothing is added to the routine; a customer who never draws accumulates nothing and loses nothing by leaving. It is not friction: the export is free, CASS moves the account in seven days, and the price is the same for a seasoned and an unseasoned account.

**R5 interaction.** Activation and accumulation share the mechanism. The first funded event under the accepted term (C5) is the first entry in the record; nothing new is asked of the customer to start accumulating, which is the invisible-accumulation test the challenge skill sets. The switch-off customer (C5) draws ahead and accumulates the same way.

**R10 interaction — by number only (VA-80).** The seasoning schedule's calibration is R9's; the moat is R10's.

**Structural, not contractual.** No term says the customer must stay; no fee is charged for leaving; no price changes with tenure. A rival with any budget can copy the schedule and cannot copy the record, because the record is made of events on this account.

---

## Productizing R8 — the strategy in the architecture

**WP-1 v2 — the seasoned limit.** The Working product amended: the rule's second input is the account's seasoning; the seasoning schedule is a published parameter of the rule; the uplift is a limit change like any other — it appears in the account, in the limit history (CP-2) with the cleared event that earned it, and in the pre-agreed credit line (PP-1). The customer is told of a limit rise by the notice the account already gives (the CCA s.82 modifying-agreement and CONC notice path decided at C5 and C6 — a rise is a variation in the customer's favour and is notified, not re-signed). *Runner's call* on the notice path; what a ruling would settle is whether a rule-driven rise needs a fresh creditworthiness assessment under CONC 5.2A each time — the design position is that the assessment made at acceptance on the rule's limit covers the rule's schedule, because the schedule is part of the rule the assessment was made on.

**Invisible accumulation.** The customer does nothing new. A cleared event is recognised by the split (C6) reaching zero; the engine reads it in the daily recompute (C1). No new event, no new screen beyond the history line.

**Down-seasoning.** A funded event that does not clear within ⚠ 90 days without receipts is not a cleared event and the multiple does not rise; a write-off resets the seasoning to zero. The rule is symmetrical in what it counts and asymmetrical in what it does: seasoning raises the multiple; the flow alone can lower the limit, as at C1. *Runner's call.*

**The at-scale test.** At ⚠ 760,000 accounts with a limit the seasoning is a field on each account and a schedule in the rule: the daily recompute already runs on every account (AOM v7 e.daily_recompute); the addition is one more input. No person is added. The seasoning schedule is validated yearly by model risk (SS1/23) inside the ⚠ 10 model-risk people at HQ — ⚠ 100–200 hours a year, a cohort reading, not a person. The engine build is ⚠ 200–400 hours once.

**What the customer now has.** A limit that grows because they used it and repaid it here; the reason shown beside each rise; the record theirs to keep; nothing to sign, apply for, or ask.

---

## Cumulative business form factor (C1–C8)

**The architecture's central mechanism.** The standing limit as a property of the account — computed from the flow and from the account's own record, present before any need, published wherever the account is read. Remove the second input and the form returns to C7: a limit any reader can copy.

**The evolved BFF.** A bank whose credit facility is a standing property of every business account with enough flow: the limit is computed daily from the flow and shown in the account before any need arises (C1); it is priced below the tariff the customer pays today and the existing overdraft is retired into it (C2); it is released in stages against a kill band, with the rule proven on history before it is trusted (C3); it is believed because the customer checks it against the twelve months of their own shortfalls it would have covered (C4); it is used without an act, because a payment that exceeds the balance is met from it under a term accepted once (C5); it is paid for only from the money that comes in — one rate on the days drawn, a slice of each receipt, no fee and no charging date (C6); it is present wherever the account is read (C7); and it grows with use, because each funded event cleared through the receipts share raises the multiple of flow on this account and nowhere else (C8). Read cold: one product, a limit that is a property of the account and of what the account has done.

**Components at C8.** WP-1 v2 (amended C8 — the seasoned limit), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, CP-1 (amended C2, C4, C6), CP-2 (amended C8 — the seasoning line in the history), PC-1 (resolved C6), PP-1 (C7; carries the seasoned figure, unamended). No component removed; no new component.

---

## Considered / not chosen (VA-4)

- **Integration depth (B)** — rejected at the mutation gate: Case A's store, and one the CMA has already made portable.
- **The record as a third-party trade signal (C)** — rejected: makes the record portable and adds a conduct question the design does not need.
- **The export as the store (D)** — folded in: a portability device, present since C4, not a store.
- **Loyalty pricing (E)** — rejected: contractual, reprices, copied at once.
- **Exit fees or notice periods** — not chosen: an artificial barrier; a fee on leaving a facility with no fee to hold would also fail the C6 form and CONC 6.7's unfair-terms tests.
- **Seasoning by tenure alone (months on the limit, no cleared events)** — not chosen: tenure is public (the account's age is in the feed); cleared events are not; a tenure-only schedule would be copied by a rival's rule on the first read.
- **Seasoning that lowers the multiple on a late clearance** — not chosen as a rule input: a stalled event already fails to count; a penalty would make the schedule a conduct term the customer must be told of in advance and would move the rule toward the tariff's unarranged-overdraft pricing the C2 form left behind.
- **A relationship manager for seasoned accounts** — not chosen: the conventional relationship-lending form; a person per account at a cost the cap cannot carry.

---

## Synthesis check (VA-1)

A supplier's trade-credit account: the credit a supplier extends to a business rises with the invoices the business has paid on time, the record sits with the supplier, the customer can show it to a new supplier, and the new supplier still starts the account at its own opening terms because it has not been paid by this customer yet. The bank's seasoned limit works the same way on the account's receipts. The analogue's limit: a supplier's record is one line of trade; the bank's record is every payment and receipt on the account, which is why the seasoned limit can be a multiple of monthly flow and not a single invoice's worth.

---

## VA-106 synergy line

Does the one move also serve an earlier requirement, with a mechanism? Seven candidates:

- **R1 (design) — yes.** The rule gains a second observed input at no new operation: the cleared event is already a state the split produces. Mechanism: the daily recompute reads one more field.
- **R3 (scale) — yes.** Seasoning starts at release and can only rise from zero, so the stage readings (C3) read cohorts by seasoning as well as by flow band; the overlay on the unproven model can be lifted on seasoned cohorts first. Mechanism: the release track's cohorts gain a second axis.
- **R4 (conviction) — yes.** The history now shows the multiple rising with each cleared event — the customer sees their own conduct move the limit, which is a stronger credibility mechanism than the counterfactual history alone. Mechanism: the seasoning line in CP-2.
- **R5 (use) — yes.** Accumulation begins with the first funded event under the accepted term; nothing to do. Mechanism: the shared event.
- **R7 (access) — yes.** The published line carries the seasoned figure, so the forecast in the ledger shows the larger limit without any change to the element. Mechanism: PP-1 unamended.
- **R2 (value) — no.** The price and the KMC do not move; the seasoned limit adds headroom, not a lower outflow. Recorded as "no" with the reason.
- **R6 (buy) — no.** The charge is unchanged; the split is unchanged.

Five earlier requirements served with a mechanism. R9 and R10 by number only (VA-80).

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per year unless stated; every ⚠ is T4.

| Actor | Behaviour needed | How often | Effect on own book | What it gains | What it costs | Best alternative and its surplus | Arithmetic (VA-157) | Surplus at scale | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|---|---|
| The business owner (drawn account) | draws and clears on this account; reads the seasoning line; weighs the seasoned limit when a rival offers | per funded event; at each offer | — | headroom ⚠ 15–30% above the flow-only limit on ⚠ £37.5–87.5k = ⚠ £5.6–26k of limit, earned without an application; the shortfall events that headroom covers (C5: ⚠ £30–135 avoided per event) | nothing — the behaviour is the C5 routine | move to a rival's flow-only limit: its surplus is the rival's opening offer less the application (⚠ £525–2,650 in fee and hours) — nil or negative in the first year | central: gain £400 (⚠ 3 events avoided at £135) − cost £0 − alternative's surplus £0 = **£400** · pessimistic: gain £30 − cost £0 − alternative's surplus £0 = **£30** | rises with seasoning | **PASS** |
| The business owner (never-borrowed, no funded event) | nothing — accumulates nothing | — | — | nothing lost | nothing | leave: surplus unchanged | central: £0 − £0 − £0 = **£0** · pessimistic: **£0** | flat | **nil by design** — no behaviour needed; the store exists only through use |
| The bank's limit-engine team (internal) | builds the seasoning input and schedule into the rule; keeps the schedule as a published parameter | once; parameter changes yearly | adds (a rule input already in the data) | a rule that reads conduct as well as flow — a lower loss on the uplift than on a flow-only rise (assumption 2) | ⚠ 200–400 h once = ⚠ £20–40k | leave the rule flow-only: surplus £0 and the C7 copyability stands | central: gain £0.5m (the uplift's contribution at the set price on ⚠ 10% more drawn-days, judged) − cost £0.008m a year (amortised) − £0 = **£0.49m** · pessimistic: gain £0.05m − cost £0.008m − £0 = **£0.04m** | rises with the book | **PASS** — the mode-3 decision carries it in any case |
| The bank's model-risk function (internal) | validates the seasoning schedule yearly on cohorts (SS1/23); reads the uplift's loss against the pool | yearly | neutral (inside the existing model inventory) | a documented second input with a cohort reading — the validation it would have to do on any rule change | ⚠ 100–200 h a year inside the ⚠ 10 model-risk people | not validate: not available under SS1/23 | central: gain £0.02m (a finding avoided) − cost £0.015m − £0 = **£0.005m** · pessimistic: gain £0.01m − cost £0.02m − £0 = **−£0.01m** | unchanged | **PROVISIONAL — FAIL at the pessimistic corner.** Force: SS1/23 — a rule input in use must be validated; the cost is the bank's regulatory obligation, not a choice |
| The bank's conduct function (internal) | signs the position that a rule-driven rise is a variation in the customer's favour, notified not re-signed; the CONC 5.2A position on the schedule | once; yearly review | neutral | a limit-rise path with no per-account paperwork | ⚠ 40–80 h once = ⚠ £4–8k | treat each rise as a new agreement: ⚠ 0.25 h × ⚠ 100,000 rises a year = ⚠ 25,000 h; surplus negative | central: gain £2.5m (hours avoided) − cost £0.006m − £0 = **£2.49m** · pessimistic: gain £1m − cost £0.008m − £0 = **£0.99m** | rises with rises | **PASS** |
| The rival lender | none — the design needs nothing from it | — | — | — | — | — | — | — | not an actor of the architecture; named because the mechanism is tested against its rule |
| The account-information readers (C7 class) | display the seasoned figure — the same element | per call | neutral | nothing new | nothing new | — | central: **£0** · pessimistic: **£0** | unchanged | **nil** — no new behaviour |

**The model-risk row, disposed.** The pessimistic corner prices a validation that costs more than the finding it avoids, which is true of most validations; the force is SS1/23, under which a rule input in use is validated whether or not the validation pays. The cost is booked in RC at HQ inside the existing people (AOM v8 3c) and does not move the floor.

---

## Actor tracks (VA-102)

No new actor class this challenge; one internal holder gains a behaviour (model risk validates the schedule) and one gains a build (the limit-engine team). **(1) Where does each track open?** The customer's track is the C5 use track; the seasoning line opens at the first cleared event — a state the track already has (funded → cleared). No later state is skipped: the seasoned limit is a state of WP-1 that follows the cleared event. **(2) Where a transition carries no product by decision, what activity does the work?** The cohort reading (model risk, yearly, AOM v8 3c) and the seasoning-review query in the exception cell (AOM v8 3b) — both with a driver. **(3) Which driver scales with a count of counterparties?** None; `q.seasoned_share` scales with the customer's own use. No counterparty with an acquiring transition. Decisions stated on each row in the CTM v8.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** WP-1 amended to v2 (the seasoned limit): the rule reads a second input; the seasoning schedule is a published parameter; the uplift is a limit change. CP-2 gains the seasoning line. No component removed; PP-1 carries the seasoned figure without change.

**Earlier requirements this same move also serves (VA-106).** R1, R3, R4, R5, R7 with mechanisms; R2 and R6 no, with reasons (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — one input added, no check failed.** The four removed operations stay removed; the rule reads one more field the split already produces; property holder of "seasons" is the limit engine (a track row). The exposure model changes: undrawn per drawn ⚠ 1.5–2.5 → ⚠ 1.9–3.6 at the average uplift, booked in IC | re-verified: at-scale margin on the selected customer 30.5% at the set price |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — unchanged.** The KMC, the price and the TAM data object do not move; seasoning narrows nothing (v3 stands until C10 by number) | re-verified: 30.5% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — strengthened on one line.** The back-test (Stage 0) can read cleared events in the history as seasoning and so tests the schedule before Stage 1; the cohort readings gain a second axis; SC gains the engine build (⚠ £20–40k once) inside the 0–1 band. Stage 1 margin at the set price falls to 4.0% (spread count below) | re-verified: Stage 1 4.0% at the set price |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — strengthened.** The seasoning line adds a second credibility mechanism inside the signed display: the customer's own conduct moving the limit. The conduct reviewer's signature covers the history; the new line is a history line (a *runner's call*; the yearly review reads it) | re-verified: 30.5%; cap line carried |
| R5 (C5 record v1.1) | use routine; routine disruption; Madrian and Shea; default funding; switch-off and reversal; the loss gap; CONC 5.2A timing | **re-verified — one position extended.** The CONC 5.2A position (assessment at acceptance on the rule's limit) now covers the schedule; the design says the schedule is part of the rule assessed. What a ruling would settle: whether a rule-driven rise above the accepted limit needs a fresh assessment. Loss gate at the set price 4.47% (floor high 107.28) | re-verified: 30.5%; loss gate 4.47% |
| R6 (C6 record v1) | lifecycles; CVTs; buy block type; Prelec and Loewenstein; mutation gate; price structure; representative example; R2 and R3 interactions | **re-verified — unchanged.** The split is the same; the price is the same; the seasoned limit changes headroom, not the charge. The representative example is unchanged (rate, not limit) | re-verified: 30.5% at the set price (25.8% / 32.8% at the band's ends) |
| R7 (C7 record v1) | access routines; gateway class; Farrell and Saloner; PP-1; conformance; desk position; G15 | **re-verified — unchanged.** The element carries whatever the released limit is; the seasoned figure needs no change to the element, the flag or the desk position. The F2 audit's owed items carried here: S2 (the C5 headroom split into a first-year and a recurring line — done in AOM v8 3b); S1 and S3 (design positions restated in the C7 record's next regeneration — carried, not owed to R8); verify F-5/F-6 (recast as convergence items — carried) | re-verified: 30.5% |

No FAILED row. **Function-gate re-run:** not at C8 (at C10 by number).

---

## Financial check — the floor on four layers, the ceiling as a price, the cap and the position-holding table

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1 v2 (amended C8), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, CP-1 (amended C2, C4, C6), CP-2 (amended C8), PC-1 (resolved C6), PP-1 (C7).

**Pricing note.** F3 does not reprice. The ceiling stays the R2 KMC resolved to the C6 price (140; band ⚠ 135–142.5). The seasoned limit adds headroom at the same rate.

**The exposure change, stated once.** The drawn book is set by the customers' shortfalls, not by the limit (C5: a payment that exceeds the balance draws what it needs). The seasoned uplift therefore lands in the undrawn commitment: the limit rises ⚠ 15–30% on average and the drawn balance does not. Undrawn per drawn moves from ⚠ 1.5–2.5 to ⚠ 1.9–3.6 (limit-to-drawn 2.5–3.5 × 1.15–1.30, less the drawn unit). *Runner's call*; the threshold at which the assumption fails is stated in the position-holding table.

**What R8 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v8 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| read the seasoning field in the daily recompute | per account per day, automated | e.daily_recompute on q.accounts_with_limit | 760,000 × 365 | ⚠ £0.00001 (one field in a computation already run) | ⚠ £3k | 0.00 |
| recognise a cleared event when the split reaches zero | per funded event, automated | e.cleared_event on q.drawn_accounts | 228,000 × ⚠ 3–12 a year = ⚠ 0.7–2.7m | ⚠ £0.001 | ⚠ £1–3k | 0.00 |
| build the seasoning input and the schedule into the rule | HQ, once | e.engine_build | 1 | ⚠ 200–400 h at ⚠ £100/h = ⚠ £20–40k once, amortised over five years | ⚠ £4–8k | 0.00 |
| validate the schedule yearly on cohorts (SS1/23) | HQ, yearly | e.seasoning_review | 1 | ⚠ 100–200 h inside the ⚠ 10 model-risk people | inside RC | 0.00 |
| sign the variation and CONC 5.2A positions | HQ, once then yearly | e.field_position (C7's event, one more position) | 1 | ⚠ 40–80 h inside the existing conduct people | inside RC | 0.00 |
| answer a seasoning query ("why did my limit rise" / "why not") | cell | e.seasoning_query on q.replica_accounts × drawn share | ⚠ 0.5–1.5% of drawn accounts a year = ⚠ 500–1,500 per cell | 0.25 h | ⚠ 125–375 h per cell — the first-year headroom line (AOM v8 3b) carries ⚠ 0–425 h; with C6 and C7's recurring queries (87–300 h) the recurring line is over by ⚠ 0–250 h at the high corner: **one handler added at the high corner** (cell 14 → ⚠ 14–15), booked | ⚠ £0–60k per cell × 2 replicas = ⚠ £0–0.12m | 0.00–0.02 |
| capital on the larger undrawn commitment | at scale | q.undrawn_per_drawn × 10% CCF × 75% RW × 12% × 12–15% CoE | 1.9–3.6 per £1 drawn | — | — | **2.05–4.86 in place of 1.62–3.38: +0.43–1.48** |
| **R8 total, unrounded** | | | | | **⚠ £0.03–0.2m operating, plus capital** | **⚠ 0.45–1.50** |

*Runner's call on the seasoning-query rate.* A limit that rises without an application will draw the question "why" from some customers and "why not mine" from others; ⚠ 0.5–1.5% of drawn accounts a year is judged from the C4 limit-query rate (⚠ 1–3% of accounts with a limit) halved, because the history line answers most of it on the screen. Threshold: above ⚠ 2% a second handler is added and the R8 operating line rises to ⚠ 0.04. Convergence: the first replica's six months. The F2 audit's S2 item is closed in AOM v8 3b: the C5 headroom is now a first-year line (⚠ 0–425 h) and a recurring line (⚠ 212–675 h across C6, C7 and C8 queries), and the recurring line is what adds the handler at the high corner.

**The four-layer floor at C8 (AOM v8 section 6).**

```
PVC  40.02–83.24   funding 15–30 · expected loss 20–40 (C8: the uplift's loss at or below the pool average — assumption 2; unmeasured) · computing and payments 2.02–5.11 (C8: +0.00) · exceptions and write-off 3.00–8.13 (C8: +0.00–0.02, one handler at the high corner, inside the rounded band)
RC    2.02–5.04    unchanged — the validation and the positions sit inside the existing people
SC    0–1          unchanged — the engine build (⚠ £20–40k once) sits inside the band
IC   13–18         was 12–17 — undrawn commitment 2.05–4.86 (was 1.62–3.38) on undrawn per drawn ⚠ 1.9–3.6; unrounded 12.85–18.36; whole-number convention kept (C1)
FLOOR 55.04–107.28  (C7: 54.04–106.28; C6: 54.04–106.27; C5: 54.04–106.26; C4: 54.03–106.20; C3: 54–106)
```

**Carrying check.**

```
CARRYING CHECK — R8
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v3 KMC-OD-STD-TARIFF)
  the price (C6)                        140.00 — band ⚠ 135.00–142.50 (F3 does not reprice)
  floor                                  55.04–107.28
  operating bar = floor × 1.25           68.80–134.10
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  price against the operating bar        140.00 − 134.10 = 5.90 at the set price · 0.90 at the band's low end · 8.40 at its top
  carries                                true at every point of the band
  FMOS worst corner (price − floor high) ÷ floor high
                                         30.5% at 140 · 25.8% at 135 · 32.8% at 142.5
  FMOS best corner (price − floor low) ÷ floor low
                                         154.4% at 140 (the fit model's KMC-band figure is not used)
  conventional additions used (RD-030)   R8 line ⚠ 5–15 removed; added ⚠ 1.00 on the rounded layers (⚠ 0.45–1.50 unrounded); cumulative ⚠ 1.05–1.28 rounded (⚠ 0.50–1.78 unrounded); remaining ⚠ 6.72 at the high corner
  max payable to any holder (VA-164)     5.90 at central; 0 at the pessimistic corner; paid: 0
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C8.yaml`).** By hand: **30.5% at the worst corner at the set price; 25.8% at the band's low end; 32.8% at its top; 154.4% at the best corner. PASS on the 25% gate at every point of the band** — the band's low end now sits 0.8 points above the gate. R8 is the first requirement since C3 to move the worst-corner margin by more than a tenth of a point (31.7 → 30.5). `fit_margin.py` is run on the at-C8 model; its output is in the verifier r8.

**Binding gate — by driving (VA-84).** Sixteen gates driven at C8: the fifteen of C7 and (16) the average seasoned uplift. Ordered by margin at the set price:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.47%** at the set price (4.07% at the band's low end; 4.67% at its top); at C8 the loss line is 67.28 + 10L and the bar is 112.00; zero margin at 7.27%; assumed ⚠ 2–4%; surplus 0.47 points at the assumed high corner — R8's capital on the seasoned undrawn commitment consumed 0.10 points of the C7 surplus. **First to fail.**
2. the default-funded loss gap (C5) — on the same line; ⚠ 0.3–0.5 of the 0.47 points; unmeasured. At the top of that band the surplus is 0.0 — the loss line is now at its threshold at the assumed corners. Stated, not softened.
3. the price condition's room — 5.90 at the set price; 0.90 at the band's low end.
4. the rate against the lowest published EAR — 0.54 points (C6).
5. **the average seasoned uplift (new, G16)** — ⚠ 15–30% assumed; the band's low end (135) falls under the 25% margin above an average uplift of ⚠ 38% (the unrounded floor high reaches 108.00); the set price fails above ⚠ 145%. Reads at the first replica's 24 months.
6. G15 — the platforms' display (C7), unchanged.
7. the connected share, unchanged.
8. the non-empty history share, unchanged.
9. the use gates — switch-off, funding-query, charge-query, display-query, and the seasoning-query rate (new, ⚠ 0.5–1.5%; threshold 2%).
10–16. carried from C7 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, including default-funded draws and the seasoned uplift
  threshold:    4.47% at the set price (4.07% at the band's low end · 4.67% at its top) — the 25% margin fails above it at the worst corner; zero margin at 7.27%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.47 points at the assumed high corner; the default-funded gap (C5) may consume ⚠ 0.3–0.5 of it, so the surplus at the top of that band is nil
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the seasoning schedule is a rule parameter model risk can cut to zero without touching the price
  reads at:     the Stage 1 12-month reading (the pool); the first replica's 12-month reading (the gap) and 24-month reading (the uplift's loss by cohort)
```

**Independence (VA-97).** NOT shown — the margin is a transform of the loss gate. Free counts named: the switch-out ratio on seasoned against unseasoned accounts (the R8 hypothesis) and the seasoning-query rate — counts of acts, not of losses; both unmeasured.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts). At Stage 1 (⚠ £0.4–1.9bn): floor 56.86–134.62 (the C7 figure plus the rounded IC unit); worst-corner margin at the set price (140 − 134.62) ÷ 134.62 = **4.0%**; 0.3% at the band's low end; 5.9% at its top. Stage 1 does not carry the 25% margin at any point of the band — as at C3 to C7. At Stage 1 the seasoning is nil (no cleared events at release) so the true Stage 1 IC is the C7 figure and the margin 4.8%; the 4.0% is the convention's figure and is the one recorded.

**Working capital timing.** Unchanged from C6.

**The conventional line removed, priced.** The counterfactual's R8 line is ⚠ 5–15 per £1,000: loyalty pricing (⚠ 0.5–1.0 points off the rate for tenure), exit and early-settlement fees (foregone in the form), product tie-ins (a lending discount for a card or a merchant account) and a retention desk (⚠ 5–15 people). On a £4.5bn book that is ⚠ £23–68m a year the conventional bank spends to hold a customer the seasoned limit holds for the capital on ⚠ 15–30% more undrawn commitment.

**The switching-cost score (SCIS) — registry row "F3 barrier scores".**

| Term | Conservative | Central | Optimistic | Basis |
|---|---|---|---|---|
| Annual spend with the bank on the line | ⚠ £3,500 | ⚠ £2,800 | ⚠ £2,100 | 14% × average drawn ⚠ £15–25k per drawn account (£3.4–5.7bn ÷ 228,000) |
| Switching cost, cash and hours | ⚠ £525 | ⚠ £1,500 | ⚠ £2,650 | a rival's arrangement fee ⚠ 1–2% on a ⚠ £37.5–87.5k limit + ⚠ 5–15 owner hours at ⚠ £30–60; the exported record is free |
| Value of the seasoned uplift foregone | ⚠ £56 | ⚠ £250 | ⚠ £525 | ⚠ 1–2% (a rival's fee on the same headroom) × ⚠ £5.6–26k |
| SC ratio | 0.17 | 0.63 | 1.51 | (cost + uplift value) ÷ spend |
| Magnitude (0–3) | 0 | 1 | 2 | < 0.25 → 0; 0.25–1.0 → 1; 1.0–2.0 → 2 |
| Portability (0–2) | 1 | 1 | 2 | the record is portable as information (the customer's export); the position it earns is not; scored partially portable, non-portable at the optimistic corner |
| Trajectory in 24 months (0–2) | 1 | 2 | 2 | two-thirds of the uplift by ⚠ 12 cleared events (⚠ 12–36 months on a drawn account): compounds at central; moderate where events are few |
| **SCIS (max 7; ≥ 5 pass; ≤ 3 NCR)** | **2 — NCR** | **4 — below the pass line** | **6 — pass** | |

**The score, read plainly.** The switching cost is genuine and too small relative to the spend. A customer paying ⚠ £2,800 a year for a limit does not stay for a ⚠ £1,500 one-off cost; they stay because the seasoned limit is larger than the rival's and the rival's is not larger. That is a value difference, not a switching cost in Klemperer's sense, and the score says so. **What is done about it (registry row "position-holding assumption named"):** the fit verifier r8 re-tests the margin at the failure value in the table below and reports it. The requirement is not looped back: the mutation gate's alternatives were rejected on structural grounds that a second pass would not change, and the only way to raise the SC ratio is a term (E, exit fees) the F3 rule forbids. Recorded as **FAIL at the conservative corner, below the line at central**, carried as a design finding to the C10 audit.

**Position-holding table (registry F3 row).** Every model assumption that depends on R8 holding; the requirement it holds because of; the failure value as a band; where it lives in the fit model.

| Assumption in the model | Holds because of | Value if R8 holds | Failure value (band) | In the fit model as |
|---|---|---|---|---|
| Switch-out of drawn accounts a year (drives RC re-release and the base's stability) | R8 — a seasoned account is worth more here than at a rival | ⚠ ≤ 4% (CMA 2016 for all reasons) | ⚠ 10–15% (the rate a flow-only limit would see once rivals copy it through the feed) | `position_holding.switch_out` — the release-scaling share of RC (⚠ 5–8%) rises with the churn ratio 12.5 ÷ 4: RC 5.04 → ⚠ 5.58–5.90 at the high corner; SC unrounded 0.72 → 0.84, still inside 0–1 |
| Average seasoned uplift on the book | R8 — the schedule | ⚠ 15–30% | 0% (schedule cut to zero by model risk) — the IC returns to 12–17 and the margin to 31.7%; the failure is of the store, not of the margin | `position_holding.uplift` |
| The uplift's loss at or below the pool average | R8 — cleared events select the accounts | ⚠ ≤ 4.0% | ⚠ 4.0–5.0% on the uplift's drawn share (⚠ 10% of drawn-days) — adds ⚠ 0.0–0.1 to the loss line | `position_holding.uplift_loss` |

**Re-test at the failure value (by hand; the script's figure in r8).** RC 5.90 at the top of the failure band, SC 1, floor 55.04–108.14: (140 − 108.14) ÷ 108.14 = **29.5% — PASS** (29.8% at 5.58). The margin holds without the lock. What R8 holds is position — the customer's reason to stay — and it holds it on value, not on cost.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Customer of record declared; one run; the routine positioned in named ✓ (VA-154).
- F3 ordering — the store of value identified at SR1 before any theory ✓.
- Extended product use routine — five steps in the order they happen; the block named as one operation (the rule's single input) ✓ (SR1). Store of value type named (data accumulation) with the two other types excluded by reason ✓. Customer-ownership test passed with the asymmetry stated ✓. Trajectory stated with the flat case (the never-borrowed account) ✓.
- ToC — parameter named ✓; theory named with researcher, year and paper ✓ (Sharpe 1990; supported by Petersen and Rajan 1994 and Ioannidou and Ongena 2010); contrast theory named (Rajan 1992) and the premise Open Banking changed stated ✓; fragile-findings check ✓; context and outcome as states ✓; hypothesis with falsification condition on the theory and three named assumptions ✓.
- Strategy — one sentence; exactly one structural decision ✓; mutation gate emitted before the strategy; five genuine mutations (A–E), one folded in; justification mode false ✓; switching cost test (genuine, not friction) ✓; R5 interaction ✓; R10 by number ✓; structural not contractual ✓.
- Productising — invisible accumulation ✓; R5 continuity ✓; at-scale test with the volume and no person added ✓; down-seasoning rule stated ✓; the notice and CONC 5.2A positions stated with what a ruling would settle ✓.
- Cumulative BFF (C1–C8) read cold as one product; central mechanism named; components listed with amendments ✓ (parent's instruction; the challenge skill's own F3 note that cumulative statements are not produced at R8 is overridden by the parent's brief and recorded in the WS1 feedback log).
- Considered and not chosen — eight entries with reasons ✓ (VA-4). Synthesis check with the analogue's limit ✓ (VA-1).
- VA-106 line, seven candidates, five served, two "no" with reasons ✓. VA-103 table, seven rows, no FAILED row, the F2 audit's owed items placed ✓. VA-127 table, two arithmetic lines per row; one PROVISIONAL row with the force named; two nil rows by design ✓. VA-102 three questions answered ✓. VA-82 classified ✓.
- No forward references (VA-80) ✓ — R9, R10 by number only. Launch constraints absent (VA-23) ✓. Completeness contract (VA-73) ✓.
- Conventional cost line named (⚠ 5–15) and removed; the cap line printed with the rounded and unrounded figures ✓ (F3 rule).
- Binding gate by driving ✓ (16 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162). Independence stated ✓ (VA-97).
- Position-holding table — three assumptions, each with the requirement it holds because of, the failure value as a band and its place in the fit model ✓; re-test at the failure value by hand ✓ (registry F3 row).
- **F3 barrier score (SCIS): 2 · 4 · 6 — FAIL at the conservative corner (NCR), below the pass line at central.** Disposed under the registry row: re-tested at the failure value (29.5%, PASS); carried as a design finding to C10. ✗
- Verdict order (VA-95) ✓ — `check_verdict_order.py` on the verdict record with R8 added. Loop-gate branch (VA-153): no FAIL on the design's FIT. Loop-backs (VA-151): 0.
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r8-2026-09-21.md`.

Checks failed: 1 (the SCIS at the conservative and central corners). **PASS WITH ONE FAIL DISPOSED.**

**Operational check.** The CTM v8 and AOM v8 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v8 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. The customer's use track carries the seasoning at a state it already had ✓ (VA-102). **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at the central corner, unchanged; **at the high corner 21,900 hours and a 15th handler** — the C5 headroom is now split into a first-year line (⚠ 0–425 h) and a recurring line (⚠ 212–675 h across the C6, C7 and C8 queries), and the recurring line exceeds the headroom by ⚠ 0–250 h at the high corner. Handlers: **14 per cell (band 13–15)**, the band's top now used at the high corner. At scale: 2.28 cells, ⚠ 46,500–49,900 hours, ⚠ 32–34 handlers + 3 leads + a trainer = 36–38 people in cells. Every calculation in this record uses 20,400 and 14 at central. Role support: no new role; the seasoning-query script is a handbook page (AOM v8 section 4) ✓. Unit sizing: the cell's fixed cost ⚠ £0.9–1.24m ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin 30.5% at the worst corner at the set price (25.8% / 32.8% at the band's ends), 154.4% best, by hand; PASS at every point; `fit_margin.py` run on the at-C8 model (verifier r8). Carrying check: carries; room 5.90 at the set price, 0.90 at the band's low end. Binding gate: the loss rate, unmeasured, threshold 4.47% at the set price; the C5 gap on the same line, and the surplus at the top of the gap's band is nil. Conventional additions used: ⚠ 1.05–1.28 of ⚠ £8 rounded (⚠ 0.50–1.78 unrounded); the R8 line ⚠ 5–15 removed. Max payable to any holder 5.90 at central, 0 at pessimistic; paid 0. Independence NOT shown; two free counts named. Position-holding re-test 29.5% at the failure value. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- The SCIS below the pass line — **design finding**, not a design defect: the store is genuine and the spend it is measured against is small; the margin holds at the failure value (29.5%); no term is available to raise the score under the F3 rule. Owner: the runner, at the C10 consistency audit (the moat test reads it). Convergence: the R8 hypothesis at the first replica's 24 months — if seasoned accounts switch out at half the rate, the score understates the lock; if not, the finding stands.
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- The model-risk actor row — FAIL at the pessimistic corner, **disposed with the force named** (SS1/23); no input to measure.
- The average seasoned uplift (⚠ 15–30%) — **unmeasured input**; owner: model risk (the back-test at Stage 0 on cleared events in the history; the cohort reading at the first replica's 24 months); threshold ⚠ 38% at the band's low end.
- The uplift's loss against the pool (assumption 2) — **unmeasured input**; owner: model risk; convergence: the first replica's 24-month cohort reading.
- The switch-out ratio, seasoned against unseasoned (the hypothesis) — **unmeasured input**; owner: the account line (CASS and closure counts by cohort); convergence: the first replica's 24 months.
- The seasoning-query rate (⚠ 0.5–1.5%) — **unmeasured input**; owner: the cell lead; convergence: the first replica's six months.
- The cleared-event count per drawn account (⚠ 3–12 a year) and the time to clear (⚠ 5–40 days) — **unmeasured inputs**; owner: the Stage 0 back-test; convergence: the back-test output.
- The variation-notice and CONC 5.2A positions on the schedule — **standing constraint, designed for**, with what a ruling would settle named; owner: the conduct function; convergence: the signed position before Stage 1.
- The seasoning input and schedule in the engine — **build item**; owner: the limit-engine team; convergence: the Stage 0 back-test reads cleared events.
- The 15th handler at the high corner — **build item** (a hiring line, not a person until the recurring query line is read); owner: the cell lead; convergence: the first replica's six months.
- C7's and earlier carried items — carried unchanged; the F2 audit's S2 closed here; S1, S3, F-5, F-6 carried to the C7 record's next regeneration.

```
GATE VERDICT — on the cumulative architecture C1 to C8
  logical limb:      PASS WITH ONE FAIL DISPOSED   checks failed: 1 (SCIS 2 · 4 · 6 — below the pass line; re-tested at the failure value, 29.5%; carried as a design finding)
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     FMOS 30.5% worst corner at the set price (25.8% at the band's low end / 32.8% at its top) / 154.4% best (by hand; `fit_margin.py` output in verifier r8) · binding gate the loss rate on the pool: surplus 0.47 points at the assumed high corner, unmeasured; the default-funded gap may consume 0.3–0.5 of it — nil surplus at the top of that band · conventional additions used ⚠ 1.05–1.28 of ⚠ £8 rounded (0.50–1.78 unrounded); the R8 line ⚠ 5–15 removed
  price:             14.0% simple a year on the daily drawn balance = £140 per £1,000 drawn (band ⚠ 135–142.5); no fee; collected from receipts (C6, unchanged; F3 does not reprice)
  partner:           none new; the C7 class carries the seasoned figure in the same element
  decisions:         34 unmeasured inputs (28 carried, 6 new), 12 build items (10 carried, 2 new), 1 standing-constraint set (1 new row), 2 structural limits (carried), 1 carried question (fixed against variable, C6), 1 design finding (new: the SCIS); 1 actor-level FAIL at the pessimistic corner disposed with the force named
  capacity figure:   20,400 exception hours per cell a year at central (21,900 at the high corner), 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15; the 15th at the high corner) at 1,400–1,600 productive hours — used throughout   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; two new free counts named and unmeasured   VA-97
  gates driven:      16; first to fail on evidence: the loss rate, margin 0.47 points at the set price; second: the default-funded gap on the same line; third: the price condition's room (5.90)   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r8-2026-09-21.md   VA-90
  inherited:         R7, R6, R5, R4, R3, R2, R1 PROVISIONAL — R8 cannot exceed them; F1 and F2 closed PROVISIONAL with conditions carried   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design's FIT; the SCIS FAIL is disposed with owner and convergence; the model files are build items   VA-153
  launch constraints:none inside SR1–SR3 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn; at the Stage 1 count the worst-corner margin is 4.0% at the set price by the convention (4.8% with seasoning nil at release), 0.3% at the band's low end   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; the price sets where on that line the gate sits; the seasoned uplift adds capital on the same accounts   VA-160
  function gate:     F3 (C8–C10) — not yet; C10 by number
  VERDICT:           PROVISIONAL
```

**R8 failure test.** Would R8 have failed? Three conditions. First, nothing accumulates that a rival cannot read: the flow does not; the record of clearance through the receipts share does — a rival reads it and cannot fund from it. Second, the accumulation is a term and not a record: it is a record; the export is free and the price is flat. Third, the switching cost is too small to matter: **it is** — the SCIS says so at two corners — and the design does not fail on it because the margin holds at the failure value and the F3 rule forbids the term that would raise it. The third condition is the finding, and it is carried, not hidden.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the calibration of the seasoning schedule on the bank's own history; the key resource — R9
  - the at-scale price hold; the yearly rate review; the funding line's movement with Bank Rate; the shelf check for any supplier binding at launch; the moat test on the SCIS finding — R10
- **Unmeasured inputs (new at C8, 6):** the average seasoned uplift; the uplift's loss against the pool; the switch-out ratio by seasoning; the seasoning-query rate; the cleared-event count per drawn account; the time to clear. **Carried from C1–C7 (28):** unchanged.
- **Build items (new at C8, 2):** the seasoning input and schedule in the engine; the 15th handler line at the high corner. **Carried (10):** the CTM and AOM model files; the accrual ledger; the charge-first split; the representative example and APR basis; default funding's authorisation, notice and record; the term and the CONC 4.7 information; the limit-history placement; the release order's instrumentation; the element's population rule; the conformance test.
- **Standing constraints (new at C8):** CCA 1974 s.82 (a limit rise as a variation, notified); CONC 5.2A (the creditworthiness assessment at acceptance covering the schedule) — designed for, with what a ruling would settle named. C7's and earlier: unchanged.
- **Structural limits (carried):** the C1 limit rule's exposure model; the Stage 1 margin below 25% at every point of the band; the unconnected account's single conviction moment. **New at C8:** none.
- **Design finding (new at C8):** the SCIS below the pass line — the switching cost is genuine and too small relative to the spend; position is held on value.
- **Carried question (C6):** a fixed rate against a Bank Rate–linked rate.
- **TAM data object:** v3 stands; no narrowing at C8 (seasoning selects nothing; it grows on the selected pool). The C8 record is added as a consumer at v4 (C10 by number).
- **F2 audit and verification items:** S2 closed (AOM v8 3b); S1, S3, F-5, F-6 carried to the C7 record's next regeneration; F-2 closed (the headroom split); F-3, F-4 carried.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Customer of record declared; one run per customer of record (VA-154) | PASS — one | header |
| F3 ordering — store of value before theory | PASS | SR1 |
| Extended product use routine stated in order; the block as one operation | PASS — five steps; the rule's single input | SR1 |
| Store of value type named; the other two excluded by reason | PASS — data accumulation | SR1 |
| Customer-ownership test | PASS — the record is the customer's; the position is not portable | SR1 |
| Trajectory stated with the flat case | PASS | SR1 |
| ToC parameter, theory (researcher, year, paper), context, outcome | PASS — Sharpe 1990 | SR2 |
| Contrast theory named; fragile-findings check | PASS — Rajan 1992; none on the list | SR2 |
| Hypothesis with falsification condition; named assumptions | PASS — three | SR2 |
| Mutation gate before the strategy; ≥ 2 genuine mutations; justification mode false | PASS — five | SR3 |
| Exactly one structural move | PASS — WP-1 v2 | SR3 |
| Switching cost test — genuine, not artificial | PASS | SR3 |
| R5 interaction — activation and accumulation share the mechanism | PASS | SR3 |
| Structural, not contractual | PASS | SR3 |
| Invisible accumulation; at-scale test | PASS | Productizing |
| Cumulative BFF read cold; central mechanism named (parent's brief) | PASS | BFF |
| Considered and not chosen with reasons (VA-4) | PASS — eight | Considered |
| Synthesis check with the analogue's limit (VA-1) | PASS | Synthesis |
| VA-106 line — every requirement; "no" with reason | PASS — five served, two no | VA-106 |
| VA-127 — one row per behaviour; two arithmetic lines; FAIL rows forced | PASS — seven rows; one PROVISIONAL forced | VA-127 |
| VA-102 — tracks opened at arrival; dispositions; counterparty drivers | PASS — none new | VA-102 |
| VA-103 — every earlier requirement re-verified; FIT per row | PASS — seven rows | VA-103 |
| VA-80 — no forward references | PASS | throughout |
| VA-23 — no launch constraints in the design | PASS | throughout |
| VA-73 — completeness contract | PASS | throughout |
| Conventional line named and removed; cap line printed (F3 rule, RD-030) | PASS — ⚠ 5–15 removed; 6.72 remaining | Financial |
| ABC bottom-up, every line with driver and volume (RD-031) | PASS — seven lines | Financial |
| Four-layer floor printed; each layer with tier and basis | PASS — 55.04–107.28 | Financial |
| Carrying check printed | PASS — carries | Financial |
| FMOS ≥ 25% at the worst corner | PASS — 30.5% (25.8% at the band's low end) | Financial |
| Binding gate by driving (VA-84) | PASS — 16 gates; the loss rate first | Financial |
| Independence (VA-97) | stated — NOT shown; free counts named | Financial |
| Spread count (VA-162) | PASS — printed; Stage 1 4.0% | Financial |
| Shared input (VA-160) | PASS — the loss rate | close |
| Position-holding assumption named (F3) — table; each assumption in the fit model; re-test at the failure value | PASS — three assumptions; re-test 29.5% | Financial |
| **F3 barrier score — SCIS ≥ 5 pass; ≤ 3 NCR** | **FAIL — 2 conservative (NCR) · 4 central · 6 optimistic; disposed** | Financial |
| Three-limb close; GATE VERDICT block (VA-89, VA-91) | PASS — printed | close |
| Capacity figure, one number (VA-91) | PASS — 20,400 (21,900 at the high corner) | close |
| Verdict composition (VA-95); `check_verdict_order.py` | PASS — PROVISIONAL; IN ORDER (verifier r8) | close |
| Loop-backs (VA-151); loop-gate branch (VA-153) | PASS — 0; no FIT FAIL | close |
| Carried items classified (VA-82) | PASS | Carried |
| Verification artefact exists (VA-90) | PASS — verifier r8 | close |
| Incremental write (VA-88) | PASS | header |
| House-style checker run | recorded in the f1-status file | — |

---

## Quality check

- Does the switching cost grow from genuine value accumulation? **Yes** — cleared events on this account.
- Could an incumbent replicate this without changing their BFF? **No** — an incumbent with an application-based overdraft has no daily rule to give a second input to, and no receipts share to define a cleared event.
- Is the trajectory material within a commercially relevant timeframe? **Partly** — material in the limit (⚠ 15–30% by 36 months); not material as a switching cost against the spend (SCIS 4 at central). Stated as the design finding.
- Does the customer experience the accumulated asset as theirs? **Yes** — the seasoning line in their history, exportable.
- Confidence: **Medium** — the mechanism is the best-evidenced in relationship lending (T1 literature); the schedule's figures are all T4; the score is honest and below the line.

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15, C5 G1–G10, C6 H1–H12, C7 I1–I13)

- J1 — Sharpe, S. A. (1990), "Asymmetric Information, Bank Lending, and Implicit Contracts: A Stylized Model of Customer Relationships", *Journal of Finance* 45(4): 1069–1087.
- J2 — Petersen, M. A. and Rajan, R. G. (1994), "The Benefits of Lending Relationships: Evidence from Small Business Data", *Journal of Finance* 49(1): 3–37.
- J3 — Ioannidou, V. and Ongena, S. (2010), "'Time for a Change': Loan Conditions and Bank Behavior when Firms Switch Banks", *Journal of Finance* 65(5): 1847–1877.
- J4 — Rajan, R. G. (1992), "Insiders and Outsiders: The Choice between Informed and Arm's-Length Debt", *Journal of Finance* 47(4): 1367–1400.
- J5 — Klemperer, P. (1987), "Markets with Consumer Switching Costs", *Quarterly Journal of Economics* 102(2): 375–394.
- J6 — Farrell, J. and Klemperer, P. (2007), "Coordination and Lock-In: Competition with Switching Costs and Network Effects", *Handbook of Industrial Organization* vol. 3, ch. 31.
- J7 — Boot, A. W. A. (2000), "Relationship Banking: What Do We Know?", *Journal of Financial Intermediation* 9(1): 7–25 (review; the hold-up and soft-information strands).
- J8 — CMA (2016), Retail banking market investigation, final report — SME current-account switching about 4% a year. T1.
- J9 — Pay.UK, Current Account Switch Service — seven-working-day guarantee; redirection of payments for 36 months. FACT.
- J10 — Consumer Credit Act 1974, s.82 (variation of agreements) and the Consumer Credit (Agreements) Regulations 2010 (modifying agreements). FACT.
- J11 — FCA CONC 5.2A (creditworthiness assessment) and CONC 6.7 (post-contract business practices). Read for the positions at Productizing.
- J12 — PRA PS9/24, Basel 3.1 standards — 10% credit-conversion factor on unconditionally cancellable commitments from 1 January 2027; CRR Art. 123 (75% retail risk weight). FACT.
- J13 — PRA SS1/23, Model risk management principles for banks — validation of models and their inputs. FACT.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | Created at R8 by the runner (Path C, mode 3, autonomous). PROVISIONAL, capped by R1–R7 (VA-95). Object-after to 23 September 2026 17:00. Opens Function 3. One registry row FAIL (SCIS) recorded and disposed. House-style checker run on this file: result recorded in the f1-status file. |
