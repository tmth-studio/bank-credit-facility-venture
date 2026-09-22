# A business bank's credit facility line — challenge five (R5) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R5 carries. The block is a routine disruption the C1 form itself introduced: the draw was written as an act by the customer, at a moment when the customer's present routine has no act in it. A payment goes out; the arranged overdraft absorbs it; nothing is done. The one move removes the act: a payment that exceeds the balance is met from the limit by the account, as an accepted term, unless the customer has switched that term off. The customer accepts the term once, after reading the history (C4); after that there is nothing to learn and nothing to remember. The verdict cannot exceed R1–R4's PROVISIONAL (VA-95). The move adds ⚠ £0.02–0.06 per £1,000 drawn a year; cumulative conventional additions used ⚠ 0.05–0.26 of ⚠ £8 (RD-030). Floor ⚠ £54.04–106.26. Margin at the worst corner 27.0% at the surplus band's low end, 34.1% at the convention. Binding gate unchanged: the loss rate on the flow-underwritten pool, 25% margin fails above ⚠ 4.2–5.4% across the surplus band; a new unmeasured input on the same gate — whether a draw the account makes by default carries a higher loss rate than a draw the customer makes by hand. The conventional R5 line — onboarding calls, help content and a support line for the first draws, ⚠ 1–2 per £1,000 — is named and removed.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c4-v1-2026-09-21.md` (R4, PROVISIONAL, object-after to 23 September 2026 17:00), and the C3, C2 and C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3. **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F2 rule this record works under (Tom, 16 September 2026).** R4 to R7 remove the blocks the conventional form pays for. The conventional R5 line is what a bank spends to get a customer through the first draws — onboarding calls, help content, a support line: ⚠ £15–40 per drawn account in the first year, ⚠ 1–2 per £1,000 (counterfactual, RD-030). This record names it, removes it, and books only what the one move costs.

**Sections in this record.** Defined terms. SR1 to SR5. Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C4. Financial check. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

As in the C1–C4 records: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *exception cell*, *standard tariff*, *migration*, *price condition*, *shadow limit*, *back-test*, *release*, *stage*, *shortfall*, *limit history*, *placement*, *conventional additions used*. New at C5:

- **Use block** — the structural reason a customer who has decided to use the limit does not build it into their routine. Not a doubt about the value (C4 removed that) but a failure to act, or an act that fails.
- **Default funding** — the term of the account under which a payment that exceeds the available balance is met from the standing limit, up to the limit, by the account itself. The customer does nothing. The term can be switched off by the customer at any time; with it off, a payment that exceeds the balance is returned, as it is today on an account with no overdraft.
- **Acceptance** — the one act the customer performs: agreeing the limit term once, in the account, after the history is shown. For the migrated overdraft customer the acceptance is the migration agreement (C2); nothing further is asked.
- **Draw ahead** — the explicit form of the draw retained as an option: the customer moves money from the limit to the balance before any payment. This is the C1 draw (WP-2) in its original form; at C5 it is the exception, not the routine.
- **Funded event** — one payment met from the limit by default funding. The unit the account line counts, tells the customer about, and the exception cell is asked about.
- **Available balance** — the balance plus the undrawn limit, shown as one figure. The reading a business owner makes today on an account with an arranged overdraft.

---

## SR1 — Required product use routine

The routine is written for the mainstream customer — the business owner with median tolerance for disruption, who runs the account on their phone in the evening and does not read terms. It is the routine as the C1–C4 form stands (the baseline), before this record changes anything. Steps 1–2 are conviction (C4) and are stated for the join only.

| Step | The customer must | What must be true for the step to work | Change |
|---|---|---|---|
| 1 | see the limit and its history beside the balance, on the shortfall day (C4) | the account is released; the history is non-empty (gate 12) | cognitive |
| 2 | decide the limit is real (C4) | the history matches events they lived through | emotive |
| 3 | **notice that a payment due will exceed the balance, in time to act** | the customer looks at the account before the payment day; the payment is one the bank can see in advance (Bacs, three days) — an instant payment (Faster Payments, a card authorisation) gives no notice | behavioural |
| 4 | **decide how much to draw** | the customer estimates the shortfall and the receipts to come | cognitive |
| 5 | **move money from the limit to the balance (the draw, WP-2)** | the customer performs the act before the payment leaves | behavioural |
| 6 | let the payment go out | the balance now covers it | — |
| 7 | let receipts arrive; the share repays (WP-3) | nothing to do; the customer sees the drawn balance fall | behavioural (nothing to do) |
| 8 | repeat at the next shortfall (Phase 4) | steps 3–5 again | behavioural |

The Key Cost reduction (the tariff outflow, R2) is delivered at step 6: the payment is made from money that costs less than the overdraft did. Steps 3, 4 and 5 are the ones the routine adds that the customer's present routine does not contain.

**The present routine, for contrast (C2 record, SR2).** The arranged-overdraft customer does nothing at a shortfall: the payment goes out and the overdraft absorbs it. The owner-funded customer transfers personal money in, on their own timing, when they notice. The deterred customer lets the payment fail or delays it. None of the three performs steps 3–5 as written.

---

## SR2 — Key learning block

**Step where the block manifests: step 5, the draw — and step 3 before it.** The customer must perform an act (move money from the limit) at a moment when their routine contains no act, and must have noticed the need (step 3) in time. For the arranged-overdraft customer — the selected customer of R2, and the whole of Stage 1 — this is a step backwards: the product they are migrated from needs no act, and the form they are migrated to needs one.

**Structural cause: routine disruption.** Not learning burden — the draw is one screen and one number; nobody fails to learn it. Not dependency gap — nothing outside the customer's control prevents the draw once the account is released. The cause is that the act must be inserted into an embedded routine that runs without it, and, for payments that clear at once, there is no moment into which to insert it.

**Specific manifestation.** The payment leaves before the draw is made. Three ways, in order of incidence:

1. The payment is instant (a Faster Payment the customer sends, a card authorisation, a direct debit called on the day) and the customer has no notice — the account has a limit that would have covered it and the payment is returned or declined anyway. UK Finance reports Faster Payments and card payments as the majority of business payments by count; Bacs, the one channel with three days' notice, is the minority (T2).
2. The payment is a Bacs payment the bank can see, but the customer does not look at the account in the three days (the mainstream owner reads the account when something goes wrong, not before — the SME Finance Monitor's "low attention" reading at C2 step 2).
3. The customer looks, sees the shortfall, and intends to draw, and does not — the act is displaced by the day (the intention–action gap: Sheeran 2002, T2).

In each case the result is the same event: a returned or declined payment on an account whose limit would have covered it, an unpaid-item fee (⚠ £10–35), and a customer who concludes that the limit did not work. That conclusion undoes the verified belief C4 built. The block is therefore not only an activation loss; it is a reversal of R4.

**What the customer does when activation fails (the three responses).** Stops trying: the owner-funded customer returns to personal money, which never needed an act at a fixed moment. Tries intermittently: draws ahead when they remember, and is caught when they do not. Seeks a workaround: keeps a personal buffer in the account — which is the owner-funded routine under another name. All three leave the limit unused at the moment it exists for.

**Which cluster faces it most acutely.** The migrated overdraft customer (Stage 1, the whole of the first release). Their routine has zero acts in it today, and the C2 acceptance reading (decline > ⚠ 30% is the trigger) is the first place a routine disruption would show — as declines at migration, not as failed draws after it.

---

## SR3 — Adoption theory of change

**Nature of the challenge: disruptive.** The learning required is not of a skill but of a new habit — inserting an act at a cue (the shortfall) that today produces no act. Habit change of this kind is the hardest class for a mainstream customer, because the existing response is automatic and the new one must be remembered each time.

```
ADOPTION THEORY OF CHANGE — R5
  class of problem:  a disruptive routine change — the customer must add an act at a cue where their present routine has none
  theory:            default effects — Madrian and Shea (2001), "The Power of Suggestion: Inertia in 401(k) Participation and Savings Behavior", Quarterly Journal of Economics 116(4): when the desired behaviour is the default, participation rises from 49% to 86% with no change in the offer; the customer who would otherwise have to act does not have to. Supporting mechanism: habits are cued responses, and a routine is changed by changing what the cue produces, not by asking the person to override it — Wood and Neal (2007), "A New Look at Habits and the Habit–Goal Interface", Psychological Review 114(4)
  context:           the customer holds an account whose limit is real to them (C4) and whose present routine at a shortfall contains no act; the payment channels are mostly instant; the bank sees every payment order at the moment of authorisation, as it does for an arranged overdraft today
  outcome:           the customer has never made a draw and every shortfall in the year was met; the drawn balance rises and falls with the flow; the customer reads one available figure and runs the business against it — the state the arranged-overdraft customer is in today, on a limit that costs less and was never applied for
```

**Stress test.** The contrast theory is active choice: where preferences differ and a wrong default is costly, requiring a decision beats a default (Carroll, Choi, Laibson, Madrian and Metrick 2009, "Optimal Defaults and Active Decisions", *Quarterly Journal of Economics* 124(4)). Applied here: for whom is a default draw wrong? The customer who would rather have a payment returned than borrow. The cost of the wrong default is interest for the days drawn, ⚠ £1–5 on a ⚠ £1,000 draw held ⚠ 10–20 days, and it is reversed by repaying. The active decision is retained where it is cheap and matters — once, at acceptance — and removed where it is repeated and costly to miss. **Fragile-findings list:** default effects are among the most replicated results in the field (Jachimowicz, Duncan, Weber and Johnson 2019, meta-analysis of 58 studies, *Behavioural Public Policy* 3(2): mean effect d = 0.68, robust across domains). Not on the list. Sheeran 2002 (the intention–behaviour gap) is a meta-analysis, not a single-study finding. Not on the list.

---

## SR4 — Adoption strategy

**Step 4a — baseline.** The C1–C4 form gives the customer a real limit (C1), proven (C3) and believed (C4), and asks the customer to draw on it by an act (WP-2). On the use block it does this: nothing. It leaves the act in the routine at a cue that has no act today, and it leaves the instant-payment case with no moment for the act at all. The baseline creates the block it now has to remove.

**Step 4b — candidate mutations.**

```
MUTATION GATE — R5
baseline: the customer moves money from the limit to the balance before a payment (WP-2 as written at C1); the form asks for an act at a cue where the present routine has none, and gives no moment for it on instant payments
mutation_A: default funding — a payment that exceeds the balance is met from the limit by the account, as an accepted term, switch-off available; the explicit draw is retained as an option | reason_considered: removes the act entirely; the customer's routine is unchanged from an arranged overdraft; works on instant payments because the account line authorises against balance plus limit at the moment of the order, as it does for an arranged overdraft today | verdict: adopted | reason_verdict: eliminates the cause (no act to insert); mainstream by construction (the customer does nothing); the C4 rejection of this mechanism was on scope (activation is R5's, not R4's) and on two conduct objections, both disposed at assumption (3) below; cost inside the account line's existing authorisation
mutation_B: pre-funded balance — the limit is pushed into the balance every day; the drawn balance is always the limit; the receipts share repays | reason_considered: no act, no shortfall ever | verdict: rejected | reason_verdict: the customer is drawn, and pays interest, whether or not they need the money — the tariff outflow (R2's KMC) is replaced by an interest outflow on money not used; fails the price-and-value outcome (PRIN 2A.4) and contradicts C1 ("pay on the drawn balance")
mutation_C: scheduled pre-draw — the account draws three days before a Bacs payment that will exceed the balance | reason_considered: uses the notice the bank has | verdict: rejected | reason_verdict: covers the minority channel only; instant payments still fail; reduces the block, does not eliminate it
mutation_D: a prompt at the shortfall — "draw now?" with one tap, plus help content and a support line | reason_considered: the smallest change | verdict: rejected | reason_verdict: the conventional R5 line (⚠ 1–2 per £1,000); the act remains; an incumbent can add it; the instant case is not reached
mutation_E: hold the payment until the customer confirms the draw | reason_considered: never a returned payment | verdict: rejected | reason_verdict: a card authorisation and a Faster Payment cannot be held; a Bacs payment held past its date is a late payment; the act remains and a delay is added
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: A — default funding on an accepted term
evolvedBFF: a bank whose credit facility is a standing property of every account with enough flow, proven before it is trusted, believed because the customer checks it against their own past, and used without an act — a payment that exceeds the balance is met from the limit by the account under a term the customer accepted once
synthesisCheck: the arranged overdraft as every UK bank operates it today (a payment order is authorised against balance plus facility and met without an act), for the use mechanism — the C1 form kept the overdraft's exposure model out and, by the same stroke, its one good property; R5 puts the property back on a limit the overdraft never had; the repayment side is Square Loans' (a share of each receipt)
```

**Step 4c — decision.** A adopted. The evolved BFF is stated in SR5.

**Adoption strategy.** *Make the draw the account's act, not the customer's.* The structural decision is to define the standing limit as a term of the account that the account line enforces at authorisation — a payment order is authorised against the balance plus the undrawn limit, and met from the limit where the balance is short — rather than as a pool the customer moves money out of. The customer accepts the term once; the account does the rest.

**Mechanism — elimination, not reduction.** The block was an act at a cue with no act. After the move there is no act: step 3 (notice), step 4 (decide how much) and step 5 (move the money) do not exist in the routine. The instant-payment case is met because authorisation happens at the moment of the order, for every channel, as it does for an arranged overdraft. If the customer used the product for the first time entirely alone, would the block still occur? No — the customer would not know the first funded event had happened until the account told them, after the fact.

**R1 consistency.** Nothing in the exposure model changes: the limit is computed daily from the flow (WP-1); the drawn balance is repaid by the receipts share (WP-3); exposure never exceeds the limit. What changes is who performs the draw. The C1 record's "drawn by the customer without an application" becomes "drawn by the account under a term the customer accepted".

**At-scale test.** The mechanism is the account line's existing authorisation rule with one more input (the undrawn limit). It runs per payment order, automated, at any volume the account line already runs. No founding-team step, no managed exception. At-scale volume: ⚠ 228,000 drawn accounts, ⚠ 760,000 accounts with a limit, ⚠ 1.4–4.1m funded events a year.

**R8 signal: yes.** A routine with no act in it is a switching cost: leaving means acquiring one — an application elsewhere, a timing to remember, a buffer to hold. The funded-event record joins the limit history (C4) as data the customer has here and nowhere else. Flagged for R8 by number.

**Hypothesis (falsifiable).** Among released accounts with the term on, the share of shortfalls met (not returned or declined) in the first ⚠ 90 days is ⚠ ≥ 95%; the share of customers who switch the term off before their first funded event is ⚠ ≤ 10%; the share of funded events reversed by the customer within ⚠ 3 days (repaid from own funds) is ⚠ ≤ 5%. **Falsified** if the switch-off share exceeds ⚠ 25% or the reversal share exceeds ⚠ 15% at ⚠ 10,000 accounts (the Stage 2 replicas as arms) — a wrong default for the mainstream — in which case R5 loops back to SR2 with the switch-off reasons as the brief. Read at the first replica's 90-day point; no cost beyond the count.

**Named assumptions (T4 with logic).**

1. *The account line can authorise against balance plus limit for every channel.* It does so today for arranged overdrafts on the same account (the available-balance figure UK banks display includes the arranged overdraft; T1 by product pages). The limit replaces the overdraft figure in the same rule.
2. *Payment channel mix.* Instant channels (Faster Payments, cards, same-day direct debits) are the majority of SME payments by count (UK Finance payment statistics, T2). If Bacs were the majority, mutation C would eliminate most of the block at lower cost; it is not.
3. *Conduct status of default funding — the desk position.* The C4 record rejected this mechanism on two objections: "an unrequested draw" and "CONC 3 / Consumer Duty". Both are disposed here. (a) It is not unrequested: the term is accepted by the customer once, in writing, in the account; the agreement is an overdraft on a current account within CCA 1974 s.74(1)(b), for which the FCA's determination under s.74(3) exempts the agreement from Part V form requirements provided the pre-contract information in CONC 4.7 (the limit, the rate, the conditions, the right to end) is given — it is, at acceptance; a customer with the term off has no credit and no draw. (b) It is not an unarranged overdraft: the funded payment sits inside an agreed limit, so the PS19/16 prohibition on unarranged charges above arranged does not bite, and there is no unarranged price to disclose. (c) Consumer Duty PRIN 2A.4 (price and value) is met by construction: the customer pays interest on the days drawn only, and can reverse a funded draw at no charge by repaying. **What a ruling would settle:** whether an account with the term on and no draw yet is "credit provided" for CONC 5.2A creditworthiness purposes at acceptance or at first funding — the design position is at acceptance, on the rule's limit (the model under SS1/23, C3), which is the stricter reading. Owner: the bank's conduct function; convergence: the signed term.
4. *Loss rate on default-funded draws.* A draw the account makes by default may be made on accounts that would not have drawn by hand — including some that let the payment fail because they knew the money was not coming. The loss rate on the flow-underwritten pool is already the binding gate; this assumption says the default may move it. Design position: the same gate reads it — the Stage 2 arms compare the loss rate on default-funded and hand-drawn events at the same ⚠ 10,000 accounts; threshold: if default-funded draws carry a loss rate more than ⚠ 1 point above hand draws, the term is switched to opt-in for the flow bands where the gap sits (a rule change, not a form change). Owner: model risk; convergence: the first replica's 12-month reading.

**Credibility mechanism (VA-81).** Receiver: the business owner, at acceptance. Proposition: "a payment that exceeds your balance will be met from your limit; you will be told each time; you can switch this off." Instrument in use today: the account's own available-balance figure and the arranged overdraft's identical behaviour, which the migrated customer has lived with for years; for the never-borrowed customer, the funded-event notice on the first occasion — their own returned-payment history (C4's placement) says what would have happened without it. Public-record supplier: the account statement (PSR 2017 regs. 53–56) shows each funded event as a line.

**Existence test (VA-92) and affordability screen (VA-164).** Is there a holder of the "funds by default" property outside the bank? No: the property is the account line's, an internal holder admitted. No partner is named. Maximum payable to any holder from the binding gate and the cap: none is payable; the cost is the account line's own, stated in the financial check. The conventional R5 line (⚠ 1–2) is shown as a comparison, not as displaced spend to be re-booked.

**Three tests.** *Primary cause:* the move removes the act, which is the cause — not the difficulty of the act. *Entry point:* the shortfall, the same moment as C4's placement — the history says what the limit would have covered; the funded event is the limit covering it. *Incumbent:* an incumbent operates default funding today on an arranged overdraft — this element is not new; what the incumbent cannot do is operate it on a limit computed daily from the flow without the C1 engine, the C3 release and the C4 history, and on a customer who never applied. The test is passed on the cumulative form, not on the R5 element alone (*runner's call*; recorded for WS1 as a question about how the incumbent test reads when the block was created by an earlier requirement's own form).

**Property-holder test (VA-71).** Properties in the strategy: *authorises and funds* — holder: the account line (Case A); *accepts* and *switches off* — holder: the customer; *is told* — holder: the account line (the notice); *reads the funded-event loss* — holder: model risk (the release track); *drafts the term* — holder: the bank's product and conduct function. Each has a row on a track in the CTM v5.

---

## SR5 — Business form factor (C1–C5)

**Central structure.** The central structure is the daily limit computed from the flow the bank already observes (WP-1). Remove it and C1 has no exposure model, C2 nothing to migrate to, C3 nothing to shadow or release, C4 no history to show, and C5 nothing for the account to fund from. Every other component is a way of proving, believing, or using that one number.

*Cumulative BFF (C1–C5).* A bank whose credit facility is a standing property of every account with enough flow — a limit computed daily from the receipts and payments the bank already observes, repaid by a fixed share of each receipt as it arrives, and used without an act: a payment that exceeds the balance is met from the limit by the account itself, under a term the customer accepted once and can switch off. The customer's existing overdraft is retired into it at a one-time migration at a price held below the tariff. The rule is proven before it is trusted — run first as a shadow limit on the whole base, back-tested on the bank's own history, released first where it is at or below the exposure the bank already carries, then by stages against a pre-registered kill band. The limit is believed because it is shown as its own history, placed in front of the customer on the day a payment exceeds the balance; and it is used because, from that day, the account meets the payment and tells the customer it did. The bank keeps no per-application decision, no security process, no annual review, no collections operation, no marketing line and no onboarding line — only a rule under review, a release order, a history the customer can check, a term the account enforces at authorisation, and exception cells for accounts whose flow stops, whose holder declines, or whose holder asks why a limit or a funded payment was what it was.

**Read cold.** One product: a limit that exists, is proven, is believed, and works without being operated. The labels are citations.

**Fault-line check.** C1 wrote the draw as the customer's act; C5 makes it the account's, with the customer's act retained as an option (draw ahead). C4 measured conviction by the draw share; with the draw automatic, that measure no longer reads conviction — VA-103 restates it. C3's release: an account with the term on and its limit unreleased has nothing to fund from; the term takes effect at release, and the acceptance is asked at release, not before (consistent with C4's "the unreleased account sees nothing"). C2's migration: the migrated customer already holds an agreement with this behaviour; the modifying agreement (s.82) carries the term without a second acceptance. No fault line remains.

BFF confirmed. Sections 5–8 (the model updates and the FIT gate) run next; their outputs are the CTM v5, the AOM v5, the fit model at C5 and the verifier r5.

---

## Considered / not chosen (VA-4)

**Baseline on this dimension.** The C1–C4 form asks for an act at a cue where the mainstream routine has none, and gives no moment for it on instant payments (SR4, step 4a).

**Candidate mutations and options.**

- A. Default funding on an accepted term, switch-off available, explicit draw retained → no act; instant channels covered; the arranged overdraft's own behaviour → **adopted**.
- B. Pre-funded balance → no shortfall ever → rejected: interest on money not used; fails price and value; contradicts C1.
- C. Scheduled pre-draw on Bacs notice → uses the notice → rejected: minority channel; reduces, does not eliminate.
- D. Prompt, help content and a support line → smallest change → rejected: the conventional R5 line; the act remains; an incumbent's move.
- E. Hold the payment for confirmation → no returned payment → rejected: cannot hold a card or a Faster Payment; a held Bacs payment is a late payment.
- F. Opt-in default (the term off unless switched on) → the cautious reading of "unrequested" → rejected: the Madrian and Shea result is that the opt-in form leaves the mainstream customer where they started (49%, not 86%); the conduct objection is disposed at assumption (3) without it. Retained as the fallback the loss-gate threshold in assumption (4) switches to, by flow band.

**Decision.** A adopted; the evolved BFF is restated in SR5.

---

## Synthesis check (VA-1)

**Real-business analogue.** The venture now looks like an arranged business overdraft as every UK clearing bank operates it — a payment order authorised against balance plus facility and met without an act, the customer told on the statement — with Square Loans' repayment (a fixed share of each receipt) and a limit no overdraft has (computed daily from the flow, never applied for, proven on the bank's own exposure, shown with its history). The shared mechanism is authorisation against an agreed facility at the moment of the payment order. **Limit of the analogue.** The overdraft's facility is fixed, applied for, reviewed and repayable on demand; the form's is none of those. The analogue holds for the use mechanism only.

---

## VA-106 synergy line

The one move (default funding on an accepted term) also serves:

- **R4** — the placement and the funded event are one continuous experience: the history says "it would have covered March"; the first funded event says "it covered Tuesday". Conviction is confirmed by the product's own act, which is Hoch and Deighton's self-generated evidence in its strongest form.
- **R2** — for the migrated customer the routine at a shortfall is unchanged from the overdraft, so migration asks nothing new of them; the C2 acceptance reading (decline > ⚠ 30%) is protected by removing the one change that would have shown up as declines.
- **R1** — the exposure model is unchanged; the move confirms that the limit is a term of the account, which is where C1's "no application" always sat.
- **R8** (by number) — the routine with no act is a switching cost; the funded-event record is data held here only.
- **R6** (by number) — the funded event is the natural unit for the price: interest on days drawn, no separate buy act.

Five candidates. Not a local optimisation.

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per event unless stated; every ⚠ is T4.

| Actor | Behaviour needed | How often | What it gains | What it costs | Best alternative and its surplus | Arithmetic (VA-157) | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|
| The business owner (the customer) | accepts the limit term once; leaves it on; repays a funded draw they did not want, if any | once; then nothing per event | per funded event: the unpaid-item fee avoided ⚠ £10–35 (T2, published tariffs) and the late-payment cost avoided ⚠ £20–100 (statutory interest under the Late Payment Act, supplier goodwill; judged) | interest for the days drawn: ⚠ £1,000 × ⚠ 5.4–15% a year × ⚠ 10–20 days = ⚠ £1.5–8; time nil | personal money transferred in (owner-funded): ⚠ 0.25 h at ⚠ £30 = £7.5 plus the money not elsewhere; surplus ⚠ £5–20 when the money is to hand, nil when it is not | central: gain £70 − cost £4 − alternative's surplus £10 = **£56** · pessimistic: gain £30 − cost £8 − alternative's surplus £20 = **£2** | **PASS** (pessimistic > 0) — the case is marginal for the customer with personal money to hand, who is the customer the switch-off serves |
| The account line (Case A) | authorises against balance plus limit; funds; notifies; stores the funded event | per payment order | interest income on funded draws (the drawn book rises by the share that would have been returned: ⚠ 5–15% of drawn balances, at ⚠ £54–150 per £1,000); the returned-item handling saved ⚠ £5–15 per item | the unpaid-item fees given up — restated from C4: with the term on for ⚠ 80–95% of accounts, ⚠ 228,000 × ⚠ 2–6 × 0.80–0.95 × £10–35 = ⚠ £3.6–45m a year (was ⚠ £0.9–24m at C4 on a 20–50% share) | keep the unpaid-item fee: surplus = the fee | central: gain (interest £10m + handling £3m) £13m − cost £12m − alternative's surplus £12m = **−£11m** · pessimistic: gain £4m − cost £45m − alternative's surplus £45m = **−£86m** | **FAIL at both corners at the actor level.** Force: the bank itself (mode 3 — the pricing committee's price condition, C2, and the decision to run the line) and the FCA — PRIN 2A.4 price and value on a fee charged for a payment the account could have met, and PS19/16's direction of travel on overdraft and returned-item charges. Disposed below as a mode-3 standing constraint and an unmeasured input to C6 by number |
| The bank's product and conduct function | drafts the term and the CONC 4.7 pre-contract information; signs the notice wording | once; reviewed yearly | a regulated agreement in a form the FCA's overdraft determination already covers (no new form of agreement) | ⚠ 200–400 hours once = ⚠ £15–30k | a per-account credit agreement for each draw (the conventional form): ⚠ hours per account; surplus negative | central: gain £0.5m (agreements not drafted per account) − cost £0.02m − alternative's surplus £0 = **£0.48m** · pessimistic: gain £0.1m − cost £0.03m − alternative's surplus £0 = **£0.07m** | **PASS** |
| Model risk (the release track) | reads the loss rate on default-funded against hand-drawn events at the Stage 2 arms | per stage reading | the answer to assumption (4) at no new cost — the arms exist (C3) | ⚠ 40–80 hours per reading inside the existing stage reading | not reading it: surplus nil, and a gate unread | central: gain £0.1m (a rule change made by flow band before scale) − cost £0.005m − alternative's surplus £0 = **£0.095m** · pessimistic: gain £0.02m − cost £0.008m − £0 = **£0.012m** | **PASS** |
| The payee (the supplier, HMRC, the landlord) | none — receives the payment on the day | — | — | — | — | not a required behaviour; no row | — |

**The account-line row, disposed.** The bank gives up a fee it charges for not meeting a payment it could have met. That is a constraint of mode 3 — the bank has decided to run the line — and the fee is the bank's own revenue, not a cost of the form. The number is carried to C6 as an input to the price by number: the price must recover, on the drawn book, what the unpaid-item fee earned, or the bank must accept a lower fee income as the price of the line. The C4 decision stands; the number is larger.

---

## Actor tracks (VA-102)

No new actor this challenge. Rows added at arrival: the account line track — authorisation against balance plus limit, funding, the notice, the funded-event record (C5); the customer's own row — acceptance and the switch-off; the exception cell — funded-event queries; the release track — the default-funded loss reading; the regulator track — CCA s.74(1)(b) and CONC 4.7. No counterparty with an acquiring transition. Decisions stated on each row in the CTM v5.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** WP-2 (the draw) is amended: the draw is the account's act under an accepted term (default funding); the customer's explicit draw is retained as an option. One acceptance act is added at release for the never-borrowed customer; the migrated customer's acceptance is the migration agreement. No component is removed.

**Earlier requirements this same move also serves (VA-106).** R4, R2, R1 with mechanisms; R8 and R6 by number (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — unchanged with one restatement.** "Drawn by the customer without an application" reads "drawn under a term the customer accepted, without an application". The exposure model, the rule, the receipts share and the four removed operations are untouched. Property holder of "the customer draws without applying" moves from the customer (the act) to the account line (the term) — a track row, not a defect | re-verified: the C1 figure is non-gating in mode 3; at-scale FMOS on the selected customer 27.0% / 34.1% / 41.2% |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — unchanged, strengthened on one line.** The attendant routine's step 1 ("pays the supplier from the overdraft") is now identical in the form: nothing is asked of the migrated customer at a shortfall. The acceptance reading (decline > ⚠ 30%) loses its most likely cause. The KMC is untouched | re-verified: FMOS 27.0% / 34.1% / 41.2% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — unchanged with one addition.** The term takes effect at release; the acceptance is asked at release. The stage reading gains one line (assumption 4 — default-funded against hand-drawn loss) inside the existing reading; the kill band is unchanged. Stage 1's migrated accounts carry the term from the modifying agreement | re-verified: Stage 1 margin 6.7% at the convention, 1.0% at the band's low end (spread count below) |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — one measure restated, no check failed.** The C4 hypothesis read conviction as "draw share within ⚠ 90 days of first shortfall, ⚠ ≥ 3× the number-alone arm". With the draw automatic that ratio reads the default, not the belief. Restated measure, same arms, same accounts: the switch-off share before the first funded event (the unconvinced act) and the reversal share within ⚠ 3 days — history arm ⚠ ≤ 10% and ≤ 5%; number-alone arm expected ⚠ ≥ 2× both; falsified if the arms do not differ at ⚠ 10,000 accounts. The C4 record is annotated, not overwritten. The mutation-gate rejection of B at C4 is confirmed as a scope ruling (R5's mechanism) and its two conduct objections are disposed at SR4 assumption (3). The account-line FAIL row's number rises (⚠ £3.6–45m); decision unchanged | re-verified: FMOS 27.0% / 34.1% / 41.2%; cap line ⚠ 0.03–0.20 carried |

No FAILED row. Function-gate re-run: NOT YET — C7's.

---

## Financial check — the floor on four layers, the ceiling as a band and the cap

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2 (amended C5), WP-3, WP-4, WP-5, CP-1 (amended C2, C4), CP-2, PC-1 (condition).

**What R5 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v5 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| authorise a payment order against balance plus limit; fund from the limit; record the funded event | per event, automated | e.funded_event on q.accounts_with_limit | 760,000 × 2–6 shortfalls × 0.80–0.95 term-on = 1.2–4.3m | £0 — the authorisation the account line runs today with one more input (T2: the available-balance rule on every UK current account with an arranged overdraft) | £0 | 0.00 |
| tell the customer a payment was funded (in-account notice; a statement line) | per event, automated | e.funded_event | 1.2–4.3m | ⚠ £0.005–0.02 | ⚠ £6–86k | 0.00–0.02 |
| explain a funded or a returned payment to a customer who asks | cell | e.funding_query on q.replica_accounts | ⚠ 0.05–0.2% of funded events per cell = 270–1,900 per cell | 0.25 h | ⚠ 70–475 h per cell; 0–1 handler per cell × 2.28 cells × ⚠ £50–65k = ⚠ £0–148k | 0.00–0.04 |
| draft the term and the CONC 4.7 information; the notice wording | HQ, once | e.term_drafting | 1 | ⚠ 200–400 h = ⚠ £15–30k, once, amortised over five years | ⚠ £3–6k | 0.00 |
| read the default-funded loss line at each stage reading | HQ, per reading | e.stage_reading (C3) | 3 readings | ⚠ 40–80 h inside the existing reading | inside SC | 0.00 |
| **R5 total** | | | | | **⚠ £0.08–0.24m** | **⚠ 0.02–0.06** |

*Runner's call on the query rate.* Funded events on an arranged overdraft generate few queries today — the mechanism is familiar. ⚠ 0.05–0.2% of events is judged from the C2 saving-query and C4 limit-query rates, lower because the event is expected (the placement precedes it). Threshold: above ⚠ 0.5% the cell needs a 16th handler and the R5 line rises to ⚠ 0.10. Convergence: the first replica's six months.

**The four-layer floor at C5 (AOM v5 section 6).**

```
PVC  40.02–83.22   funding 15–30 · expected loss 20–40 · computing and payments 2.02–5.09 (C5: +0.00–0.02, the notice) · exceptions and write-off 3.00–8.13 (C5: +0.00–0.04, the funding-query handlers)
RC    2.02–5.04    unchanged — no new HQ person; the term is drafted inside the existing 13
SC    0–1          unchanged — the term drafting (⚠ £15–30k once) sits inside the band
IC   12–17         unchanged
FLOOR 54.04–106.26  (C4: 54.03–106.20; C3: 54–106)
```

The drawn book itself rises under default funding (the payments that would have been returned are now draws — ⚠ 5–15% of drawn balances, T4). That raises the denominator and every per-£1,000 fixed line falls a little; the runner does not take the credit — the floor is stated at the C4 book.

**Carrying check (challenge skill section 8).**

```
CARRYING CHECK — R5
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v2 KMC-OD-STD-TARIFF)
  floor                                  54.04–106.26
  operating bar = floor × 1.25           67.55–132.83
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  ceiling low corner × surplus band      135.00 at 0.90 · 142.50 at 0.95 · 150.00 at 1.00
  headroom over the operating bar        2.17 · 9.67 · 17.17
  carries                                true at every corner
  FMOS worst corner (ceiling low × f − floor high) ÷ floor high
                                         27.0% at 0.90 · 34.1% at 0.95 · 41.2% at 1.00
  FMOS best corner                       399.6% · 427.4% · 455.1%
  conventional additions used (RD-030)   R5 ⚠ 0.02–0.06; cumulative ⚠ 0.05–0.26; remaining ⚠ 7.74 at the high corner; the cap itself ⚠ £2.00 / £8.00 / £14.00 across the surplus band
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C5.yaml`).** By hand: **27.0% at the worst corner at the surplus band's low end; 34.1% at the convention; 427.4% at the best corner at the convention. PASS on the 25% gate at every point of the band.** The fall from 34.2% (C4) to 34.1% is R5's cost. The script refused (verifier r5); the re-run is queued behind the seal.

**Binding gate — by driving (VA-84).** Thirteen gates driven at C5: the twelve of C4 and (13) the default-funded loss gap. Ordered by margin at the assumed high corner:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.2% / 4.8% / 5.4%** across the surplus band (floor high may rise to 108.0 / 114.0 / 120.0; at C5 the loss line is 66.26 + 10L); zero margin at 6.9% / 7.6% / 8.4%; assumed ⚠ 2–4%; surplus 0.2–1.4 points at the assumed high corner. **First to fail.**
2. the price condition's room — £2.17 at the band's low end.
3. the default-funded loss gap (new) — ⚠ 1 point above hand draws switches the term to opt-in by flow band; assumed nil; unmeasured. Sits on gate 1's line: a gap of 1 point on ⚠ 30–50% of draws moves the pool rate by ⚠ 0.3–0.5 points — inside the 0.2–1.4 surplus at the convention, outside it at the band's low end.
4. the non-empty history share (gate 12 of C4), unchanged.
5. the switch-off share (⚠ ≤ 10%; falsified above 25%) — a use gate, no floor effect.
6. the funding-query rate (⚠ 0.05–0.2%; threshold 0.5%).
7–13. carried from C4 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, now including default-funded draws
  threshold:    4.2% at the surplus band's low end · 4.8% at the convention · 5.4% at the top — the 25% margin fails above it at the worst corner; zero margin at 6.9% / 7.6% / 8.4%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.2–1.4 points at the assumed high corner; the default-funded gap (gate 3) may consume ⚠ 0.3–0.5 of it
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the default term switches to opt-in by flow band at a ⚠ 1-point gap (SR4 assumption 4)
  reads at:     the Stage 1 12-month reading (the pool); the first replica's 12-month reading (the gap)
```

**Independence (VA-97).** NOT shown — the margin is a transform of the loss gate. Free counts named: the switch-off share and the funding-query rate (gates 5 and 6) — counts of acts, not of losses; both unmeasured.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts; more under default funding, not credited). At Stage 1 (⚠ £0.4–1.9bn): RC 3.84–32.38; floor 55.86–133.60; worst-corner margin 6.7% at the convention, 1.0% at the band's low end.

**Working capital timing.** No change. A funded event is a draw on the day of the payment order; the receipts share repays as before. The bank's cash leaves on the same day it would have left for a hand draw.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Required product use routine mapped, numbered, from the decision to the Key Cost reduction; the present routine stated for contrast ✓ (SR1).
- Key learning block tied to a step number (5, and 3 before it); structural cause named (routine disruption); the other two causes tested and set aside; manifestation stated with its three forms and the three customer responses; the acute cluster named ✓ (SR2).
- ToC — nature a named class (disruptive) ✓; theory named with researcher, year and paper ✓ (Madrian and Shea 2001; Wood and Neal 2007); context as conditions ✓; outcome as a state ✓.
- Theory stress test run; the contrast theory named (Carroll et al. 2009); fragile-findings list checked (Jachimowicz et al. 2019) ✓.
- Strategy — exactly one structural move ✓; mechanism stated as elimination with the "alone for the first time" test ✓; R1 consistency ✓; at-scale test with the volume named ✓; R8 signal ✓; hypothesis with falsification and four named assumptions ✓.
- Mutation gate emitted before the strategy; six genuine mutations (A–F); justification mode false ✓.
- Three tests: primary cause, entry point, incumbent — passed, with the incumbent test's reading recorded as a runner's call ✓.
- Credibility mechanism (VA-81) ✓. Existence test and affordability screen (VA-92, VA-164) ✓ — internal holder admitted; nothing payable.
- Property-holder test (VA-71) ✓ — five holders, each on a track.
- Pointing test ✓ — the move removes the act, not its difficulty.
- Launch constraints absent from SR1–SR5 (VA-23) ✓.
- Limit of the analogue stated ✓.
- Completeness contract (VA-73) ✓. No forward references (VA-80) ✓ — R6, R7, R8 by number only.
- VA-106 line, five candidates ✓. VA-103 table, four rows, one measure restated at R4 ✓. VA-127 table, two arithmetic lines per row; one FAIL row with the force named; one marginal PASS ✓. VA-82 classified ✓.
- Conventional cost line named and removed (F2) ✓ — R5's ⚠ 1–2; the cap line printed.
- Binding gate by driving ✓ (13 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162).
- Verdict order (VA-95) ✓ by reading. Loop-gate branch (VA-153): no FAIL on the design. Loop-backs (VA-151): 0.
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r5-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v5 and AOM v5 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v5 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at C5 (19,500 at C4 plus ⚠ 70–475 funding-query hours plus ⚠ 0–425 of headroom the runner adds for the first-year query peak; the high corner is the figure used), covering ⚠ 100,000 drawn accounts and ⚠ 333,000 accounts with a limit per cell. Handlers: 20,400 ÷ ⚠ 1,400–1,600 = 12.8–14.6 → **14 handlers per cell (band 13–15)** against 13 at C4. At scale: 2.28 cells, ⚠ 46,500 hours, ⚠ 32 handlers + 3 leads + a trainer = 36 people in cells. Every calculation in this record uses 20,400 and 14. Role support: no new role; the funding-query handler is an exception handler with the same supervisor, trainer and reviewer (AOM v5 section 4) ✓. Unit sizing: the cell's fixed cost ⚠ £0.9–1.18m ✓. Component carriage: every C5 transition in the CTM v5 is carried by WP-2 (amended) or a flag ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin 27.0% / 34.1% / 41.2% at the worst corner across the surplus band, 427.4% best at the convention, by hand; PASS at every point; `fit_margin.py` run after the seal of 21 September 2026 19:49 (not the runner's) confirms 34.1% at the convention and a floor of 54.04–106.26 — the low corner corrected from a hand slip of 0.01. Carrying check: carries; headroom £2.17 at the band's low end. Binding gate: the loss rate, unmeasured; a new gap on the same line, unmeasured. Conventional additions used: ⚠ 0.05–0.26 of ⚠ £8. Independence NOT shown; two free counts named. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- `fit_margin.py` — **run** (the toolchain was re-sealed at 19:49 on 21 September 2026, after this record's first draft; the runner did not seal): PASS at 34.1%, output in verifier r5; this record's margin lines agree.
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- `check_verdict_order.py` — **run** on a new verdict record (`sme-fintech-models/bank-credit-facility-verdict-record.yaml`, R1–R5 all PROVISIONAL): IN ORDER.
- The account line's actor row — FAIL at the actor level, **disposed as a mode-3 standing constraint**, number restated (⚠ £3.6–45m a year); **unmeasured input** to C6 by number; owner: the pricing committee; convergence: the bank's own count of unpaid-item fees on accounts with a limit (a red field).
- The customer's row — PASS at £2 pessimistic: **marginal**; the switch-off is the design's answer for that customer; no force needed.
- Default funding's authorisation, notice and funded-event record — **build items**; owner: the account line (Case A); convergence: the Stage 1 release funds a payment.
- The term and the CONC 4.7 information — **build item**; owner: the product and conduct function; convergence: the signed term.
- The hypothesis (met share ⚠ ≥ 95%; switch-off ⚠ ≤ 10%; reversal ⚠ ≤ 5%) — **unmeasured inputs**; owner: model risk; convergence: the first replica's 90 days.
- The default-funded loss gap (⚠ 1-point threshold) — **unmeasured input** on the binding gate; owner: model risk; convergence: the first replica's 12 months.
- The funding-query rate (⚠ 0.05–0.2%; threshold 0.5%) — **unmeasured input**; owner: the exception cell lead.
- The payment-channel mix (instant the majority) — **unmeasured input** for the bank's own base (T2 for the market); owner: the account line; convergence: the bank's payment counts by channel (a red field).
- CONC 5.2A timing (creditworthiness at acceptance, on the rule's limit) — **standing constraint**, designed for; what a ruling would settle is named at SR4 assumption (3).
- CCA s.74(1)(b) and CONC 4.7 — **standing constraint**, designed for.
- C4's and earlier carried items — carried unchanged, except the C4 hypothesis measure, restated under VA-103.

```
GATE VERDICT — on the cumulative architecture C1 to C5
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files; coverage and trace scripts not run)
  financial limb:    PROVISIONAL     FMOS 27.0% worst corner at the surplus band's low end / 34.1% at the convention / 427.4% best (by hand, confirmed by `fit_margin.py` after the seal) · binding gate the loss rate on the pool: surplus 0.2–1.4 points at the assumed high corner, unmeasured; the default-funded gap may consume 0.3–0.5 of it · conventional additions used ⚠ 0.05–0.26 of ⚠ £8
  decisions:      17 unmeasured inputs (12 carried), 7 build items (3 carried), 1 standing-constraint set (2 new rows), 2 structural limits (carried); 1 actor-level FAIL disposed as a mode-3 standing constraint with an unmeasured input; 1 marginal PASS noted
  capacity figure:   20,400 exception hours per cell a year, 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15) at 1,400–1,600 productive hours — used throughout   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; two free counts (the switch-off share, the funding-query rate) named and unmeasured   VA-97
  gates driven:      13; first to fail on evidence: the loss rate, margin 0.2–1.4 points; second: the price condition's room (£2.17); third: the default-funded gap on the same line   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r5-2026-09-21.md   VA-90
  inherited:         R4, R3, R2, R1 PROVISIONAL — R5 cannot exceed them; F1 closed PROVISIONAL with one condition   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design; the actor-level FAIL is disposed with owner and convergence; the CTM and AOM model files are build items   VA-153
  launch constraints:none inside SR1–SR5 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn; at the Stage 1 count the worst-corner margin is 6.7% at the convention, 1.0% at the band's low end   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; the new gap sits on the same input   VA-160
  VERDICT:           PROVISIONAL
```

**R5 failure test.** Would R5 have failed? Three conditions. First, the move books an activation cost: it does not — ⚠ 0.02–0.06, none of it onboarding, help or support, against the conventional ⚠ 1–2. Second, the move reduces rather than eliminates: it does not — no act remains in the routine; the mutations that reduce (C, D, E) are named and rejected. Third, the default is wrong for the mainstream: unmeasured; if the switch-off share exceeds ⚠ 25% or the reversal share ⚠ 15% at ⚠ 10,000 accounts, R5 loops back to SR2. None fails today. The nearest is the third, and it is read at the first replica at no cost.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the price, its structure and its presentation; the unpaid-item fee given up (restated ⚠ £3.6–45m) as an input; the funded event as the billing unit — C6
  - who brings the customer to the limit — C7
  - the routine with no act, and the funded-event record, as switching costs — R8
  - the default-funded loss history as a scarce resource — R9
- **Unmeasured inputs (owner named):**
  - the met share ⚠ ≥ 95%; the switch-off share ⚠ ≤ 10% (falsified above 25%); the reversal share ⚠ ≤ 5% (falsified above 15%) — model risk; the first replica's 90 days
  - the default-funded loss gap, threshold ⚠ 1 point — model risk; the first replica's 12 months
  - the funding-query rate ⚠ 0.05–0.2%, threshold 0.5% — the exception cell lead; six months
  - the payment-channel mix on the bank's base — the account line; a red field
  - the drawn-book rise under default funding ⚠ 5–15% — finance; the Stage 1 reading (not credited in the floor)
  - the unpaid-item fee revenue given up ⚠ £3.6–45m — the pricing committee; a red field
  - the C4 hypothesis, restated: switch-off and reversal by arm — model risk; the Stage 2 arms
  - carried from C4, C3 and C2 as listed in the C4 record; every ⚠ figure
- **Build items:**
  - the script runs after the seal (Tom); the CTM and AOM model files and the coverage and trace scripts (Venture Architect seat) — carried
  - default funding at authorisation; the funded-event notice and record; the switch-off control — the account line (Case A)
  - the term and the CONC 4.7 pre-contract information; the notice wording — the product and conduct function
  - carried from C4: the limit-history display; the promotion template; and from C3 and C2 as listed
- **Standing constraints:**
  - CCA 1974 s.74(1)(b) and the FCA determination under s.74(3); CONC 4.7 pre-contract information at acceptance — new
  - CONC 5.2A creditworthiness at acceptance on the rule's limit (the stricter reading) — new
  - the account line's unpaid-item fee given up — a mode-3 constraint, restated
  - carried: CONC 3 (the display); SS1/23 scope; the CCA modifying agreement; PS9/24; the Consumer Duty price-and-value outcome; IFRS 9 5.5.20
- **Structural limits:** carried — the new-to-trading business; the released account with no shortfall in twelve months. R5 adds none: the customer with the term off is a choice, not a limit.
- **Unowned design defects:** none.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Required product use routine — numbered, from decision to Key Cost reduction | PASS — eight steps; the present routine for contrast | SR1 |
| Key learning block — step number, structural cause, manifestation | PASS — step 5 (and 3); routine disruption; the payment leaves before the draw | SR2 |
| Other two causes tested and set aside | PASS | SR2 |
| Acute cluster named | PASS — the migrated overdraft customer | SR2 |
| ToC — nature of the challenge (a named class) | PASS — disruptive | SR3 block |
| ToC — theory (researcher + year + paper) | PASS — Madrian and Shea 2001; Wood and Neal 2007 | SR3 block |
| ToC — context; outcome as a state | PASS | SR3 block |
| Theory stress test; contrast theory; fragile-findings list | PASS — Carroll et al. 2009; Jachimowicz et al. 2019 | SR3 |
| Baseline stated honestly (4a) | PASS — the baseline creates the block | SR4 |
| Mutation gate before the strategy; ≥ 2 genuine mutations | PASS — six | SR4 block |
| Strategy — one structural move; elimination not reduction; at-scale test | PASS | SR4 |
| Strategy — hypothesis with falsification and named assumptions | PASS — four assumptions | SR4 |
| R8 signal flagged | PASS — yes | SR4 |
| Incumbent test | PASS on the cumulative form — reading recorded as a runner's call | SR4 |
| Credibility mechanism (VA-81) | PASS | SR4 |
| Existence test and affordability screen (VA-92, VA-164) | PASS — internal holder; nothing payable | SR4 |
| Launch constraints absent (VA-23) | PASS | SR4; GATE VERDICT |
| Architectural central structure found before the BFF | PASS — the daily limit (WP-1) | SR5 |
| Elegance line (VA-106) | PASS — R4, R2, R1 with mechanisms; R8, R6 by number | VA-106 |
| CTM update — Phase 2 Activation rows; traceability | PASS | CTM v5 sections 2 and 4 |
| AOM — every activity ↔ a flow; resolving drivers; no ratios; role support; LMU sizing | PASS — 14 handlers per cell (band 13–15) | AOM v5 |
| Fin-sim — working capital timing captured | PASS — no change | financial check |
| FIT — margin (per-requirement, 25%) | PASS at 27.0–41.2% (worst corner, surplus band) — **script REFUSED**, by hand | verifier r5 |
| FIT — I check; T check | PASS | verifier r5 |
| FIT staleness — component set recorded (VA-74) | PASS | financial check |
| Loop gate | PASS — PROVISIONAL fully specified | close |
| Three-limb close (VA-89, VA-91) | PASS — one capacity figure (20,400 h per cell) | close |
| Financial halves shown independent (VA-97) | NOT shown — two free counts named; shared input declared (VA-160) | financial check |
| Spread count (VA-162) | PASS | financial check |
| Partner business case (VA-99) | not applicable — no partner at C5 | VA-127 |
| Structural-limit decision (VA-101) | PASS — two carried, none added | carried items |
| Verdict composes forward (VA-95) | PASS — `check_verdict_order.py` IN ORDER on the verdict record | GATE VERDICT |
| Upstream re-verified (VA-103) | PASS — four rows; one measure restated at R4, annotated not overwritten | VA-103 table |
| Actor business cases with two arithmetic lines (VA-127, VA-157) | PASS on the table — one FAIL row with the force named and disposed; one marginal PASS | VA-127 table |
| Property-holder test (VA-71) | PASS — five holders | SR4 |
| Binding gate by driving (VA-84) | PASS — 13 gates | financial check |
| No parallel close (VA-85) | PASS — C6 not opened | status file |
| Classified carried items (VA-82) | PASS | carried items |
| Independent verification artefact (VA-90) | PASS — artefact exists; its script half queued | verifier r5 |
| No forward references (VA-80) | PASS | throughout |
| Every load-bearing figure a band with type, evidence method, threshold and convergence event | PASS | financial check |
| **Conventional cost line named and removed (F2)** | **PASS — R5's ⚠ 1–2 removed; additions used ⚠ 0.05–0.26 of ⚠ £8 cumulative** | financial check |
| Consistency audit; verification at the function gate | not at C5 — C7's | — |
| Counterfactual costed (RD-030) | stands — read against | counterfactual file |

**Rows that did not pass, and what was decided:** FIT — margin and VA-95 order: by hand at the first draft, then confirmed by `fit_margin.py` and `check_verdict_order.py` after the seal; one hand slip of 0.01 at the floor's low corner corrected. VA-97: NOT shown; two free counts named. The VA-127 account-line row: FAIL at the actor level, force named (the bank itself in mode 3; PRIN 2A.4; PS19/16), disposed as a standing constraint and an unmeasured input to C6 by number.

---

## Quality check

| Test | Result |
|---|---|
| Does the strategy eliminate (not reduce) the primary disruption? | **Yes** — no act remains in the routine |
| Is it stated as a strategy, not a feature or an onboarding process? | **Yes** — the limit as a term the account enforces at authorisation |
| Does it work within the R1 BFF? | **Yes** — the exposure model is unchanged; who performs the draw changes |
| Could an incumbent do this without changing their BFF? | **No on the cumulative form** — the element (default funding) is the incumbent's own; the limit it funds from is not |
| Is it designed for mainstream customers, not early adopters? | **Yes** — the customer does nothing; the early adopter keeps the draw-ahead option |
| Conventional R5 line named and removed; cap line printed | ✓ — ⚠ 1–2 removed; ⚠ 0.05–0.26 of ⚠ £8 used |
| Margin by the correct formula, cost denominator, bands from the registry | ✓ — by hand; script queued |
| Named assumptions (authorisation rule; channel mix; conduct status; default-funded loss) | ✓ |
| Pivot trigger written | ✓ — loss > ⚠ 5% (C2's); the opt-in fallback by flow band at a ⚠ 1-point gap |
| Verdict composes forward | ✓ |
| Confidence | **Medium** — the mechanism is the most replicated effect in the field and costs almost nothing on the account line's existing rule; the default-funded loss gap is unmeasured and sits on the binding gate; the C4 measure had to be restated |
| What would increase confidence? | the first replica's 12-month reading of default-funded against hand-drawn loss — one number, already inside the stage reading |
| No tooling vocabulary or metaphor in prose; house-style checker run | run on file save — see changelog |

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15)

| # | Source | Used for |
|---|---|---|
| G1 | Madrian, B. and Shea, D. (2001), "The Power of Suggestion: Inertia in 401(k) Participation and Savings Behavior", *Quarterly Journal of Economics* 116(4) | the adoption theory — default effects (49% → 86%) |
| G2 | Wood, W. and Neal, D. (2007), "A New Look at Habits and the Habit–Goal Interface", *Psychological Review* 114(4) | the supporting mechanism — habits as cued responses |
| G3 | Carroll, G., Choi, J., Laibson, D., Madrian, B. and Metrick, A. (2009), "Optimal Defaults and Active Decisions", *Quarterly Journal of Economics* 124(4) | the contrast theory — active choice |
| G4 | Jachimowicz, J., Duncan, S., Weber, E. and Johnson, E. (2019), "When and why defaults influence decisions: a meta-analysis of default effects", *Behavioural Public Policy* 3(2) | robustness — 58 studies, d = 0.68 |
| G5 | Sheeran, P. (2002), "Intention–Behavior Relations: A Conceptual and Empirical Review", *European Review of Social Psychology* 12 | the intention–action gap (manifestation 3) |
| G6 | Consumer Credit Act 1974, s.74(1)(b) and s.74(3); FCA CONC 4.7 (pre-contract information: current-account overdrafts); CONC 5.2A (creditworthiness) | the conduct status of default funding (T1) |
| G7 | FCA PS19/16, Overdraft pricing remedies (2020) | no unarranged charge above arranged; the direction of travel on returned-item charges |
| G8 | FCA PRIN 2A.4 (the Consumer Duty — price and value) | the force on the account line's fee given up |
| G9 | UK Finance, UK Payment Markets 2025 (payment volumes by method) | instant channels the majority of business payments by count (T2) |
| G10 | Late Payment of Commercial Debts (Interest) Act 1998 | the late-payment cost avoided (customer row) |
| G11 | Lloyds Bank, HSBC UK, Barclays business overdraft product pages (read 21 September 2026) | available balance includes the arranged overdraft; unpaid-item fees ⚠ £10–35 (T1 for the tariff, T2 for the range) |
| G12 | Counterfactual, RD-030 (`sme-fintech-models/bank-credit-facility-counterfactual.md`), R5 row | the conventional R5 line ⚠ 1–2, removed |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | First record. R5 designed on the C4 form; verdict PROVISIONAL; WP-2 amended (default funding on an accepted term); conventional R5 line removed; the C4 conviction measure restated under VA-103; the account-line fee row restated. House-style checker run on save; findings fixed. |
| v1.1 | 21 September 2026 | The toolchain was re-sealed at 19:49 (not by the runner). `fit_margin.py` run: PASS at 34.1%, floor 54.04–106.26 — the hand figure 54.05 corrected (best-corner margin 427.4%, Stage 1 floor low 55.86). `check_verdict_order.py` run on the new verdict record: IN ORDER. The two script build items closed. Two metaphor and two tooling words removed after the checker. |
