# Business bank credit facility line — activity and operating model (AOM), v8, at C8

**Venture:** the credit facility line of a large UK SME bank (Case B), Path C mode 3 — see `../bank-credit-facility-c8-v1-2026-09-21.md`. **v8 written at R8** (21 Sep 2026), runner-drafted under the propose-and-confirm rule. **v7**, **v6**, **v5**, **v4**, **v3**, **v2** and **v1** are retained unchanged as the C7, C6, C5, C4, C3, C2 and C1 records. **Update mode:** only the rows R8 adds or changes are new (marked *C8*, in bold); every other row is carried from v7 with its trace and its bold removed. R8 amends one component — WP-1 to v2, the seasoned limit: the rule's multiple of flow rises on a published schedule with the account's own cleared events, so the limit an account carries after two years of use is one no rival can offer on the first day. CP-2 gains the seasoning line. No component is removed and no new component is added. The operating model gains no new holder: the engine reads one more field it already stores; the exception cell answers one more query class inside the C5 headroom at the central corner and needs a 15th handler at the high corner; model risk validates the schedule yearly. The floor moves by ⚠ 0.45–1.50 per £1,000 a year, all of it capital on the larger undrawn commitment; IC 12–17 → 13–18. The conventional R8 line — loyalty pricing, exit fees, product tie-ins and a retention desk, ⚠ 5–15 per £1,000 — is not booked.

**Defined terms.** As in the CTM v2: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *standard tariff*, *migration*, *price condition*. *Exception cell* — the smallest operating unit of people in the form: the team that handles accounts whose flow has stopped, whose limit rule has been overridden by a fraud or conduct signal, or whose holder has declined migration or queried the saving statement. New at C3, as in the CTM v3: *shadow limit*, *back-test*, *release*, *overlay*, *trial band*, *replica band*. *Stage* — one step of the release order: Stage 0 the back-test, Stage 1 the migrated accounts, Stage 2 the replicas, Stage 3 at scale. New at C4, as in the CTM v4: *shortfall*, *limit history*, *placement*. *Productive hours* — the hours a year one handler spends on cases, after leave, public holidays, sickness and non-case time. New at C6: *The charge* — interest accrued daily on the drawn balance at 14.0% simple a year (band ⚠ 13.5–14.25%), no fee. *Accrual* — the daily ledger line (drawn balance × rate ÷ 365), held apart from the drawn balance, bearing no interest. *Collection* — the first slice of each receipts share clears the accrued charge. *Representative example* — the CONC 3.5.5R illustration. *Calendar debit* — the conventional charging event R6 removes. New at C8, as in the CTM v8: *Cleared event* — a funded event whose drawn balance the receipts share has returned to zero without a stalled or written-off outcome, read from the ledger (⚠ 90-day cut). *Seasoning* — the count of an account's cleared events under the form. *Seasoned limit* — the rule's multiple of flow raised on the seasoning schedule (WP-1 v2). *Seasoning schedule* — the published table: two-thirds of the uplift by ⚠ 12 cleared events, the full uplift by ⚠ 36 months; average uplift ⚠ 15–30% over the unseasoned limit. *Store of value* — what a customer holds at the bank that a rival cannot supply on day one; in this form, the seasoned limit.

## 0 · Quantities, events and actors — what every driver resolves to (RD-031, VA-140)

Every Driver cell in sections 3a to 3c names one entry below. A quantity carries its source and tier. An event carries its frequency and its parent. Nothing in a Driver cell is a free-text ratio.

```
quantities:
  q.accounts_with_limit:   760000        # own base 950,000 × ⚠ 80% with six months of flow; T4; PCO S11
  q.drawn_accounts:        228000        # q.accounts_with_limit × ⚠ 30% drawn at any time; T4
  q.drawn_book_gbp:        [3.4e9, 5.7e9]  # q.drawn_accounts × ⚠ £15–25k average drawn; T4
  q.overdraft_accounts:    [104500, 161500] # own base × 11–17% overdraft use; T1 rate (SME Finance Monitor) on a T4 base
  q.tariff_accounts:       [41800, 113050]  # q.overdraft_accounts × ⚠ 40–70% on the standard tariff; T4, share logic in the TAM data object
  q.cell_drawn_accounts:   100000        # the coverage of one exception cell; declared, the cell's design unit (VA-91)
  q.cell_overdraft_origin: [46000, 71000]  # q.cell_drawn_accounts × q.overdraft_accounts / q.drawn_accounts; T4
  q.productive_hours_fte:  [1400, 1600]  # C4: a band, was a point (verify-F1 fault F-2). ONS average actual weekly hours, full-time, ⚠ 36.5 (T2) × 52 weeks, less 5.6 weeks' leave (WTR 1998 reg. 13, T1), 1.6 weeks' public holidays and ⚠ 0.9 weeks' sickness (ONS 2024, T2) = ⚠ 1,600 gross; less ⚠ 0–12% non-case time (meetings, training, admin; T4) = 1,400–1,600. Threshold: below 1,340 the cell needs a 15th handler at the high query corner. Convergence: the first cell's timesheets at six months
  q.undrawn_per_drawn:     [1.9, 3.6]    # C8: was [1.5, 2.5]. Limit-to-drawn ⚠ 2.5–3.5 × the seasoned uplift 1.15–1.30, less the drawn £1 = 1.9–3.6; T4. Threshold: an average uplift above ⚠ 38% takes the R8 addition past the £8 cap's remaining room at the high corner (C8 gate G16). Convergence: the first replica's undrawn-to-drawn ratio at 24 months (a red field)
  q.seasoned_share:        stage-dependent # share of drawn accounts at the full uplift: Stage 1 0; first replica at 24 months ⚠ 30–50%; at scale ⚠ 60–80%; T4; C8
  q.replica_accounts:      333000        # accounts with a limit per replica = q.cell_drawn_accounts ÷ 30% drawn; one replica = one cell (VA-91); C3
  q.replica_count:         2             # ⚠ (760,000 − 104,500..161,500 − Stage 1) ÷ 333,000, rounded; T4; C3
  q.history_years:         [3, 5]        # years of readable transaction history for the back-test; MLR 2017 reg. 40 five-year retention sets the ceiling; T4; C3
  q.unreleased_accounts:   stage-dependent # q.accounts_with_limit − released; Stage 1 ⚠ 600,000–655,000; Stage 3 = 0; C3
  q.connected_accounts:    [342000, 532000] # q.accounts_with_limit × ⚠ 45–70% read through a bank feed by a platform or an accountant; T4 (Xero ⚠ ~1m UK subscribers, T2; MTD for income tax from April 2026, FACT); threshold 30%; convergence: the bank's live-consent count (a red field); C7
events:
  e.daily_recompute:  {parent: q.accounts_with_limit, frequency: 365 a year}
  e.draw:             {parent: q.drawn_accounts, frequency: ⚠ 3 a year}
  e.receipt:          {parent: q.drawn_accounts, frequency: ⚠ 300 a year}
  e.flow_stop:        {parent: q.cell_drawn_accounts, frequency: ⚠ 2% a year}
  e.signal:           {parent: q.cell_drawn_accounts, frequency: ⚠ 3% a year}
  e.dispute:          {parent: q.cell_drawn_accounts, frequency: ⚠ 1% a year}
  e.write_off:        {parent: q.cell_drawn_accounts, frequency: ⚠ 1% a year}
  e.migration:        {parent: q.overdraft_accounts, frequency: once, at launch}          # C2, WP-4
  e.migration_decline:{parent: q.cell_overdraft_origin, frequency: ⚠ 10% once, at launch} # C2, decline or ask for an explanation
  e.saving_statement: {parent: q.overdraft_accounts, frequency: 1 a year}                # C2, CP-1 amended
  e.saving_query:     {parent: q.cell_drawn_accounts, frequency: ⚠ 2% a year}            # C2, a customer queries the statement
  e.backtest:         {parent: q.history_years, frequency: once, Stage 0}                # C3, WP-5
  e.stage_reading:    {parent: q.replica_count + 1, frequency: once each, ⚠ 3 in all}    # C3, the trial band at 12 months, each replica band at 6 months
  e.release:          {parent: q.replica_count + 1, frequency: once each}                # C3, the board risk committee signs each
  e.shortfall:        {parent: q.accounts_with_limit, frequency: ⚠ 2–6 a year}                 # C4, CP-2 — a scheduled payment exceeds the available balance; the placement trigger; T4 (judged from late-payment incidence, DBT 2025); convergence: the Stage 0 back-test counts it
  e.limit_query:      {parent: q.replica_accounts, frequency: ⚠ 1–3% a year}                  # C4, CP-2 — a customer asks why the limit on a day was what it was; T4; convergence: the first replica at six months
  e.template_review:  {parent: a.conduct_reviewer, frequency: 1 a year}                       # C4, CP-2 — the promotion template signed and reviewed
  e.funded_event:     {parent: q.accounts_with_limit, frequency: ⚠ 2–6 shortfalls × 0.80–0.95 term-on a year}  # C5, WP-2 v2 — a payment exceeding the balance is met from the limit; 1.2–4.3m a year; T4; convergence: the Stage 1 release counts it
  e.funding_query:    {parent: q.replica_accounts, frequency: ⚠ 0.05–0.2% of funded events}                   # C5, WP-2 v2 — a customer asks why a payment was funded or asks to switch off; 270–1,900 per cell a year; T4; threshold 0.5%; convergence: the first replica at six months
  e.term_drafting:    {parent: a.product_conduct, frequency: once, before Stage 1}                            # C5, WP-2 v2 — the accepted term and the CONC 4.7 information drafted once, reviewed yearly
  e.charge_accrual:   {parent: q.drawn_accounts, frequency: 365 a year}                                          # C6, PC-1 resolved — one ledger line per drawn account per day; ⚠ 83m a year; inside the daily batch
  e.charge_collection:{parent: e.receipt, frequency: 1 per receipt}                                             # C6, WP-3 v2 — the charge-first split on every receipt; ⚠ 68m a year; inside WP-3's per-receipt cost
  e.rate_review:      {parent: a.pricing_committee, frequency: 1 a year}                                       # C6, PC-1 — the rate set once and reviewed yearly against the funding line and the loss reading
  e.representative_example: {parent: a.product_conduct, frequency: once, before Stage 1}                      # C6, PC-1 — the CONC 3.5.5R example and the APR basis drafted and signed once, reviewed yearly
  e.charge_query:     {parent: q.cell_drawn_accounts, frequency: ⚠ 0.2–0.5% a year}                           # C6, PC-1 — a customer asks why a receipt was split as it was; 200–500 per cell a year; T4; threshold 1.5%; convergence: the first replica at six months
  e.balance_call:     {parent: q.connected_accounts, frequency: ⚠ 4 a day × 365 = 1,460 a year}              # C7, PP-1 — the unattended-access limit under the UK SCA-RTS art. 36(5); ⚠ 0.50–0.78bn a year; the element rides inside a response already served
  e.display_query:    {parent: q.replica_accounts × connected share, frequency: ⚠ 0.1–0.3% a year}          # C7, PP-1 — a customer asks why the software shows more than the balance; 150–700 per cell a year; T4; threshold 1%; convergence: the first replica at six months
  e.field_build:      {parent: a.account_information_team, frequency: once, before Stage 1}                  # C7, PP-1 — the population rule (released accounts only; flag not included); ⚠ 400–800 h
  e.conformance_test: {parent: a.account_information_team, frequency: once, before Stage 1; 6 counterparties} # C7, PP-1 — the three largest account-information providers and the three largest platforms; ⚠ 100–200 h
  e.field_position:   {parent: a.product_conduct, frequency: once, then 1 a year}                            # C7, PP-1 — the desk position: account information (PSRs 2017 reg. 69), not a financial promotion (CONC 3); ⚠ 40–80 h
  e.cleared_event:    {parent: q.drawn_accounts, frequency: ⚠ 3–12 a year}                                     # C8, WP-1 v2 — the drawn balance returns to zero; ⚠ 0.7–2.7m a year; read from the ledger, no person acts; T4; convergence: the first replica's ledger at 12 months
  e.engine_build:     {parent: a.limit_engine, frequency: once, before Stage 1}                                 # C8, WP-1 v2 — the seasoning field and the schedule in the rule; ⚠ 200–400 h
  e.seasoning_review: {parent: a.model_risk, frequency: 1 a year}                                              # C8, WP-1 v2 — validates the schedule against cleared-event loss by cohort (SS1/23); ⚠ 100–200 h
  e.seasoning_query:  {parent: q.replica_accounts × drawn share, frequency: ⚠ 0.5–1.5% a year}                  # C8, CP-2 v2 — a customer asks why the limit stepped, or did not; ⚠ 500–1,500 per cell; threshold 2%; convergence: the first replica's query log at 12 months
actors:
  a.limit_engine · a.account_line · a.treasury · a.exception_handler · a.cell_lead · a.model_risk
  a.product_conduct · a.pricing_committee (C2) · a.customer · a.risk_committee (C3) · a.finance (C3) · a.conduct_reviewer (C4)
  a.account_information_team (C7, internal) · a.platform (C7, external) · a.aggregator (C7, external) · a.accountant (C7, external)
floors:
  f.cell_min_people: 14 handlers + 1 lead (band 13–15) — reason: the C5 row adds ⚠ 70–475 hours a year plus ⚠ 0–425 hours of headroom for the first-year query peak to the 19,500 of v4; at the high corner (20,400 hours) and 1,400–1,600 productive hours the cell needs 12.8–14.6 handlers; 14 is the figure used (VA-91). Was 13 (band 12–14) at C4. Unchanged at C6: the ⚠ 50–125 charge-query hours sit inside the ⚠ 0–425 hours of headroom booked at C5 C7: the display-query row adds ⚠ 37–175 hours a year inside the same headroom (with C6's 50–125 hours, ⚠ 87–300 of the 0–425 used); the cell stays at 14. C8: the seasoning-query row adds ⚠ 125–375 hours a year; the headroom is now split — first-year ⚠ 0–425 (the funding-query peak) and recurring ⚠ 212–675 (C6 + C7 + C8); at the central corner (20,400 hours) the cell stays at 14; at the high corner (⚠ 21,900 hours at 1,400 productive hours) it needs a 15th handler — 14 is the figure used, the band 13–15 holds, the 15th is costed in section 3c as the high corner of the cells line.
```

## 1 · Actors

| Actor | Role in the form | Level |
|---|---|---|
| The business (customer) | holds its account; draws; is repaid from by the receipts share; accepts or declines migration (C2); accepts the limit term once at release; may draw ahead; may switch default funding off (C5) | customer |
| The account line (Case A) | holds the flow and the balance; the ledger the limit engine reads; produces the saving statement (C2); stores each day's limit, renders the limit history and places it at the shortfall (C4) | internal dependency — not designed here; authorises every payment against the available balance (credit balance plus undrawn limit), funds a payment that exceeds the credit balance from the limit, records the funded event and writes the notice (C5) |
| **The limit engine** | **computes every account's standing limit daily from the flow by a rule; no person decides an account; from C8 reads the account's seasoning (its count of cleared events) and applies the published schedule to the multiple — the seasoned limit (WP-1 v2)** | **HQ, automated (C8: one more field)** |
| The exception cell | the people who act when the flow stops, a signal fires, a customer disputes, a customer declines migration or queries the saving statement (C2); answers a customer who asks why the limit on a day was what it was (C4) | LMU; explains a funded or a returned payment; records a switch-off instruction (C5) |
| **Model risk and credit oversight** | **owns the limit rule as a model; sets the risk appetite the rule expresses; reports to the board's risk committee; validates the back-test and reads each stage (C3); reads the default-funded pool's loss against the drawn-ahead pool's at each stage (C5); validates the seasoning schedule yearly against cleared-event loss by cohort (C8, ⚠ 100–200 hours; SS1/23 — a change to the model's inputs is a change to the model)** | **HQ (C8: the yearly seasoning review)** |
| Product, conduct and compliance | the account terms, the CCA-regulated agreement for sole traders under £25,000, Consumer Duty outcomes; the modifying agreement or variation notice at migration (C2); drafts the accepted term (default funding, the receipts share, switch-off) and the CONC 4.7 pre-contract information once; signs the notice wording (C5) | HQ |
| The pricing committee | holds the price condition (PC-1) and, from C6, sets the rate inside it — 14.0% simple a year, one number for every account with a limit, reviewed yearly | HQ, existing function (C2; the rate at C6) |
| Treasury | funds the drawn book from the account line's deposits; holds capital against drawn and undrawn exposure; funds the replicas' drawn balance as they release (C3) | HQ, existing function |
| The board risk committee | signs each stage's release against its pre-registered band (SS1/23 Principle 2) | HQ, existing committee (C3) |
| Finance and the external auditor | books the overlay on the unproven model at release and releases it at the reading; IFRS 9 5.5.20 on the undrawn part | HQ, existing function (C3) |
| PRA and FCA | permissions and capital unchanged; the rule is a model under SS1/23 | external, unchanged |
| The conduct reviewer | signs the limit-history display as a financial promotion template (CONC 3.3.1R) and reviews it yearly; one person inside product, conduct and compliance | HQ (C4) |
| The bank's account-information team | populates the pre-agreed credit-line element for released accounts and withholds it for unreleased ones (PP-1); runs the conformance test with the largest providers and platforms once; the CMA Order 2017 conformance the bank already carries | HQ, existing function (C7); no new people — the build is a one-off in 3e |
| The account-information provider (aggregator) | passes the balance response, including the credit-line element, through to the platforms it serves; paid per connection by the platform, nothing by the venture | external, a conduit (C7) |
| The accounting platform | reads the account through the bank feed; shows the credit line beside the balance; forecasts against it; its lending marketplace prompt does not fire on a covered shortfall | external, loss side — the referral pool is lost to the C1 form either way (C7) |
| The accountant | reads the credit line in the client ledger; at a forecast shortfall tells the client it is covered; does not counsel a rival facility | external, loss side — the application-pack fee is lost either way (C7) |

## 2 · Ops map — the three flows

**Money.** Deposits on the account line fund the drawn book (treasury). **New at C8:** the seasoned limit raises the undrawn commitment per £1 drawn from ⚠ 1.5–2.5 to ⚠ 1.9–3.6; treasury holds capital against it at the 10% credit conversion factor — the only money flow R8 changes. A draw moves money from the limit to the account balance. Each receipt into the account is split: the receipts share reduces the drawn balance; the rest stays with the customer. **New at C6:** the charge accrues daily on the drawn balance (14.0% a year) on its own ledger; each receipt's share is split charge-first, then principal, so the charge is cash to the bank with every receipt — the accrued-charge receivable cycle is ⚠ 1–3 days against ⚠ 30 under a monthly debit, and interest cash arrives ⚠ 27 days earlier on average (worth ⚠ £0.9–2m a year at the funding line's 1.5–3.0% on a £4.5bn book at 140; stated, not credited in the floor); no debit is ever made for the charge; no arrears exist on it; the capital bar is unchanged because the accrued charge is not exposure. A write-off leaves the book when an account's flow has stopped and the exception cell has closed it. **New at C2:** at migration the drawn overdraft balance moves onto the limit as a draw — no money moves, the ledger reclassifies the balance; the overdraft's renewal fee event stops. **New at C3:** during the path the drawn balance grows by stage, not by application; treasury funds each replica as it releases; finance books an overlay on the allowance at each release and releases it at the reading. No money moves for a shadow limit. **New at C5:** a payment that exceeds the credit balance is met from the limit at authorisation — the draw is the account's act, not the customer's; the receipts share repays it as before; the drawn book rises by the funded events the customer would otherwise not have drawn (not credited in the floor; read on the release track).

**Information.** The ledger (account line) → the limit engine → the standing limit shown in the account (CP-1). Signals (fraud, conduct, flow-stop) → the exception cell. The rule's performance (loss by cohort) → model risk → the rule. **New at C2:** the ledger → the saving statement once a year (what the overdraft cost in the year before migration; what the limit cost since) → the customer; a decline or a query → the exception cell; the tariff the customer paid → the pricing committee (the reference for PC-1). **New at C3:** history → the back-test → model risk (validation) → the board risk committee (release); the shadow ledger → the stage reading → the band → the next release. **New at C4:** the stored daily limit and the back-test (WP-5) → the limit history (CP-2) → the customer, beside the balance; the scheduled-payment file matched against the balance → the placement on the shortfall day; a limit-history query → the exception cell. **New at C5:** the payment order → the available-balance rule → funded or returned; a funded event → the notice in the account and a line on the statement (CP-1); a funding query or a switch-off instruction → the exception cell; the funded-event record by pool → model risk (the loss gap reading). **New at C7:** the released limit → the pre-agreed credit-line element of the balance response → the account-information provider → the platform's balance line and forecast → the accountant's client ledger; the receipt splits travel as transaction lines in the same feed; an unreleased account shows no credit line; the limit history does not travel. **New at C8:** the ledger → the drawn balance returns to zero → a cleared event → the engine's seasoning field → the next step on the schedule → the seasoned limit shown with its own line in the limit history (CP-2 v2); a query on a step → the exception cell; cleared-event loss by cohort → model risk → the schedule.

**Product.** The standing limit is the product. It exists on every account with enough flow before any need arises. The draw and the receipts share are the customer's only two actions. **New at C2:** for the selected customer the product replaces the overdraft on the same account — migration is the one event that retires the old product. **New at C4:** the limit is shown with its own twelve-month history, so the customer can check it before drawing; nothing is sent. **New at C5:** the limit is used by the account, not by the customer — a payment that exceeds the balance is met from it under a term accepted once; the explicit draw ("draw ahead") and the switch-off are the customer's two options; the funded event is the unit the account records and C6 will price. **New at C6:** the limit is paid for from receipts only — one rate on the days drawn, no fee, no charging date; the representative example is shown wherever the rate is shown. **New at C7:** the product is present wherever the account is read — in the ledger, the forecast and at the accountant — because the limit is published as a property of the account's balance; no partner is sold anything. **New at C8:** the limit grows with use — each cleared event moves the account one step along the published schedule, so the product a customer holds after two years is larger than the one any rival can offer on the first day; nothing is sent, nothing is applied for, nothing is priced differently.

**What the conventional form performs that this form does not.** The application; the per-application credit decision; the security process; the annual review (**including the overdraft's annual renewal, C2**); the collections operation. Each is named so its absence is a design, not an omission. **The marketing of the facility and the relationship manager's outreach (C4) — the conventional want-block line, ⚠ 2–8 per £1,000, removed.** **Onboarding calls, help content and a support line for the first draws (C5) — the conventional use-block line, ⚠ 1–2 per £1,000, removed: there is no first draw to support.** **The calendar debit and the arrangement and renewal fee (C6) — the conventional charging events; with them the arrears and returned-debit work on the charge. The conventional R6 line is nil in the counterfactual (RD-030): nothing is removed from the cap, and the block's cost to the bank is revenue and work, not a booked line.** **New at C7:** the broker channel and its commission; the platform referral agreement and its fee; the partner desk and partner marketing; the accountant programme — each named so its absence is a design; together they are the conventional R7 line (⚠ 6–35 per £1,000, RD-030), removed. **Loyalty pricing, exit fees, product tie-ins and a retention desk (C8) — the conventional R8 line, ⚠ 5–15 per £1,000, removed: the form holds the customer by what it has accumulated, not by a barrier.**

## 3 · Activity table — LMU first (one exception cell), then HQ

Every row names the flow it serves (money · information · product), its performer, and a driver that resolves to section 0.

### 3a · Making — the limit, the draw and the migration (stream: Making; level: per account, automated)

| Activity | Flow | Performer | Driver | Volume at scale | Unit cost ⚠ | Note |
|---|---|---|---|---|---|---|
| read the account's flow and compute the standing limit | information | a.limit_engine | e.daily_recompute | ⚠ 760,000 × 365 | compute ⚠ £1–2 per account a year | a rule, not a decision (C1) |
| record the limit as a shadow limit with a release flag on every unreleased account | information | a.limit_engine, a.account_line | e.daily_recompute on q.unreleased_accounts | ⚠ 600,000–655,000 × 365 at Stage 1, falling to 0 | inside the compute cost above — the same computation, one extra field | WP-5 (C3). Path only; the field is dropped at Stage 3 |
| show the limit and the receipts share in the account | information | a.account_line | q.accounts_with_limit | ⚠ 760,000 | inside the account line's existing cost | CP-1 (C1) |
| **read the account's seasoning field and apply the schedule to the multiple** | **information** | **a.limit_engine** | **e.daily_recompute** | **⚠ 760,000 × 365** | **inside the compute cost above — the same computation, one more field read** | **WP-1 v2 (C8)** |
| **recognise a cleared event on the ledger and step the seasoning field** | **information** | **a.account_line, a.limit_engine** | **e.cleared_event on q.drawn_accounts** | **⚠ 0.7–2.7m a year** | **⚠ £0.001 per event = £1–3k a year** | **WP-1 v2 (C8); the ledger already records the balance — the event is a read, not a write** |
| serve the pre-agreed credit-line element (the released limit; flag not included) in each balance response to an account-information reader; the receipt splits as transaction lines | information | a.account_line | e.balance_call on q.connected_accounts | ⚠ 342,000–532,000 × 1,460 = 0.50–0.78bn | ⚠ £0.00001 per call = ⚠ £5–8k a year | PP-1 (C7) — one element inside a response the bank already serves; 0.00 per £1,000 |
| execute a draw | money | a.account_line | e.draw | ⚠ 680,000 | ⚠ £0.5 per draw | WP-2 (C1) |
| split each receipt by the receipts share | money | a.account_line | e.receipt | ⚠ 228,000 × ⚠ 300 | ⚠ £0.01 per receipt | WP-3 (C1) |
| fund the drawn balance | money | a.treasury | q.drawn_book_gbp | ⚠ £3.4–5.7bn | ⚠ 1.5–3.0% a year | the deposit cost of the account line (C1) |
| absorb expected loss | money | the book | q.drawn_book_gbp × loss rate | ⚠ 2.0–4.0% of drawn | — | the critical assumption; the binding gate (C1, tested at C2) |
| retire the overdraft and reclassify its drawn balance as a draw on the limit; issue the modifying agreement or variation notice | product | a.account_line, with a.product_conduct | e.migration | ⚠ 104,500–161,500, once | ⚠ £1–3 per account (notice, agreement, ledger change) | WP-4 (C2). One-off ⚠ £0.1–0.5m; outside the annual floor; a scaling cost carried to C3 by number |
| produce the saving statement | information | a.account_line | e.saving_statement | ⚠ 104,500–161,500 a year | ⚠ £0.1 per statement | CP-1 amended (C2). ⚠ £10–16k a year, inside the computing line |
| store each day's limit as a record; render the twelve-month shortfall history beside the balance; match the scheduled-payment file against the balance and place the history on the shortfall day | information | a.account_line | e.shortfall on q.accounts_with_limit | ⚠ 760,000 accounts × ⚠ 2–6 shortfalls | ⚠ £0.10–0.30 per account a year (a read of WP-5 and a match the account line already performs for returned items) | CP-2 (C4). ⚠ £76–228k a year = ⚠ 0.01–0.07 per £1,000; inside the computing line |
| authorise a payment order against the available balance (credit balance plus undrawn limit); fund a payment that exceeds the credit balance from the limit; record the funded event | money | a.account_line | e.funded_event | ⚠ 1.2–4.3m a year | £0 — the authorisation the account line runs today for every account with an arranged overdraft, with one more input (T2) | WP-2 v2 (C5). No new cost line; the same rule the arranged overdraft already uses |
| tell the customer a payment was funded — an in-account notice and a statement line | information | a.account_line | e.funded_event | ⚠ 1.2–4.3m a year | ⚠ £0.005–0.02 per notice | CP-1 amended (C5). ⚠ £6–86k a year = ⚠ 0.00–0.02 per £1,000; inside the computing line |
| accrue the day's charge on the drawn balance; hold it on the accrued-charge ledger | money | a.account_line | e.charge_accrual on q.drawn_accounts | ⚠ 228,000 × 365 = 83m a year | ⚠ £0.0001 per line inside the daily batch | PC-1 resolved (C6). ⚠ £8k a year = 0.00 per £1,000 |
| split each receipt charge-first, then principal (WP-3's rule, one more line) | money | a.account_line | e.charge_collection on e.receipt | ⚠ 68m a year | inside WP-3's ⚠ £0.01 per receipt (C1) — no new cost | WP-3 v2 (C6). £0 |

Per drawn account, the automated activities cost ⚠ £2–5 a year on a ⚠ £15–25k balance — ⚠ £0.1–0.3 per £1,000 drawn, rounded up to £2–5 per £1,000 in the FIT model to hold a margin for the computing and payment cost the account line would allocate. The C2 rows add ⚠ £0.003 per £1,000 a year (the statement) and nothing else to the annual line; the rounding absorbs them. The C4 row adds ⚠ 0.01–0.07 per £1,000 a year. The C5 notice adds ⚠ 0.00–0.02 per £1,000 a year; the funded event itself adds nothing.** The computing line is carried as 2.02–5.09 so each addition is visible against the ⚠ £8 cap (C5 record, financial check). **The C8 rows add ⚠ £1–3k a year — ⚠ 0.00 per £1,000; the computing line is unchanged at 2.02–5.11.**

### 3b · Making — exceptions (stream: Making; level: LMU — one exception cell)

| Activity | Flow | Performer | Driver | Volume per cell a year ⚠ | Hours each ⚠ | Hours a year ⚠ |
|---|---|---|---|---|---|---|
| contact an account whose flow has stopped with a balance drawn; agree a clearing plan or close | money | a.exception_handler | e.flow_stop | 2,000 | 4 | 8,000 |
| review an account where a fraud or conduct signal has overridden the rule | information | a.exception_handler | e.signal | 3,000 | 2 | 6,000 |
| handle a customer dispute on the limit or the share | product | a.exception_handler | e.dispute | 1,000 | 1 | 1,000 |
| close and write off | money | a.exception_handler | e.write_off | 1,000 | 1 | 1,000 |
| explain the saving statement to a customer who queries it | information | a.exception_handler | e.saving_query | 2,000 | 0.5 | 1,000 |
| answer a customer who asks why the limit on a given day was what it was — read the history and the rule's inputs for that day; no discretion to change the limit | information | a.exception_handler | e.limit_query on q.replica_accounts | 3,330–10,000 | 0.25 | 830–2,500 |
| explain a funded or a returned payment to a customer who asks; record a switch-off or switch-on instruction — no discretion | information | a.exception_handler | e.funding_query on q.replica_accounts | 270–1,900 | 0.25 | 70–475 |
| explain the charge or a receipt split to a customer who asks — read the ledger; no discretion on the rate | information | a.exception_handler | e.charge_query on q.cell_drawn_accounts | 200–500 | 0.25 | 50–125 — inside the ⚠ 0–425 hours of headroom booked at C5; the cell total is unchanged |
| answer a customer who asks why the software shows more than the balance — explain the credit line and the flag; no discretion | information | a.exception_handler | e.display_query on q.replica_accounts × connected share | 150–700 | 0.25 | 37–175 — inside the ⚠ 0–425 hours of headroom booked at C5 (with C6's 50–125: 87–300 used); no handler added (C7) |
| **answer a customer who asks why the limit stepped, or did not — read the seasoning field and the schedule; no discretion to move the step** | **information** | **a.exception_handler** | **e.seasoning_query on q.cell_drawn_accounts** | **500–1,500** | **0.25** | **125–375 — with C6's 50–125 and C7's 37–175, the recurring query hours are ⚠ 212–675 against the ⚠ 0–425 headroom booked at C5; at the central corner the cell stays at 14; at the high corner it needs a 15th handler (C8)** |
| **Cell total, recurring** | | | **q.cell_drawn_accounts = 100,000 (q.replica_accounts = 333,000 with a limit)** | | | **⚠ 17,955–21,900 — the figure used is the central corner, 20,400 (C5: 19,500 + 70–475 + ⚠ 0–425 headroom; C8: the recurring query hours ⚠ 212–675 use the headroom at the central corner and exceed it by ⚠ 250 at the high corner, where the total is ⚠ 21,900 and a 15th handler is needed)** |
| *explain migration to a customer who declines or asks; record the decline (one-off, launch year only)* | *product* | *a.exception_handler* | *e.migration_decline* | *4,600–7,100, once* | *0.5* | *2,300–3,600, once* |

**Capacity figure used throughout (VA-91): ⚠ 20,400 exception hours per cell a year at the central corner (C8: ⚠ 21,900 at the high corner of demand — the recurring query hours ⚠ 212–675 against the ⚠ 0–425 headroom booked at C5); ⚠ 46,500 hours at scale (2.28 cells on ⚠ 228,000 drawn accounts), ⚠ 49,900 at the high corner.** One cell is ⚠ 14 handlers (band 13–15) at ⚠ 1,400–1,600 productive hours (19,600–22,400 hours against the 20,400) with a cell lead; the trainer is shared across cells. At the low corner of demand (17,955 hours) and the high corner of hours (1,600) the cell runs on 12 handlers with 1,245 hours of slack; 13 is the band floor because the headroom is held. At the high corner of demand (21,900) and the low corner of hours (1,400) it needs 15.6 — the 15th handler is costed and a 16th is not: the query rates that drive the high corner are Tier 4 and the first replica's query log at 12 months converges them. At scale: ⚠ 2.28 cells, ⚠ 32–34 handlers and 3 leads, ⚠ 36–38 people with the shared trainer. Every calculation in the C8 record uses 20,400 and 14 at the central corner and 21,900 and 15 at the high corner.

### 3c · HQ functions (level: HQ; stream: Making support, Delivering, Selling)

| Function | Flow | People ⚠ | Cost a year ⚠ £m | Driver |
|---|---|---|---|---|
| limit engine and data team — builds and runs the rule, the data pipeline, the monitoring | information | 25 | 3.0–4.0 | fixed per HQ |
| **model risk and credit oversight — validates the rule, sets appetite, reports loss by cohort; reads each stage of the release order (C3; the hours are in 3e, no new people); validates the seasoning schedule yearly (C8, ⚠ 100–200 hours inside the 10 people; no new people)** | **information** | **10** | **1.5–2.0** | **fixed per HQ** |
| **product, conduct and compliance — account terms, the CCA agreement under £25,000, Consumer Duty; the migration agreements and the saving statement's conduct standard (C2, +2 people); the limit-history display as a financial promotion template — sign-off, yearly review, complaints (C4, +1 person: the conduct reviewer); the accepted term and the CONC 4.7 information drafted once — ⚠ 200–400 hours = ⚠ £15–30k one-off inside the existing 13 people; no new person (C5) | product | 13 | 1.3–1.95 | fixed per HQ ; the seasoning schedule as a line of the accepted term and its variation notice (C8, ⚠ 40–80 hours inside existing people)**|
| pricing committee — holds PC-1; sets the rate (14.0%) and reviews it yearly | money | existing function, no new people | 0 | fixed per HQ (C2); the review is ⚠ 40–80 hours inside existing sittings (C6) |
| account-information team — populates and withholds the credit-line element; runs the conformance test once | information | existing function, no new people | 0 recurring (the one-offs are in 3e) | fixed per HQ (C7); the element is served by the account line (3a) |
| technology run cost — computing, storage, the payment systems inside the account line allocated to the limit | information | — | 1.0–3.0 | q.accounts_with_limit |
| fraud monitoring allocation | information | — | 0.5–2.0 | q.accounts_with_limit |
| HQ running cost (the RC layer) | | ⚠ 48 | ⚠ 7.3–12.95 | C5: no new people; the one-off drafting sits in SC |
| **exception cells (from 3b; counted in the PVC layer, not here)** | **money · information · product** | **36–38** | **2.05–2.82** | **q.drawn_accounts — C5: 14 handlers per cell (band 13–15), 2.28 cells; C8: 15 at the high corner; 32–34 handlers ⚠ £50–65k, 3 leads ⚠ £70–90k, trainer ⚠ £20–30k, tooling ⚠ £0.23–0.34m** |
| **All people in the form** | | **⚠ 84–86** | **⚠ 9.35–15.77** | ≈ ⚠ 0.16–0.46% of the drawn book, stated for scale only — no cost line is derived from it |

**Correction at v2.** v1 counted the exception cells in both 3b (the PVC exceptions line) and 3c (the RC line). v2 counts them once, in PVC. The RC layer falls from ⚠ £8.5–14.5m to ⚠ £7.2–12.8m; the rounded RC figure per £1,000 (section 6) is unchanged.

Headcount check: the conventional form at this volume employs relationship managers (a portfolio of ⚠ 200–300 clients each below £2m turnover, CMA 2016 and judged), credit underwriters, security administrators and a collections and recoveries function (FCA SME collections review 2022 covered 11 banks). None of those roles exists in this form. The insider corrects the conventional headcount; no public source carries it.

### 3e · Scaling stages — the release order (stream: Making support; level: HQ; path only, not in the annual floor) — C3

Every row here is a one-off or a stage-bound cost. None is an annual cost of the at-scale form. Together they are the SC layer.

| Activity | Flow | Performer | Driver | Volume | Cost ⚠ | Note |
|---|---|---|---|---|---|---|
| assemble ⚠ 3–5 years of transaction history and run the rule over it; compare the limits it would have set with the loss the bank took | information | a.limit_engine, a.model_risk | e.backtest | once | £0.2–0.5m (engine team time ⚠ 1,500–3,000 hours at £100–150 loaded; data extraction inside the account line) | Stage 0, ⚠ 3–6 months. The record is the validation evidence |
| independent validation of the back-test (SS1/23 Principle 4: outcomes analysis, back-testing, documentation) | information | a.model_risk | e.backtest | once | £0.1–0.3m (⚠ 800–1,500 hours; no new people — inside the 10 in 3c) | Stage 0 |
| migrate the overdraft accounts (WP-4, from 3a) with the rule's limit released only where it is at or below the existing limit | product | a.account_line, a.product_conduct | e.migration | ⚠ 104,500–161,500, once | £0.1–0.5m notices; ⚠ 5,300–8,200 handler hours (3b, one-off) = ⚠ £0.3–0.85m in all | Stage 1. Carried by number from C2; the release rule is C3's |
| read the trial band on the Stage 1 pool (loss by cohort against 4.8% / 5.0%) and put it to the committee | information | a.model_risk, a.risk_committee | e.stage_reading | once, at 12 months | ⚠ 150–300 hours = £15–45k | Stage 1 → 2. The yes-threshold is pre-registered (VA-163) |
| release a replica: switch the release flag on ⚠ 333,000 accounts; show the limit (CP-1) | product | a.account_line | e.release | ⚠ 2, once each | inside the account line's cost — a flag change and the existing statement | Stage 2 |
| read the replica band at 6 months and put it to the committee | information | a.model_risk, a.risk_committee | e.stage_reading | ⚠ 2, once each | ⚠ 150–300 hours each = £15–45k each | Stage 2 |
| book the overlay at each release; release it at the reading | money | a.finance | e.release | ⚠ 3 | Stage 1 ⚠ £0–19m for 12 months; each replica ⚠ £0–50m for 6 months; carrying cost at ⚠ 12–15% cost of equity ⚠ £0–10.4m in all | the working capital of the path — the CLO II's capital, not a cost line of the form; the carrying cost is the SC layer's largest item |
| fund each replica's drawn balance | money | a.treasury | e.release | ⚠ 2 | ⚠ £155–281m of lending capital per replica, ⚠ £0.31–0.56bn in all; the deposit cost is already in PVC — no new line | at scale the funding is the C1 funding line; nothing is added |
| build the population rule for the pre-agreed credit-line element (released accounts only; flag not included; the shadow limit never published) | information | a.account_information_team | e.field_build | once | ⚠ 400–800 hours at ⚠ £100/h = £40–80k | C7, PP-1 — amortised over five years in section 6 |
| test conformance with the three largest account-information providers and the three largest platforms; read each platform's display | information | a.account_information_team | e.conformance_test | once, 6 counterparties | ⚠ 100–200 hours = £10–20k | C7, PP-1 — the hours per close read for the aggregate form (VA-165): there is no close, only this test |
| **build the seasoning field and the schedule into the rule; test it on the back-test history** | **information** | **a.limit_engine** | **e.engine_build** | **once** | **⚠ 200–400 hours at ⚠ £100/h = £20–40k** | **C8, WP-1 v2 — inside the engine team's 25 people; the form's own item because the schedule is the form's, not the roadmap's** |
| **SC layer, one-off total** | | | | | **⚠ £0.74–12.29m** (back-test 0.3–0.8; migration 0.3–0.85; readings 0.045–0.135; carrying cost 0–10.4; the term drafting 0.015–0.03 (C5); the representative example 0.01–0.02 (C6); the element build and the conformance test 0.05–0.10 (C7); **the seasoning build 0.02–0.04 (C8)**) | ÷ 5 years ÷ £3.4–5.7bn = £0.03–0.72 per £1,000 a year → 0–1 (section 6) |

**Two things the section does not contain, and why.** The engine build is a roadmap cost the bank carries whether or not this form launches (C1); it is not the form's. The overlay itself is capital held, not a cost; only its carrying cost is costed. Both are stated in the C3 record.

**Capacity at each stage (VA-91).** Stage 1 runs one exception cell (⚠ 46,000–71,000 overdraft-origin drawn accounts inside the 100,000 the cell covers). Each replica opens one cell. The cell count at scale (⚠ 2.3) is unchanged from v2.

### 3d · Activities the conventional form performs and this form removes (for the drop, not the floor)

| Conventional activity | Zone | Cost evidence |
|---|---|---|
| assess an application on financial statements, credit history and security | Making | US benchmark $3,000–4,000 per small loan (ProSight, T3); judged UK bank cost per person-decision ⚠ £500–1,500 (bank-conventional-model-object.yaml, 14 Sep 2026); "the transaction cost of a $100,000 loan is comparable to that of a $1m loan" (Mills and McCarthy, HBS 2014) |
| take and perfect security | Making | ⚠ £200–800 per facility |
| annual review of each facility, **including the overdraft's annual renewal and its fee event (C2)** | Making | ⚠ £200–500 per facility a year |
| collections and recoveries | Delivering | FCA 2022 review; ⚠ £5–15 per £1,000 drawn |
| relationship management allocated to lending | Selling | ⚠ £240–360 per client a year below £2m (judged, from Glassdoor pay and a judged portfolio) |
| product marketing of the facility and the relationship manager's outreach to make the customer want it | Selling | ⚠ £30–100 per drawn account a year = ⚠ 2–8 per £1,000 (counterfactual, RD-030, R4 line); removed at C4 — the form books no acquisition cost |
| onboarding calls, help content and a support line for the customer's first draws | Using | ⚠ £15–40 per drawn account in the first year = ⚠ 1–2 per £1,000 (counterfactual, RD-030, R5 line); removed at C5 — there is no first draw for the customer to learn |

### 3f · Selling stream — conviction (C4)

The Selling stream in this form contains no acquisition activity. Conviction is a read of a ledger the bank already holds, placed at a moment the bank already sees. Its three activities sit in the tables above, each with a driver that resolves to section 0:

| Activity | Where costed | Level | Driver | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|
| store, render and place the limit history (CP-2) | 3a | per account, automated | e.shortfall | £76–228k | 0.01–0.07 |
| sign and review the promotion template; handle display complaints | 3c | HQ | e.template_review | £0.1–0.15m | 0.02–0.04 |
| answer limit-history queries | 3b | cell | e.limit_query | £0–296k (0–2 handlers per cell × 2.28 cells) | 0.00–0.09 |
| Selling stream total at C4 | | | | ⚠ £0.18–0.67m | ⚠ 0.03–0.20 |

**Conventional additions used against the ⚠ £8 cap (RD-030), as at C4:** R4 ⚠ 0.03–0.20; cumulative through R4 ⚠ 0.03–0.20; remaining at the high corner ⚠ 7.80. The running line continues in 3g.

### 3g · Using stream — activation (C5) and the charge (C6)

The Using stream in this form contains no activation activity for the customer to perform. The draw is the account's act under a term accepted once. Its four activities sit in the tables above, each with a driver that resolves to section 0:

| Activity | Where costed | Level | Driver | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|
| authorise against the available balance; fund; record the funded event (WP-2 v2) | 3a | per event, automated | e.funded_event | £0 | 0.00 |
| the funded-event notice and statement line (CP-1 amended) | 3a | per event, automated | e.funded_event | £6–86k | 0.00–0.02 |
| explain a funded or returned payment; record a switch-off | 3b | cell | e.funding_query | £0–148k (0–1 handler per cell × 2.28 cells) | 0.00–0.04 |
| draft the term and the CONC 4.7 information; the notice wording | 3c (one-off, in SC) | HQ, once | e.term_drafting | £15–30k once = £3–6k a year over five years | 0.00 |
| Using stream total at C5 | | | | ⚠ £0.08–0.24m | ⚠ 0.02–0.06 |
| accrue the day's charge (PC-1 resolved) | 3a | per account per day, automated | e.charge_accrual | ⚠ £8k | 0.00 |
| split each receipt charge-first (WP-3 v2) | 3a | per receipt, automated | e.charge_collection | £0 (inside WP-3) | 0.00 |
| set and review the rate | 3c | HQ, yearly | e.rate_review | inside RC | 0.00 |
| draft the representative example and the CONC 4.7 rate line; sign the APR basis | 3e (one-off, in SC) | HQ, once | e.representative_example | ⚠ £10–20k once = £2–4k a year over five years | 0.00 |
| explain the charge or a receipt split | 3b | cell | e.charge_query | ⚠ £0–30k (50–125 h × 2.28 cells, inside the C5 headroom; costed here at the handler rate for visibility) | 0.00–0.01 |
| Using stream total at C6 | | | | ⚠ £0.09–0.28m | ⚠ 0.02–0.07 |

**Conventional additions used against the ⚠ £8 cap (RD-030), as at C6:** R4 ⚠ 0.03–0.20; R5 ⚠ 0.02–0.06; R6 ⚠ 0.00–0.01 (the conventional R6 line is nil — nothing removed); cumulative through R6 ⚠ 0.05–0.27; remaining at the high corner ⚠ 7.73. The running line continues in 3h.

### 3h · Selling stream — access (C7)

The Selling stream gains its second class of activity: access. It contains no acquisition activity, no partner agreement and no fee. The limit reaches the seat where a connected customer's shortfall is first foreseen because it is published as a property of the account's balance under a standard every reader already conforms to. Its five activities sit in the tables above, each with a driver that resolves to section 0:

| Activity | Where costed | Level | Driver | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|
| serve the credit-line element in each balance response (PP-1) | 3a | per call, automated | e.balance_call | ⚠ £5–8k | 0.00 |
| build the population rule | 3e (one-off, in SC) | HQ, once | e.field_build | ⚠ £40–80k once = £8–16k a year over five years | 0.00 |
| test conformance with six counterparties | 3e (one-off, in SC) | HQ, once | e.conformance_test | ⚠ £10–20k once = £2–4k a year over five years | 0.00 |
| sign and review the desk position (account information, not a promotion) | 3c | HQ, once then yearly | e.field_position | inside RC | 0.00 |
| answer display queries | 3b | cell | e.display_query | ⚠ £3–14k (37–175 h × 2.28 cells, inside the C5 headroom; costed here at the handler rate for visibility) | 0.00–0.01 |
| Selling stream — access, total at C7 | | | | ⚠ £0.02–0.04m | ⚠ 0.00–0.01 |

**What the class is paid.** Nothing. The platform's return is its own forecast's accuracy (⚠ £150–300k a year of retained subscribers per platform, judged); the accountant's is the pack hours not spent; the provider's is the conformance it sells. The venture's maximum payable to any holder (VA-164) is 7.15 per £1,000 at the central corner and 0 at the pessimistic corner; paid: 0.

**Conventional additions used against the ⚠ £8 cap (RD-030):** R4 ⚠ 0.03–0.20; R5 ⚠ 0.02–0.06; R6 ⚠ 0.00–0.01; R7 ⚠ 0.00–0.01 (the conventional R7 line ⚠ 6–35 — broker commission, platform referral fees, partner marketing and a partner desk — removed); cumulative through R7 ⚠ 0.05–0.28; remaining at the high corner ⚠ 7.72. Function 2 complete: R4–R7 used ⚠ 0.05–0.28 of the ⚠ £8.

### 3i · Using stream — accumulation (C8)

The Using stream gains its second class of activity: accumulation. The customer performs nothing; the store of value is a field the engine already writes, read on a schedule the customer can see. Its six lines sit in the tables above, each with a driver that resolves to section 0:

| Activity | Where costed | Level | Driver | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|
| **read the seasoning field and apply the schedule (WP-1 v2)** | **3a** | **per account per day, automated** | **e.daily_recompute** | **inside the compute cost** | **0.00** |
| **recognise a cleared event and step the field** | **3a** | **per event, automated** | **e.cleared_event** | **⚠ £1–3k** | **0.00** |
| **build the field and the schedule; test on the back-test** | **3e (one-off, in SC)** | **HQ, once** | **e.engine_build** | **⚠ £20–40k once = £4–8k a year over five years** | **0.00** |
| **validate the schedule yearly** | **3c** | **HQ, yearly** | **e.seasoning_review** | **inside RC** | **0.00** |
| **answer seasoning queries** | **3b** | **cell** | **e.seasoning_query** | **⚠ £14–43k at the central corner (125–375 h × 2.28 cells, inside the headroom, costed at the handler rate for visibility); ⚠ £0.12m at the high corner (the 15th handler in 2.28 cells)** | **0.00–0.02** |
| **capital on the larger undrawn commitment** | **6 (IC)** | **book** | **q.undrawn_per_drawn** | **⚠ £1.5–8.4m (0.4–1.1 × 10% × 75% × 12% × 12–15% × £3.4–5.7bn)** | **⚠ 0.43–1.48** |
| **Using stream — accumulation, total at C8** | | | | **⚠ £1.5–8.6m** | **⚠ 0.45–1.50** |

**Conventional additions used against the ⚠ £8 cap (RD-030):** R4 ⚠ 0.03–0.20; R5 ⚠ 0.02–0.06; R6 ⚠ 0.00–0.01; R7 ⚠ 0.00–0.01; **R8 ⚠ 0.45–1.50 unrounded, carried as ⚠ 1.00 in the rounded IC layer (the conventional R8 line ⚠ 5–15 — loyalty pricing, exit fees, product tie-ins, a retention desk — removed); cumulative through R8 ⚠ 0.50–1.78 unrounded, ⚠ 1.05–1.28 rounded; remaining at the high corner ⚠ 6.72.** Function 3 opens with ⚠ 6.72 of the ⚠ £8 unused.

## 4 · Role support (every performer has a supervisor, a trainer and a quality reviewer)

| Performer | Supervisor | Trainer | Quality reviewer |
|---|---|---|---|
| exception handler | cell lead | cell lead, with the product team's conduct standard; **the migration and saving-statement scripts are part of the handbook (C2)** | model risk (samples closed cases monthly); **conduct samples migration declines quarterly (C2)** |
| cell lead | head of exceptions (one across cells) | head of exceptions | model risk |
| limit engine (the rule) | head of the engine team | — (a rule; the team is trained by the engine team's own onboarding) | model risk (independent validation under SS1/23) |
| account line (the ledger, the statement) | head of the account line (Case A) | — (a system) | second-line operational risk (existing) |
| product, conduct and compliance | head of product | second-line compliance (the conduct standard) | second-line compliance (existing) |
| the conduct reviewer (the promotion template) | head of compliance (existing) | the FCA's CONC 3 material and the firm's promotion procedure (existing) | internal audit (existing); the signed template and its yearly review are a documented control (C4) |
| exception handler — the funding-query and switch-off script (C5) | cell lead | cell lead, with the accepted term and the notice wording in the handbook | model risk (samples funded-event queries monthly with the closed cases); conduct samples switch-off handling quarterly |
| exception handler — the charge-query script (C6) | cell lead | cell lead, with the representative example and the split rule in the handbook | the conduct function (samples charge queries for the wording of the example) |
| exception handler — the display-query script (C7) | cell lead | cell lead, with the credit-line element and the flag explained in the handbook | the conduct function (samples display queries for the desk position's wording) |
| **exception handler — the seasoning-query script (C8)** | **cell lead** | **cell lead, with the published schedule and the cleared-event definition in the handbook** | **the conduct function (samples seasoning queries for the schedule's wording); model risk (samples stepped accounts with the closed cases)** |
| the account-information team (the element) | head of the account line (Case A, existing) | the Open Banking standard's specification and the firm's conformance procedure (existing) | second-line operational risk (existing); the conformance test is a documented control |
| pricing committee | the chief financial officer's function (existing) | — (a committee of existing officers) | second-line compliance and internal audit (existing); the condition is a documented control |
| treasury | head of treasury (existing) | — | asset and liability committee (existing) |
| the board risk committee (the release signatory) | the board (existing) | — (a committee of existing directors) | internal audit (existing); each release is a minuted decision against a pre-registered band |
| finance (the overlay) | the chief financial officer (existing) | — | the external auditor (existing); PRA Dear CFO letters on post-model adjustments set the standard |

PASS: no performer lacks a supervisor, a trainer or a reviewer.

## 5 · LMU sizing — one exception cell

| Item | Value ⚠ |
|---|---|
| drawn accounts covered | 100,000 (q.cell_drawn_accounts) |
| drawn balance covered | £1.5–2.5bn |
| people | 14 handlers (band 13–15) + 1 lead + 1 trainer (shared across cells) — C5 |
| fixed cost a year | £0.9–1.24m (14 handlers, 15 at the high corner (C8) ⚠ £50–65k loaded; lead ⚠ £70–90k; trainer share ⚠ £20–30k; tooling and premises ⚠ £0.1–0.15m) — C5; was £0.85–1.12m at 13 handlers |
| contribution from the balance covered at the ⚠ 7.5–12% price paid today on the whole book | £110–300m of revenue |
| stand-up time | ⚠ 6–10 weeks (the handbook is the training; the rule is already running) |
| replica (C3) | one replica of the release order = one cell: ⚠ 333,000 accounts with a limit, ⚠ 100,000 drawn. The scaling unit and the operating unit are the same object |
| limit-history queries (C4) | ⚠ 3,330–10,000 a year per cell at 0.25 hours; the C4 rows are the reason the cell is 13 handlers |
| funding queries and switch-off instructions (C5) | ⚠ 270–1,900 a year per cell at 0.25 hours, plus ⚠ 0–425 hours of headroom for the first-year peak; the C5 row is the reason the cell is 14 handlers |
| charge queries (C6) | ⚠ 200–500 a year per cell at 0.25 hours = 50–125 hours, inside the C5 headroom; the cell stays at 14 handlers |
| display queries (C7) | ⚠ 150–700 a year per cell at 0.25 hours = 37–175 hours, inside the C5 headroom (87–300 of 0–425 used with C6); the cell stays at 14 handlers |
| **seasoning queries (C8)** | **⚠ 500–1,500 a year per cell at 0.25 hours = 125–375 hours; recurring query hours ⚠ 212–675 against the ⚠ 0–425 headroom; the cell stays at 14 at the central corner and needs a 15th handler at the high corner (⚠ 21,900 hours)** |

The cell covers its cost from a fraction of a per cent of the revenue on the balance it covers. PASS on contribution. The price used here is the whole book's price paid today (C1), not the selected customer's KMC; the C2 fit model carries the KMC.

## 6 · Cost floor derivation (per £1,000 of average drawn balance, per year, at scale — the FIT input)

| Layer | £ per £1,000 a year ⚠ | Derivation |
|---|---|---|
| PVC — funding | 15–30 | deposit cost ⚠ 1.5–3.0% (Bank Rate 4.0% from August 2025, FACT); unchanged by migration — the balance was already funded |
| PVC — expected loss | 20–40 | ⚠ 2.0–4.0% on a flow-underwritten pool; the critical assumption. At C2 the migrated pool is an observed-conduct pool (the bank has seen its overdraft behaviour), which cannot raise the rate above the flow-underwritten assumption; the band is held, not lowered — the insider's figure replaces it |
| PVC — computing and payments | 2.02–5.11 | 3a, rounded up; the saving statement adds ⚠ £0.003; the limit history adds ⚠ 0.01–0.07 (C4); the funded-event notice adds ⚠ 0.00–0.02 (C5); the accrual ledger adds ⚠ 0.00–0.01 (C6); the charge-first split adds nothing; the credit-line element adds ⚠ 0.00–0.01 (C7) |
| PVC — exceptions and write-off handling | 3.00–8.13 (3.00–8.15 at the high corner of the cells with the 15th handler; inside the rounded band) | 3b: ⚠ £2.05–2.7m across 2.28 cells ÷ £3.4–5.7bn = £0.36–0.79, plus write-off administration and legal ⚠ £3–7; the limit-query handlers add ⚠ 0.00–0.09 (C4); the funding-query handlers add ⚠ 0.00–0.04 (C5); the charge queries add nothing (inside the C5 headroom, C6); the display queries add nothing — inside the C5 headroom (C7) |
| PVC | 40.02–83.24 | C7: +0.00–0.01 on C6's 40.02–83.23 |
| RC | 2.02–5.04 | 3c: ⚠ £7.3–12.95m ÷ £3.4–5.7bn = £1.28–3.81, carried at the C1 band plus the conduct reviewer, ⚠ 0.02–0.04 (C4); unchanged at C5; unchanged at C6 — the rate review sits in existing sittings; unchanged at C7 — the desk position sits inside the existing conduct people |
| SC | 0–1 | 3e: one-off ⚠ £0.64–12.1m (back-test and validation, migration, stage readings, the overlay's carrying cost) plus the term drafting ⚠ £15–30k (C5) plus the representative example ⚠ £10–20k (C6) plus the element build and the conformance test ⚠ £50–100k (C7) ÷ 5 years ÷ £3.4–5.7bn = £0.03–0.72, rounded up to 0–1. The 5-year period is the runner's call: the MLR retention period and the path's ⚠ 27–42 months both sit inside it |
| IC — capital on drawn | 10.8–13.5 | 75% risk weight (regulatory retail SME, standardised, FACT) × ⚠ 12% total capital × ⚠ 12–15% cost of equity |
| **IC — capital on undrawn** | **2.05–4.86** | **q.undrawn_per_drawn ⚠ 1.9–3.6 (C8: was 1.5–2.5 — the seasoned limit raises the undrawn commitment) × 10% credit conversion factor (Basel 3.1, PRA PS9/24, from 1 January 2027, FACT) × 75% × 12% × 12–15%; an overdraft limit already carried this treatment, so migration adds nothing; C8 adds ⚠ 0.43–1.48** |
| **IC** | **13–18** | **rounded; unrounded 12.85–18.36 (C8: was 12–17)** |
| **Cost floor at C8 (PVC + RC + SC + IC)** | **55.04–107.28** | **C8 adds ⚠ 1.00 per £1,000 in the rounded IC layer (⚠ 0.45–1.50 unrounded) to the 54.04–106.28 of C7; carried at two decimals so the addition is visible against the ⚠ £8 cap** |

**What R8 changed in the floor: ⚠ 0.45–1.50 per £1,000 a year unrounded, carried as ⚠ 1.00 in the rounded IC layer — all of it capital on the larger undrawn commitment.** Computing unchanged (the seasoning field and the cleared event are ⚠ £1–3k a year); exceptions unchanged at the central corner (the seasoning queries sit inside the headroom) and +0.02 at the high corner (the 15th handler, inside the rounded 3.00–8.13 band); RC unchanged (the yearly validation sits inside model risk's 10 people); SC unchanged at 0–1 (the seasoning build, ⚠ £20–40k once, sits inside the band); IC +0.43–1.48 (undrawn per drawn 1.5–2.5 → 1.9–3.6). The floor is 55.04–107.28. The conventional R8 line of ⚠ 5–15 — loyalty pricing, exit fees, product tie-ins, a retention desk — is not booked. Conventional additions used against the ⚠ £8 cap through R8: ⚠ 1.05–1.28 rounded (0.50–1.78 unrounded); remaining ⚠ 6.72 at the high corner.

**What R7 changed in the floor: ⚠ 0.00–0.01 per £1,000 a year, all of it inside existing layers.** Computing +0.00–0.01 (the credit-line element in the balance response); exceptions unchanged (the display queries sit inside the C5 headroom); RC unchanged (the desk position sits inside the existing conduct people); SC unchanged at 0–1 (the element build and the conformance test, ⚠ £50–100k once, sit inside the band). The floor is 54.04–106.28. The conventional R7 line of ⚠ 6–35 — broker commission, platform referral fees, partner marketing, a partner desk — is not in this floor because no partner is paid: the class carries the limit by conformance to a standard it already meets. Cumulative conventional additions R4–R7: ⚠ 0.05–0.28 of the ⚠ £8 cap.

**What R6 changed in the floor: ⚠ 0.00–0.01 per £1,000 a year, all of it inside existing layers.** Computing +0.00–0.01 (the accrual ledger); exceptions unchanged (the charge queries sit inside the C5 headroom); RC unchanged (the rate review sits in existing sittings); SC unchanged (the representative example sits inside the band). The floor is 54.04–106.27. The conventional R6 line is nil: the counterfactual books no cost against the price structure, so nothing is removed from the cap; the block's cost to the conventional bank is revenue given up and arrears work, which this form does not have. The set price is 140 per £1,000 (14.0%); the margin at the worst corner is (140 − 106.27) ÷ 106.27 = 31.7%. The working-capital gain from collection at each receipt (⚠ £0.9–2m a year) is stated in section 2 and not credited. Conventional additions used against the ⚠ £8 cap: R4 0.03–0.20; R5 0.02–0.06; R6 0.00–0.01; cumulative 0.05–0.27; remaining ⚠ 7.73 at the high corner.

**What R5 changed in the floor: ⚠ 0.02–0.06 per £1,000 a year, all of it inside existing layers.** Computing +0.00–0.02 (the notice), exceptions +0.00–0.04 (the funding-query handlers), SC unchanged (the term drafting sits inside the band). The floor is 54.04–106.26. The conventional R5 line of ⚠ 1–2 is not booked. The drawn-book rise under default funding is not credited: it would lower every fixed line per £1,000 and is an unmeasured input. Conventional additions used against the ⚠ £8 cap: R4 0.03–0.20 + R5 0.02–0.06 = ⚠ 0.05–0.26; remaining ⚠ 7.74 at the high corner.

**What R4 changed in the floor: ⚠ 0.03–0.20 per £1,000 a year, all of it inside existing layers.** Computing +0.01–0.07 (the history), RC +0.02–0.04 (the conduct reviewer), exceptions +0.00–0.09 (the query handlers). The floor is 54.03–106.20. The conventional R4 line of ⚠ 2–8 is not booked. Conventional additions used against the ⚠ £8 cap: ⚠ 0.03–0.20; remaining ⚠ 7.80 at the high corner.

**What R3 changed in the floor: the SC layer, from unpopulated to 0–1.** The floor is 54–106 per £1,000 a year, complete on four layers. The high corner moves by £1; the low corner does not move. The floor a C3 price must clear is ⚠ 54–106.

**What R2 changed in the floor: nothing that survives rounding.** The migration is a one-off; the statement is ⚠ £0.003 per £1,000; the extra exception hours are ⚠ £0.02–0.05 per £1,000 inside the 3–8 band. The floor a C2 price had to clear was ⚠ 54–105 per £1,000 a year. The KMC it is measured against is ⚠ £150–300 (TAM data object, KMC-OD-STD-TARIFF).

Conventional form on the same unit, all ⚠, unchanged from v1: application form ⚠ 60–154; roadmap form (v1 section 7) ⚠ 63–164 blended, ⚠ 57–133 on the pre-approved segment. On the selected customer's own alternative — the standard-tariff overdraft — the price paid is ⚠ 150–300, and the conventional cost behind it is the roadmap form's ⚠ 57–133 plus the tariff's margin; the gap between what the customer pays and what the form costs is what R2 selects.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. Runner-drafted, PROVISIONAL on the object-after PCO. |
| v1.1 | 18 September 2026 | Baseline correction (roadmap form). |
| v2 | 21 September 2026 | R2 update. Section 0 added: every driver now resolves to a named quantity, event or actor (RD-031). Every activity row names its flow. Migration (WP-4), the saving statement (CP-1) and the pricing committee (PC-1) added; two exception rows added (saving query, recurring; migration decline, one-off); capacity figure restated once at ⚠ 17,000 hours per cell; cells resized to 12 handlers. Double count of the exception cells between 3b and 3c removed. Floor recomputed on four layers: ⚠ 54–105, unchanged. |
| v3 | 21 September 2026 | R3 update. Section 0: four quantities (replica, replica count, history years, unreleased accounts), three events (back-test, stage reading, release), two actors (the board risk committee, finance). Section 3a: the shadow-limit row. New section 3e: the scaling stages as costed activities, one-off total ⚠ £0.64–12.1m. Section 4: two role-support rows. Section 5: replica = cell. Section 6: SC populated at 0–1; floor 54–106, complete on four layers; the C2 indicative caveat closed. Capacity figure unchanged at ⚠ 17,000 hours per cell. |

| v4 | 21 September 2026 | R4 update. Section 0: productive hours restated as a band ⚠ 1,400–1,600 with sources (verify-F1 F-2 closed); three events (shortfall, limit query, template review); one actor (the conduct reviewer); the cell floor at 13 handlers (band 12–14). Section 1: two actor rows amended, one added. Section 2: the C4 information and product flows; marketing and outreach named as not performed. Section 3a: the limit-history row. Section 3b: the limit-query row; capacity figure restated once at ⚠ 19,500 hours per cell. Section 3c: +1 conduct person; RC ⚠ £7.3–12.95m. Section 3d: the marketing line as removed. New section 3f: the Selling stream and the cap line. Sections 4 and 5: the conduct reviewer; the cell at 13. Section 6: floor 54.03–106.20, carried at two decimals. |
| v5 | 21 September 2026 | R5 update. Section 0: three events (funded event, funding query, term drafting); the cell floor at 14 handlers (band 13–15). Section 1: five actor rows amended. Section 2: the C5 money, information and product flows; onboarding, help content and the support line named as not performed. Section 3a: the authorisation-and-funding row (£0) and the notice row. Section 3b: the funding-query row; capacity figure restated once at ⚠ 20,400 hours per cell with ⚠ 0–425 hours of headroom. Section 3c: no new people; cells at 36 people; all people ⚠ 84. Section 3d: the onboarding line as removed. New section 3g: the Using stream and the running cap line (cumulative 0.05–0.26; remaining 7.74). Sections 4 and 5: the funding-query script; the cell at 14. Section 6: floor 54.04–106.26, carried at two decimals. C4 rows carried with their bold removed. |
| v6 | 21 September 2026 | R6 update. Section 0: five events (charge accrual, charge collection, rate review, representative example, charge query); the cell floor unchanged at 14 handlers. Section 1: the pricing committee row amended. Section 2: the money flow carries the accrued-charge receivable cycle (⚠ 1–3 days) and the conventional charging events removed. Section 3a: the accrual row and the charge-first split row; 3b: the charge-query row inside the C5 headroom; 3c: the pricing committee row amended; 3e: the representative example in the SC total; 3g: five rows and the C6 total; the cap line through R6. Section 4: the charge-query script. Section 5: the charge-query line. Section 6: computing 2.02–5.10, PVC 40.02–83.23, floor 54.04–106.27; "What R6 changed in the floor". C5 rows carried with their bold removed. |
| v7 | 21 September 2026 | R7 update. Section 0: one quantity (connected accounts ⚠ 342,000–532,000), five events (balance call, display query, field build, conformance test, field position), four actors (the account-information team, internal; the provider, the platform and the accountant, external); the cell floor unchanged at 14 handlers. Section 1: four actor rows. Section 2: the C7 information and product flows; the broker channel, the referral agreement, the partner desk and the accountant programme named as not performed (the conventional R7 line). Section 3a: the credit-line element row. Section 3b: the display-query row inside the C5 headroom. Section 3c: the account-information team row. Section 3e: the element build and the conformance test (SC one-off total ⚠ £0.72–12.25m). New section 3h: the Selling stream — access, with the cap line through R7 (cumulative ⚠ 0.05–0.28; remaining ⚠ 7.72). Sections 4 and 5: the display-query script and the account-information team. Section 6: computing 2.02–5.11; PVC 40.02–83.24; floor 54.04–106.28. C6 rows carried with their bold removed. |
| v8 | 21 September 2026 | R8 update. Section 0: q.undrawn_per_drawn restated at ⚠ 1.9–3.6 (was 1.5–2.5) with its threshold and convergence; q.seasoned_share; four events (cleared event, engine build, seasoning review, seasoning query); the cell floor unchanged at 14 (band 13–15) with the 15th handler costed at the high corner. Section 1: the limit engine and model risk rows amended. Section 2: the C8 money, information and product flows; loyalty pricing, exit fees, tie-ins and a retention desk named as not performed. Section 3a: the seasoning-read row and the cleared-event row. Section 3b: the seasoning-query row; the C5 headroom split into first-year and recurring; capacity figure restated once at ⚠ 20,400 central / ⚠ 21,900 high corner. Section 3c: model risk and conduct rows amended, no new people; cells at 36–38 people; all people ⚠ 84–86. Section 3e: the seasoning build in the SC total (⚠ £0.74–12.29m). New section 3i: the Using stream — accumulation, with the running cap line. Section 4: the seasoning-query script. Section 5: the seasoning-query row. Section 6: IC 13–18 (12.85–18.36 unrounded); floor 55.04–107.28. |
