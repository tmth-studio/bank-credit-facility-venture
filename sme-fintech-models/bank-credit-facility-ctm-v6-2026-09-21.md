# Business bank credit facility line — customer transformation map (CTM), v6, at C6

**Venture:** the credit facility line of a large UK SME bank (Case B — term loan and overdraft), Path C mode 3 — see `../bank-credit-facility-c6-v1-2026-09-21.md`. **v6 written at R6** (21 Sep 2026), runner-drafted under the propose-and-confirm rule. **v5**, **v4**, **v3**, **v2** and **v1** are retained unchanged as the C5, C4, C3, C2 and C1 records. **Update mode:** only the rows R6 adds or changes are new (marked *C6*, in bold); every other row is carried from v5 with its trace and its bold removed. R6 fills Phase 3 — Paying by resolving PC-1 from a condition to a price — the charge: 14.0% simple a year on the daily drawn balance, no fee, accrued daily and collected only from receipts as the first slice of each receipts share (WP-3, amended) — and by naming the buy block it removes: the calendar debit, a charge due on the bank's date rather than with the customer's trade. No component is added; none is removed.

**Defined terms.** As in v1: *flow*, *standing limit*, *draw*, *receipts share*, *account line*. New at C2: *Standard tariff* — the published interest rate and fees a bank charges on a business overdraft that is not individually negotiated. *Migration* — the one-time move of a customer's existing arranged overdraft, and any balance drawn on it, into the standing limit and a draw with a receipts share. *Price condition* — the rule that the all-in price of the limit per £1,000 drawn stays below the standard-tariff cost the customer paid before migration; a condition, not a price — the price and its structure are C6's. New at C3: *Shadow limit* — the standing limit the rule computes and records for an account without the customer being able to draw on it. *Back-test* — the rule run over the bank's own past flow and compared with the loss actually taken. *Release* — the event at which a shadow limit becomes drawable; by stage, never by application. *Overlay* — the extra loss allowance finance books while a model is unproven. *Trial band* and *replica band* — the kill bands for the first instance and for each repeat (VA-163). New at C4: *Shortfall* — the day a scheduled payment (direct debit, standing order or a payment the customer has set up) exceeds the available balance; the bank sees it before it settles. *Limit history* — the standing limit shown beside the twelve months of the customer's own shortfalls it would have covered, each with the date, the amount, the balance that day and the limit that day; computed from the stored daily limit and the back-test (WP-5). *Placement* — the limit history put in front of the customer on the shortfall day, in the account, with nothing sent. New at C5: *Use block* — the routine disruption the C1 form itself introduced: the draw was a customer act at a cue (the shortfall) that instant payment channels give no moment to perform. *Default funding* — the account rule that a payment exceeding the available balance is met from the standing limit, within the limit, with nothing for the customer to do; the same mechanism an arranged overdraft already uses. *Acceptance* — the customer's one-time agreement to the limit term at release (for the migrated customer, the modifying agreement under CCA 1974 s.82 where the agreement is regulated). *Draw ahead* — the explicit draw retained as an option: the customer moves money from the limit to the balance before a payment. *Funded event* — one payment met from the limit under default funding; the unit the account records and the billing unit C6 will price. *Available balance* — the credit balance plus the undrawn standing limit, shown as one figure. *Switch-off* — the customer's option to turn default funding off for the account; a payment that then exceeds the balance is returned as it is today. *Reversal* — a customer's repayment of a funded event within three days of it, read as a signal that the funding was unwanted. New at C6: *The charge* — the price of the limit: interest accrued daily on the drawn balance at one rate (14.0% simple a year; band ⚠ 13.5–14.25%), no fee. *Accrual* — the daily addition to the accrued-charge ledger (drawn balance × rate ÷ 365); the accrued charge is not added to the drawn balance and bears no interest. *Collection* — the first slice of each receipts share clears the accrued charge; the remainder repays the drawn balance; no debit is made for the charge. *Representative example* — the CONC 3.5.5R illustration shown wherever the rate is shown. *Calendar debit* — the conventional charging event (interest and fees debited on a fixed date), the block R6 removes.

## 1 · Component register (Flow Register format)

| ID | Product | Component | Introduced at | Carries |
|---|---|---|---|---|
| WP-1 | Working | the standing limit — computed from the flow by the limit engine, shown in the account, recomputed daily | C1 | the customer's "I can see what I can draw" state; the bank's exposure decision, which no person makes |
| WP-2 | Working | the draw — the customer moves money from the limit to the balance in the account, no application (C1); v2 at C5: default funding — a payment that exceeds the available balance is met from the limit by the account under a term the customer accepted once at release; the explicit draw is retained as "draw ahead"; switch-off available; each funded event recorded | C1; C5 (amended) | the customer's "I have the money" state (C1); the customer's "the payment went through" state with nothing done (C5) |
| **WP-3** | Working | **the receipts share — a term of the account agreement under which a fixed fraction of each receipt is split: the first slice clears the accrued charge, the remainder repays the drawn balance** | C1; **v2 amended at C6: the charge-first split** | the customer's "it repays itself from what comes in" state — now "and pays for itself from what comes in"; the bank's collections operation, which no longer exists as an operation — confirmed at C6: a charge only taken from receipts has no arrears to collect |
| **WP-4** | Working | **the migration** — the customer's existing arranged overdraft is retired and any drawn overdraft balance becomes a draw on the standing limit with a receipts share; one event per overdraft account; the customer may decline and keep the overdraft | **C2** | the customer's "the money I already owe now sits on the limit, at less than I was paying" state; the retirement of the standard-tariff overdraft as a product on the account |
| WP-5 | Working | the shadow limit and the release order — the rule runs on every eligible account and records a limit; the limit is released as drawable first where it is at or below the exposure the bank already carries (the migrated overdraft accounts), then by replica against a kill band; at scale the release order ends and every eligible account's limit is live | C3 | the customer's "my limit appeared" state for the unreleased population; the bank's "the rule is proven before it is trusted" state (holder: model risk and the board risk committee — the release track) |
| **CP-1** | Communications | the limit statement — the standing limit and the receipts share, visible in the account before any need arises | C1 (v2 amended at C2: the statement also shows, once a year, what the customer paid on the overdraft in the year before migration and what the limit cost in the year since; v3 at C3: during the scaling path the statement appears at the account's release, not at its eligibility; v4 at C4: for the migrated customer the saving statement and the limit history (CP-2) are one statement — the saving shows what the tariff cost, the history shows what the limit would have covered) | the "aware" state (C1); the "I can see the saving" state (C2); the "my limit appeared" state (C3, path only); the migrated customer's "convinced" state (C4) **v5 at C6: the statement shows the year's charge as one figure beside the tariff line, and the representative example** |
| **PC-1** | Payment | **the charge — 14.0% simple a year on the daily drawn balance (band ⚠ 13.5–14.25%), no fee of any kind, accrued daily on its own ledger and collected only from receipts as the first slice of the receipts share; one rate for every account with a limit, set by the pricing committee and reviewed yearly; the representative example (⚠ 14.0–14.9% APR) shown wherever the rate is shown** | **C2 (condition); resolved at C6 (the price)** | the customer's "this costs me less than the overdraft did, and it is never taken on a date" state; the pricing committee's "one number, inside the condition" state; the conduct function's "signed example" state |
| CP-2 | Communications | the limit history and its placement — at release the account shows the standing limit beside the twelve months of the customer's own shortfalls it would have covered (date, amount, balance that day, limit that day), read from the stored daily limit and the back-test (WP-5); the history is placed in front of the customer on the shortfall day; an account with no shortfall in twelve months is shown the limit without a history and without a placement | C4 | the customer's "I have checked this against my own year and it would have covered March" state — a verified belief, formed by reading, before any draw; the conduct reviewer's "signed" state (the display is a financial promotion for a sole trader under £25,000, CONC 3) |
| — | Partner | the accountant, the accounting software or the platform through which the customer meets the limit | `[REQUIRES C7]` | not designed |
| — | Working | the limit for an account with no flow history anywhere (new to trading) | excluded at C2 — recorded in the TAM data object as an excluded sub-class; no later requirement is named as its owner | not designed |

## 2 · The customer's journey — the business (four phases)

Sparse states; a component sits on each transition; a transition with no component carries a flag.

### Phase 1 — Becoming

| From state | To state | Component | Change (cognitive / emotive / behavioural) | Requirement |
|---|---|---|---|---|
| holds an account and pays a standard-tariff overdraft for recurrent draws (the selected customer); or borrows nowhere, or is refused, or puts in personal money | aware that the account carries a standing limit | CP-1 | cognitive | C1 |
| eligible (enough flow) but not yet released — the unreleased population during the scaling path | the account's replica is released; the limit statement appears | WP-5, then CP-1 | cognitive | C3 — path only; at scale the state does not exist |
| aware; a scheduled payment will exceed the balance within the Bacs cycle (the shortfall) | sees the limit beside the twelve months of their own shortfalls it would have covered, on the account, that day | CP-2 | cognitive | C4 |
| sees the history | convinced the limit is real — checked against events they lived through; the receipts share read as bearable against the receipts shown | CP-2 | emotive | C4 |
| aware at migration (the selected customer) | convinced — the saving statement and the limit history are one statement | CP-1 (amended), CP-2 | emotive | C2 (the saving); C4 (the history) |
| released with no shortfall in the prior twelve months | sees the limit without a history; not convinced by this mechanism | CP-2 (empty case) | cognitive | C4 — a bounded structural limit; the share is gate (12) in the C4 record |
| convinced | draws for the first time (a customer with no overdraft); **or accepts migration of the existing overdraft (the selected customer)** | WP-2; **WP-4** | behavioural | C1; **C2** |
| convinced | accepts the limit term once, at release — default funding, the receipts share and switch-off stated in one term (a customer with no overdraft); for the migrated customer the acceptance is the modifying agreement at migration | WP-2 (v2) | behavioural — once | C5 — the acceptance replaces "draws for the first time" as the activation event; the first draw is no longer a customer act |

### Phase 2 — Consuming (core delivery — the phase R1 changed; R2 adds the value-realisation rows)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| a scheduled or instant payment exceeds the available balance | the payment is met from the limit; the balance shows the funded amount; the customer has done nothing | WP-2 (v2) — default funding, within the standing limit, under the accepted term | behavioural (nothing to do) | C1 (the draw); C5 (the draw becomes the account's act) |
| knows a payment is coming and wants the money on the balance first | draws ahead — moves money from the limit to the balance explicitly | WP-2 (v2) — draw ahead, the C1 draw retained as an option | behavioural | C5 — the option is kept because the C4 hypothesis on conviction is measured on it; not the default path |
| has default funding on and does not want it | switches it off for the account; a payment that exceeds the balance is then returned as today | WP-2 (v2) — switch-off | behavioural — once | C5 — the share that switches off is the R5 falsification measure (⚠ ≤10% hypothesis; falsified above 25%) |
| a funded event the customer did not want | repays it within three days; the account records a reversal | WP-2 (v2), WP-3 | behavioural | C5 — the reversal share is the second falsification measure (⚠ ≤5%; falsified above 15%); read with the switch-off share |
| a payment is funded | sees a notice in the account: the amount funded, the limit remaining, the receipts share that will repay it | CP-1 (v5 amended: the limit statement carries each funded event as a line) | cognitive | C5 — the notice is a record, not a prompt; nothing is sent |
| drawn | drawn balance falls as receipts arrive | WP-3 — the receipts share | behavioural (nothing to do) | C1 |
| flow grows or shrinks | standing limit rises or falls | WP-1 — recomputed daily from the flow | cognitive | C1 |
| flow stops | limit falls to zero; drawn balance stays; the exception cell contacts the customer | WP-1 and the exception activity (AOM 3b) | behavioural | C1 |
| **pays the standard tariff on an arranged overdraft, renewed each year** | **the overdraft is retired; the drawn balance sits on the limit under a receipts share; no renewal, no fee event** | **WP-4** | **behavioural** | **C2** |
| **carries the drawn balance on the limit** | **sees, once a year, what the overdraft cost and what the limit cost — the saving is visible** | **CP-1 (amended)** | **cognitive** | **C2** |
| the migrated customer whose rule limit exceeds the existing overdraft limit (Stage 1) | receives the existing limit at migration; the rule's higher figure is released with the replicas | WP-5 | cognitive (nothing is taken away at migration) | C3 — path only |
| carries the drawn balance on the limit | the all-in price stays below what the overdraft cost | PC-1 — **resolved at C6: 140 per £1,000 drawn a year against a tariff of 150–300 plus fees** | emotive (relief from the tariff) | C2 — condition; **C6 — price** |

### Phase 3 — Paying (**C6 — the charge; the block removed is the calendar debit**)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| **drawn** | **the charge accrues daily on the drawn balance at 14.0% a year — £0.384 per £1,000 per day; nothing is due** | **PC-1 (resolved C6)** | **cognitive (one rate, one figure per day)** | **C6** |
| **a receipt arrives** | **the first slice of the receipts share clears the accrued charge; the remainder repays the draw; one line per receipt** | **WP-3 (v2); PC-1** | **behavioural (nothing to do)** | **C6 — the payment trigger is the receipt; there is no charging date, no fee, no debit** |
| **no receipt for a period** | **the accrued charge waits on its own ledger; it does not compound and is not debited** | **PC-1 (resolved C6)** | **cognitive** | **C6 — a no-receipt account past ⚠ 90 days is in the cell under C3's kill band, for the flow, not for the charge** |
| **at acceptance (C5) and once a year** | **reads the representative example and the year's charge as one figure beside the tariff line** | **CP-1 (v5); PC-1** | **cognitive** | **C6 — the migrated customer's Critical Value Threshold is at acceptance; the never-borrowed customer's is at the first funded-event notice (£0.38 per £1,000 per day)** |
| **a charge query** | **asks the cell why a receipt was split as it was; the handler reads the ledger; no discretion on the rate** | **PC-1 (resolved C6)** | **behavioural** | **C6 — ⚠ 0.2–0.5% of drawn accounts a year (threshold 1.5%)** |

### Phase 4 — Repeating

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| cleared | draws again when needed; the limit was never withdrawn | WP-1 | behavioural | C1 |
| the business grows | the limit grows with the flow; no new application at any size below the form's ceiling | WP-1 | cognitive | C1 |
| **a year on the limit** | **does not return to an overdraft — there is none to return to on this account** | **WP-4 (the overdraft was retired)** | **behavioural** | **C2; the switching cost this creates is R8's by number** |

## 3 · User and partner tracks (property holders who are not the customer — VA-71)

### Account line track (the bank's own account, Case A) — internal holder, C1

| State | Component | Holder | Note |
|---|---|---|---|
| the flow is observed and held as a record | the account ledger | the bank (the Kept design on Case A; a dependency, not designed here) | the limit engine reads the ledger |
| the receipts share is a term of the account agreement | WP-3 | the bank's account terms; regulated under the Consumer Credit Act 1974 for a sole trader or a partnership of two or three persons borrowing under £25,000 (s.16B) | a compliance line, not a decision |
| **the existing overdraft agreement is varied or replaced at migration** | **WP-4** | **the bank's product and conduct function** | **C2 — for a CCA-regulated customer, a modifying agreement or a new regulated agreement is needed (CCA 1974 s.82); for a limited company, a variation of terms with notice. Carried as a standing constraint** |
| the shadow limit is recorded against every eligible account and carries a release flag | WP-5 | the bank's account line (Case A) | C3 — a ledger field, not a decision; falls away at scale |
| each day's live limit is stored as a record; the twelve-month shortfall history is rendered beside the balance; the scheduled-payment file is matched against the balance and the history is placed on the shortfall day | CP-2 | the bank's account line (Case A) | C4 — a read of WP-5 and a match the account line already performs for returned items; the history is what the rule set on each day, not a re-projection; when the rule is re-versioned the display says so |
| each payment is authorised against the available balance (credit balance plus undrawn limit); a payment that exceeds the credit balance is funded from the limit; the funded event is recorded; a notice is written to the account | WP-2 (v2) | the bank's account line (Case A) | C5 — the same authorisation rule the account already applies to an arranged overdraft; no new decision point; instant channels (Faster Payments, card) and scheduled channels (Bacs, standing orders) all authorise against the one available balance |
| the accepted term is held on the account: default funding on or off, the receipts share, the limit | WP-2 (v2) | the bank's product and conduct function | C5 — one term, accepted once at release; for a regulated customer a modifying agreement (CCA 1974 s.82); the term is drafted once (AOM 3c, C5 one-off) |
| **the day's charge is accrued on the accrued-charge ledger at close of day; each receipt is split charge-first, then principal** | **PC-1 (resolved C6); WP-3 (v2)** | **the bank's account line (Case A)** | **C6 — one ledger line per drawn account per day (⚠ 83m a year) inside the daily batch; one more split rule on the receipt event WP-3 already acts on (⚠ 68m receipts); the accrued charge is not exposure; interest cash arrives with each receipt (⚠ 1–3 days) instead of monthly (⚠ 30 days)** |

### Limit engine track (the bank's own operators) — internal holder, C1

| State | Component | Holder | Note |
|---|---|---|---|
| the limit is computed by a rule from the flow; no person decides an account | WP-1 | the limit engine team and the model-risk reviewer (AOM 3c) | the rule is a model under SS1/23 |
| an account whose flow stops is handled by a person | exception activity (AOM 3b) | the exception cell | the only human contact in the form |
| **a customer declines migration, or queries the saving statement** | **exception activity (AOM 3b, C2 rows)** | **the exception cell** | **C2 — the customer keeps the overdraft; the account carries both until the overdraft's next renewal** |
| the rule is back-tested on the bank's own history before any release | WP-5 | the limit engine team | C3 — Stage 0; the record stays as validation evidence; the gate falls away; C4 — the back-test is also the source of each released account's first twelve-month history |
| a customer asks why the limit on a given day was what it was | exception activity (AOM 3b, C4 row: e.limit_query) | the exception cell | C4 — the handler reads the same history and the rule's inputs for that day; no discretion to change the limit |
| a customer asks why a payment was funded, or asks to switch default funding off or on | exception activity (AOM 3b, C5 row: e.funding_query) | the exception cell | C5 — the handler reads the funded-event record and the accepted term; switch-off is a customer instruction, not a discretion; rate ⚠ 0.05–0.2% of funded events (threshold 0.5%) |

### Release track (model risk, the board risk committee and finance) — internal holders, new at C3

| State | Component | Holder | Note |
|---|---|---|---|
| the rule is validated on the back-test and on the Stage 1 conduct | WP-5 | model risk and credit oversight (SS1/23 Principle 4) | C3 — the holder of "proven" is model risk, not the customer; the instrument is the validation report it reads today |
| the release of each stage is signed against its band | WP-5 | the board risk committee (SS1/23 Principle 2) | C3 — trial band at 12 months; replica band at 6 months; the yes-threshold sits inside a pre-registered acquisition budget of £0 |
| the overlay is booked at release and released at the reading | WP-5 | finance and the external auditor | C3 — ⚠ 0–25% on Stage 1; the replica band on each replica; none at scale |
| the release order ends when the last replica is read | WP-5 | model risk | C3 — the track closes; monitoring in use continues as for every Tier 1 model |
| the customer-facing use of the back-test and the stored daily limit is inside the model's validation scope | CP-2 | model risk (SS1/23 Principle 1) | C4 — a displayed limit is a model output used in a customer communication; reviewed once at Stage 0 and at each rule version |
| the loss rate on the default-funded pool is read against the loss rate on the drawn-ahead pool at each stage | WP-2 (v2) (release track) | model risk and finance | C5 — default funding raises the drawn book; if the loss gap between the two pools exceeds ⚠ 1 point, default funding falls to opt-in for the flow band where the gap sits (the C5 loss-gate fallback); the reading is inside the Stage 1 and Stage 2 bands (VA-163) |
| **the no-receipt accrued-charge line (accounts with an accrued charge outstanding more than ⚠ 30 days) is read at each stage as a free count** | **PC-1 (resolved C6) (release track)** | **model risk** | **C6 — a count of acts, not of losses (VA-97); ⚠ ≤ 2% of drawn accounts expected, every one a no-flow account already in the cell; ⚠ 10–20 hours inside the existing reading** |

### Pricing track (the bank's own pricing function) — internal holder, new at C2

| State | Component | Holder | Note |
|---|---|---|---|
| the price condition is set as a constraint on the Payment product | PC-1 | the bank's pricing committee | C2 — the holder of "the price remains below the tariff" is the pricing committee, not the customer; the committee carries the condition |
| **the rate is set at 14.0% simple a year (band ⚠ 13.5–14.25%) inside the condition — below the lowest published standard-tariff EAR (14.54%, HSBC) and above the operating bar (132.84 per £1,000); reviewed once a year against the funding line and the loss reading** | **PC-1 (resolved C6)** | **the bank's pricing committee** | **C6 — one number, no fee; threshold: below 13.28% the 25% margin fails, above 14.5% the "lower for every migrated customer" claim fails; convergence: Stage 1 acceptance with "the rate" as a decline reason (> ⚠ 30% moves the rate toward the band's low end); the fixed-against-Bank-Rate question is the committee's at the first review; the tariff and fee income given up on the migrated book against the funded book's contribution is the committee's unmeasured input (C6 VA-127)** |

### Regulator track — C1, unchanged

| State | Component | Holder | Note |
|---|---|---|---|
| the bank holds Part 4A permission to lend and accept deposits | — | PRA and FCA | no new permission; capital under the standardised approach |
| the limit-history display is signed as a financial promotion template (sole traders and small partnerships under £25,000) and reviewed yearly | CP-2 | the bank's conduct reviewer (CONC 3.3.1R) | C4 — clear, fair, not misleading; no rate or cost shown at C4, so no representative example (CONC 3.5.5R); if the amount of the limit alone is held to trigger the representative example, it is added at C6 by number with the price |
| default funding under an accepted term is treated as drawing on an arranged facility, not as an unarranged overdraft | WP-2 (v2) | the bank's conduct function | C5 — desk position: a running-account credit agreement within the limit (CCA 1974 s.74(1)(b) and s.74(3) for the overdraft form); CONC 4.7 pre-contract explanation given once at acceptance; PS19/16 unarranged-overdraft rules do not apply within an agreed limit; PRIN 2A.4 met because the customer can switch off; what a ruling would settle: whether the CONC 5.2A creditworthiness assessment is timed at acceptance or at each funded event — design position: at acceptance, on the rule's limit |
| **the representative example (rate, APR, a worked figure on £1,000 for 30 days = £11.51) is signed wherever the rate is shown; the APR basis is chosen** | **PC-1 (resolved C6); CP-1 (v5)** | **the bank's conduct function (CONC 3.5.3R, 3.5.5R; CONC App 1.2)** | **C6 — desk position: the charge is interest at a stated rate, so the APR carries nothing but the rate — ⚠ 14.0% where collection follows accrual, up to 14.93% on a monthly-compounding calculation; the collection-from-receipts term is the payment mechanism for interest, not a charge for the total-charge-for-credit calculation; CONC 4.7 pre-contract information names the rate and the collection method (C5's acceptance); PRIN 2A.4 met on the short draw (interest for the days drawn only) and on the never-drawn account (nothing charged); what a ruling would settle: the APR basis and whether the term is a "charge" — the conduct function chooses the stricter** |

### Partner track — flagged

| State | Component | Holder | Note |
|---|---|---|---|
| who brings the customer to the limit | — | `[REQUIRES C7]` | not designed |

## 4 · State changes traced to requirements (the traceability check)

| State change | Component | Requirement | Status |
|---|---|---|---|
| refused or self-funding → aware of a standing limit | CP-1 | C1 | carried |
| aware, at the shortfall → sees the limit with its twelve-month history | CP-2 | C4 | carried |
| sees the history → convinced (verified against own events) | CP-2 | C4 | carried |
| aware at migration → convinced (saving and history, one statement) | CP-1, CP-2 | C2; C4 | carried |
| released, no shortfall in twelve months → not convinced by this mechanism | CP-2 (empty case) | C4 | carried as a bounded structural limit |
| asks why the limit was what it was → answered from the history | AOM 3b (C4 row) | C4 | carried |
| the display → signed as a promotion; inside model-risk scope | CP-2 (regulator and release tracks) | C4 | carried |
| convinced → accepts the limit term once | WP-2 (v2) | C5 | carried |
| a payment exceeds the balance → met from the limit, nothing done | WP-2 (v2) | C5 | carried |
| wants the money first → draws ahead | WP-2 (v2) | C5 | carried as an option |
| does not want default funding → switches off; unwanted funding → reversal | WP-2 (v2), WP-3 | C5 | carried; both shares are falsification measures |
| funded → sees the notice | CP-1 (amended) | C5 | carried |
| asks why a payment was funded → answered from the record | AOM 3b (C5 row) | C5 | carried |
| default-funded pool → loss read against the drawn-ahead pool | WP-2 (v2) (release track) | C5 | carried; the loss gap is an unmeasured input |
| default funding → treated as arranged, not unarranged | WP-2 (v2) (regulator track) | C5 | carried as a desk position |
| needs money → has money, no application | WP-2 | C1 | carried; at C5 the act moves from the customer to the account |
| drawn → repaid from receipts, no collections operation | WP-3 | C1 | carried |
| flow changes → limit changes | WP-1 | C1 | carried |
| flow stops → exception contact | AOM 3b | C1 | carried |
| **pays the tariff on an overdraft → the overdraft is retired and the balance sits on the limit** | **WP-4** | **C2** | **carried** |
| **on the limit → sees the saving once a year** | **CP-1 (amended)** | **C2** | **carried** |
| **on the limit → the price stays below the tariff** | **PC-1 (condition)** | **C2 (condition); C6 (price)** | **carried as a condition; the price is flagged** |
| **declines migration → keeps the overdraft** | **AOM 3b (C2 row)** | **C2** | **carried** |
| eligible, unreleased → released; the limit appears | WP-5, CP-1 | C3 | carried (path only) |
| migrated with a higher rule limit → keeps the existing limit until the replicas | WP-5 | C3 | carried (path only) |
| the rule unproven → validated on history and existing exposure | WP-5 (release track) | C3 | carried |
| each stage → released against its band; overlay booked and released | WP-5 (release track) | C3 | carried |
| **drawn → the charge accrues daily; nothing is due** | **PC-1 (resolved)** | **C6** | **carried** |
| **a receipt → the accrued charge is cleared first, the draw repaid second** | **WP-3 (v2)** | **C6** | **carried** |
| **the price condition → a price inside it** | **PC-1 (resolved)** | **C6** | **carried** |
| **the saving statement → shows the year's charge as one figure and the representative example** | **CP-1 (v5)** | **C6** | **carried** |
| **the rate unsigned → the representative example and the APR basis signed** | **PC-1 (regulator track)** | **C6** | **carried** |
| **the calendar debit → does not exist in the form** | **PC-1 (resolved); WP-3 (v2)** | **C6** | **carried (the block removed)** |
| no flow history → a limit | — | excluded (TAM data object) | recorded, not carried |

Every C1, C2, C3, C4, C5 and C6 transition carries a component or a flag. No transition is carried by a component that a later requirement has not yet designed: PC-1 is now the Payment product itself; the Partner track stays C7's.

**Component set at C6 (for the margin-of-safety check, VA-74):** WP-1, WP-2 (amended at C5), **WP-3 (amended at C6)**, WP-4, WP-5, CP-1 (amended at C2, C4, C5 and **C6**), CP-2, **PC-1 (resolved at C6)**. The path-only rows (WP-5's release states) exist during Stages 0–2 and not at scale; the at-scale journey is the v2 journey with the C5 funding rule and the C6 charge.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. |
| v2 | 21 September 2026 | R2 update. Added WP-4 (migration), PC-1 (price condition) and the amended CP-1; three Phase 2 rows, one Phase 1 row, one Phase 4 row; the pricing track; the migration row on the account line track; the decline row on the limit engine track. The new-to-trading row is now an excluded sub-class in the TAM data object, not a `[REQUIRES C2]` flag. |
| v3 | 21 September 2026 | R3 update. Added WP-5 (the shadow limit and the release order); one Phase 1 row and one Phase 2 row, both path-only; the shadow ledger row on the account line track; the back-test row on the limit engine track; the release track (model risk, the board risk committee, finance) with four states; CP-1's release-time note. Phase 3 (Paying) unchanged for the customer — the price stays C6's. |
| v4 | 21 September 2026 | R4 update. Added CP-2 (the limit history and its placement) in place of the `[REQUIRES C4+]` flag; four Phase 1 rows (the shortfall, the verified belief, the migrated customer's one statement, the empty-history case); CP-1 amended to carry the history for the migrated customer; the display and placement row on the account line track; the limit-query row on the limit engine track; the validation-scope row on the release track; the conduct row on the regulator track. Phases 2–4 unchanged. Phase 3 (Paying) stays C6's. |
| v5 | 21 September 2026 | R5 update. WP-2 amended (v2): default funding on an accepted term, draw ahead retained, switch-off, funded-event record; the Phase 1 acceptance row; five Phase 2 rows (funded payment, draw ahead, switch-off, reversal, notice); CP-1 amended to carry funded events; two account line rows (authorisation against the available balance; the accepted term held); the funding-query row on the limit engine track; the default-funded loss reading on the release track; the arranged-not-unarranged desk position on the regulator track; eight traceability rows. C4 rows carried with their bold removed. Phase 3 (Paying) stays C6's; the Partner track stays C7's. |
| v6 | 21 September 2026 | R6 update. PC-1 resolved from a condition to the charge (14.0% simple a year on the daily drawn balance, no fee, accrued daily, collected from receipts as the first slice of the receipts share); WP-3 amended (v2, the charge-first split); CP-1 amended (v5, the year's charge and the representative example); the `[REQUIRES C6]` price row removed from the register; five Phase 3 rows; the accrual-and-split row on the account line track; the rate row on the pricing track; the no-receipt line on the release track; the representative-example row on the regulator track; six traceability rows. C5 rows carried with their bold removed. The Partner track stays C7's. |