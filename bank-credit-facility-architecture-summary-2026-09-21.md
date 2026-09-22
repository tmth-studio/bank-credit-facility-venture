# A business bank's credit facility line — the architecture in two pages · 21 September 2026

**For:** Tom. **From:** the runner (Path C, mode 3 — "just show me"). **Status:** all ten requirements designed; Function 3 closed PROVISIONAL at C10; object-after to 23 September 2026 17:00. The bank is not named and every figure only the bank holds is a red field `⚠`. **Where the detail is:** the ten challenge records, the status file (`sme-fintech-models/bank-credit-facility-f1-status.md`), the financial simulation and the C10 consistency audit and verification, all dated 21 September 2026.

## The one idea

A UK SME bank's overdraft and small term loan are sold as products. A customer applies, a person decides, the bank takes security, the limit is reviewed yearly and collected by a desk when it goes wrong. Most of what the bank pays for is that machinery, and most of it exists because the bank does not trust the number it already has — the customer's own flow through the account it holds. The venture makes the credit line a property of the account instead of a product: every eligible account gets a standing limit set by a rule on its own receipts, funded by default when a payment would take the balance below zero, repaid as a slice of the receipts that follow, priced as a rate on the drawn balance and nothing else. No application, no security, no review, no collections desk, no fee. The customer sees a number in the account that is already money. Everything below is the ten moves that make that hold at scale, against rivals, and against the bank's own treasury.

## The ten moves, one line each

1. **R1 — the cost floor.** Replace the per-facility machinery (assessment, security, review, collections) with a rule on the account's own flow; the floor per £1,000 drawn a year falls to ⚠ 54–106 against a roadmap-form floor of ⚠ 57–133.
2. **R2 — the customer's number.** The customer who gains most is the one on the standard overdraft tariff paying ⚠ 150–300 per £1,000 drawn a year; that is the ceiling the price must clear.
3. **R3 — releasing without a loss history.** Release the limit in order of exposure the bank already carries — shadow limits, a back-test on its own history, migrated accounts first, then replicas against pre-registered loss bands — so no whole-book overlay is needed.
4. **R4 — believing the number.** The limit is shown as its own verifiable history at the moment of the shortfall, so the customer does not need a person to have decided.
5. **R5 — using it without a routine.** Funding is the default on an accepted term: a payment that would breach the balance draws what it needs; the customer can switch off.
6. **R6 — paying without a bill.** The charge is the first slice of the receipts share at 14.0% simple a year on the daily drawn balance (£140 per £1,000; band ⚠ 135–142.5), no fee, no charging date.
7. **R7 — being where the shortfall is foreseen.** The limit is published as the account's pre-agreed credit line by the public account-information standard, so the customer's own accounting platform shows it; no partner fee.
8. **R8 — the store of value.** The multiple rises on the account's own cleared events (seasoning); the record belongs to the customer and stays with the bank because the bank was there when it was made.
9. **R9 — the lock-out.** The rule's parameters are re-fitted yearly on an outcome ledger — the multiple in force and whether it cleared or was lost — which no consented feed carries and which a rival needs ⚠ 27–54 months to build.
10. **R10 — the supplier hold.** The drawn balances are funded by the same pool's credit balances under a signed term at the measured deposit cost, read daily, capped at ⚠ 10% of the pool; a standby securitisation on the R9 ledger is documented and never issued, so treasury cannot re-price the line to the market.

## The numbers

| Reading | Conservative | Central | Optimistic | Source |
|---|---|---|---|---|
| Floor per £1,000 drawn a year (four layers) | ⚠ 107.47 | ⚠ 81.28 | ⚠ 55.09 | AOM v10; fit model at C10 |
| Price (set at C6; F3 did not reprice) | 140 (band ⚠ 135–142.5) | 140 | 140 | C6 record |
| Margin above the floor at the set price (gate 25%) | **30.3% — PASS** (25.6% at 135) | 72.2% | 154.1% | verifier r10; simulation |
| Cost added by R4–R10 against the ⚠ £8 the counterfactual allows | ⚠ 1.10–1.47 (6.53 remains) | | | verifier r10 cap line |
| Conventional lines removed by R4–R10 | ⚠ 15–63 per £1,000 | | | the seven records |
| Loss rate at which the 25% margin fails | 4.45% (zero margin at 7.25%); the loss band assumed is ⚠ 2–4% | | | C10 record; verifier r10 |
| Deposit cost at which the 25% margin fails | 3.45%; the deposit cost assumed is ⚠ 1.5–3.0% | | | C10 record (corrected the same day from 3.99) |
| At-scale drawn book | ⚠ £3.4bn | ⚠ £4.55bn | ⚠ £5.7bn | TAM v4; simulation |
| Phase II capital gate (≥ 60% at the conservative scenario) | **BORDERLINE — 30.3% against 60%**; passes if the loss rate reads ⚠ 2.0%, or funding 1.5% with loss ⚠ 2.6% | PASS | PASS | simulation §3 |
| Peak venture capital on the path | ⚠ £50m (the replica overlay, month 13, held six months; operating cash positive from month 6) | ⚠ £25m | ⚠ £0.5m | simulation §2 |
| Lending capital at scale (regulatory, not venture) | ⚠ £0.36–0.70bn | | | simulation §1 |
| Months to the at-scale book | 43 | 35 | 27 | simulation §2 |
| Cumulative operating cash at month 60 | ⚠ £1.10bn | ⚠ £1.34bn | ⚠ £1.42bn | simulation §2 |
| Barrier scores (pass ≥ 5) | SCIS 2 · FIS 5 · HRS 5 (with the design commitment) | 4 · 6 · 6 | 6 · 7 · 6 | C8, C9, C10 records |
| Design integrity at F3 (SOUND ≥ 85) | 87.7 SOUND — validation maturity pre-operational | | | verification C10 |

## What the moat is, and is not

It is not a switching cost. The C8 score says so at the conservative corner (2, below the line) and the record prints it rather than raising it: R7 published the limit to every reader, and a published limit is a reconstructible one. What holds is R9 and R10 together. R9 is the outcome column — what the rule's own limits did — which does not move when the customer moves and which no feed carries. R10 is the deposit franchise: a rival without a current-account pool funds at the market, and at the market this design fails its own margin (19.2% at a Bank Rate transfer price, BORDERLINE; 13.4% at SONIA plus 0.6, and 9.8% at SONIA plus 1.0, both FAIL). A bank that has both can run the form; a fintech that has neither cannot copy it at the price. The one real business that shares the whole shape is Square — Square Loans from the sellers' own receipts, since 2021 funded inside Block's own Utah bank beside the sellers' deposits — and it stops where this design goes further: Square is the acquirer, not the account holder, and publishes no cap and no standby route.

## What is unmeasured, and who measures it

Two numbers carry the whole margin and neither has been measured. **The loss rate** on a pool underwritten by flow (⚠ 2–4% assumed): every point of loss moves the floor by 10 per £1,000; at 4.45% the margin is gone at the set price; the C3 trial band's "continue" line of 4.8% is now above that gate and is routed back to the C3 record for re-setting. Stage 0's back-test on the bank's own history measures it first; the twelve-month reading on the first ⚠ 10,000 Stage 1 accounts confirms it. **The deposit cost** under the funding term (⚠ 1.5–3.0% assumed): treasury's transfer-pricing reading at signing, then a year of daily readings. Behind those two: the pool's balances and the cap's use (treasury's balance sheet), the seasoning schedule and the ⚠ 90-day cut (the back-test), the query rates (the first replica's six months), the undrawn commitment per £1 drawn (Stage 1 at twelve months), the standby route's set-up cost (the agents' quotes). Every one has a named holder and a dated event; none needs the venture to ask a customer anything.

## Verdict

**The architecture is complete and coheres.** Ten requirements, one form, no structural contradiction; one earlier number (the trial band) made false by the later floor and sent back to be re-set, not patched; a design-integrity score of 87.7. **It is a venture, not an improvement:** the bank's roadmap makes the decision cheap and leaves the machinery standing; this form removes the machinery. **The margin is real but rests on two unmeasured inputs.** At the conservative corner it passes the design gate (30.3% against 25%) and reads BORDERLINE on the Phase II capital gate (against 60%). That verdict does not change with more design. It changes with one measurement: the loss rate on the bank's own history under this rule. Stage 0 is a back-test on data the bank already holds, costs ⚠ £0.3–0.8m (⚠ £1.3m of cumulative cash by its end, with the engine's first months), needs no customer and no release, and is the next thing to do.

**Object-after:** everything above lapses into the record at 23 September 2026 17:00 unless you object. Nothing in it commits spend, sends anything, or names the bank.
