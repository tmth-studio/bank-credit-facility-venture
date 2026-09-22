# A business bank's credit facility line — challenge six (R6) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R6 carries. The buy block is a timing mismatch the conventional form pays for: the standard tariff debits interest to the account on a fixed calendar date and charges the arrangement and renewal fee as a lump, so the charge falls due at a moment that has nothing to do with the money coming in — and the debit itself can be the shortfall the customer was trying to avoid. The one move removes the calendar from the charge: the charge accrues daily on the drawn balance at one rate, and is collected only from receipts, as the first slice of each receipts share (WP-3). No fee, no debit event, no renewal. The price is **14.0% simple a year on the daily drawn balance — £140 per £1,000 drawn a year (band ⚠ 135–142.5)**; representative example ⚠ 14.0–14.9% APR. That resolves PC-1 (C2) from a condition to a number: below the standard tariff (150–300 plus fees), above the operating bar (132.84). The verdict cannot exceed R1–R5's PROVISIONAL (VA-95). The move adds ⚠ £0.00–0.01 per £1,000 drawn a year; cumulative conventional additions used ⚠ 0.05–0.27 of ⚠ £8 (RD-030). Floor ⚠ £54.04–106.27. Margin at the worst corner **31.7% at the set price**; 27.0% at the band's low end, 34.1% at its top. Binding gate unchanged: the loss rate on the flow-underwritten pool — at the set price the 25% margin fails above ⚠ 4.57%; the assumed high corner is 4.0%; the C5 default-funded gap may consume ⚠ 0.3–0.5 of the 0.57 points. The conventional R6 line is nil (the counterfactual books no cost against the price); nothing is removed, and nothing is added but the accrual inside computing.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c5-v1-2026-09-21.md` (R5, PROVISIONAL, object-after to 23 September 2026 17:00), and the C4, C3, C2 and C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3. **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F2 rule this record works under (Tom, 16 September 2026).** R4 to R7 remove the blocks the conventional form pays for. The conventional R6 line is nil in the counterfactual (RD-030): a bank does not book a cost against the price structure; it books the price structure's effect as revenue given up, arrears and returned debits. This record names that effect, removes its cause, and books only what the one move costs.

**Sections in this record.** Defined terms. SR1 to SR5 (SR4b, the gateway partner). Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C5. Financial check. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

As in the C1–C5 records: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *exception cell*, *standard tariff*, *migration*, *price condition*, *shadow limit*, *back-test*, *release*, *stage*, *shortfall*, *limit history*, *placement*, *use block*, *default funding*, *acceptance*, *draw ahead*, *funded event*, *available balance*, *switch-off*, *reversal*. New at C6:

- **the charge** — the price of the limit: interest that accrues daily on the drawn balance at one rate, with no fee of any kind. It is the Payment product; PC-1 (C2) is resolved by it.
- **accrual** — the daily addition to the accrued-charge ledger: drawn balance at close of day × the rate ÷ 365. The accrued charge is held on its own ledger; it is not added to the drawn balance and does not itself bear interest.
- **collection** — the act by which the accrued charge is paid: the first slice of each receipts share (WP-3) clears the accrued charge; the remainder repays the drawn balance. No debit is ever made to the account for the charge.
- **the rate** — 14.0% simple a year (⚠ band 13.5–14.25%), set by the pricing committee once, reviewed yearly; one rate for every account with a limit.
- **the representative example** — the CONC 3.5.5R illustration shown wherever the rate is shown: the rate, the APR, a worked figure on £1,000 drawn for 30 days.
- **the calendar debit** — the conventional form's charging event: interest and fees debited to the account on a fixed date each month or quarter, whatever the balance that day. The block this record removes.
- **timing mismatch** — the buy block type: the charge falls due at a time set by the calendar, the money arrives at a time set by the customer's trade.

---

## SR1 — Interim product value lifecycle, per party

Two parties pay or receive under the Payment product: the customer (who pays the charge) and the bank's account line (which receives it, and gives up the tariff to do so). The lifecycle is drawn for each as the C1–C5 form stands, before this record changes anything, with the block marked; the value curve shows where each party is, at each stage, against the alternative they hold.

**The customer.** The selected customer is the migrated overdraft user (C2's acute cluster) and the never-borrowed customer with enough flow. Under the C1–C5 form the customer accepts the term (C5), holds a limit that does nothing until a shortfall, has a payment met by default (C5), watches the receipts share repay the draw (WP-3) — and, in the form as it stands, is charged by the incumbent's method: a calendar debit, because nothing at C1–C5 designed the charge. The debit is the block: it arrives on a date, not with a receipt; on an account run close to the balance it is itself a shortfall (met from the limit under C5 — a draw to pay the charge on a draw); and the arrangement fee at acceptance is a lump paid before any value has been received.

<div style="font-family:'DM Sans',system-ui,sans-serif;color:#0f1923;--accent:#1f4fa8;--accent-light:#e8eef8;--green-bg:#e6f4ec;--green-text:#166534;--green-border:#a7d4b8;--warning-bg:#fff8e6;--warning-border:#d4820a;--border:#dde1e7;--text:#0f1923;--text-secondary:#4a5568;--text-muted:#718096;--panel-bg:#0f2744;margin:16px 0;">
<div style="font-size:13px;letter-spacing:0.04em;color:#718096;margin-bottom:8px;">LIFECYCLE — THE CUSTOMER (as the C1–C5 form stands; the block at stage 4)</div>
<div style="display:grid;grid-template-columns:1fr 3fr 1fr 2fr 2fr 1fr;gap:6px;">
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 1 · once</div><div style="font-weight:700;font-size:14px;">Acceptance</div><div style="font-size:12px;color:#4a5568;">Accepts the limit term after reading the history (C4, C5). Pays an arrangement fee in the conventional form.</div><div style="font-size:12px;color:#718096;">~10 minutes</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#fff8e6;color:#854d0e;border:1px solid #d4820a;">Decision point</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 2 · days to months</div><div style="font-weight:700;font-size:14px;">Limit on, no draw</div><div style="font-size:12px;color:#4a5568;">Runs the business against the available balance. Nothing to do; nothing to pay.</div><div style="font-size:12px;color:#718096;">⚠ 70% of accounts stay here</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#f5f4f1;color:#4a5568;border:1px solid #b0b8c4;">Passive</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 3 · a day</div><div style="font-weight:700;font-size:14px;">Funded event</div><div style="font-size:12px;color:#4a5568;">A payment that exceeds the balance is met from the limit (C5). The fee and the late-payment cost are avoided.</div><div style="font-size:12px;color:#718096;">⚠ 2–6 a year</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#e6f4ec;color:#166534;border:1px solid #a7d4b8;">Value delivered</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 4 · ⚠ 10–20 days</div><div style="font-weight:700;font-size:14px;">Charge falls due</div><div style="font-size:12px;color:#4a5568;">Conventional form: interest debited on the calendar date, whatever the balance. The debit can itself be a shortfall. <strong>The block.</strong></div><div style="font-size:12px;color:#718096;">monthly, fixed date</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#e8eef8;color:#1f4fa8;border:1px solid #b8c8e8;">Forced engagement</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 5 · ⚠ 10–20 days</div><div style="font-weight:700;font-size:14px;">Receipts repay</div><div style="font-size:12px;color:#4a5568;">The receipts share repays the draw (WP-3). The drawn balance falls with the trade.</div><div style="font-size:12px;color:#718096;">per receipt</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#f5f4f1;color:#4a5568;border:1px solid #b0b8c4;">Passive</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 6 · ongoing</div><div style="font-weight:700;font-size:14px;">Repaid, limit stands</div><div style="font-size:12px;color:#4a5568;">The limit is unchanged; the next shortfall is met the same way.</div><div style="font-size:12px;color:#718096;">until the next event</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#e6f4ec;color:#166534;border:1px solid #a7d4b8;">Retained</span></div>
</div>
<svg viewBox="0 0 900 80" width="100%" style="margin-top:8px;display:block;">
  <line x1="0" y1="40" x2="900" y2="40" stroke="#b0b8c4" stroke-width="1"/>
  <polyline points="0,40 90,46 360,46 450,14 630,14 810,20 900,18" fill="none" stroke="#1f4fa8" stroke-width="2"/>
  <line x1="0" y1="40" x2="90" y2="46" stroke="#d4820a" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="450" y1="14" x2="630" y2="14" stroke="#991b1b" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="90" y1="4" x2="90" y2="76" stroke="#166534" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="96" y="12" font-size="10" fill="#166534">CVT — migrated customer (at acceptance)</text>
  <line x1="360" y1="4" x2="360" y2="76" stroke="#166534" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="366" y="72" font-size="10" fill="#166534">CVT — never-borrowed (first funded event)</text>
  <text x="4" y="76" font-size="10" fill="#718096">acceptance</text>
  <text x="200" y="76" font-size="10" fill="#718096">limit on</text>
  <text x="380" y="30" font-size="10" fill="#718096">funded</text>
  <text x="470" y="30" font-size="10" fill="#991b1b">deferred cost — the calendar debit (the block)</text>
  <text x="700" y="76" font-size="10" fill="#718096">receipts repay</text>
  <text x="830" y="76" font-size="10" fill="#718096">retained</text>
</svg>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="border-left:4px solid #1f4fa8;background:#e8eef8;padding:12px;"><div style="font-size:13px;letter-spacing:0.04em;color:#718096;">CRITICAL VALUE THRESHOLD</div><div style="font-size:14px;">Migrated customer: at acceptance — the representative example beside their own tariff. Never-borrowed customer: at the first funded event — the notice that shows what the day cost (⚠ £0.38 per £1,000).</div></div>
  <div style="border-left:4px solid #d4820a;background:#fff8e6;padding:12px;"><div style="font-size:13px;letter-spacing:0.04em;color:#718096;">BUY BLOCK TYPE</div><div style="font-size:14px;">Timing mismatch (primary): the charge is due on a calendar date, the money arrives with the trade. Lumpiness (secondary): the arrangement and renewal fee is paid before any value is received.</div></div>
</div>
</div>

**The bank's account line (the receiving party).** The account line gives up the standard tariff on migrated balances at release (C3) and gives up the unpaid-item fee under default funding (C5). It receives the charge on the drawn book. Under the C1–C5 form its receipt is by the incumbent's method too: a monthly debit that, on an account run close to the balance, becomes an arrears item, an unarranged position or a draw on the limit — a collections activity the C1 form removed as an operation (WP-3's "collections no longer exists") and which the calendar debit would bring back.

<div style="font-family:'DM Sans',system-ui,sans-serif;color:#0f1923;margin:16px 0;">
<div style="font-size:13px;letter-spacing:0.04em;color:#718096;margin-bottom:8px;">LIFECYCLE — THE BANK'S ACCOUNT LINE (the receiving party)</div>
<div style="display:grid;grid-template-columns:1fr 2fr 2fr 1fr;gap:6px;">
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 1 · at release</div><div style="font-weight:700;font-size:14px;">Tariff given up</div><div style="font-size:12px;color:#4a5568;">Migrated balances move from the standard tariff (150–300 plus fees) to the line. Revenue falls first.</div><div style="font-size:12px;color:#718096;">Stage 1, ⚠ 12 months</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#fff8e6;color:#854d0e;border:1px solid #d4820a;">Decision point</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 2 · Stage 1 to Stage 2</div><div style="font-weight:700;font-size:14px;">Charge accrues on the book</div><div style="font-size:12px;color:#4a5568;">Interest on the drawn book; in the conventional form collected by monthly debit — with arrears and returned debits to work.</div><div style="font-size:12px;color:#718096;">continuous</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#f5f4f1;color:#4a5568;border:1px solid #b0b8c4;">Passive</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 3 · Stage 2 opening</div><div style="font-weight:700;font-size:14px;">Funded book pays for the tariff given up</div><div style="font-size:12px;color:#4a5568;">The contribution on the never-borrowed and default-funded book exceeds the tariff and fee income lost. The F1 condition (Stage 2 within ⚠ 24 months).</div><div style="font-size:12px;color:#718096;">⚠ 12–24 months</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#e6f4ec;color:#166534;border:1px solid #a7d4b8;">Value delivered</span></div>
  <div style="border:1px solid #dde1e7;padding:10px;"><div style="font-size:12px;color:#718096;">Stage 4 · at scale</div><div style="font-weight:700;font-size:14px;">Line at scale</div><div style="font-size:12px;color:#4a5568;">Drawn book ⚠ £3.4–5.7bn at the charge, no collections operation.</div><div style="font-size:12px;color:#718096;">ongoing</div><span style="display:inline-block;margin-top:6px;font-size:11px;padding:2px 6px;border-radius:3px;background:#e6f4ec;color:#166534;border:1px solid #a7d4b8;">Retained</span></div>
</div>
<svg viewBox="0 0 900 80" width="100%" style="margin-top:8px;display:block;">
  <line x1="0" y1="40" x2="900" y2="40" stroke="#b0b8c4" stroke-width="1"/>
  <polyline points="0,40 150,62 450,50 600,40 750,22 900,16" fill="none" stroke="#1f4fa8" stroke-width="2"/>
  <line x1="0" y1="40" x2="150" y2="62" stroke="#991b1b" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="150" y1="62" x2="450" y2="50" stroke="#d4820a" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="600" y1="4" x2="600" y2="76" stroke="#166534" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="606" y="12" font-size="10" fill="#166534">CVT — Stage 2 opens (the F1 condition)</text>
  <text x="4" y="76" font-size="10" fill="#718096">release</text>
  <text x="200" y="76" font-size="10" fill="#991b1b">tariff and fees given up; arrears work in the conventional form</text>
  <text x="780" y="76" font-size="10" fill="#718096">at scale</text>
</svg>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px;">
  <div style="border-left:4px solid #1f4fa8;background:#e8eef8;padding:12px;"><div style="font-size:13px;letter-spacing:0.04em;color:#718096;">CRITICAL VALUE THRESHOLD</div><div style="font-size:14px;">Stage 2 opening: the point at which the contribution on the funded book exceeds the tariff and fee income given up. It is the F1 condition read as a value threshold.</div></div>
  <div style="border-left:4px solid #d4820a;background:#fff8e6;padding:12px;"><div style="font-size:13px;letter-spacing:0.04em;color:#718096;">BUY BLOCK TYPE</div><div style="font-size:14px;">Timing mismatch, mirrored: a monthly debit against a balance that moves daily makes arrears the bank must work, on a line that removed collections as an operation (C1).</div></div>
</div>
</div>

**Where the value is at each stage (the curve, in words).** For the customer the curve is at zero at acceptance, dips by the reading time and (in the conventional form) the arrangement fee, and rises at the first funded event by the fee and late-payment cost avoided (⚠ £30–135 per event, C5's VA-127 row). The calendar debit then takes value on a date unrelated to the trade — a deferred cost whose timing, not its size, is the block. For the bank the curve goes below zero at release (tariff given up) and crosses zero at Stage 2 opening.

**Limit of the diagram.** The stage widths are durations judged (T4); the curve is ordinal, not a cash figure.

---

## SR2 — Critical Value Threshold, per party

**The customer — migrated.** Trigger event: the acceptance screen (C5), where the representative example is shown beside the customer's own tariff line from the saving statement (CP-1, amended C2). Comparison: 14.0% simple with no fee, collected from receipts, against 15.62–20% EAR plus a ⚠ 1–2% arrangement fee, debited monthly. Why it tips: the customer already pays the tariff (the outflow exists, by existence — C2); the comparison is a lower number on a line they read once a year, and a charging method that cannot itself cause a shortfall. The threshold is crossed at acceptance because nothing after it asks the customer for money at a time they did not choose.

**The customer — never-borrowed.** Trigger event: the first funded-event notice (C5), which states the day's cost: "£0.38 per £1,000 for each day drawn; taken from what comes in". Comparison: the unpaid-item fee (⚠ £10–35) and the late-payment cost (⚠ £20–100) of the payment the account just met, against ⚠ £1.5–8 for the days drawn. Why it tips: the comparison is between two figures on the same screen, one of which the customer has paid before (C4's history places it). The threshold is not at acceptance for this customer — they accepted a term, not a price they expected to pay — it is at the first event, when the price becomes a figure on their own account.

**The bank's account line.** Trigger event: the Stage 2 opening decision (C3's release order; the F1 condition — within ⚠ 24 months of Stage 1). Comparison: contribution on the funded book (the charge less the floor, on the never-borrowed and default-funded balances) against the tariff and fee income given up on the migrated book. Why it tips: at Stage 1 the migrated book is most of the drawn book, and the charge is below the tariff by construction; the line pays for itself only as the book the tariff never reached is drawn. The price is the lever on both sides of that comparison, and the financial check below prices it.

**Parties with no threshold.** The payee receives the payment on the day (C5): no row. The pricing committee sets the rate; it is an actor (VA-127), not a party to the payment.

---

## SR3 — Amortisation theory of change

**Class of problem: a timing mismatch.** The customer receives value continuously (a limit that meets shortfalls as they arise; a draw that is repaid as trade comes in) and, in the conventional form, pays for it in lumps on dates set by the bank's calendar. The mismatch is structural, not a matter of the amount: the same £140 a year, debited on the 28th, is a block; taken a few pence at a time from each receipt, it is not.

```
AMORTISATION THEORY OF CHANGE — R6
  class of problem:  timing mismatch — the charge falls due on the bank's calendar; the money that pays it arrives on the customer's trade
  theory:            coupling of payment and consumption — Prelec and Loewenstein (1998), "The Red and the Black: Mental Accounting of Savings and Debt", Marketing Science 17(1): a payment is felt least when it is coupled to the benefit it pays for and made from the money the benefit produced; a payment decoupled in time from the benefit is felt as a loss, and the accounting of debt makes the decoupled instalment the most painful case. Applied: collect the charge from each receipt, at the moment the drawn money returns as trade, and there is no decoupled payment left to feel
  current state:     the customer's charge is a monthly debit (the incumbent's method, unchanged by C1–C5), decoupled from both the funded event and the receipts; on an account run close to the balance it is a shortfall in its own right; the arrangement fee is a lump before any value
  desired state:     the charge is a fraction of each receipt — accrued daily on the drawn balance, cleared by the first slice of each receipts share; there is no charging date, no fee and no debit event; the customer sees one line per receipt and the drawn balance falling; the bank sees no arrears on the charge, because a charge that is only ever taken from money that has arrived cannot fall into arrears
```

**Stress test.** The contrast theory is payment depreciation (Gourville and Soman 1998, "Payment Depreciation: The Behavioral Effects of Temporally Separating Payments from Consumption", *Journal of Consumer Research* 25(2)): a payment made well before consumption is discounted by the time it is consumed, which lowers the felt cost and raises use — the argument for the annual fee. Applied here: the argument holds where the payment is sunk and the consumption follows; the credit line's benefit arrives at unknown dates, so a fee paid in advance is not depreciated against any use in particular and is felt in full at the worst moment (acceptance, before any value). The theory does not overturn the design; it names why mutation B (a fee) is rejected. Fragile-findings check: the coupling result rests on Prelec and Loewenstein's survey scenarios and on the later field evidence on pain of paying (Soman 2001, *Journal of Consumer Research* 27(4), payment transparency — less transparent payment mechanisms reduce the felt cost and the memory of it); the design uses the direction, not the size, and the hypothesis below measures the size on the bank's own accounts.

**Why this theory and not price sensitivity.** The KMC (C2) is a price the customer pays today; the price condition is below it. If the block were price sensitivity the C2 acceptance reading (decline > ⚠ 30%) would already be the falsification. The block that remains after C2 is not the size of the charge but when it is taken, and that is what this record removes.

---

## SR4 — Amortisation strategy

**Step 4a — baseline.** The C1–C5 form has no Payment product: PC-1 says the price must be below the tariff and nothing more; the charging method is the incumbent's by default — interest computed daily and debited monthly to the account, plus whatever fee the tariff carries. On the buy block the baseline does this: nothing. It leaves the calendar debit in place, and the debit can itself be a shortfall that C5 then funds from the limit — a draw to pay for a draw.

**Step 4b — candidate mutations.**

```
MUTATION GATE — R6
baseline: the incumbent's charging method — interest accrued daily and debited to the account on a fixed monthly date; an arrangement fee at acceptance and a renewal fee each year; PC-1 bounds the total from above and says nothing about its structure
mutation_A: the charge accrues daily on the drawn balance at one rate and is collected only from receipts, as the first slice of each receipts share (WP-3); no fee, no debit, no renewal | reason_considered: removes the calendar from the charge; a payment made only from money that has arrived cannot be a shortfall and cannot fall into arrears; the customer already accepted the receipts share at C1 | verdict: adopted | reason_verdict: eliminates the cause (no charging date exists); mainstream by construction (nothing is asked of the customer); the pricing committee sets one number; cost is the accrual ledger inside computing and the split inside WP-3's existing per-receipt cost
mutation_B: a fixed charge per funded pound, set at the funded event and collected with the receipts share (Square Loans' factor-rate form) | reason_considered: the analogue's own price; one number the customer understands at the event | verdict: rejected | reason_verdict: penalises fast repayment — a funded event cleared in three days pays the same as one carried for sixty, so the APR on a short draw is very high; fails PRIN 2A.4 price and value on the short draw, which is most draws (⚠ 10–20 days); creates a reference-point block (the customer compares the charge with the interest an overdraft would have cost for three days)
mutation_C: a monthly subscription for the limit, no interest on draws | reason_considered: predictable; simple to present | verdict: rejected | reason_verdict: a calendar payment — it recreates the block it was to remove; charges the ⚠ 70% of accounts with a limit that never draw, which contradicts C1 ("pay on the drawn balance") and C2's price condition for the never-borrowed customer (the KMC is nil for them)
mutation_D: interest accrued daily and debited monthly — the baseline, with a lower rate | reason_considered: the smallest change; a rate cut alone | verdict: rejected | reason_verdict: the debit is the block; a lower rate changes the size of the charge, not its timing; the arrears and returned-debit work the debit creates stays in the form
mutation_E: a rate that varies by flow band (risk-based pricing) | reason_considered: matches the charge to expected loss by band | verdict: rejected | reason_verdict: the limit engine already prices risk through the limit (C1: exposure scaled to flow); a second risk price on the rate re-introduces a per-account decision the C1 form removed, and creates a reference-point block ("why is my rate higher than theirs") that the one-rate form cannot have; the single rate is the price of the pool, which is what the binding gate reads
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: A — one rate, accrued daily, collected from receipts as the first slice of the receipts share; no fee
evolvedBFF: a bank whose credit facility is a standing property of every account with enough flow, proven before it is trusted, believed because the customer checks it against their own past, used without an act, and paid for only from the money that comes in — one rate on the days drawn, taken a slice at a time from each receipt, with no fee and no charging date
synthesisCheck: Square Loans, for the collection mechanism (the charge is taken as a share of each day's card receipts; there is no repayment date) — fused with the arranged overdraft's daily accrual on the drawn balance, which Square does not have (it charges a fixed fee) and which the UK tariff pages price in EAR; the fusion keeps the overdraft's fair pricing of a short draw and Square's freedom from any calendar
```

**Step 4c — decision.** A adopted. The evolved BFF is stated in SR5.

**Amortisation strategy.** *Take the charge from what comes in, never from what is there.* The structural decision is to define the charge as a first slice of the receipts share: the account accrues the day's charge on a separate ledger at close of day (drawn balance × 14.0% ÷ 365) and, on each receipt, WP-3's split clears the accrued charge before it repays the drawn balance. There is no charging date, no fee at acceptance or renewal, and no debit to the account. The pricing committee's whole act is one number, reviewed once a year.

**Payment trigger.** The receipt — money arriving in the account. It is the same trigger as the repayment (WP-3), so the customer sees one split per receipt: charge first, then principal. On an account with no receipts the accrued charge waits; it does not compound and it is not debited. If no receipt arrives for ⚠ 90 days the account is in the exception cell for a different reason (C3's kill band reads no-flow accounts), and the accrued charge is written with the drawn balance.

**Price structure — the band, with arithmetic.** The rate is set inside the price condition (PC-1, C2) from three fixed points.

```
PRICE STRUCTURE — R6 (per £1,000 of average drawn balance, per year)
  ceiling (KMC low corner)         150.00   TAM v2 KMC-OD-STD-TARIFF — Lloyds Bank / Bank of Scotland 15.62% EAR (£156.20), HSBC 14.54% EAR (£145.40), rounded to the band's low corner; fees ⚠ 1–2% of the limit on top, not counted in the 150
  operating bar (floor high × 1.25) 132.84   106.27 × 1.25 — the carrying check's bar
  capital bar                       26.05–43.68   not binding
  the rate                          14.0% simple a year = 140.00   runner's call, T4 with logic (below)
  the band                          ⚠ 135.00–142.50 (13.5–14.25%)   surplus fraction f = 140 ÷ 150 = 0.933; band 0.90–0.95
  room below the ceiling            10.00 (6.7% of the KMC low corner); 16.20 against Lloyds' EAR alone; more against every fee
  room above the operating bar      7.16 (5.4% of the bar)
  per day per £1,000 drawn          £0.384
  a 30-day funded event on £1,000   £11.51 — the worked figure in the representative example
  representative APR (CONC 3.5.5R)  ⚠ 14.0% where the charge is collected as it accrues; up to ⚠ 14.9% on the App 1.2 calculation if the conduct function computes it on a monthly basis (1 + 0.14 ÷ 12)^12 − 1 = 14.93%; no fee, so the APR carries nothing but the rate
```

*Why 14.0% (runner's call, T4 with logic).* The C4 surplus-fraction band is 0.90–1.00 with 0.95 as the convention. The rate must sit below every published EAR on the tariff pages the KMC was built from (14.54% is the lowest, HSBC) so that the acceptance comparison is a lower number for every migrated customer, whatever their bank's tariff; 14.0% does that with no fee, and no published standard tariff is lower once its fee is counted. It sits 5.4% above the operating bar, which is the room the pricing committee has before the 25% margin fails. Threshold: below **13.28%** (132.84) the worst-corner margin falls under 25%; above **14.5%** (145) the rate exceeds HSBC's EAR and the "lower for every migrated customer" claim fails. Convergence: Stage 1 acceptance — a decline share above ⚠ 30% (C2's reading) with "the rate" as the stated reason moves the rate toward the band's low end; a decline share below ⚠ 10% is not read as room to raise it (the middle-way filter; the rate is the price of the pool, not of what the customer will bear).

**Effect on the margin of safety.** At the set price the ceiling the design uses is the price: the margin at the worst corner = (140.00 − 106.27) ÷ 106.27 = **31.7%**; at the band's low end (135) 27.0%; at its top (142.5) 34.1%. The C5 convention (0.95 → 34.1%) is replaced by the set price (0.933 → 31.7%) from this record on. The best corner at the set price is (140.00 − 54.04) ÷ 54.04 = 159.1%; the fit model's KMC-band figure (280 − 54.04) ÷ 54.04 = 418.1% is printed by the script and is not used, because the customer on a £300 tariff pays 140 too.

**Mechanism — elimination, not reduction.** The block was a charge due on the bank's date. After the move there is no date: the charge exists only as a fraction of money that has arrived. Arrears on the charge cannot occur; a returned debit cannot occur; a draw to pay the charge cannot occur. If the customer used the product entirely alone, would the block still occur? No — there is no charging event for them to meet or miss.

**R2 interaction.** PC-1 is resolved from a condition to a price: 140 against a ceiling of 150–300 plus fees. The C2 acceptance reading gains the rate as a stated reason for decline. The C2 saving statement (CP-1) now shows the year's charge as one figure beside the tariff line. Nothing in the KMC changes.

**R3 interaction — flagged, and R3's model updated.** The charge is cash to the bank with each receipt (⚠ 300 receipts a year on an active account, judged from Faster Payments and card settlement counts, T4) instead of monthly. The accrued-charge receivable cycle shortens from ⚠ 30 days to ⚠ 1–3 days; the bank's interest cash is ⚠ 27 days earlier on average. The capital bar is unchanged (it is on the drawn balance, not on accrued interest). The C3 stage reading gains one line: the accrued-charge ledger by days outstanding, read at each stage as a free count of no-receipt accounts. The C3 record is annotated under VA-103; the working-capital model in the AOM v6 carries the receivable cycle as a figure (section 2, money flow).

**R1 consistency.** Nothing in the exposure model changes: the limit is computed daily from the flow (WP-1); the drawn balance is repaid by the receipts share (WP-3); exposure never exceeds the limit. The accrued charge sits on its own ledger and is not exposure; the drawn balance never rises because of the charge.

**At-scale test.** The mechanism is one arithmetic line per account per day (the accrual) and one more split rule in WP-3's per-receipt processing. It runs automated at any volume the account line already runs: ⚠ 228,000 drawn accounts × 365 accruals = ⚠ 83m a year; ⚠ 68m receipts split. No founding-team step, no managed exception, no pricing decision per account.

**R8 signal: yes.** A charge that is only ever taken from receipts, with no fee and no date, is a switching cost by absence: every alternative has a charging date. Flagged for R8 by number.

**Hypothesis (falsifiable).** Among released accounts, (a) the share of customers who query the charge in the first ⚠ 90 days is ⚠ ≤ 1% of drawn accounts; (b) accounts with an accrued charge outstanding more than ⚠ 30 days are ⚠ ≤ 2% of drawn accounts, and every one of them is a no-flow account already in the cell; (c) in the Stage 2 arms, the decline share at acceptance with "the rate" as reason is ⚠ ≤ 10%. **Falsified** if (a) exceeds ⚠ 5% or (c) exceeds ⚠ 30% at ⚠ 10,000 accounts — a price or a presentation the mainstream does not accept — in which case R6 loops back to SR2 with the query and decline reasons as the brief. Read at the first replica's 90-day point; no cost beyond the count.

**Named assumptions (T4 with logic).**

1. *The charge can be collected as a slice of the receipts share.* WP-3 already splits each receipt (C1); a second split rule on the same event is arithmetic. The account line does this today for arranged overdrafts in the reverse direction (a receipt reduces the overdrawn balance on which interest is computed); nothing new is asked of the payment systems.
2. *A charge collected from receipts is not a fee and needs no Part V form.* The agreement remains an overdraft on a current account within CCA 1974 s.74(1)(b) (C5, assumption 3); the charge is interest at a stated rate; CONC 4.7 pre-contract information names the rate and the collection method; the representative example is required once a rate is shown in a financial promotion (CONC 3.5.3R, 3.5.5R) and is drafted once. **What a ruling would settle:** whether the collection-from-receipts term is a "charge" for the CONC App 1.2 total-charge-for-credit calculation (the design position is no — it is the payment mechanism for interest, not a charge) and whether the APR is stated on the daily-collection or the monthly basis (the design states the range and lets the conduct function choose the stricter). Owner: the conduct function; convergence: the signed representative example.
3. *The rate can be one number for the pool.* The pool's expected loss is priced in the floor (20–40); the limit engine, not the rate, scales exposure to risk. A single rate is what every published standard tariff already is (one EAR per product), so the customer's comparison is like for like. If the loss rate by flow band were to differ by more than ⚠ 2 points between bands, the release track would read that at Stage 2 and the limit rule (not the rate) would change (C3's overlay).
4. *The receipts count.* ⚠ 300 receipts a year on an active drawn account (⚠ 68m at scale) — judged from UK Finance's payment counts for SMEs (Faster Payments, card settlement, Bacs); the figure sets only the split's frequency, not any cost line above ⚠ 0.01. Threshold: none in the floor; below ⚠ 50 receipts a year the charge waits longer and the no-receipt line (assumption 2 of the hypothesis) reads it.

**Credibility mechanism (VA-81).** Receiver: the business owner, at acceptance and at the first funded event. Proposition: "14.0% a year on what you have drawn, for the days you have drawn it; no fee; taken from what comes in, never from what is there." Instrument in use today: the representative example the FCA requires on every credit promotion — the customer has seen the form on every tariff page — and the account's own receipt lines, each showing the split. Public-record supplier: the account statement (PSR 2017 regs. 53–56) shows each collection as a line; the CONC 3.5.5R example is a fixed form.

**Existence test (VA-92) and affordability screen (VA-164) — the gateway partner (SR4b).** Who sits where the cash arrives? The bank's own account line: every receipt lands there, and the split is its act. Is there a holder of the "collects from receipts" property outside the bank? No — an internal holder admitted; no acquirer, no card processor, no payment initiator is between the receipt and the account. No partner is named. Maximum payable to any holder from the binding gate and the cap: none is payable; the split's cost is inside WP-3's existing ⚠ £0.01 per receipt. (Square Loans' form needs the acquirer because the receipts are card settlements it controls; a bank that owns the account needs no one — the analogue's partner is the bank's own property.)

**Three tests.** *Primary cause:* the move removes the charging date, which is the cause — not the size of the charge. *Entry point:* the receipt, the same event WP-3 already acts on; and the acceptance screen, where the representative example sits beside the customer's own tariff. *Incumbent:* an incumbent's ledger debits interest monthly to the account; collecting from receipts requires the receipts share (WP-3, C1), which the incumbent's overdraft does not have. The test is passed on the cumulative form (*runner's call*; the same reading as at R5 — recorded again for WS1).

**Property-holder test (VA-71).** Properties in the strategy: *accrues* — holder: the account line (the ledger); *collects* — holder: the account line (WP-3's split); *sets the rate* — holder: the pricing committee; *drafts the representative example and signs the APR basis* — holder: the conduct function; *reads the no-receipt line* — holder: model risk (the release track). Each has a row on a track in the CTM v6.

---

## SR5 — Business form factor (C1–C6)

**The evolved BFF.** A bank whose credit facility is a standing property of every account with enough flow (C1), priced below the tariff the customer pays today (C2), released in stages against a kill band with the exposure model proven before it is trusted (C3), believed because the customer checks the limit against their own past shortfalls (C4), used without an act because a payment that exceeds the balance is met from the limit under a term accepted once (C5), and paid for only from the money that comes in — one rate on the days drawn, taken a slice at a time from each receipt, with no fee and no charging date (C6).

**Components at C6.** WP-1, WP-2 (amended C5), WP-3 (amended C6 — the split takes the accrued charge first), WP-4, WP-5, CP-1 (amended C2, C4, C6 — the year's charge as one figure), CP-2, PC-1 (resolved C6 — the charge: 14.0% simple a year on the daily drawn balance, collected from receipts; the representative example). No component removed.

**What the customer now has.** One available figure (C5), one history (C4), one rate, one line per receipt. No application, no draw, no charging date, no fee, no renewal.

---

## Considered / not chosen (VA-4)

- **A fee-only price (Square Loans' form)** — rejected at the mutation gate (B): the short draw pays too much.
- **A subscription for the limit** — rejected (C): a calendar payment on accounts that never draw.
- **Risk-based rates by flow band** — rejected (E): a second risk price and a reference-point block.
- **A lower rate with the debit kept** — rejected (D): the debit is the block.
- **Compounding the accrued charge into the drawn balance** — not chosen: it would make the charge exposure, raise the capital bar on interest, and mean interest on interest for the no-receipt account; the separate ledger costs nothing more.
- **A rate tied to Bank Rate (variable)** — not chosen at C6: the funding line in the floor (15–30) moves with Bank Rate, so a fixed 14.0% carries rate risk to the bank; the pricing committee's yearly review is the design's answer, and the C2 saving statement shows the year's figure either way. Flagged as a carried question for the pricing committee, not a mutation: it changes the number, not the structure.
- **Charging on the limit rather than the drawn balance** — rejected at C1 (the exposure model) and again here: the never-borrowed customer's KMC is nil.

---

## Synthesis check (VA-1)

Square Loans (repayment as a fixed share of each day's card sales, no repayment date) supplies the collection mechanism. The arranged overdraft as the UK tariff pages present it (an EAR on the daily drawn balance) supplies the accrual. Neither has the other's property: Square charges a fixed fee, so the short draw overpays; the overdraft debits monthly, so the charge can itself be a shortfall. The fusion is the charge accruing as an overdraft does and being collected as Square does. The limit of the analogue: Square's receipts are card settlements it controls through its acquiring; the bank controls the whole account, so the mechanism reaches every receipt, not only cards. That is why no gateway partner is needed (SR4b).

---

## VA-106 synergy line

Does the one move also serve an earlier requirement, with a mechanism? Five candidates:

- **R5 (use) — yes.** A charge that is never debited cannot be the shortfall that default funding meets; the "draw to pay for a draw" case does not exist. Mechanism: no debit event.
- **R2 (value realisation) — yes.** PC-1 is resolved to a number the customer reads once at acceptance (the representative example) and once a year (CP-1). Mechanism: the price is the comparison the KMC asked for, made visible.
- **R4 (conviction) — yes, weakly.** A per-receipt line ("charge £0.42; repaid £48.60") is a running proof that the limit costs what was said. Mechanism: the statement line.
- **R1 (design) — yes.** WP-3 gains a second split rule and nothing else; the exposure model is untouched. Mechanism: the same event.
- **R3 (scale) — yes.** The accrued-charge receivable cycle falls from ⚠ 30 to ⚠ 1–3 days; no arrears work at any stage. Mechanism: collection from receipts only.

R7 and R8 by number only (VA-80).

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per £1,000 of average drawn balance a year unless stated; every ⚠ is T4.

| Actor | Behaviour needed | How often | What it gains | What it costs | Best alternative and its surplus | Arithmetic (VA-157) | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|
| The business owner (the customer) — migrated | accepts a price of 14.0% with no fee in place of the tariff; reads one line per receipt | once; then nothing per event | the tariff avoided: ⚠ 150–300 in interest plus ⚠ 10–20 in fees per £1,000 drawn a year; no charging date, so no debit-caused shortfall (⚠ £10–35 per avoided unpaid item) | the charge: 140 (band 135–142.5) | keep the tariff: surplus nil (it is the outflow the KMC measures); personal money in when to hand: surplus ⚠ £5–20 per event (C5) | central: gain (225 + 15) £240 − cost £140 − alternative's surplus £0 = **£100** · pessimistic: gain (150 + 10) £160 − cost £142.5 − alternative's surplus £10 = **£7.5** | **PASS** (pessimistic > 0) — marginal for the customer on the cheapest tariff with personal money to hand; the rate band's low end (135) is the design's answer for that customer |
| The business owner — never-borrowed | leaves the term on at a price of £0.38 a day per £1,000 drawn | per funded event, nothing to do | per event: the unpaid-item fee avoided ⚠ £10–35 and the late-payment cost avoided ⚠ £20–100 (C5) | ⚠ £1.5–8 per event (10–20 days at £0.384) | personal money in: ⚠ £7.5 of time plus the money not elsewhere; surplus ⚠ £5–20 when to hand | central: gain £70 − cost £4 − alternative's surplus £10 = **£56** · pessimistic: gain £30 − cost £8 − alternative's surplus £20 = **£2** | **PASS** (as at C5; the price does not move the row) |
| The bank's pricing committee (mode 3) | sets one rate at 14.0% inside the band; reviews it yearly; accepts the tariff and fee income given up | once; yearly | contribution on the drawn book at 140 less the floor: 33.73–85.96 per £1,000; the funded book the tariff never reached (⚠ 5–15% of drawn balances under default funding, C5; the never-borrowed book) | tariff and fee income given up on migrated balances: (tariff − 140) × migrated book; the unpaid-item fees ⚠ £3.6–45m (C5) | keep the tariff on the migrated book and run no line: surplus = the tariff income, at the risk the F1 pool-at-risk reading names (Reading D ⚠ £13–231m) | central: gain £4.5bn × 33.73–85.96 (mid £270m) − cost (225 − 140) × £1.1bn = £94m + fees £20m − alternative's surplus £0 (the pool at risk offsets it) = **+£156m** · pessimistic: gain £3.4bn × 33.73 = £115m − cost (300 − 140) × £1.9bn = £304m + fees £45m − alternative's surplus £0 = **−£234m** | **PROVISIONAL — FAIL at the pessimistic corner at the actor level.** Force: the bank itself (mode 3 — the decision to run the line, C2's price condition) and the pool at risk (C2, Reading D ⚠ £13–231m a year the tariff book loses to attackers if the line is not run). Unmeasured input: overdraft revenue by tariff band and the migrated book's size (both red fields, C2's open item). The pessimistic corner assumes the migrated book is 56% of the drawn book at the top tariff; the central assumes 24% at the mid tariff |
| The bank's conduct function | drafts the representative example; signs the APR basis; signs the CONC 4.7 rate line | once; reviewed yearly | a Payment product on a form the FCA's overdraft determination already covers (no new agreement form) | ⚠ 120–250 hours once = ⚠ £10–20k | a per-product fee schedule (the conventional form) with its own fair-value assessment each year: ⚠ 200–400 hours a year; surplus negative | central: gain £0.03m a year (the fee-schedule review not run) − cost £0.003m a year (amortised) − £0 = **£0.027m** · pessimistic: gain £0.015m − cost £0.004m − £0 = **£0.011m** | **PASS** |
| The account line (Case A) | accrues the charge daily; splits each receipt charge-first | per account per day; per receipt | interest income collected as cash ⚠ 27 days earlier than a monthly debit; no arrears or returned-debit work on the charge | inside computing (the accrual ⚠ 83m lines a year at ⚠ £0.0001 = ⚠ £8k) and inside WP-3's ⚠ £0.01 per receipt (C1) | the monthly debit: surplus = the arrears and returned-debit work it creates, negative | central: gain £2m (interest cash earlier, at the funding rate on £4.5bn × 140 × 27 ÷ 365 × 2%) − cost £0.01m − £0 = **£1.99m** · pessimistic: gain £0.5m − cost £0.02m − £0 = **£0.48m** | **PASS** |
| Model risk (the release track) | reads the no-receipt accrued-charge line at each stage | per stage reading | a free count of no-flow accounts inside the existing reading (C3) | ⚠ 10–20 hours per reading | not reading it: surplus nil | central: gain £0.02m − cost £0.001m − £0 = **£0.019m** · pessimistic: gain £0.005m − cost £0.002m − £0 = **£0.003m** | **PASS** |

**The pricing-committee row, disposed.** The bank gives up tariff income on the migrated book to hold a book the tariff never reached. Whether the trade pays depends on two red fields the bank holds (the migrated book's size and its tariff mix) and on the pool at risk (C2). The design's answer is the stage order (C3): Stage 2 opens only if the funded book's contribution exceeds the tariff given up within ⚠ 24 months — the F1 condition, now stated as the bank's Critical Value Threshold (SR2). The row is not a defect of the price structure; it is the mode-3 decision to run the line, priced. Carried to C7 as the affordability screen's first input (what is left for any partner after the tariff given up) and to R8–R10 by number.

---

## Actor tracks (VA-102)

No new actor this challenge. Rows added at arrival: the account line track — the accrual ledger and the charge-first split (C6); the pricing track — the rate set and the yearly review (PC-1 resolved); the regulator track — CONC 3.5.5R representative example, CONC App 1.2 APR basis; the release track — the no-receipt accrued-charge line; the customer's own row — the rate at acceptance and the line per receipt. No counterparty with an acquiring transition. Decisions stated on each row in the CTM v6.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** PC-1 (the price condition) is resolved to the charge: 14.0% simple a year on the daily drawn balance, no fee, collected from receipts. WP-3 (the receipts share) is amended: the split clears the accrued charge first. CP-1 (the saving statement) shows the year's charge as one figure. No component is removed; no new component is added — the Payment product is PC-1, resolved.

**Earlier requirements this same move also serves (VA-106).** R5, R2, R4, R1, R3 with mechanisms; R7 and R8 by number (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — unchanged with one addition.** WP-3 carries a second split rule (charge first); the exposure model, the rule and the four removed operations are untouched. The C1 record's "collections no longer exists as an operation" is confirmed: a charge only taken from receipts has no arrears to collect. Property holder of "collects the charge" is the account line — a track row | re-verified: the C1 figure is non-gating in mode 3; at-scale FMOS on the selected customer 31.7% at the set price (27.0% / 34.1% at the band's ends) |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — PC-1 resolved; the condition holds by number.** 140 < 150 (the KMC low corner, before fees); the acceptance comparison is a lower number for every migrated customer on a published standard tariff (lowest published EAR 14.54%). The C2 acceptance reading gains "the rate" as a decline reason. The KMC is untouched. The C2 open item — overdraft revenue by tariff band — is now the pricing committee's unmeasured input (VA-127) | re-verified: FMOS 31.7% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — one model line updated, no check failed.** The working-capital timing changes: interest cash arrives with each receipt (⚠ 1–3 days) instead of monthly (⚠ 30 days); the capital bar is unchanged (on the drawn balance). The stage reading gains one free count (no-receipt accrued-charge accounts). The C3 record is annotated, not overwritten; the AOM v6 money flow carries the receivable cycle. Stage 1 margin at the set price 4.8% (1.0% at the band's low end; 6.7% at its top) | re-verified: Stage 1 margin 4.8% at the set price |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — unchanged, strengthened on one line.** The per-receipt line is a second running proof (VA-106); the placement (CP-2) is untouched. The restated conviction measure (C5) is unchanged | re-verified: FMOS 31.7%; cap line ⚠ 0.05–0.27 carried |
| R5 (C5 record v1.1) | use routine; routine disruption; Madrian and Shea; default funding; switch-off and reversal; the loss gap; CONC 5.2A timing | **re-verified — one gate line restated at the set price, no check failed.** At 140 the loss line gives L ≤ 4.57% for the 25% margin (was 4.8% at the 0.95 convention); the assumed high corner is 4.0%, so the surplus is 0.57 points; the default-funded gap (C5, gate 3) may consume ⚠ 0.3–0.5 of it — inside the surplus at the set price, outside it at the band's low end (4.17%). The C5 fallback (opt-in by flow band at a ⚠ 1-point gap) is the design's answer; the fee foregone (⚠ £3.6–45m) is now inside the pricing-committee row by number. The "draw to pay for a draw" case is removed (VA-106) | re-verified: FMOS 31.7%; loss gate 4.57% |

No FAILED row. Function-gate re-run: NOT YET — C7's.

---

## Financial check — the floor on four layers, the ceiling as a price and the cap

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1, WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, CP-1 (amended C2, C4, C6), CP-2, PC-1 (resolved C6).

**What R6 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v6 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| accrue the day's charge on the drawn balance; hold it on the accrued-charge ledger | per account per day, automated | e.charge_accrual on q.drawn_accounts | 228,000 × 365 = 83m | ⚠ £0.0001 (one ledger line inside the account line's daily batch) | ⚠ £8k | 0.00 |
| split each receipt charge-first, then principal (WP-3's rule, one more line) | per receipt, automated | e.charge_collection on e.receipt (WP-3) | ⚠ 68m | inside WP-3's ⚠ £0.01 per receipt (C1) — no new cost | £0 | 0.00 |
| set the rate; review it yearly against the funding line and the loss reading | HQ, yearly | e.rate_review | 1 | ⚠ 40–80 hours inside the pricing committee's existing sittings | inside RC | 0.00 |
| draft the representative example and the CONC 4.7 rate line; sign the APR basis | HQ, once | e.representative_example | 1 | ⚠ 120–250 h = ⚠ £10–20k, once, amortised over five years | ⚠ £2–4k | 0.00 |
| explain the charge or a receipt split to a customer who asks | cell | e.charge_query on q.replica_accounts | ⚠ 0.2–0.5% of drawn accounts a year = 200–500 per cell | 0.25 h | ⚠ 50–125 h per cell — inside the ⚠ 0–425 h of headroom booked at C5; no handler added | 0.00–0.01 |
| read the no-receipt accrued-charge line at each stage reading | HQ, per reading | e.stage_reading (C3) | 3 readings | ⚠ 10–20 h inside the existing reading | inside SC | 0.00 |
| **R6 total** | | | | **⚠ £0.01–0.04m** | **⚠ 0.00–0.01** |

*Runner's call on the query rate.* A charge that appears as a line on each receipt is more visible than a monthly debit and will draw some questions in the first months; ⚠ 0.2–0.5% of drawn accounts a year is judged from the C2 saving-query and C5 funding-query rates. Threshold: above ⚠ 1.5% the cell's headroom is used up and a handler is added (R6 line rises to ⚠ 0.05). Convergence: the first replica's six months.

**The four-layer floor at C6 (AOM v6 section 6).**

```
PVC  40.02–83.23   funding 15–30 · expected loss 20–40 · computing and payments 2.02–5.10 (C6: +0.00–0.01, the accrual ledger) · exceptions and write-off 3.00–8.13 (C6: +0.00, charge queries inside the C5 headroom)
RC    2.02–5.04    unchanged — the rate review sits in the pricing committee's existing sittings
SC    0–1          unchanged — the representative example (⚠ £10–20k once) sits inside the band
IC   12–17         unchanged — the accrued charge is not exposure
FLOOR 54.04–106.27  (C5: 54.04–106.26; C4: 54.03–106.20; C3: 54–106)
```

**Carrying check (challenge skill section 8).**

```
CARRYING CHECK — R6
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v2 KMC-OD-STD-TARIFF)
  the price (C6)                        140.00 — band ⚠ 135.00–142.50
  floor                                  54.04–106.27
  operating bar = floor × 1.25           67.55–132.84
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  price against the operating bar        140.00 − 132.84 = 7.16 at the set price · 2.16 at the band's low end · 9.66 at its top
  carries                                true at every point of the band
  FMOS worst corner (price − floor high) ÷ floor high
                                         31.7% at 140 · 27.0% at 135 · 34.1% at 142.5
  FMOS best corner (price − floor low) ÷ floor low
                                         159.1% at 140 (the fit model's KMC-band figure, 418.1%, is not used)
  conventional additions used (RD-030)   R6 nil in the counterfactual; added ⚠ 0.00–0.01; cumulative ⚠ 0.05–0.27; remaining ⚠ 7.73 at the high corner
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C6.yaml`).** By hand: **31.7% at the worst corner at the set price; 27.0% at the band's low end; 34.1% at its top; 159.1% at the best corner. PASS on the 25% gate at every point of the band.** The fall from 34.1% (C5, at the 0.95 convention) to 31.7% is the set price (0.933), not a cost: R6 adds ⚠ 0.01 to the floor's high corner. `fit_margin.py` is run on the at-C6 model with the surplus fraction at 0.933; its output is in the verifier r6.

**Binding gate — by driving (VA-84).** Fourteen gates driven at C6: the thirteen of C5 and (14) the rate itself. Ordered by margin at the set price:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.57%** at the set price (4.17% at the band's low end; 4.77% at its top); at C6 the loss line is 66.27 + 10L, and the bar is the price ÷ 1.25 = 112.00; zero margin at 7.37% (6.87% / 7.62%); assumed ⚠ 2–4%; surplus 0.57 points at the assumed high corner. **First to fail.**
2. the default-funded loss gap (C5, gate 3) — on the same line; ⚠ 0.3–0.5 of the 0.57 points; unmeasured.
3. the price condition's room — 7.16 at the set price, 2.16 at the band's low end.
4. the rate against the lowest published EAR — 14.0% against 14.54% (HSBC): 0.54 points; above 14.5% the "lower for every migrated customer" claim fails.
5. the non-empty history share (gate 12 of C4), unchanged.
6. the switch-off share (C5), the funding-query rate (C5), the charge-query rate (new, ⚠ 0.2–0.5%; threshold 1.5%) — use gates, no floor effect.
7–14. carried from C5 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, including default-funded draws
  threshold:    4.57% at the set price (4.17% at the band's low end · 4.77% at its top) — the 25% margin fails above it at the worst corner; zero margin at 7.37%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.57 points at the assumed high corner; the default-funded gap (C5) may consume ⚠ 0.3–0.5 of it
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the default term switches to opt-in by flow band at a ⚠ 1-point gap (C5); the rate does not move on the loss reading — the limit rule does (C3's overlay)
  reads at:     the Stage 1 12-month reading (the pool); the first replica's 12-month reading (the gap)
```

**Independence (VA-97).** NOT shown — the margin is a transform of the loss gate. Free counts named: the switch-off share, the funding-query rate (C5), the charge-query rate and the no-receipt accrued-charge count (new) — counts of acts, not of losses; all unmeasured.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts). At Stage 1 (⚠ £0.4–1.9bn): RC 3.84–32.38; floor 55.86–133.61; worst-corner margin at the set price (140 − 133.61) ÷ 133.61 = **4.8%**; 1.0% at the band's low end; 6.7% at its top. Stage 1 does not carry the 25% margin at any point of the band — as at C3, C4 and C5; the SC layer and the stage order are the design's answer, and the F1 condition (Stage 2 within ⚠ 24 months) is what makes it tolerable.

**Working capital timing.** Changed, and stated. The charge is cash with each receipt; the accrued-charge receivable cycle is ⚠ 1–3 days against ⚠ 30 under a monthly debit; the bank's interest cash on a £4.5bn book at 140 arrives ⚠ 27 days earlier on average, worth ⚠ £0.9–2m a year at the funding line's 1.5–3.0%. The runner does not take the credit in the floor; it is stated in the account line's VA-127 row.

**The fee foregone (C5's input to C6, by number).** The unpaid-item fees given up under default funding (⚠ £3.6–45m a year, C5) against the contribution on the default-funded book at the set price: ⚠ 5–15% of £3.4–5.7bn = ⚠ £0.17–0.86bn × (140 − 106.27 to 140 − 54.04) = ⚠ £5.7–74m a year. The central case covers the fee foregone; the pessimistic corner (£5.7m against £45m) does not. The number sits inside the pricing-committee row (VA-127) and is not recovered by the rate: raising the rate to recover a fee the FCA's direction of travel (PS19/16, PRIN 2A.4) is removing would price the line above the tariff for the customer it was designed for. *Runner's call.*

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Interim product value lifecycle drawn for each party — the customer (six stages) and the bank's account line (four stages) — with the inline diagram, the stage types, the value curve, the deferred-cost segments and the Critical Value Threshold line ✓ (SR1).
- Critical Value Threshold per party — trigger event, comparison, why it tips — for the migrated customer, the never-borrowed customer and the account line ✓ (SR2).
- Buy block type named (timing mismatch; lumpiness secondary) and tested against price sensitivity ✓ (SR2, SR3).
- ToC — class of problem named ✓; theory named with researcher, year and paper ✓ (Prelec and Loewenstein 1998); current state and desired state as states ✓.
- Theory stress test run; the contrast theory named (Gourville and Soman 1998); fragile-findings check (Soman 2001) ✓.
- Strategy — exactly one structural move ✓; payment trigger named (the receipt) ✓; price structure as a band with arithmetic, three fixed points, the threshold and the convergence ✓; representative example ✓; effect on the margin stated ✓; R2 interaction ✓; R3 interaction flagged and R3's model updated ✓; R1 consistency ✓; at-scale test with the volume named ✓; R8 signal ✓; hypothesis with falsification and four named assumptions ✓.
- Mutation gate emitted before the strategy; five genuine mutations (A–E); justification mode false ✓.
- Gateway partner (SR4b): who sits where the cash arrives — the account line; internal holder admitted ✓.
- Three tests: primary cause, entry point, incumbent — passed, with the incumbent test's reading recorded as a runner's call ✓.
- Credibility mechanism (VA-81) ✓. Existence test and affordability screen (VA-92, VA-164) ✓ — nothing payable; no partner.
- Property-holder test (VA-71) ✓ — five holders, each on a track.
- Pointing test ✓ — the move removes the charging date, not the size of the charge.
- Launch constraints absent from SR1–SR5 (VA-23) ✓.
- Limit of the analogue stated ✓.
- Completeness contract (VA-73) ✓. No forward references (VA-80) ✓ — R7, R8 by number only.
- VA-106 line, five candidates ✓. VA-103 table, five rows, one model line updated at R3, one gate line restated at R5 ✓. VA-127 table, two arithmetic lines per row; one PROVISIONAL row with the force named; one marginal PASS ✓. VA-82 classified ✓.
- Conventional cost line named (nil) and the block's cost to the bank named (arrears and returned debits, the tariff's fee) ✓ (F2) — the cap line printed.
- Binding gate by driving ✓ (14 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162).
- Verdict order (VA-95) ✓ — `check_verdict_order.py` on the verdict record with R6 added. Loop-gate branch (VA-153): no FAIL on the design. Loop-backs (VA-151): 0.
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r6-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v6 and AOM v6 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v6 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at C6 (unchanged from C5; the ⚠ 50–125 charge-query hours sit inside the ⚠ 0–425 hours of headroom booked at C5), covering ⚠ 100,000 drawn accounts and ⚠ 333,000 accounts with a limit per cell. Handlers: **14 per cell (band 13–15)**, unchanged. At scale: 2.28 cells, ⚠ 46,500 hours, ⚠ 32 handlers + 3 leads + a trainer = 36 people in cells. Every calculation in this record uses 20,400 and 14. Role support: no new role; the charge-query script is a handbook page for the existing handler (AOM v6 section 4) ✓. Unit sizing: the cell's fixed cost ⚠ £0.9–1.18m ✓. Component carriage: every C6 transition in the CTM v6 is carried by WP-3 (amended), PC-1 (resolved) or CP-1 ✓. **PROVISIONAL** (one build item).

**Financial check.** Margin 31.7% at the worst corner at the set price (27.0% / 34.1% at the band's ends), 159.1% best, by hand; PASS at every point; `fit_margin.py` run on the at-C6 model (verifier r6). Carrying check: carries; room 7.16 at the set price, 2.16 at the band's low end. Binding gate: the loss rate, unmeasured, threshold 4.57% at the set price; the C5 gap on the same line. Conventional additions used: ⚠ 0.05–0.27 of ⚠ £8. Independence NOT shown; four free counts named. **PROVISIONAL.**

**What was decided about each check that did not pass.**
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- The pricing-committee actor row — FAIL at the pessimistic corner at the actor level, **disposed as the mode-3 decision to run the line, priced**; force: the pool at risk (C2); **unmeasured inputs**: the migrated book's size and tariff mix (red fields); owner: the pricing committee; convergence: the bank's overdraft revenue by tariff band and the Stage 2 opening reading.
- The migrated customer's row — PASS at £7.5 pessimistic: **marginal**; the band's low end is the design's answer for the customer on the cheapest tariff; no force needed.
- The rate (14.0%; band 13.5–14.25%) — **a runner's call, T4 with logic**; owner: the pricing committee; convergence: Stage 1 acceptance with "the rate" as a decline reason.
- The representative example and the APR basis (14.0–14.9%) — **build item**; owner: the conduct function; convergence: the signed example; what a ruling would settle is named at SR4 assumption (2).
- The accrual ledger and the charge-first split — **build items**; owner: the account line (Case A); convergence: the Stage 1 release collects a charge from a receipt.
- The hypothesis (charge queries ⚠ ≤ 1%; no-receipt accrued charge ⚠ ≤ 2%; rate-reason declines ⚠ ≤ 10%) — **unmeasured inputs**; owner: model risk and the cell lead; convergence: the first replica's 90 days.
- The receipts count (⚠ 300 a year per active account) — **unmeasured input** for the bank's own base; owner: the account line; convergence: the bank's receipt counts (a red field).
- The fixed-against-variable rate question — **carried question** for the pricing committee; not a structural item; convergence: the first yearly review.
- The fee foregone (⚠ £3.6–45m) against the default-funded contribution (⚠ £5.7–74m) — **unmeasured input** inside the pricing-committee row; owner: the pricing committee.
- CONC 3.5.5R and App 1.2 — **standing constraint**, designed for.
- C5's and earlier carried items — carried unchanged, except the R3 working-capital line and the R5 loss-gate line, restated under VA-103.

```
GATE VERDICT — on the cumulative architecture C1 to C6
  logical limb:      PASS            checks failed: 0
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     FMOS 31.7% worst corner at the set price (27.0% at the band's low end / 34.1% at its top) / 159.1% best (by hand; `fit_margin.py` output in verifier r6) · binding gate the loss rate on the pool: surplus 0.57 points at the assumed high corner, unmeasured; the default-funded gap may consume 0.3–0.5 of it · conventional additions used ⚠ 0.05–0.27 of ⚠ £8
  price:             14.0% simple a year on the daily drawn balance = £140 per £1,000 drawn (band ⚠ 135–142.5); no fee; collected from receipts as the first slice of the receipts share; representative APR ⚠ 14.0–14.9%
  decisions:         21 unmeasured inputs (17 carried), 8 build items (5 carried), 1 standing-constraint set (1 new row), 2 structural limits (carried), 1 carried question (fixed against variable); 1 actor-level FAIL at the pessimistic corner disposed as the mode-3 decision with two unmeasured inputs; 1 marginal PASS noted
  capacity figure:   20,400 exception hours per cell a year, 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15) at 1,400–1,600 productive hours — used throughout   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; four free counts named and unmeasured   VA-97
  gates driven:      14; first to fail on evidence: the loss rate, margin 0.57 points at the set price; second: the default-funded gap on the same line; third: the price condition's room (7.16)   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r6-2026-09-21.md   VA-90
  inherited:         R5, R4, R3, R2, R1 PROVISIONAL — R6 cannot exceed them; F1 closed PROVISIONAL with one condition   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design; the actor-level FAIL is disposed with owner and convergence; the CTM and AOM model files are build items   VA-153
  launch constraints:none inside SR1–SR5 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn; at the Stage 1 count the worst-corner margin is 4.8% at the set price, 1.0% at the band's low end   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; the price sets where on that line the gate sits   VA-160
  VERDICT:           PROVISIONAL
```

**R6 failure test.** Would R6 have failed? Three conditions. First, the price structure carries a calendar event: it does not — no fee, no debit, no renewal; the mutations that keep one (C, D) are named and rejected. Second, the price fails the condition or the bar: it does not — 140 sits 10 below the KMC low corner and 7.16 above the operating bar, and the whole band ⚠ 135–142.5 carries. Third, the mainstream does not accept the rate: unmeasured; if the decline share with "the rate" as reason exceeds ⚠ 30% at ⚠ 10,000 accounts, R6 loops back to SR2. None fails today. The nearest is the second at the band's low end (2.16 of room), and the pricing committee holds the number.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the gateway and any partner where the cash arrives outside the bank (none found at C6 — the affordability screen's first input is the tariff given up); the partner journey — C7
  - the switching cost by absence (no charging date anywhere else); the per-receipt line as retained data — R8
  - the at-scale price hold under the fixed rate; the yearly review; the funding line's movement with Bank Rate — R9, R10
- **Unmeasured inputs (new at C6):** the rate's acceptance (decline share with "the rate" as reason); the charge-query rate; the no-receipt accrued-charge count; the receipts count per active account; the migrated book's size and tariff mix; the fee foregone against the default-funded contribution. **Carried from C1–C5 (17):** unchanged.
- **Build items (new at C6):** the accrual ledger; the charge-first split in WP-3; the representative example and the APR basis. **Carried (5):** the CTM and AOM model files; default funding's authorisation, notice and record; the term and the CONC 4.7 information; the limit-history placement; the release order's instrumentation.
- **Standing constraints:** CONC 3.5.3R / 3.5.5R (the representative example once a rate is shown); CONC App 1.2 (the APR basis); CCA s.74(1)(b) and CONC 4.7 (C5); PRIN 2A.4; PS19/16 — designed for.
- **Structural limits (carried):** the C1 limit rule's exposure model; the Stage 1 margin below 25% at every point of the band (the stage order is the answer).
- **Carried question:** a fixed rate against a Bank Rate–linked rate — the pricing committee's, at the first yearly review.
- **TAM narrowing by a named block (C6 — "price").** SC-OD-BELOW-BAND (KMC-LOAN-RATE £75–90) and SC-LOAN-USER (KMC below the floor's high corner) are excluded: 14.0% exceeds their KMC. The surviving volume basis is SEG-OD-STD-TARIFF alone (40–70% of the selected class); the TAM data object is versioned at C7 with this block recorded and the checking script's output. Nothing else in the TAM moves.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Interim product value lifecycle — per party, inline diagram | PASS — two parties; six and four stages; value curve; CVT line | SR1 |
| Critical Value Threshold — per party, trigger, comparison, why it tips | PASS — three thresholds | SR2 |
| Buy block type — named and correct | PASS — timing mismatch (lumpiness secondary); not price sensitivity | SR2, SR3 |
| ToC — class of problem, theory, current and desired state | PASS — Prelec and Loewenstein 1998 | SR3 block |
| Theory stress test and fragile-findings check | PASS — Gourville and Soman 1998; Soman 2001 | SR3 |
| Mutation gate — ≥ 2 genuine mutations, differsFromBaseline, justification mode | PASS — five; true; false | SR4 |
| Exactly one structural move | PASS — the charge as the first slice of the receipts share | SR4 |
| Payment trigger named | PASS — the receipt | SR4 |
| Price structure — band with arithmetic; below tariff; above floor; effect on FMOS | PASS — 140 (135–142.5); 150 ceiling; 132.84 bar; 31.7% | SR4 |
| Receipts share is the repayment mechanism, not the price | PASS — the rate is the price; the share is how it is paid | SR4 |
| Representative example (CONC 3.5.5R) | PASS — drafted; APR band 14.0–14.9% | SR4 |
| R2 interaction — PC-1 resolved | PASS | SR4, VA-103 |
| R3 interaction — flagged; R3's model updated | PASS — receivable cycle ⚠ 1–3 days; AOM v6 money flow | SR4, VA-103 |
| Incumbent test | PASS on the cumulative form — runner's call recorded | SR4 |
| Gateway partner (SR4b) — who sits where the cash arrives | PASS — the account line; internal | SR4 |
| Existence test and affordability screen (VA-92, VA-164) | PASS — nothing payable | SR4 |
| Credibility mechanism (VA-81) | PASS | SR4 |
| Property-holder test (VA-71) | PASS — five holders | SR4 |
| BFF C1–C6 stated | PASS | SR5 |
| Considered and not chosen (VA-4) | PASS — seven | section |
| Synthesis check (VA-1) | PASS | section |
| VA-106 synergy line | PASS — five candidates with mechanisms | section |
| VA-127 actor table — two VA-157 lines per row | PASS — six rows; one PROVISIONAL with force; one marginal | section |
| VA-102 actor tracks | PASS — no new actor | section |
| VA-103 BFF delta and re-verification | PASS — five rows; no FAILED row | section |
| ABC floor (RD-031) — every line resolves to a driver | PASS — six lines | financial |
| Four-layer floor recomputed | PASS — 54.04–106.27 | financial |
| Carrying check | PASS — carries at every point of the band | financial |
| FMOS — by hand and by `fit_margin.py` | PASS — 31.7% worst at the set price; script output in r6 | financial, r6 |
| Cap line (RD-030) | PASS — cumulative ⚠ 0.05–0.27 of £8 | financial |
| Binding gate by driving (VA-84) | PASS — 14 gates; the loss rate first | financial |
| Independence (VA-97) | NOT shown — declared; four free counts | financial |
| Spread count (VA-162) | PASS — Stage 1 4.8% at the set price | financial |
| Shared input (VA-160) | PASS — the loss rate | financial |
| Three-limb close (VA-89) | PASS / PROVISIONAL / PROVISIONAL | close |
| Capacity figure (VA-91) | PASS — 20,400 h; 14 handlers | close |
| Verdict order (VA-95) | PASS — `check_verdict_order.py` IN ORDER on the verdict record with R6 | close, r6 |
| Loop-gate branch (VA-153); loop-backs (VA-151) | PASS — no FAIL on the design; 0 | close |
| Launch constraints (VA-23) | PASS — none in SR1–SR5 | close |
| No forward references (VA-80) | PASS — R7, R8, R9, R10 by number only | throughout |
| Carried items classified (VA-82) | PASS | section |
| House-style checker | run on save; findings fixed; exit 0 | — |
| CTM and AOM model files | FAIL — build item carried | close |

---

## Quality check

| Test | Result |
|---|---|
| Is the lifecycle diagram inline, for each party? | **Yes** — two diagrams, stage grid and value curve, with the threshold cards |
| Is the buy block type correct? | **Yes** — timing mismatch; the charge's date, not its size; price sensitivity ruled out by C2's reading |
| Is the strategy architectural, not a payment-plan feature? | **Yes** — the charge is a slice of the receipts share; there is no charging event to plan |
| Could an incumbent adopt it? | **Not without WP-3** — a monthly-debit ledger has no receipts share to take the charge from; on the cumulative form, no |
| Is the R3 interaction flagged and R3's model updated? | **Yes** — receivable cycle ⚠ 1–3 days; AOM v6 money flow; C3 annotated under VA-103 |
| Is the price a band with arithmetic, inside the condition and above the bar? | **Yes** — 140 (135–142.5); 150 ceiling; 132.84 bar |
| Confidence in the verdict | **Medium.** The structure is certain (it is arithmetic on an event the form already has); the number is a runner's call inside a band whose ends are both published (the tariff pages) and computed (the bar). What would raise it: the bank's overdraft revenue by tariff band (the pricing-committee row's two red fields) and the Stage 1 acceptance reading with "the rate" as a decline reason |

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15, C5 G1–G10)

| # | Source | Used for |
|---|---|---|
| H1 | Prelec, D. and Loewenstein, G. (1998), "The Red and the Black: Mental Accounting of Savings and Debt", *Marketing Science* 17(1) | the theory: coupling of payment and benefit; the pain of a decoupled instalment |
| H2 | Gourville, J. and Soman, D. (1998), "Payment Depreciation: The Behavioral Effects of Temporally Separating Payments from Consumption", *Journal of Consumer Research* 25(2) | the contrast theory; why a fee in advance is rejected here |
| H3 | Soman, D. (2001), "Effects of Payment Mechanism on Spending Behavior: The Role of Rehearsal and Immediacy of Payments", *Journal of Consumer Research* 27(4) | payment transparency; the fragile-findings check |
| H4 | FCA Handbook CONC 3.5.3R, 3.5.5R; CONC App 1.2 | the representative example; the APR calculation basis |
| H5 | FCA PS19/16, "High-cost credit review: overdrafts policy statement" (2019) | the direction of travel on overdraft charging; unarranged and arranged pricing |
| H6 | FCA Handbook PRIN 2A.4 (Consumer Duty — price and value) | the fair-value test on a short draw (mutation B) and on the never-drawn account (mutation C) |
| H7 | Consumer Credit Act 1974 s.74(1)(b), s.74(3); the FCA's overdraft determination; CONC 4.7 | the agreement form; pre-contract information for the rate |
| H8 | Published business overdraft tariff pages — Lloyds Bank / Bank of Scotland (15.62% EAR), HSBC (14.54% EAR), arrangement fees (as read into TAM v2, C2) | the ceiling's low corner; the "lower for every migrated customer" threshold at 14.5% |
| H9 | Square Loans (Square UK), published terms — repayment as a fixed share of daily card sales; a fixed fee | the collection mechanism (adopted) and the fee form (rejected, mutation B) |
| H10 | UK Finance, *UK Payment Markets 2025* — business payment counts by method | the receipts count per active account (assumption 4) |
| H11 | Payment Services Regulations 2017 regs. 53–56 | the statement line as public record |
| H12 | Thaler, R. (1985), "Mental Accounting and Consumer Choice", *Marketing Science* 4(3) | the mental-accounting frame behind H1 |

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | First record. R6 designed on the C5 form; verdict PROVISIONAL; PC-1 resolved to the charge (14.0% simple a year on the daily drawn balance, no fee, collected from receipts as the first slice of the receipts share); WP-3 amended; CP-1 amended; conventional R6 line nil; the R3 working-capital line and the R5 loss-gate line restated under VA-103; TAM narrowing by the named block "price" recorded for the C7 version. House-style checker run on save; findings fixed. |
