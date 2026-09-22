# A business bank's credit facility line — challenge seven (R7) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R7 carries and closes Function 2. The access block is that the limit exists only where the bank shows it: a customer who plans in accounting software, or whose accountant plans for them, sees a forecast shortfall the bank will cover — and seeks a facility elsewhere, or is sold one. The one move publishes the released standing limit as the account's pre-agreed credit line in the balance the bank already serves to every account-information reader under the Open Banking standard, and the receipt splits as the transaction lines they are. No agreement, no fee, no partner programme: the class that holds the seat where the shortfall is first foreseen — the accounting platforms, the account-information providers between them and the bank, and the accountants who work in the platforms — carries the limit because each already reads the element it sits in. The class is loss side (the platforms lose lender-referral fees; the accountants lose application packs) and is selected on that ground (VA-147). The verdict cannot exceed R1–R6's PROVISIONAL (VA-95). The move adds ⚠ £0.00–0.01 per £1,000 drawn a year; the conventional R7 line (⚠ 6–35 — partner commissions, referral fees, broker fees) is removed; cumulative conventional additions used ⚠ 0.05–0.28 of ⚠ £8 (RD-030). Floor ⚠ £54.04–106.28. Margin at the worst corner **31.7% at the set price**; 27.0% at the band's low end, 34.1% at its top. Binding gate unchanged: the loss rate on the flow-underwritten pool — the 25% margin fails above ⚠ 4.57% at the set price; the assumed high corner is 4.0%. The TAM data object is versioned at C7 (v3) with the C6 narrowing by the named block "price" recorded and the checking script's output; the surviving volume does not move.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c6-v1-2026-09-21.md` (R6, PROVISIONAL, object-after to 23 September 2026 17:00), and the C5, C4, C3, C2 and C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3. **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F2 rule this record works under (Tom, 16 September 2026).** R4 to R7 remove the blocks the conventional form pays for. The conventional R7 line is ⚠ 6–35 per £1,000 in the counterfactual (RD-030): broker commissions, platform referral fees, partner marketing and the partner desk that runs them. This record names the block that line pays for, removes it, and books only what the one move costs.

**Customer of record (VA-154).** Customer of record: the business owner who holds the account (the migrated overdraft user and the never-borrowed customer with enough flow — one customer of record, one payer). The routine positioned in: the customer's solution-seeking routine for a foreseen cash shortfall — where they look, whom they ask, what they are sold. One run. No supplier binds at launch (the C10 shelf check is R10's by number).

**Sections in this record.** Defined terms. SR1 to SR5. Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C6. Financial check. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

- **Access block** — the reason a customer who is convinced (C4), needs nothing to use the limit (C5) and pays for it only from receipts (C6) still seeks or is sold a facility elsewhere: the limit is visible only in the bank's own account, and the shortfall is first foreseen somewhere else.
- **Seat** — the place in the customer's routine where a party reads the account; three seats are named at SR2.
- **Bank feed** — the connection through which accounting software and cash-flow tools read a business current account: the account-information service the Payment Services Regulations 2017 (reg. 69) require the bank to give an authorised provider, on the customer's consent, through the Open Banking standard the CMA Order 2017 mandates for the largest current-account providers.
- **Balance response** — what the bank returns to each reader on each balance call under the Open Banking account-and-transaction standard (v3.1): the balance, its type, and an optional list of **credit lines**, each with an amount, a type (*Available · Credit · Emergency · Pre-Agreed · Temporary*) and a flag stating whether the balance figure includes it.
- **Pre-agreed credit line** — the element of the balance response designed to carry an arranged overdraft limit. In this form it carries the released standing limit (WP-1) with the flag set to *not included*, so the balance figure every reader reconciles stays the actual credit balance and the limit is shown beside it. *Runner's call* — the accountant's ledger must reconcile to the statement balance; a balance figure that includes an undrawn limit would not.
- **Published limit (PP-1)** — the Partner product: the released standing limit carried as the account's pre-agreed credit line, and the charge and repayment splits carried as the transaction lines they already are. A data property of the account; not a product sold to any partner.
- **Account-information provider** — the authorised intermediary (an aggregator) most platforms use to read the bank; it passes the balance response through in its own format.
- **Forecast shortfall** — a shortfall the customer's or the accountant's cash-flow forecast shows ⚠ 2–12 weeks ahead — before the bank's scheduled-payment file (C4's placement trigger) sees it.
- **Connected account** — an account with a limit that a platform or an accountant reads through a bank feed: ⚠ 45–70% of accounts with a limit (T4, logic at SR1).

---

## SR1 — Key customer segments and current routines

*Customer of record: the business owner who holds the account; the routine positioned in: the solution-seeking routine for a foreseen cash shortfall.*

**The segment (one, by KMC; the TAM data object v3).** The selected customer is the standard-tariff overdraft user with observable flow (SC-OD-STD-TARIFF, 40–70% of the bank's overdraft accounts), and — by the C1 form's reach — the never-borrowed account with enough flow. C6 narrowed nothing in the surviving volume: SC-OD-BELOW-BAND and SC-LOAN-USER were already outside the volume basis; the price (14.0%) now excludes them by a named block, recorded in v3 of the data object.

**The routine when a shortfall is foreseen — what the customer does today, in the order it happens.** Two routines, by where the shortfall is first seen.

*Routine A — the planning customer (a connected account).* The ledger lives in accounting software (Xero, QuickBooks, Sage, or a cash-flow tool built on one of them); the bank account feeds it daily. The forecast shows a negative balance on a date ⚠ 2–12 weeks out. The customer, or the accountant who runs the ledger, does one of: rings the bank (no relationship manager below ⚠ £500,000 turnover — CMA 2016 — so the call reaches a contact centre and an online application); opens the platform's lending marketplace, where non-bank lenders sit as apps (iwoca's integration with Xero is public); asks the accountant, who prepares an application pack or advises an alternative; delays a payment; puts personal money in. The bank's own app is opened last, if at all, because the ledger is where the planning happens.

*Routine B — the account-first customer (an unconnected account).* No software or a ledger not connected to the bank. The shortfall is seen when the bank sees it — the scheduled payment within the Bacs cycle — and C4's placement (the limit beside the customer's own history, in the account, that day) is the first and only seat. Nothing in this record changes Routine B; C4 and C5 already hold it.

**How many are in each.** Connected accounts ⚠ 45–70% of accounts with a limit — *T4 with logic:* Xero reports ⚠ about 1m UK subscribers (annual report FY2024, T2); Sage and QuickBooks carry the rest of the cloud-ledger market; SMEs with employees number ⚠ 1.4m (DBT 2025, T1) and are the population with flow enough for a limit; Making Tax Digital for income tax (from April 2026 for income above £50,000, FACT) is moving sole traders onto software. Threshold: below ⚠ 30% connected the gateway route carries a minority and R7's move is a convenience, not an access solution — the record stands, the count line moves. Convergence: the bank's own count of accounts with an active account-information consent (a red field: ⚠ [share of business current accounts with a live third-party consent]).

**What SR1 does not do.** It does not name a partner, a category entry point or an intermediary; those belong to SR2.

---

## SR2 — Gateway partner

**Affordability screen first (VA-92, VA-164).** The maximum the architecture can pay any holder of the gateway role, from the binding gate and the cap, before any candidate is named. The first input is the tariff given up (C6's pricing-committee row): at the pessimistic corner that row is −£234m, so nothing is payable to anyone; at the central corner (+£156m) the room above the operating bar at the set price is 7.15 per £1,000 (= ⚠ £24–41m a year on the drawn book) and the remaining cap is ⚠ 7.72, so up to ⚠ 7.15 per £1,000 could be paid and the 25% margin held. **The design pays 0.** Any candidate whose case needs a payment is bounded by 7.15 at central and 0 at pessimistic.

**Existence test (VA-92).** Is there a holder of "controls the customer's awareness, trust and access at the moment of need" outside the bank? *Partly.* For a connected account the forecast in the software sees the shortfall ⚠ 2–12 weeks before the bank's payment file does, and the advice given at that moment — by the platform's marketplace prompt or by the accountant — is where an alternative facility is sought. For an unconnected account the bank's own account is the only seat: an internal holder admitted, and C4 already holds it. The live question is therefore not "which partner to sign" but "does the limit reach the seat where the shortfall is first foreseen?".

**The two-class enumeration (VA-147) — every candidate present in the routine at the moment of need, with the sign of the architecture's effect on its own book.**

| Candidate | Where it stands in the routine | Effect on its own book | Class | What its case is bounded by |
|---|---|---|---|---|
| The bank's own standard-tariff overdraft line | the account (Routine B; Routine A last) | takes — the tariff pool (C2, Reading D ⚠ £13–231m a year) | loss side — the venture itself (mode 3); priced at C6, not a partner | — |
| The bank's relationship manager | absent below ⚠ £500,000 turnover (CMA 2016) | 0 | not present | — |
| The accounting platforms (Xero, QuickBooks, Sage and the cash-flow tools on them) — a class | the ledger and the forecast; the lending marketplace prompt (Routine A) | takes — lender-referral fees on referred facilities: ⚠ £0.2–3m a platform a year (T4: platform-referred non-bank SME lending ⚠ £60–300m a year × referral ⚠ 1–3%, across three large platforms); neutral on the subscription core | **loss side** | the referral pool — lost whether or not the platform carries the limit, because the limit exists on the account either way |
| The accountants who run the ledger — a class | the forecast; the advice at the shortfall; the application pack (Routine A) | takes — application-pack fees ⚠ £300–1,500 a pack (T4; sub-£25,000 facilities rarely carry a billed pack); neutral on compliance and bookkeeping fees | **loss side** | the pack fee — lost whether or not the accountant reads the limit |
| The account-information providers (the aggregators between the bank and the platforms) — a class | between the account and the ledger (Routine A) | 0 — paid per connection by the platform; the venture pays nothing | neither — a conduit; its pass-through behaviour is a VA-127 row | — |
| Commercial finance brokers | absent for sub-£25,000 tariff overdrafts (brokers place larger facilities; T4) | takes — commission ⚠ 1–5% of a placed facility | loss side, not present | — |
| Non-bank receipts-share and fintech lenders (iwoca, Capital on Tap, YouLend) | present only as the alternative the customer is sent to, not as a party in the bank customer's routine | takes — they lose the customer to a lower price on the same account | loss side, no seat — cannot carry a rival bank's product | — |
| Card acquirers and payment platforms | not in the routine of an account-funded shortfall | 0 | not present | — |

**Preference (VA-147).** Loss side, and both loss-side classes present at the seat (the platforms; the accountants) are selected together. No gain-side selection is made, so no reason from the admissible list is needed. Durability: the loss-side case does not fall at scale — the referral pool and the pack fee are lost by the C1 form at any count, so the class's surplus from carrying the limit is its own product's accuracy (SR3), which grows with the connected count.

**Presence (VA-155) — the third case.** A class present collectively; no member present in all routines. No platform is in every connected customer's ledger (three large ones between them carry most); no accountant serves more than a few hundred clients; ⚠ 30–55% of accounts are in no platform at all. One product (PP-1) activates the class across three seats: **seat 1** the bank-feed balance line (the platforms, through the aggregators); **seat 2** the cash-flow forecast (the platforms; the accountants); **seat 3** the client ledger (the accountants).

**Form (VA-165):** *aggregate* — the platforms are the aggregate form through which the accountant class is reached; no single firm is chosen because no single firm is in every routine and the standard reaches all of them at once. **Hours per close read for:** the aggregate form — there is no close: no platform is approached, because the element the limit sits in is one each already reads; the hours are the bank's own conformance test against the three largest platforms and three aggregators, ⚠ 100–200 h once (T4, a build estimate), read for the aggregate form.

**The gateway partner, named.** The class of account-information readers of the customer's account — the accounting platforms, the aggregators that serve them and the accountants who work in them — present at the moment the shortfall is first foreseen, in the balance line and the forecast. Current relationship to the venture: unaware; each reads the account today and shows a balance with no credit line.

**A stated absence, for the record (VA-92's third answer).** No party outside the bank holds the seat for an unconnected account. The test that would show otherwise: a share of unconnected released accounts whose first funded event follows a facility application elsewhere — read from the credit bureau footprint at the first replica; above ⚠ 10% a seat exists that this record has not found.

---

## SR3 — Integration theory of change

**Class of problem: a coordination problem.** The venture needs a class of parties to carry a product none was asked to carry, each acting alone, none willing to sign an agreement or take a fee for it, and the class changes membership every year. The conventional answer is bilateral: an agreement, a fee and a partner desk per platform — the R7 line the counterfactual books.

**Current state (as a state).** Every platform and accountant reads the account through the standard; the balance response carries no credit line for most accounts; the forecast shows a shortfall the bank will cover; the marketplace prompt fires; the accountant prepares a pack or advises an alternative.

**Desired state (as a state).** Every reader of the account sees the pre-agreed limit beside the balance with no contact from the bank; the forecast shows the shortfall covered; the prompt does not fire; no pack is prepared; the customer does nothing (C5) and pays from receipts (C6).

**Theory: coordination through a compatibility standard with an installed base — Farrell and Saloner 1985, "Standardization, Compatibility, and Innovation", *RAND Journal of Economics* 16(1).** Where an installed base already reads a standard, an actor adopts a compatible feature without a decision: the cost of carrying it is the cost of conformance, already paid, and the benefit is its own product's compatibility with what the rest of the base shows. Applied here: the bank does not ask any reader to do anything. It publishes into an element (the pre-agreed credit line) that every conforming reader already parses; each reader's own product — the forecast, the ledger — is correct with the element and wrong without it (a forecast that shows a shortfall the bank will cover is a wrong forecast). Mechanism: the standard makes the adoption decision; the reader's own accuracy makes the championing. No reader must know the venture exists.

**Unifying mission.** The client's cash position, seen correctly, in the tool where they plan. The platform sells it; the accountant is paid for it; the aggregator conveys it. The limit is part of the cash position; a reader that omits it shows the position wrong.

**Stress test.** The contrast theory is asymmetric motivation (Christensen and Raynor 2003, *The Innovator's Solution*): a fee-paid partner's motivation shrinks as the product substitutes for its core, so a gain-side partner is a launch partner at best. Applied here: no fee is paid, and the platform's core (the ledger and the forecast) is served, not substituted; the pool the platform loses (referral fees) is lost by the C1 form whether or not it carries the limit. The theory does not overturn the design; it names why mutation B (a display agreement with a fee) is rejected. The customer-side theory is physical availability (Sharp 2010, *How Brands Grow*; Romaniuk and Sharp 2016): the product is present in the buying situation where the customer looks — the forecast, not the bank's app. Fragile-findings check: Farrell and Saloner's result is a model, not a field finding; the design uses its direction (an installed base lowers the adoption decision to nothing), and the hypothesis at SR4 measures whether the platforms display the element with no contact.

**Why this theory and not a referral theory.** A referral theory (pay the platform per referred customer) would need the platform to know the venture, decide, and be paid — three acts the standard removes. It would also reintroduce an application, which C1 eliminated: a referral is to a facility one applies for; a published limit is already there.

---

## SR4 — Integration strategy

**Step 4a — baseline.** The C1–C6 form shows the limit (WP-1), its history (CP-2), the available balance (WP-2 v2) and the charge (PC-1) in the bank's own account only. A connected customer sees, in the tool where they plan, a forecast shortfall the bank will cover — and the tool's marketplace and the accountant answer it with a facility elsewhere. The Partner track in the CTM is flagged `[REQUIRES C7]`; nothing activates anyone outside the bank. On the access block the baseline does this: nothing.

**Step 4b — candidate mutations.**

```
MUTATION GATE — R7
baseline: the limit, its history and the charge exist only in the bank's own account; the connected customer's forecast shows a shortfall the bank will cover, and the platform's marketplace or the accountant sells a facility elsewhere; the Partner track is flagged and no party outside the bank carries the limit
mutation_A: publish the released standing limit as the account's pre-agreed credit line in the balance response the bank already serves to every account-information reader (flag: not included in the balance figure), and the charge and repayment splits as the transaction lines they are | reason_considered: every platform, aggregator and accountant already reads the element; the limit reaches the seat where the shortfall is first foreseen with no agreement and no fee | verdict: adopted | reason_verdict: one move, zero partner cost, activates the whole class at once, serves R4 and R5 by mechanism; the loss-side class is selected as VA-147 prefers
mutation_B: a display or referral agreement with each large platform — a fee per displayed limit or per funded event (the conventional R7 form) | reason_considered: a paid partner might promote the limit inside the forecast, not only show it | verdict: rejected | reason_verdict: a gain-side selection with a loss-side class present and no admissible reason; the fee competes with the platform's core the moment the limit displaces a referral; bespoke per platform (fails the one-decision test); books the conventional line (⚠ 6–35) the F2 rule removes
mutation_C: an accountant programme — a partner portal, dashboards, a referral credit | reason_considered: the accountant is the trusted adviser at the shortfall | verdict: rejected | reason_verdict: a channel, not a gateway — the accountant is already reached through the client ledger the feed populates; a programme with its own budget line fails the productising test; a credit is a fee
mutation_D: list the bank's line in the platforms' lending marketplaces beside the non-bank lenders | reason_considered: the marketplace is where the connected customer is sent | verdict: rejected | reason_verdict: a marketplace listing invites an application, which C1 removed; the limit is not applied for, so it has nothing to list
mutation_E: the bank's own cash-flow forecast inside its app, to compete with the platforms | reason_considered: moves the planning seat into the bank | verdict: rejected | reason_verdict: the customer plans where the ledger is, and the accountant is not reached at all; the roadmap form's spend, on a seat the standard reaches for nothing
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: A
evolvedBFF: a bank whose credit facility is a standing property of every account with enough flow, priced below the tariff, released in stages against a kill band, believed because the customer checks it against their own history, used without an act, paid for only from receipts — and present wherever the account is read, because the limit is published as a property of the account's balance under the standard every reader already conforms to
synthesisCheck: Square Loans' offer inside the Square dashboard for the bank's account line, because the limit is present where the customer already reads their money — through a public standard every reader parses rather than a proprietary dashboard the venture controls
```

**Step 4c — decision.** A adopted. The evolved BFF is stated in SR5.

**Integration strategy.** *Make the limit a property of the account's published balance, not a product offered to partners.* The one structural decision: the released standing limit is written into the pre-agreed credit-line element of the balance response — the element the standard designed for an arranged overdraft limit — with the flag set so the balance figure stays the actual balance. From that decision everything else follows without a further act: the aggregator passes the element through because its product conforms to the standard; the platform shows a credit line beside the balance because it already renders that element for overdrafts; the forecast that reads the balance and its credit line shows the shortfall covered; the accountant reconciling the ledger sees the limit on the client's own account; the marketplace prompt, keyed to a forecast shortfall, does not fire. The decision fires at the seat where the need is first foreseen — the forecast — not downstream at an application. Remove the decision and nothing outside the bank knows the limit exists; keep it and no one outside the bank has to be asked.

**Dual effect (the elegance test).** The same publication is the customer's conviction moved to where they plan (C4's placement, ⚠ 2–12 weeks earlier, in the customer's own numbers) and the customer's use with nothing to do (C5) extended to the moment a forecast would otherwise send them elsewhere. The partner's activation and the customer's F2 journey are one mechanism read from two seats.

**Mechanism — elimination, not reduction.** The access block was that the limit was absent from the seat where the shortfall is first foreseen. After the move the limit is present at every seat that reads the account. If the customer used the product entirely alone, would the block still occur? For an unconnected account there is no seat outside the bank, and C4 holds; for a connected account the seat now carries the limit. No partner decision remains for the block to depend on.

**What is published and what is not.** *Published:* the released limit (WP-1) as a pre-agreed credit line; the charge-first split of each receipt (WP-3 v2) as two transaction lines, which the feed already carries; the funded-event notice line (C5) as the transaction it is. *Not published:* the shadow limit (WP-5) — an unreleased account shows no credit line, so the path's discipline (C3) holds outside the bank; the limit history (CP-2) — it stays in the account, where the conduct reviewer signed it; the rate as marketing — the feed carries account information, not a promotion (assumption 5).

**R1 consistency.** Nothing in the exposure model changes; nothing is added to the product. The limit is published, not sold; the engine, the rule and the four removed operations are untouched.

**R2 interaction.** The charge appears in the customer's ledger as receipt-split lines, so the year's charge (CP-1's figure) is reconcilable in the accountant's own accounts. Nothing in the KMC changes.

**R3 interaction — flagged.** Released accounts only are published; the release flag (WP-5) gates the element. The stage reading gains nothing; the path is unchanged.

**R6 interaction.** The charge lines in the feed are ordinary transactions; no debit is explained anywhere because none exists.

**At-scale test.** The mechanism is one element in a response the bank already serves ⚠ 4 times a day to each connected account (the unattended-access limit under the UK SCA-RTS, art. 36(5)): ⚠ 0.5–0.78bn balance calls a year carrying one more element. Automated at any volume; no founding-team step; no partner desk; no per-platform work after the conformance test.

**R8 signal: yes.** A limit that sits in the customer's own ledger, in the tools they keep, is a switching cost by presence: a rival account shows no credit line in the same forecast. Flagged for R8 by number.

**Hypothesis (falsifiable).** At the first replica's six months, among connected released accounts: (a) ⚠ 2 or more of the 3 largest UK platforms display the pre-agreed line with no contact from the bank; (b) the C4 conviction measure (the share of released accounts whose first funded event is followed by neither a query nor a switch-off) is ⚠ no lower than among unconnected accounts; (c) the display-query rate ("why does my software show more than my balance") is ⚠ ≤ 0.3% of connected accounts a year. **Falsified** if (a) fewer than 2 of 3 display it at 12 months — the element is not read, and R7 loops back to SR2 with a gain-side selection on the admissible reason "no loss-side party reads the seat" — or if (c) exceeds ⚠ 1%. Read at the first replica's six-month reading; no cost beyond the count and one reading of each platform's display.

**Named assumptions (T4 with logic).**
1. *Connected share ⚠ 45–70%* — SR1; threshold 30%; convergence: the bank's consent count.
2. *The three largest platforms parse and display the pre-agreed credit-line element* — T2 for the standard (the element exists for arranged overdrafts and is rendered as a credit line by platforms that show overdraft limits today); T4 for the display of a limit the customer never applied for; convergence: hypothesis (a).
3. *The aggregators pass the element through* — T2: the standard is what they sell conformance to; T4 for each provider's mapping; convergence: the conformance test before Stage 1.
4. *Forecast lead ⚠ 2–12 weeks* — judged from the forecast horizons the platforms offer (30–90 days); threshold: below one week the seat is no earlier than the bank's payment file and R7's move is Routine B's placement in a second place; convergence: the platforms' own documentation.
5. *The element is account information, not a financial promotion* — desk position: the balance response is data the bank must supply under PSRs 2017 reg. 69 on the customer's consent; it carries no invitation and no rate; the platform's rendering is the platform's communication, not the bank's; CONC 3 does not reach a data element, and the representative example (C6) travels with the rate in the account, not in the feed. What a ruling would settle: whether publishing an undrawn pre-agreed line for an account that never applied is an "invitation" — the design keeps the element factual and the conduct function signs the position. Owner: the conduct function; convergence: the signed position before Stage 1.

**Credibility mechanism (VA-81).** Receiver: the accountant and the planning customer, at the forecast. Proposition: "the limit your bank shows is on your account already; this shortfall is covered." Instrument in use today: the bank-feed balance line — the one figure the accountant reconciles to the bank statement every month, and the platform's own credit-line display, which it already renders for arranged overdrafts. Public-record supplier: the standard's balance resource (Open Banking account-and-transaction specification, public) and the aggregator's published conformance.

**Property-holder test (VA-71).** *Publishes the element for released accounts and withholds it for unreleased ones* — holder: the bank's account-information team (internal; a new track row). *Passes it through* — the aggregator. *Displays it and forecasts against it* — the platform. *Reads it and does not counsel a rival facility* — the accountant. *Signs the desk position* — the conduct function. *Answers a display query* — the exception cell. Each has a row on a track in the CTM v7.

**Three tests.** *Primary cause:* the limit was absent from the seat where the shortfall is first foreseen; the move puts it there. *Entry point:* the balance call the reader already makes, and the forecast it feeds. *Incumbent:* an incumbent can populate the same element today for an arranged overdraft — some do — but it has no standing limit on every account with flow to publish; the element carries C1's product, and the incumbent's form has nothing to put in it for the never-borrowed account. The test passes on the cumulative form (*runner's call*; the same reading as at R5 and R6 — recorded a third time for WS1).

---

## SR5 — Business form factor (C1–C7)

**The architecture's central mechanism.** The standing limit as a property of the account — computed from the flow, present before any need, published wherever the account is read. Remove it and every requirement fails at once: there is nothing to price (C2), release (C3), verify against history (C4), fund from (C5), charge for (C6) or publish (C7).

**The evolved BFF.** A bank whose credit facility is a standing property of every business account with enough flow: the limit is computed daily from the flow and shown in the account before any need arises (C1); it is priced below the tariff the customer pays today and the existing overdraft is retired into it (C2); it is released in stages against a kill band, with the rule proven on history before it is trusted (C3); it is believed because the customer checks it against the twelve months of their own shortfalls it would have covered (C4); it is used without an act, because a payment that exceeds the balance is met from it under a term accepted once (C5); it is paid for only from the money that comes in — one rate on the days drawn, a slice of each receipt, no fee and no charging date (C6); and it is present wherever the account is read — in the customer's ledger, the accountant's forecast and the platform's balance line — because the released limit is published as the account's pre-agreed credit line under the standard every reader already conforms to (C7). Read cold: one product, a limit that is a property of the account, inside and outside the bank.

**Components at C7.** WP-1, WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, CP-1 (amended C2, C4, C6), CP-2, PC-1 (resolved C6), **PP-1 (new C7 — the published limit)**. No component removed. F2 complete: Selling (CP-2, PP-1), Using (WP-2 v2), Payment (PC-1), Partner (PP-1) — each a view of the same limit.

**What the customer now has.** One limit, in the account and in the ledger; one history; one rate; one line per receipt; nothing to apply for, draw, pay on a date, or tell anyone.

---

## Considered / not chosen (VA-4)

- **A display or referral agreement per platform (the conventional R7 form)** — rejected at the mutation gate (B): gain side with a loss-side class present; bespoke; books the line the F2 rule removes.
- **An accountant partner programme** — rejected (C): a channel with a budget line; the accountant is reached through the ledger already.
- **A marketplace listing** — rejected (D): it invites an application.
- **The bank's own forecast in its app** — rejected (E): the planning seat is the ledger; the accountant is not reached.
- **Publishing the limit history (CP-2) through the feed** — not chosen: the feed carries balances and transactions; the history is a promotion the conduct reviewer signed for display in the account; publishing it through readers whose rendering the bank does not control would move the signed display outside the signature. The limit and the transaction lines are enough for the seat.
- **Setting the "included" flag to true (the available balance as the balance figure)** — rejected: the accountant's ledger reconciles to the statement balance; an included undrawn limit would show cash the business does not hold. *Runner's call*; the flag is the standard's own device for this.
- **Publishing the shadow limit** — rejected: an unreleased limit is not drawable; the path's discipline (C3) is kept outside the bank by the release flag.
- **A per-platform commercial term for the non-bank marketplace's loss** — not chosen: the referral pool is lost to the C1 form, not to R7; the design owes the platform nothing and pays nothing.

---

## Synthesis check (VA-1)

Square Loans presents its offer inside the Square dashboard — the merchant meets the limit where they already read their takings, before they look elsewhere. The bank's form does the same at the seat where its customer reads their money, which for the connected customer is the ledger and the forecast, not the bank's app. The difference is the channel: Square owns its dashboard; the bank does not own the platforms, and reaches them through a public standard each already conforms to — a credit-line element designed for exactly the object the bank now has on every account. The analogue's limit: Square's seat is proprietary and single; the bank's is a class of seats it controls none of, which is why the mechanism is a standard and not an agreement.

---

## VA-106 synergy line

Does the one move also serve an earlier requirement, with a mechanism? Six candidates:

- **R4 (conviction) — yes.** The forecast shortfall shown as covered is C4's placement moved to where the customer plans, ⚠ 2–12 weeks earlier, beside their own ledger figures. Mechanism: the credit-line element beside the balance the customer already trusts.
- **R5 (use) — yes.** The marketplace prompt does not fire and no application pack is prepared; the forecast shortfall needs nothing done. Mechanism: the forecast reads the limit as available.
- **R6 (buy) — yes.** The charge appears in the ledger as receipt-split lines, ordinary transactions; nothing to explain. Mechanism: the feed already carries transactions.
- **R2 (value) — yes, weakly.** The year's charge is reconcilable in the accountant's own accounts beside the tariff the ledger used to carry. Mechanism: the transaction lines.
- **R1 (design) — yes.** Nothing is added to the product; the limit is published, not sold. Mechanism: the same object in one more place.
- **R3 (scale) — yes.** The release flag gates the element; the path's discipline holds outside the bank. Mechanism: released accounts only.

R8 by number only (VA-80).

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per year unless stated; every ⚠ is T4. Two columns added under VA-147: effect on the actor's own book; surplus at scale.

| Actor | Behaviour needed | How often | Effect on own book | What it gains | What it costs | Best alternative and its surplus (VA-147: for a loss-side actor, the world in which the architecture exists and it does not carry) | Arithmetic (VA-157) | Surplus at scale | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|---|---|
| The accounting platform (class; per platform) | parses the pre-agreed credit-line element; shows it beside the balance; forecasts against it | per balance call, automated | takes (referral fees ⚠ £0.2–3m a year, lost to the C1 form either way); neutral on the subscription core | forecast accuracy — subscribers retained ⚠ 0.05–0.1% of ⚠ 1m × ⚠ £300 = ⚠ £150–300k; support contacts avoided ("my forecast shows a shortfall my bank covered") | ⚠ 0–40 h once to map an element already in the standard = ⚠ £0–4k | not display the element: surplus £0 (the referral pool is lost in that world too) | central: gain £225k − cost £2k − alternative's surplus £0 = **£223k** · pessimistic: gain £150k − cost £4k − £0 = **£146k** | rises with the connected count | **PASS** |
| The accountant (class; per client shortfall) | reads the pre-agreed line in the client ledger; at a forecast shortfall, tells the client it is covered; does not counsel a rival facility | per forecast shortfall | takes (application-pack fees ⚠ £300–1,500 a pack, lost either way); neutral on compliance and bookkeeping | hours not spent on a pack ⚠ 3–8 h at ⚠ £60–120/h, most of it unbilled for a sub-£25,000 facility; a client that does not fail | ⚠ 0.25 h reading the line = ⚠ £20–30 | prepare and bill a pack for a rival facility: its margin ⚠ £0–300 (fee less hours; often nil) | central: gain £400 − cost £20 − alternative's surplus £100 = **£280** · pessimistic: gain £180 − cost £30 − alternative's surplus £300 = **−£150** | unchanged | **PROVISIONAL — FAIL at the pessimistic corner.** Force: the client — a limit already on the client's account cannot be replaced by a pack the client has no reason to buy; the behaviour needed is only not to counsel a rival, and the client's own comparison (C4's history, C6's rate) is on the same screen. The accountant who bills packs profitably on sub-£25,000 facilities is a minority (T4) |
| The account-information provider (class; per provider) | passes the credit-line element through in its balance object | per call, automated | neutral (paid per connection by the platform) | conformance to the standard it sells; no support tickets on a missing element | ⚠ 0–20 h if the element is unmapped = ⚠ £0–2k once | drop the element: surplus £0 | central: gain £5k − cost £1k − £0 = **£4k** · pessimistic: gain £2k − cost £2k − £0 = **£0** | unchanged | **PASS at central; nil at pessimistic.** Force: the standard — an element in the specification is passed through by a conforming provider by construction; a provider that dropped it would fail the conformance the platform buys |
| The bank's account-information team (internal) | populates the element for released accounts; withholds it for unreleased ones; tests conformance with three aggregators and three platforms | once, then automated | adds (one fewer class of balance-mismatch contact) | the CMA Order conformance the bank already carries; the C4 conviction moment not contradicted in the customer's own software | ⚠ 400–800 h once = ⚠ £40–80k; the conformance test ⚠ 100–200 h = ⚠ £10–20k | leave the element empty: surplus £0, and the connected customer's forecast contradicts the limit | central: gain £0.15m (contacts avoided, judged) − cost £0.02m a year (amortised) − £0 = **£0.13m** · pessimistic: gain £0.05m − cost £0.02m − £0 = **£0.03m** | rises with the connected count | **PASS** — the mode-3 decision carries it in any case |
| The bank's conduct function | signs the desk position that the element is account information, not a promotion; reviews it yearly | once; yearly | neutral | a Partner product with no partner communication to review | ⚠ 40–80 h once = ⚠ £4–8k | review each platform's rendering as a bank communication: ⚠ 100–300 h a year; surplus negative | central: gain £0.02m − cost £0.001m − £0 = **£0.019m** · pessimistic: gain £0.01m − cost £0.002m − £0 = **£0.008m** | unchanged | **PASS** |
| The business owner (the connected customer) | reads the limit where they plan; at a forecast shortfall, does nothing | per forecast shortfall | — | the facility search avoided ⚠ 1–3 h; the unpaid-item and late-payment costs avoided (C5, ⚠ £30–135 per event) | nothing | search the marketplace or ask the accountant: surplus nil (it ends in a facility priced at or above the tariff) | central: gain £120 − cost £0 − £0 = **£120** · pessimistic: gain £30 − cost £0 − £10 (a delayed payment) = **£20** | unchanged | **PASS** |

**The accountant row, disposed.** The behaviour the architecture needs from the accountant is small — not to counsel a rival facility at the forecast — and the force that supplies it is the client's own screen: the limit, the history and the rate are on the client's account, and a pack cannot be sold against a facility that already exists. The pessimistic corner prices an accountant who bills packs profitably on facilities under £25,000; the record judges that a minority (T4) and names the reading that would show otherwise: the share of connected released accounts whose first funded event follows a credit application elsewhere, at the first replica (SR2's stated-absence test, read on the connected pool).

---

## Actor tracks (VA-102)

Three new actor classes this challenge — the platform, the account-information provider, the accountant — and one new internal holder, the bank's account-information team. **(1) Where does each track open?** Each opens at a state in which the actor does not know the venture exists: the platform "reads the account; shows a balance with no credit line"; the provider "passes the balance response through"; the accountant "reconciles the ledger to the statement balance". Arrival is the first balance call after the account's release — no later state is skipped. **(2) Where a transition carries no product by decision, what activity does the work?** The conformance test (the account-information team, once, AOM v7 3e) and the display-query script (the exception cell, AOM v7 3b) — both in the operating model with a driver. **(3) Which driver scales with a count of counterparties, and which routine is accountable?** `q.connected_accounts` scales with the customer's consents, not with a partner count; no acquisition activity exists by design — the mechanism that replaces it is the standard, and its cost is the conformance test. No counterparty with an acquiring transition. Decisions stated on each row in the CTM v7.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** PP-1 (the published limit) is added: the released standing limit carried as the account's pre-agreed credit line, and the receipt splits as transaction lines, in the balance and transaction responses the bank already serves. The Partner track's `[REQUIRES C7]` flag is resolved. No component is removed; no earlier component is amended.

**Earlier requirements this same move also serves (VA-106).** R4, R5, R6, R2, R1, R3 with mechanisms; R8 by number (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — unchanged.** Nothing is added to the product; the exposure model, the rule and the four removed operations are untouched. Property holder of "publishes" is the account-information team — a track row | re-verified: non-gating in mode 3; at-scale margin on the selected customer 31.7% at the set price |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — unchanged; the TAM data object versioned.** v3 records the C6 narrowing by the named block "price" (SC-OD-BELOW-BAND, SC-LOAN-USER excluded); the surviving volume is unchanged; the pool-at-risk block the checking script asks for is added from the C2 block. The KMC is untouched | re-verified: 31.7% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — one line added, no check failed.** The release flag gates the published element; the shadow limit is never published. SC gains the field build and the conformance test (⚠ £50–100k once) inside the 0–1 band. Stage 1 margin at the set price 4.8% | re-verified: Stage 1 4.8% at the set price |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — strengthened on one line.** The placement reaches the connected customer ⚠ 2–12 weeks earlier at the forecast (VA-106); CP-2 itself is untouched and stays inside the signed display | re-verified: 31.7%; cap line ⚠ 0.05–0.28 carried |
| R5 (C5 record v1.1) | use routine; routine disruption; Madrian and Shea; default funding; switch-off and reversal; the loss gap; CONC 5.2A timing | **re-verified — unchanged.** The forecast shortfall needs nothing done; default funding meets it when it arrives. The loss gate at the set price 4.57% (floor high 106.28 — unchanged at two decimals) | re-verified: 31.7%; loss gate 4.57% |
| R6 (C6 record v1) | lifecycles; CVTs; buy block type; Prelec and Loewenstein; mutation gate; price structure; representative example; R2 and R3 interactions | **re-verified — unchanged.** The charge lines travel in the feed as ordinary transactions; the representative example stays with the rate in the account; the price and the band do not move | re-verified: 31.7% at the set price (27.0% / 34.1% at the band's ends) |

No FAILED row. **Function-gate re-run (C7):** every earlier requirement re-run on the cumulative BFF — `bank-credit-facility-consistency-audit-F2-2026-09-21.md` and `bank-credit-facility-verify-F2-2026-09-21.md`.

---

## Financial check — the floor on four layers, the ceiling as a price and the cap

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, CP-1 (amended C2, C4, C6), CP-2, PC-1 (resolved C6), PP-1 (new C7).

**Pricing note (challenge skill section 7).** The gateway partner is not the payer; R7 sets no ceiling. The ceiling stays the paying customer's R2 KMC, resolved to the C6 price (140; band ⚠ 135–142.5).

**Count line (VA-155).** The count the gateway route carries at central: ⚠ 437,000 connected accounts with a limit (57.5% of 760,000) · the at-scale count: ⚠ 342,000–532,000 connected of ⚠ 760,000 with a limit (228,000 drawn) · the PCO screen: ⚠ 760,000 accounts with a limit (own base 950,000 × 80%) · the objective: the PCO's £148.5m at year five = ⚠ £1.06bn drawn at 140 = ⚠ 42,000–71,000 drawn accounts, against 228,000 at scale · partners active (G15): ⚠ 3 of the 3 largest platforms displaying the pre-agreed line at the first replica's six months; gate ≥ 2 of 3; margin one platform; the same for the three largest account-information providers.

**The partner's return (VA-156).** Neither fee-in-the-floor nor share-of-surplus: the venture pays the class nothing. Unit margin under the fee-in-the-floor reading (fee = 0.00): 31.7%; under the share-of-surplus reading (share = 0): 31.7%. The venture's reading: no return is paid; the partner's return is its own product's accuracy — a state of its book, not a payment from the venture. The classification decides nothing here because both readings carry the same margin; it is recorded so that a later fee, if one were ever proposed, would be read against the 7.15 of room and the 7.72 of cap.

**Partner business case (VA-99) — PP-1 as the enabler.** *earns:* the platform — subscribers retained by a correct forecast ⚠ £150–300k a year; the accountant — pack hours not spent ⚠ £180–400 a shortfall; the provider — conformance. *costs:* ⚠ £0–4k once (platform), ⚠ £20–30 a reading (accountant), ⚠ £0–2k once (provider). *beats_next_best:* against the world in which the limit exists and the reader does not show it — the referral pool and the pack fee are lost in that world too, so the alternative's surplus is nil. *operational_fit:* the element is in the standard each reader conforms to; no integration project. *timing:* at the first balance call after release; the conformance test before Stage 1. No `kmc` on any partner.

**What R7 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v7 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| serve the pre-agreed credit-line element in each balance response for a released account | per call, automated | e.balance_call on q.connected_accounts | 342,000–532,000 × ⚠ 4 a day × 365 = ⚠ 0.50–0.78bn | ⚠ £0.00001 (one element in a response already served) | ⚠ £5–8k | 0.00 |
| build the element's population rule (released accounts only; the flag not included) | HQ, once | e.field_build | 1 | ⚠ 400–800 h at ⚠ £100/h = ⚠ £40–80k once, amortised over five years | ⚠ £8–16k | 0.00 |
| test conformance with the three largest account-information providers and the three largest platforms | HQ, once | e.conformance_test | 6 | ⚠ 100–200 h = ⚠ £10–20k once, amortised over five years | ⚠ £2–4k | 0.00 |
| sign the desk position (account information, not a promotion); review yearly | HQ, once then yearly | e.field_position | 1 | ⚠ 40–80 h inside the existing 13 people | inside RC | 0.00 |
| answer a display query ("my software shows more than my balance") | cell | e.display_query on q.replica_accounts × connected share | ⚠ 0.1–0.3% of connected accounts a year = 150–700 per cell | 0.25 h | ⚠ 37–175 h per cell — inside the ⚠ 0–425 h of headroom booked at C5 (with C6's 50–125 h: 87–300 h used); no handler added; costed at the handler rate for visibility: ⚠ £3–14k | 0.00 |
| **R7 total** | | | | | **⚠ £0.02–0.04m** | **⚠ 0.00–0.01** |

*Runner's call on the display-query rate.* A credit line that appears in the ledger beside a balance it does not include will draw some questions from customers who have never had an overdraft; ⚠ 0.1–0.3% of connected accounts a year is judged from the C4 limit-query rate (⚠ 1–3% of accounts with a limit, most of it at release) scaled to the seat. Threshold: above ⚠ 1% the cell's headroom is used up with C6's queries and a handler is added (R7 line rises to ⚠ 0.05). Convergence: the first replica's six months.

**The four-layer floor at C7 (AOM v7 section 6).**

```
PVC  40.02–83.24   funding 15–30 · expected loss 20–40 · computing and payments 2.02–5.11 (C7: +0.00–0.01, the element in the balance response) · exceptions and write-off 3.00–8.13 (C7: +0.00, display queries inside the C5 headroom)
RC    2.02–5.04    unchanged — the desk position sits inside the existing conduct people
SC    0–1          unchanged — the field build and the conformance test (⚠ £50–100k once) sit inside the band
IC   12–17         unchanged — nothing published is exposure
FLOOR 54.04–106.28  (C6: 54.04–106.27; C5: 54.04–106.26; C4: 54.03–106.20; C3: 54–106)
```

**Carrying check (challenge skill section 8).**

```
CARRYING CHECK — R7
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v3 KMC-OD-STD-TARIFF)
  the price (C6)                        140.00 — band ⚠ 135.00–142.50 (unchanged at C7)
  floor                                  54.04–106.28
  operating bar = floor × 1.25           67.55–132.85
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  price against the operating bar        140.00 − 132.85 = 7.15 at the set price · 2.15 at the band's low end · 9.65 at its top
  carries                                true at every point of the band
  FMOS worst corner (price − floor high) ÷ floor high
                                         31.7% at 140 · 27.0% at 135 · 34.1% at 142.5
  FMOS best corner (price − floor low) ÷ floor low
                                         159.1% at 140 (the fit model's KMC-band figure, 418.1%, is not used)
  conventional additions used (RD-030)   R7 line ⚠ 6–35 removed; added ⚠ 0.00–0.01; cumulative ⚠ 0.05–0.28; remaining ⚠ 7.72 at the high corner
  max payable to any holder (VA-164)     7.15 at central (the room above the bar at the set price); 0 at the pessimistic corner (the tariff given up, C6); paid: 0
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C7.yaml`).** By hand: **31.7% at the worst corner at the set price; 27.0% at the band's low end; 34.1% at its top; 159.1% at the best corner. PASS on the 25% gate at every point of the band.** R7 adds ⚠ 0.01 to the floor's high corner and nothing to its low corner; no figure moves at one decimal. `fit_margin.py` is run on the at-C7 model; its output is in the verifier r7.

**Binding gate — by driving (VA-84).** Fifteen gates driven at C7: the fourteen of C6 and (15) the platforms' display of the element (G15). Ordered by margin at the set price:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.57%** at the set price (4.17% at the band's low end; 4.77% at its top); at C7 the loss line is 66.28 + 10L, and the bar is the price ÷ 1.25 = 112.00; zero margin at 7.37%; assumed ⚠ 2–4%; surplus 0.57 points at the assumed high corner. **First to fail.**
2. the default-funded loss gap (C5, gate 3) — on the same line; ⚠ 0.3–0.5 of the 0.57 points; unmeasured.
3. the price condition's room — 7.15 at the set price, 2.15 at the band's low end.
4. the rate against the lowest published EAR — 0.54 points (C6).
5. G15 — the platforms' display: ⚠ 3 of 3 assumed; gate 2 of 3; margin one platform; no floor effect (a failed G15 loops R7 back to SR2, it does not move the margin).
6. the connected share — ⚠ 45–70%; threshold 30%; no floor effect.
7. the non-empty history share (gate 12 of C4), unchanged.
8. the use gates — switch-off share, funding-query rate, charge-query rate, display-query rate (new, ⚠ 0.1–0.3%; threshold 1%) — no floor effect.
9–15. carried from C6 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, including default-funded draws
  threshold:    4.57% at the set price (4.17% at the band's low end · 4.77% at its top) — the 25% margin fails above it at the worst corner; zero margin at 7.37%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.57 points at the assumed high corner; the default-funded gap (C5) may consume ⚠ 0.3–0.5 of it
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the default term switches to opt-in by flow band at a ⚠ 1-point gap (C5); the rate does not move on the loss reading — the limit rule does (C3's overlay)
  reads at:     the Stage 1 12-month reading (the pool); the first replica's 12-month reading (the gap)
```

**Independence (VA-97).** NOT shown — the margin is a transform of the loss gate. Free counts named: the switch-off share, the funding-query rate (C5), the charge-query rate and the no-receipt count (C6), the display-query rate and the platforms' display (new) — counts of acts, not of losses; all unmeasured.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts). At Stage 1 (⚠ £0.4–1.9bn): floor 55.86–133.62; worst-corner margin at the set price (140 − 133.62) ÷ 133.62 = **4.8%**; 1.0% at the band's low end; 6.6% at its top. Stage 1 does not carry the 25% margin at any point of the band — as at C3 to C6; the stage order is the design's answer and the F1 condition (Stage 2 within ⚠ 24 months) is what makes it tolerable.

**Working capital timing.** Unchanged from C6 (the accrued-charge receivable cycle ⚠ 1–3 days). Nothing published moves money.

**The conventional line removed, priced.** The counterfactual's R7 line is ⚠ 6–35 per £1,000: broker commission (⚠ 1–5% of a placed facility, on the share placed), platform referral fees (⚠ 1–3% of referred lending), partner marketing and a partner desk (⚠ 5–15 people at HQ). On a £4.5bn book that is ⚠ £27–160m a year the conventional bank spends to be present at the seat this form reaches for ⚠ £0.02–0.04m. *Runner's call on the low corner:* an incumbent bank spends less on brokers for sub-£25,000 overdrafts than a non-bank lender does, which is why the RD-030 line starts at 6 and not higher.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Customer of record declared; one run; the routine positioned in named ✓ (VA-154).
- Key customer segments and current routines — two routines, by where the shortfall is first seen; the connected share as a band with logic, threshold and convergence ✓ (SR1). No partner named in SR1 ✓.
- Affordability screen stated before any candidate ✓ (VA-164); existence test with an internal holder admitted for the unconnected account and the live question redirected ✓ (VA-92).
- Two-class enumeration — eight candidates, each with the sign of the architecture's effect on its own book; loss side selected; no gain-side reason needed ✓ (VA-147). Stated absence for the unconnected seat, with the test that would show otherwise ✓.
- Presence — the third case (a class present collectively), three seats named ✓ (VA-155). Form stated (aggregate) with the reason; hours per close read for that form ✓ (VA-165).
- ToC — class of problem named ✓; theory named with researcher, year and paper ✓ (Farrell and Saloner 1985); unifying mission ✓; current state and desired state as states ✓; mechanism names what causes the class to move ✓.
- Theory stress test run; the contrast theory named (Christensen and Raynor 2003); customer-side theory (Sharp 2010); fragile-findings check ✓.
- Strategy — exactly one structural decision ✓; the architectural-decision test (remove it and nothing outside the bank knows) ✓; fires at the forecast, not downstream ✓; one decision across all partner types ✓; dual effect ✓; written as prose ✓; what is published and what is not ✓; R1, R2, R3, R6 interactions ✓; at-scale test with the volume ✓; R8 signal ✓; hypothesis with falsification and five named assumptions ✓.
- Mutation gate emitted before the strategy; five genuine mutations (A–E); justification mode false ✓.
- Three tests: primary cause, entry point, incumbent — passed, with the incumbent test's reading recorded as a runner's call (third time) ✓.
- Credibility mechanism (VA-81) ✓. Property-holder test (VA-71) ✓ — six holders, each on a track.
- Productising — one architecture, two views ✓; accumulation (no earlier component changed) ✓; F2 completeness (the BFF read cold as one product; the central mechanism named) ✓.
- Pointing test ✓ — the move puts the limit at the seat, it does not persuade the seat's holder.
- Launch constraints absent from SR1–SR5 (VA-23) ✓. Limit of the analogue stated ✓.
- Completeness contract (VA-73) ✓. No forward references (VA-80) ✓ — R8, R10 by number only.
- VA-106 line, six candidates ✓. VA-103 table, six rows, no FAILED row, the function-gate re-run named ✓. VA-127 table with the two VA-147 columns, two arithmetic lines per row; one PROVISIONAL row with the force named; one nil-at-pessimistic row with the force named ✓. VA-99 five fields on the enabler; no `kmc` on a partner ✓. VA-102 three questions answered ✓. VA-82 classified ✓.
- Count line printed (VA-155); the partner's return classified under both readings (VA-156) ✓. Pricing note: the partner is not the payer, no ceiling set ✓.
- Conventional cost line named (⚠ 6–35) and removed; the cap line printed ✓ (F2).
- Binding gate by driving ✓ (15 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162).
- Verdict order (VA-95) ✓ — `check_verdict_order.py` on the verdict record with R7 added. Loop-gate branch (VA-153): no FAIL on the design. Loop-backs (VA-151): 0.
- TAM data object versioned at the function gate (v3), the C6 narrowing by a named block recorded, the checking script run and its output recorded ✓ (VA-83).
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r7-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v7 and AOM v7 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v7 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. The Partner track is opened at arrival and every transition on it carries PP-1 or a named activity ✓ (VA-102). **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at C7 (unchanged from C5; the ⚠ 37–175 display-query hours and C6's ⚠ 50–125 charge-query hours together use ⚠ 87–300 of the ⚠ 0–425 hours of headroom booked at C5), covering ⚠ 100,000 drawn accounts and ⚠ 333,000 accounts with a limit per cell. Handlers: **14 per cell (band 13–15)**, unchanged. At scale: 2.28 cells, ⚠ 46,500 hours, ⚠ 32 handlers + 3 leads + a trainer = 36 people in cells. Every calculation in this record uses 20,400 and 14. Role support: no new role; the display-query script is a handbook page (AOM v7 section 4) ✓. Unit sizing: the cell's fixed cost ⚠ £0.9–1.18m ✓. Component carriage: every C7 transition in the CTM v7 is carried by PP-1 or by a named activity ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin 31.7% at the worst corner at the set price (27.0% / 34.1% at the band's ends), 159.1% best, by hand; PASS at every point; `fit_margin.py` run on the at-C7 model (verifier r7). Carrying check: carries; room 7.15 at the set price, 2.15 at the band's low end. Binding gate: the loss rate, unmeasured, threshold 4.57% at the set price; the C5 gap on the same line. Conventional additions used: ⚠ 0.05–0.28 of ⚠ £8; the R7 line ⚠ 6–35 removed. Max payable to any holder 7.15 at central, 0 at pessimistic; paid 0. Independence NOT shown; six free counts named. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- The accountant's actor row — FAIL at the pessimistic corner at the actor level, **disposed with the force named** (the client's own screen; a pack cannot be sold against an existing facility); **unmeasured input**: the share of connected released accounts whose first funded event follows a credit application elsewhere; owner: model risk (the bureau footprint at the first replica).
- The account-information provider's row — nil at the pessimistic corner, **disposed with the force named** (conformance to the standard it sells); no input to measure beyond the conformance test.
- The connected share (⚠ 45–70%) — **unmeasured input**; owner: the account-information team; convergence: the bank's consent count (a red field).
- The platforms' display of the element (G15) and the aggregators' pass-through — **unmeasured inputs**; owner: the account-information team; convergence: the conformance test before Stage 1 (the providers) and the first replica's six months (the platforms).
- The display-query rate (⚠ 0.1–0.3%) — **unmeasured input**; owner: the cell lead; convergence: the first replica's six months.
- The forecast lead (⚠ 2–12 weeks) — **unmeasured input**; owner: the runner (desk, from the platforms' documentation); convergence: before Stage 1.
- The desk position (account information, not a promotion) — **standing constraint, designed for**, with what a ruling would settle named at assumption (5); owner: the conduct function; convergence: the signed position before Stage 1.
- The element's population rule and the conformance test — **build items**; owner: the account-information team; convergence: the Stage 1 release serves a credit line to a platform.
- The referral pool per platform (⚠ £0.2–3m) and the pack fee (⚠ £300–1,500) — **unmeasured inputs** that size the loss-side class's pool; owner: the runner (desk); convergence: the platforms' published lending-partner terms.
- C6's and earlier carried items — carried unchanged.

```
GATE VERDICT — on the cumulative architecture C1 to C7
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     FMOS 31.7% worst corner at the set price (27.0% at the band's low end / 34.1% at its top) / 159.1% best (by hand; `fit_margin.py` output in verifier r7) · binding gate the loss rate on the pool: surplus 0.57 points at the assumed high corner, unmeasured; the default-funded gap may consume 0.3–0.5 of it · conventional additions used ⚠ 0.05–0.28 of ⚠ £8; the R7 line ⚠ 6–35 removed
  price:             14.0% simple a year on the daily drawn balance = £140 per £1,000 drawn (band ⚠ 135–142.5); no fee; collected from receipts (C6, unchanged); the partner is paid nothing
  partner:           the class of account-information readers of the account — platforms, aggregators, accountants — loss side (VA-147); aggregate form (VA-165); present collectively across three seats (VA-155); return neither fee nor share (VA-156); G15 gate 2 of 3 platforms displaying, margin one
  decisions:         28 unmeasured inputs (21 carried, 7 new), 10 build items (8 carried, 2 new), 1 standing-constraint set (1 new row), 2 structural limits (carried), 1 carried question (fixed against variable, C6); 1 actor-level FAIL at the pessimistic corner disposed with the force named; 1 nil-at-pessimistic row disposed with the force named
  capacity figure:   20,400 exception hours per cell a year, 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15) at 1,400–1,600 productive hours — used throughout   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; six free counts named and unmeasured   VA-97
  gates driven:      15; first to fail on evidence: the loss rate, margin 0.57 points at the set price; second: the default-funded gap on the same line; third: the price condition's room (7.15)   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r7-2026-09-21.md   VA-90
  inherited:         R6, R5, R4, R3, R2, R1 PROVISIONAL — R7 cannot exceed them; F1 closed PROVISIONAL with one condition   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design; the actor-level FAIL is disposed with owner and convergence; the CTM and AOM model files are build items   VA-153
  launch constraints:none inside SR1–SR5 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn; at the Stage 1 count the worst-corner margin is 4.8% at the set price, 1.0% at the band's low end   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; the price sets where on that line the gate sits   VA-160
  function gate:     F2 (C4–C7) — consistency audit F2 and verify F2 run on the cumulative BFF; their results in the f1-status file
  VERDICT:           PROVISIONAL
```

**R7 failure test.** Would R7 have failed? Three conditions. First, no party outside the bank holds the seat where the shortfall is first foreseen: it does for a connected account (the forecast), so a stated absence alone would have been a failure to ask; the enumeration ran. Second, the class does not read the element: unmeasured; if fewer than 2 of 3 large platforms display it at 12 months, R7 loops back to SR2 and a gain-side selection is made with the admissible reason recorded. Third, the loss-side class needs a payment to carry: it does not — each reader's surplus is positive at central without one, and the pessimistic accountant is forced by the client's screen. None fails today. The nearest is the second, and it is the hypothesis.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the switching cost by presence (a credit line in the customer's own ledger; a rival account shows none) — R8
  - the at-scale price hold; the yearly rate review; the funding line's movement with Bank Rate — R9, R10
  - the shelf check for any supplier binding at launch — R10 (none named at C7)
- **Unmeasured inputs (new at C7, 7):** the connected share; the platforms' display (G15); the aggregators' pass-through; the display-query rate; the forecast lead; the credit-application-elsewhere share on the connected pool (the accountant row's test); the referral pool and pack fee that size the loss-side class. **Carried from C1–C6 (21):** unchanged.
- **Build items (new at C7, 2):** the element's population rule (released accounts only; flag not included); the conformance test. **Carried (8):** the CTM and AOM model files; the accrual ledger; the charge-first split; the representative example and APR basis; default funding's authorisation, notice and record; the term and the CONC 4.7 information; the limit-history placement; the release order's instrumentation.
- **Standing constraints:** PSRs 2017 reg. 69 and the CMA Order 2017 (the account-information service, on the customer's consent); the Open Banking account-and-transaction standard (the credit-line element and its flag); the UK SCA-RTS art. 36(5) access limit; the desk position that the element is account information and not a promotion under CONC 3 — designed for. C6's and earlier: unchanged.
- **Structural limits (carried):** the C1 limit rule's exposure model; the Stage 1 margin below 25% at every point of the band. **New at C7:** the unconnected account has no seat outside the bank — C4's placement is its only conviction moment; a bounded limit, not a defect.
- **Carried question (C6):** a fixed rate against a Bank Rate–linked rate.
- **TAM data object:** v3 written at C7 — the C6 narrowing by the named block "price" recorded (SC-OD-BELOW-BAND, SC-LOAN-USER excluded); the pool-at-risk block added from the C2 block; the surviving volume unchanged; the checking script's output in the verifier r7.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Customer of record declared; one run per customer of record (VA-154) | PASS — one | SR1 |
| Key customer segments and current routines — no partner in SR1 | PASS — two routines | SR1 |
| Affordability screen before enumeration (VA-164) | PASS — 7.15 at central; 0 at pessimistic; paid 0 | SR2 |
| Existence test (VA-92) — internal holder admitted; redirect stated | PASS | SR2 |
| Two-class enumeration (VA-147) — loss side preferred; reason if gain side | PASS — eight candidates; loss side selected; no reason needed | SR2 |
| Presence — one · none · class collectively (VA-155) | PASS — the third case; three seats | SR2 |
| Form named before count and hours; hours read for that form (VA-165) | PASS — aggregate; no close; conformance hours | SR2 |
| Stated absence with a falsifiable test | PASS — the unconnected seat | SR2 |
| ToC — unifying mission; theory; mechanism that causes the move | PASS — Farrell and Saloner 1985 | SR3 |
| Theory stress test and fragile-findings check | PASS — Christensen and Raynor 2003; Sharp 2010 | SR3 |
| Mutation gate — ≥ 2 genuine mutations, differsFromBaseline, justification mode | PASS — five; true; false | SR4 |
| Exactly one structural decision; the architectural-decision test | PASS — the limit as a property of the published balance | SR4 |
| Fires at the seat of need, not downstream (the presence test) | PASS — the forecast | SR4 |
| One decision across all partner types | PASS — the standard | SR4 |
| Dual effect on the customer's F2 | PASS — R4 and R5 by mechanism | SR4 |
| Written as prose, not labelled components | PASS | SR4 |
| Hypothesis with falsification; assumptions named | PASS — five | SR4 |
| Credibility mechanism (VA-81) | PASS | SR4 |
| Property-holder test (VA-71) | PASS — six holders | SR4 |
| Three tests — primary cause, entry point, incumbent | PASS — incumbent reading a runner's call | SR4 |
| Productising — one architecture two views; accumulation; F2 completeness | PASS | SR5 |
| BFF read cold as one product; central mechanism named | PASS | SR5 |
| Considered / not chosen (VA-4) | PASS — eight | section |
| Synthesis check (VA-1) | PASS — Square Loans' dashboard, with the limit named | section |
| VA-106 line — count and mechanism | PASS — six | section |
| VA-127 — two arithmetic lines per row; VA-147 columns | PASS — six rows; one PROVISIONAL, one nil, both forced | section |
| Partner business case (VA-99) — five fields; no kmc | PASS | financial check |
| VA-102 — three questions | PASS | section |
| VA-103 — every earlier requirement re-run; function-gate re-run at C7 | PASS — six rows; audit F2 and verify F2 named | section |
| Count line (VA-155) | PASS — printed | financial check |
| Partner's return classified (VA-156) | PASS — neither; both readings 31.7% | financial check |
| Pricing note — partner not the payer, no ceiling | PASS | financial check |
| ABC floor lines (RD-031) — every driver resolves | PASS — five lines | financial check |
| Four-layer floor; carrying check; margin by hand and by script | PASS — 54.04–106.28; 31.7% | financial check |
| Conventional cost line named and removed; cap line (RD-030) | PASS — ⚠ 6–35 removed; 0.05–0.28 used | financial check |
| Binding gate by driving (VA-84); shared input (VA-160); spread count (VA-162) | PASS — 15 gates | financial check |
| Independence (VA-97) | NOT shown — declared | financial check |
| Three-check close (VA-89, VA-91); every failed check disposed | PASS — 0 / 1 / 0 failed; all disposed | the close |
| Verdict composes forward (VA-95); `check_verdict_order.py` | PASS — IN ORDER | verifier r7 |
| Verification artefact (VA-90) | PASS — verifier r7 | the close |
| Carried items classified (VA-82) | PASS | section |
| TAM data object versioned; checking script run (VA-83) | PASS — v3; output in verifier r7 | carried items |
| No forward references (VA-80); no launch constraints (VA-23) | PASS | throughout |
| Fit staleness (VA-74) — component set recorded | PASS — nine components incl. PP-1 | financial check |
| Bank unnamed; internal figures as red fields | PASS | throughout |
| House-style checker on this record | run — output in the changelog | — |

---

## Quality check

- Is the gateway partner already present in the customer's routine (not just convenient)? **Yes** — the ledger and the forecast, for a connected account.
- Does the Integration ToC explain why the partner moves from passive to active? **Yes** — the standard makes the decision; the reader's own accuracy makes the championing.
- Does partner activation also advance customer F2? **Yes** — R4 and R5 by mechanism.
- Could an incumbent deploy this without changing their BFF? **No** — it can populate the element; it has no standing limit on every account to publish.
- Confidence: **Medium** — the mechanism rests on a public standard and an element designed for this object (T2); whether the platforms display a never-applied-for limit is unmeasured (T4) and is the hypothesis.

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15, C5 G1–G10, C6 H1–H12)

- I1 — CMA, Retail Banking Market Investigation Order 2017, Part 2 (Open Banking): the largest current-account providers must make account data available to authorised third parties through open standards. FACT.
- I2 — Payment Services Regulations 2017, reg. 69 (access to payment accounts for account information services). FACT.
- I3 — Open Banking Implementation Entity, Read/Write Data Standard — Account and Transaction specification v3.1: the balance resource, its credit-line element (amount; type: Available, Credit, Emergency, Pre-Agreed, Temporary; included flag). T1 for the element; T4 for each platform's rendering.
- I4 — UK SCA-RTS (the onshored regulatory technical standards on strong customer authentication), art. 36(5): four unattended accesses a day. T2.
- I5 — Farrell, J. and Saloner, G. (1985), "Standardization, Compatibility, and Innovation", *RAND Journal of Economics* 16(1): 70–83.
- I6 — Christensen, C. and Raynor, M. (2003), *The Innovator's Solution*, ch. 2 (asymmetric motivation).
- I7 — Sharp, B. (2010), *How Brands Grow*; Romaniuk, J. and Sharp, B. (2016), *How Brands Grow Part 2* (physical and mental availability).
- I8 — Xero Limited, Annual Report FY2024 — UK subscriber count (⚠ about 1m). T2.
- I9 — HMRC, Making Tax Digital for Income Tax — mandatory from April 2026 for income above £50,000. FACT.
- I10 — Xero App Store — iwoca listing (a non-bank lender present in the platform's marketplace). T2.
- I11 — CMA (2016), Retail banking market investigation, final report — no relationship manager below £500,000 turnover. T1.
- I12 — DBT, Business Population Estimates 2025 — ⚠ 1.4m SMEs with employees. T1.
- I13 — FCA CONC 3 (financial promotions); CONC 3.5.5R (representative example) — read for the desk position at assumption (5).

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | Created at R7 by the runner (Path C, mode 3, autonomous). PROVISIONAL, capped by R1–R6 (VA-95). Object-after to 23 September 2026 17:00. Closes Function 2. House-style checker run on this file: result recorded in the f1-status file. |
