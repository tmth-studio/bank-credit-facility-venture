# A business bank's credit facility line — challenge ten (R10) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R10 asks which supplier input the venture cannot do without, and what it does if that supplier turns adversarial. The value chain is mapped at scale and ranked by cost × volume: deposit funding is first by a distance — 15–30 per £1,000 on a drawn book of ⚠ £3.4–5.7bn is ⚠ £51–171m a year, more than every other supplier line together. The supplier is the bank's own treasury, which prices funding to every lending book by an internal convention it can change at a sitting; a convention that priced the line at Bank Rate would take the worst-corner margin from 30.3% to 19.2%, and one that priced it at the wholesale rate would take it to 13.4–9.8%. The one move funds the line inside its own pool: the drawn balances of the pool's accounts are funded by the credit balances of the same pool of accounts, the aggregate drawn book is capped at ⚠ 10% of the pool's credit balances so the pool is always a net depositor, and the line pays the pool's measured deposit cost under a signed funding term read daily. Beside it the line keeps one market route — a revolving master trust on the R9 ledger as its data tape, set up before Stage 3 and maintained without issuance — so that no internal price above the market's can be held against it. The floor rises by ⚠ 0.09–0.36 per £1,000 unrounded (the standby route's set-up and upkeep) to 55.09–107.47; the margin at the worst corner is 30.3% at the set price, PASS. The hold-up resistance score is 4 at the conservative corner without the design commitment and 5 with it; 6 at central. The position-holding re-test is printed unsoftened: the margin depends on the funding line holding at the pool's deposit cost, and the market route holds the venture's existence, not its margin. Function 3 closes PROVISIONAL at this record; the Phase II capital gate reads BORDERLINE at the conservative scenario (30.3% against 60%), and what tightens it is the loss rate.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c9-v1-2026-09-21.md` (R9, PROVISIONAL, object-after to 23 September 2026 17:00), `bank-credit-facility-c8-v1-2026-09-21.md` (R8, PROVISIONAL) and the C7 to C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3; F2 closed PROVISIONAL at C7 (audit PASS WITH CONDITIONS; verification 93.1 SOUND). **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F3 rule this record works under (Tom, 16 September 2026).** R8 to R10 make the at-scale price and cost hold. R10 does it by making the largest supplier input replaceable — the test is what the venture does if the supplier turns adversarial, not what a competitor cannot get (R9). Cost-shifting is not architecture: moving a line from one budget to another changes nothing about who can raise its price. The conventional R10 line in the counterfactual (RD-030) is ⚠ 1–3 per £1,000: the bureau data, scoring vendor and aggregator feeds a conventional facility book buys to underwrite and monitor. The form does not carry it — the rule reads the account line and the ledger (C1, C9) and reads a bureau only for the fraud and conduct signal, a line inside computing since C1. Nothing is removed by R10's own move; the removal is booked here by number because the bureau was named as R10's at C9.

**F3 ordering (challenge skill).** Map the value chain and find the key input first; the theory and the strategy follow from it. **VA-23 at Diagnose:** the block tested is the at-scale one — the supplier's power over a ⚠ £3.4–5.7bn book, not over a pilot's.

**Customer of record (VA-154).** The business owner who holds the account (the migrated overdraft user and the never-borrowed customer with enough flow — one customer of record, one payer). The routine positioned in: the rule's own routine on the customer's account — set the limit, fund the event, clear it, record the outcome, re-set the limit. One run. No supplier binds at launch (the shelf check is in SR1).

**Sections in this record.** Defined terms. SR1 to SR3 with the mutation gate. Productizing. Cumulative business form factor (C1–C10) with the evolution test. Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C9 and the function-gate re-run line. Financial check with the position-holding table and the hold-up resistance score. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

- **Interim value chain** — every input the form buys or draws on at scale, from a supplier inside or outside the bank, with its cost per £1,000 and its volume. Mapped in SR1.
- **Key input** — the supplier input with the highest cost × volume for which the venture has, at C9, no alternative it controls: deposit funding.
- **Transfer price** — the rate an internal treasury charges a lending book for the funds it lends. A convention set by the bank's asset and liability committee, not a market price.
- **The pool** — the accounts the form runs on (C1's population, C3's release order). At scale ⚠ 760,000 accounts with a limit, ⚠ 228,000 drawn, on a base whose credit balances are ⚠ £50–100bn (*runner's call*: UK SME deposit balances ⚠ £250–300bn across all banks, T2, and a large bank's share ⚠ 20–33%, T4).
- **Levelled-line funding (PC-2)** — the drawn balances of the pool's accounts are funded by the credit balances of the same pool; the line pays the pool's measured deposit cost under a signed funding term read daily; the aggregate drawn book is capped at ⚠ 10% of the pool's credit balances (G18).
- **Measured deposit cost** — the interest the bank actually pays on the pool's credit balances in the period, divided by those balances; ⚠ 1.5–3.0% a year at Bank Rate 4.0% (C1). Read daily by treasury from figures it already computes.
- **Standby route** — a revolving master trust: a special-purpose vehicle that can issue notes to investors against the pool's drawn balances, with the R9 ledger as its data tape. Set up before Stage 3 and maintained without issuance; opened only on the trigger. All-in cost if opened ⚠ SONIA + 0.6–1.0% = ⚠ 4.6–5.0% (T2, from public revolving-trust pricing).
- **Trigger** — the transfer price charged to the line exceeds the standby route's all-in cost for two consecutive quarters. On the trigger the route issues.
- **Hold-up resistance score (HRS)** — the registry's barrier score for R10. The registry states its thresholds (≥ 5 pass; ≤ 3 NCR) and not its terms; *runner's call*, patterned on the SCIS and FIS: asset ownership (0–2), alternative availability (0–3), replacement time (< 12 months 2; 12–36 months 1; > 36 months 0). Maximum 7. Recorded for the WS1 feedback log.
- **Deposit beta** — the share of a change in Bank Rate that passes into the rate paid on deposits; below one where the bank holds market power over its depositors. ⚠ 0.3–0.5 for SME current-account balances (T4, patterned on the published aggregate figures).

---

## SR1 — Interim value chain and key input

*Customer of record: the business owner who holds the account; the routine positioned in: the rule's own routine on the account — set, fund, clear, record, re-set.*

**The value chain at scale, ranked by cost × volume.** Every supplier input the form draws on, from the AOM v9 floor. Volume is the drawn book ⚠ £3.4–5.7bn unless stated.

| Rank | Input | Supplier | Per £1,000 a year | A year at scale ⚠ | Inside or outside the bank | Alternative the venture controls at C9 |
|---|---|---|---|---|---|---|
| 1 | deposit funding of the drawn book | treasury, pricing the pool's deposits to the line | 15–30 | £51–171m | inside | none — the transfer price is treasury's convention |
| 2 | regulatory capital on drawn and undrawn exposure | the bank's shareholders, through the capital plan | 13–18 | £44–103m | inside | none needed — capital is the owner's input, not a supplier's; its price (⚠ 12–15% cost of equity) is set by the market for the bank as a whole |
| 3 | exception handling, write-off administration and legal | the cells (14 handlers × 2.28 cells) and external collection agents and solicitors | 3.00–8.13 | £10–46m | inside; the legal line outside | many agents and firms; contracts of under a year |
| 4 | HQ people — the engine team, model risk, conduct, pricing, data protection | the bank's own employees | 2.02–5.04 | £7–29m | inside | the labour market |
| 5 | computing, storage and payments | the core banking platform; cloud batch compute; the payment scheme through which receipts arrive | 2.02–5.12 | £7–29m | the core inside; cloud and the scheme outside | three cloud providers; the scheme is a regulated utility every bank uses |
| 6 | the fraud and conduct signal | a credit bureau (one of three) | ⚠ 0.1–0.3 (inside the computing line) | £0.3–1.7m | outside | two other bureaus; a contract switch of 3–6 months |
| 7 | the account-information standard and its operator | the standard body and its directory (public, mandated by the CMA Order) | ⚠ 0.00–0.01 (inside the C7 conformance line) | under £0.1m | outside | the bank's own channel under PSRs 2017 reg. 69 |
| 8 | model validation | the bank's model-risk function (10 people) | inside RC | inside RC | inside | external validation firms at ⚠ £0.2–0.5m a year |

The expected-loss line (20–40) is not a supplier input: it is what the customers do, and it is the binding gate (C1 onward).

**The five diagnostic questions.**

1. *Who supplies inputs the venture cannot easily source elsewhere?* Treasury. Every other line has a market with several sellers or is the bank's own people. Funding has no market the line can reach on its own at C9: a lending book inside a bank takes the price treasury sets.
2. *Which input, priced up 30%, most damages the unit economics?* Funding. A 30% rise on the funding line is +4.5–9.0 per £1,000 and takes the worst-corner margin from 30.3% to 20.3%; the same rise on the next largest supplier line (exceptions and legal) is +0.9–2.4 and takes it to 27.4%. But 30% is the wrong test for funding: the convention treasury can adopt is not a 30% rise, it is a change of reference — from the deposit cost (1.5–3.0%) to Bank Rate (4.0%) or to the wholesale rate (4.6–5.0%) — a rise of 33–233%.
3. *Which supplier's withdrawal takes longest to replace?* Funding, from a standing start: a master trust takes ⚠ 12–18 months to document, rate and place (T2, from public programme timetables); the core platform's replacement is longer still but is the bank's decision for every product, not the line's.
4. *Which dependency concentrates with scale?* Funding. At Stage 1 the drawn book is ⚠ £0.4–1.9bn against pool balances of ⚠ £50–100bn — under 4% at the worst corner; at scale it is ⚠ £3.4–5.7bn, 3.4–11.4%. The more the form succeeds, the more of the pool's balances it draws on, and the more a change of transfer price costs it.
5. *Are any R7 gateway partners now supply-side dependencies?* No. The platforms read the element the bank publishes; they supply nothing to the form. The standard's operator is on the supply side (rank 7) but at a cost near zero and under a public order.

**The key input, named.** Deposit funding at the pool's deposit cost, supplied by treasury under a transfer-price convention the line does not control. Cost × volume ⚠ £51–171m a year — larger than ranks 3 to 8 together (⚠ £25–106m).

**The block, named as one operation.** The line's funding is priced by a convention outside the line. At C1 the funding line was booked at the pool's deposit cost (⚠ 1.5–3.0%) on the argument that the balance was already funded by the account line's deposits; nothing in the design at C9 makes that price hold. A treasury that prices every lending book at its marginal wholesale cost — a common convention, and one the asset and liability committee can adopt — charges the line ⚠ 4.6–5.0% and the floor's high corner rises by 16–20.

**Why this is not the other candidates.** *Capital (rank 2)* — the owner's input; its price is set for the bank, not for the line; R10 cannot make the bank's cost of equity replaceable and does not try. *The core platform (rank 5)* — a standing constraint of the bank as a whole; the line's input from it is one row (the daily balance) that any core produces, and the engine sits beside the core, not inside it (C1). *The bureau (rank 6)* — three sellers, a short contract, a signal that is not in the limit rule; a supplier with no hold. *The standard's operator (rank 7)* — a public order compels the bank to publish, and the bank's own channel carries the element under the same regulation. *Model validation (rank 8)* — inside the bank, with an external market at ⚠ £0.2–0.5m. *Labour (rank 4)* — a market.

**The shelf check at launch (carried from C9).** Suppliers binding at Stage 0 and Stage 1: the core platform (the daily balance row — existing), the bureau (the signal — an existing contract), cloud compute (the back-test — three sellers), the standard's operator (the C7 element — the bank's existing programme). None binds: each is in place for the bank today and none can withhold the input from the line alone. Funding at Stage 1 is the pool's own at ⚠ 0.4–3.8% of its balances. No launch constraint is written into the design (VA-23).

**The existence test with the affordability screen first (VA-92).** *Affordability:* the room above the operating bar at the set price is 5.89 per £1,000 (C9); a standing cost in the floor is multiplied by 1.25 at the bar, so the most the venture can pay for any R10 route without the price failing is 5.89 ÷ 1.25 = **4.71 per £1,000 a year = ⚠ £16–27m a year** at scale; at the band's low end (135) it is 0.89 ÷ 1.25 = 0.71 per £1,000 = ⚠ £2.4–4.0m. *Existence:* does a route exist by which a UK lender funds a revolving book of small-business balances in the market against a ledger of daily balances and outcomes? Yes — revolving master trusts on credit-card receivables have issued in the UK public market for two decades (Penarth Master Issuer; Delamare Cards MTN Issuer — T2), and a public securitisation of UK small-business loans has priced (SBOLT 2016-1 — T2). The set-up cost of such a programme is ⚠ £1–3m once and its upkeep without issuance ⚠ £0.3–0.6m a year (T2, from published programme fee schedules and legal budgets) — ⚠ 0.09–0.36 per £1,000, inside the screen at every corner of the band. The route exists and is affordable. The supplier of the route is a class (arrangers, trustees, administrators) with several sellers — commodity vendors, no VA-99 business case owed.

**VA-101 test at SR1.** Could any competitor, with any budget, remove the limit? The limit here is not a rival's: it is a supplier's power to reprice. The market route removes the supplier's power to withhold the input; it does not remove the gap between the pool's deposit cost and the market's — that gap is of the world (a deposit franchise is cheaper than wholesale money because depositors accept less than Bank Rate, SR2). The value that rests on it: the funding line at 15–30, and through it the margin; stated in the position-holding table.

---

## SR2 — Supplier-power theory of change

**Parameter the input rests on.** When one party holds an asset whose value depends on a specific counterparty, the counterparty can take the difference between the asset's value in that use and its value elsewhere; the remedy is to own the input rather than contract for it.

**Theory.** Klein, B., Crawford, R. G. and Alchian, A. A. (1978), "Vertical Integration, Appropriable Rents, and the Competitive Contracting Process", *Journal of Law and Economics* 21(2): 297–326. Where an asset is specific to a relationship, the quasi-rent it earns can be appropriated by the other party after the investment is sunk; contracts reduce this and do not remove it, and the structural remedy is integration — the input is held by the party whose return depends on it. Supported by Drechsler, I., Savov, A. and Schnabl, P. (2017), "The Deposits Channel of Monetary Policy", *Quarterly Journal of Economics* 132(4): 1819–1876: banks hold market power over their depositors, so the rate paid on deposits rises by less than Bank Rate (a deposit beta below one), and the deposit franchise is a funding source cheaper than wholesale money and stable across the rate cycle. The two together say what the line must hold and why it is worth holding: the pool's deposits are cheap because of the franchise, and the line keeps that price only if the funding is the pool's own and not a supplier's.

**Contrast.** Williamson, O. E. (1985), *The Economic Institutions of Capitalism*, Free Press — hold-up can be met by contractual safeguards (hostages, long terms, credible commitments) short of integration. The design rejects the contractual answer for R10 because the challenge skill does: a contract with treasury is a convention the same committee can rewrite. A second contrast: Diamond, D. W. and Dybvig, P. H. (1983), "Bank Runs, Deposit Insurance, and Liquidity", *Journal of Political Economy* 91(3): 401–419 — deposits can leave. The theory survives it because the cap (G18) keeps the drawn book at a tenth of the pool's balances, and because the standby route exists for the case the balances fall.

**Fragile-findings check.** Klein, Crawford and Alchian 1978 and Williamson 1985 are theory; Diamond and Dybvig 1983 is a model; Drechsler, Savov and Schnabl 2017 is an empirical finding on United States bank data, replicated on European and UK data by later work. None is on the fragile-findings list. The deposit-beta figure used here is a Tier 4 band, not a finding.

**Context in which the mechanism holds.** The line is a property of the account (C1), so the drawn balance and the credit balance are states of the same pool. The pool's credit balances exceed its drawn balances by a wide margin (⚠ 9–29 times). The bank measures its deposit cost daily. A market route for the drawn balances exists and can be kept ready without issuing.

**Outcome.** The line's funding cost is the pool's measured deposit cost — ⚠ 1.5–3.0% at Bank Rate 4.0% — and moves with the deposit beta rather than with the policy rate; no internal price above the market's can be held against it; the venture's existence does not depend on treasury's consent.

**Hypothesis (falsifiable).** In every quarter of the first five years of Stage 3, the transfer price charged to the line is within ⚠ 0.25 points of the pool's measured deposit cost, and the drawn book is under the cap. Falsified if in two consecutive quarters the price charged exceeds the measured deposit cost by more than ⚠ 1.0 point and the standby route is not opened. **Falsification condition on the theory:** if, on the trigger, the standby route cannot issue against the ledger tape within ⚠ 6 months at ⚠ SONIA + 1.5% or better, the route was not a replacement and the funding was not replaceable.

**Named assumptions.** (1) The pool's credit balances are ⚠ 9–29 times its drawn balances at scale — T4 from public totals and a share; (2) the deposit beta on SME current-account balances is ⚠ 0.3–0.5 — T4; (3) a revolving master trust can be documented and rated on the R9 ledger's fields without a new observation — T2 from the field lists public programmes disclose; (4) the bank's asset and liability committee will sign a funding term that fixes the line's reference at the measured deposit cost — T4; the term is the productization and the committee is an actor row.

---

## SR3 — Supplier-power strategy

**The strategy in one sentence.** Fund the line inside its own pool — the pool's credit balances fund the pool's drawn balances, capped at a tenth, priced at the measured deposit cost — and keep one market route ready so that no internal price above the market's can be held against it.

```
MUTATION GATE — R10
baseline: the line's funding is booked at the pool's deposit cost (C1) and priced by treasury's transfer-price convention; nothing in the design fixes the reference; a change of convention to Bank Rate or to the wholesale rate is a committee decision the line cannot answer; no market route exists for the line's balances.
mutation_A: levelled-line funding (PC-2) — the pool funds the pool: the drawn balances of the pool's accounts are funded by the credit balances of the same pool, the aggregate drawn book is capped at ⚠ 10% of the pool's credit balances (G18), the line pays the measured deposit cost under a signed funding term read daily, and a revolving master trust on the R9 ledger is set up before Stage 3 and maintained without issuance, opened on the trigger | reason_considered: it is the structural bypass — the funding is the pool's own liability, not a supply from treasury's wholesale book; and the market route removes the supplier's power to withhold | verdict: adopted | reason_verdict: the input is owned (the pool's deposits are the bank's liabilities); the price is read, not negotiated; the route exists and is affordable (VA-92); costs ⚠ 0.09–0.36 per £1,000; no person added
mutation_B: the market route alone — a warehouse line or a securitisation as the line's funding | reason_considered: substitute development; removes treasury from the chain entirely | verdict: rejected as the sole route | reason_verdict: the market's price is ⚠ 4.6–5.0% and the margin at that price is 13.4–9.8%, FAIL; a substitute that fails the margin is an existence guarantee, not a funding architecture — kept as the standby inside A
mutation_C: a locked deposit sweep — each drawn account's own credit balances swept into a term deposit that funds its own limit | reason_considered: the purest form of the pool funding the pool, account by account | verdict: rejected | reason_verdict: the drawn account has no credit balance while drawn (the balance is below zero — C1); the funding comes from other accounts in the pool, which is A at the pool level; and a lock on a customer's balance is a term the customer must accept (a Selling cost, R4–R5 re-opened)
mutation_D: a central-bank funding scheme | reason_considered: the cheapest wholesale money there is | verdict: not available | reason_verdict: the Term Funding Scheme with additional incentives for SMEs closed to drawings on 31 October 2021 (FACT); the existence test fails at the date of this record
mutation_E: a covered-bond programme on the drawn balances | reason_considered: the cheapest private market route a UK bank has | verdict: not available | reason_verdict: the Regulated Covered Bonds Regulations 2008 limit eligible assets to residential and commercial mortgages, public-sector and certain other loans; small-business revolving balances are not eligible (FACT)
mutation_F: a long-term funding contract with treasury at a fixed spread over the deposit cost | reason_considered: Williamson's contractual safeguard | verdict: rejected | reason_verdict: a contract inside one legal entity binds no one — the committee that signs it can rewrite it; and the challenge skill names contracts as not R10
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: mutation_A — levelled-line funding (PC-2) with the standby route
evolvedBFF: a bank whose credit facility is a standing property of every business account with enough flow — computed daily from the flow and from the account's own record, by a rule fitted only to what its own limits did on this pool, funded by the pool's own credit balances at the pool's own deposit cost and capped at a tenth of them; priced below the tariff, released in stages, believed on its history, used without an act, paid from receipts, published wherever the account is read, seasoned by use, calibrated on its own outcomes, and funded from within.
synthesisCheck: a building society's funding limit — the Building Societies Act 1986 s.7 requires at least half of a society's funds to come from its members' shares, so its lending is funded from within by law, and the society keeps a wholesale programme beside it for the balance; the line's cap is the same shape set by design rather than by statute, with the market route kept ready rather than in use.
```

**Supplier-power approach.** Structural bypass — the highest of the three (substitute development, exclusivity capture, structural bypass). The input is not sourced from a second supplier and not locked by contract; it is made the venture's own by the form's construction — the pool's liabilities fund the pool's assets — with a substitute held ready for the case the construction is overridden.

**The architectural decision test.** The single structural move is that the line is funded by the pool's own credit balances at the measured deposit cost, capped at a tenth. Its removal makes the outcome impossible: without it the line takes the transfer price treasury sets, and the margin is whatever that convention leaves. The standby route is part of the same move (it is what makes the cap and the price hold against a committee), not a second move; the signed term is how the move is written down. What follows — a margin held at 30.3%, a rate review that reads a deposit beta rather than Bank Rate — is evidence, not the strategy.

**The at-scale test (VA-23).** At ⚠ £3.4–5.7bn drawn against ⚠ £50–100bn of pool balances the cap is 3.4–11.4% used: surplus at central (⚠ £4.5bn against a cap of ⚠ £7.5bn); at the worst corner (⚠ £5.7bn drawn, ⚠ £50bn of balances) the cap binds at ⚠ £5.0bn and the book is ⚠ 12% smaller than the proxy's high end. Stated unsoftened; the fin-sim reads it at the PCO's objective. *Runner's call* on 10%: high enough that the cap does not bind at central; low enough that the pool stays a net depositor at every corner, so the funding never reaches treasury's wholesale book; threshold — if the measured share exceeds ⚠ 8% for two quarters the cap is reviewed at the committee before it binds.

**R1 continuity.** R1 made the limit a property of the account. R10 makes the funding a property of the pool of accounts: the same construction, one level up. The rule that sets the limit reads the account; the cap that sizes the book reads the pool. Nothing is added to the customer's routine.

**R9 interaction.** The R9 ledger is the standby route's data tape: every field a rating agency and an investor read (balance by day, limit in force, funded events, clearances, losses by cohort) is a WP-6 row. No new observation.

**R2 and R6 interaction (the C6 carried question).** The price is fixed at 14.0% simple and reviewed yearly (PC-1). R10 states what the funding line does across the rate cycle: it moves with the deposit beta (⚠ 0.3–0.5), not with Bank Rate. A one-point rise in Bank Rate adds ⚠ 3–5 per £1,000 to the floor; a two-point rise ⚠ 6–10. The yearly review reads the measured deposit cost from the funding term. The fixed-against-linked question stays Tom's (a pricing-structure decision); R10 supplies the mechanism it is decided on.

**Structural, not contractual.** The funding is the pool's own liability by the form's construction. The signed term records a price the bank already measures; the standby route is a legal vehicle the bank owns. No third party's consent holds the input.

---

## Productizing R10 — the strategy in the architecture

**PC-2 — levelled-line funding and the standby route.** A new Payment-product component in the Making stream's funding layer. It has three parts. *The funding term:* treasury supplies the line's drawn balances from the pool's credit balances at the measured deposit cost, computed daily from figures treasury already holds (interest paid on the pool's balances in the period ÷ those balances), signed by the asset and liability committee and reviewed at the yearly rate sitting with PC-1. *The cap:* the aggregate drawn book is held at or under ⚠ 10% of the pool's credit balances, read monthly at the committee; above ⚠ 8% for two quarters the cap is reviewed; at the cap, release (C3) pauses — no account's limit is cut. *The standby route:* a revolving master trust documented and administered before Stage 3, with the R9 ledger as its tape produced monthly by the engine, maintained without issuance at ⚠ £0.3–0.6m a year; opened on the trigger for the share of the book that restores the price charged to the market's or lower.

**Structural against contractual scarcity of the input.** The pool's credit balances are the bank's liabilities; they are not bought from anyone. The transfer price is a reading, not a negotiation. The market route is a vehicle the bank owns and can open without a counterparty's consent; the counterparties it needs on opening (investors, a rating agency, a trustee) are a class with many members.

**The customer sees nothing.** No term changes; no notice is sent; the limit, the price, the split and the schedule are as at C9. The cap acts on release, which the customer already experiences as the stage at which the shadow limit becomes drawable (C3). A customer whose release is paused by the cap is told nothing new: the shadow limit is shown as at C3.

**Data protection.** The tape carries per-account rows to the vehicle only on issuance; until then it is produced and held inside the bank under the Article 30 record made at C9. On issuance the vehicle is a data processor for the bank under a written contract (Article 28) and the rows are pseudonymised (Recital 26, Article 4(5)) — the standard practice of every public UK programme (T2). What a ruling would settle: nothing new; the position is the market's.

**Prudential position.** The standby route is a securitisation once it issues; the bank retains at least 5% of the material net economic interest (UK Securitisation Regulation, FACT) and reads the significant-risk-transfer rules if it seeks capital relief — it does not, in this design: the route is for funding, and the capital line (IC) is unchanged. Under the net stable funding ratio, retail and small-business deposits carry an available-stable-funding factor of 90–95% (CRR Part Six, Title IV, FACT), so a drawn book funded inside them is stably funded by construction — a fact the cap makes true for the line at every corner.

**The at-scale test.** At ⚠ £3.4–5.7bn drawn the tape is the ledger's monthly cut (⚠ 0.06–0.23m outcome rows and ⚠ 23m balance rows a month) — a job the engine already runs for the calibration. The daily price is one arithmetic line in treasury's existing computation. The cap reading is one figure at a sitting the committee already holds. No person is added. The set-up is ⚠ £1–3m once in the SC layer; the upkeep ⚠ £0.3–0.6m a year in RC (external administrators, trustee and legal refresh; treasury's ⚠ 100–200 hours a year sit inside its existing people).

**What the bank now has.** A line whose funding is its own pool's, at its own pool's price, that cannot be repriced from inside above the market's price and cannot be withdrawn from outside; and a market route it need never use.

---

## Cumulative business form factor (C1–C10)

**The architecture's central mechanism.** The standing limit as a property of the account — computed from the flow and from the account's own record by a rule fitted only to what its own limits did on this pool, funded by the pool's own balances at the pool's own price, present before any need, published wherever the account is read. Remove the pool funding and the form returns to C9: a line whose price is right and whose cost is a committee's convention.

**The evolved BFF.** A bank whose credit facility is a standing property of every business account with enough flow: the limit is computed daily from the flow and shown in the account before any need arises (C1); it is priced below the tariff the customer pays today and the existing overdraft is retired into it (C2); it is released in stages against a kill band, with the rule proven on history before it is trusted (C3); it is believed because the customer checks it against the twelve months of their own shortfalls it would have covered (C4); it is used without an act, because a payment that exceeds the balance is funded from the limit by default (C5); it is paid for from receipts, as the first slice of the receipts share, at one rate and no fee (C6); it is published wherever the account is read, as the account's own credit line (C7); it grows with use, because the account's cleared events raise the multiple (C8); its parameters are fitted only to what its own limits did on this pool (C9); and it is funded by the pool's own credit balances at the pool's own deposit cost, capped at a tenth of them, with a market route held ready (C10).

**The evolution test (challenge skill, mandatory at C10).** Does the BFF at C10 differ from the BFF at C1 in kind, not only in count? At C1 the form was a rule on one account: read the flow, set the limit. At C10 it is a pool: the rule's parameters come from the pool's outcomes (C9), the rule's funding comes from the pool's balances (C10), the rule's growth comes from the account's own use (C8), and the rule's reach comes from the account's readers (C7). Each of R4 to R10 removed a block the C1 form could not have removed by being run harder; none is a feature. The test passes — the C10 form is a different object from the C1 form, and the C1 form is recoverable from it by removing nine moves in reverse order.

**Components at C10.** WP-1 v2 (amended C8), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, WP-6 (C9), CP-1 (amended C2, C4, C6), CP-2 (amended C8), PC-1 (resolved C6), **PC-2 (new C10 — levelled-line funding and the standby route)**, PP-1 (C7). One new component; none removed.

---

## Considered / not chosen (VA-4)

- **The market route alone (B)** — rejected as the sole route at the mutation gate: it fails the margin; kept as the standby.
- **A locked deposit sweep (C)** — rejected: the drawn account has no balance to sweep; the pool-level form is A.
- **A central-bank scheme (D)** — not available: closed to drawings since 31 October 2021.
- **A covered-bond programme (E)** — not available: the assets are not eligible.
- **A funding contract with treasury (F)** — rejected: a contract inside one entity is a convention; the skill names contracts as not R10.
- **Diversifying the bureau to two suppliers** — not chosen: the bureau is rank 6 at ⚠ £0.3–1.7m a year with three sellers; diversification is not R10 and the input has no hold.
- **Bringing model validation outside to an independent firm** — not chosen: the internal function is the cheaper route and is owed under SS1/23; the external market is the alternative that scores the input 7.
- **Replacing the core platform's ledger with the engine's own** — not chosen: the engine reads one row the core produces; a second ledger of balances would be the bank's book kept twice, and the core is the bank's constraint, not the line's.
- **Raising the cap above 10%** — not chosen: at ⚠ 15% the pool is still a net depositor at every corner, but the share of the pool's balances the line draws on is the share treasury's wholesale book would have to replace if the balances fell; 10% keeps the standby route's opening size under ⚠ £1bn at the worst corner (*runner's call*; threshold above).
- **Pricing the line at Bank Rate and raising the price to hold the margin** — not chosen: F3 does not reprice; and at 15.0% the price would be above three of the seven published tariffs the C2 KMC was priced against.

---

## Synthesis check (VA-1)

A building society's funding limit: the Building Societies Act 1986 s.7 requires a society to raise at least half of its funds from its members' shares, so its mortgage book is funded from within by statute, and the society keeps a wholesale programme beside it — covered bonds and a master trust — for the balance and for the day the members' balances fall short. The line's structure is the same: the book is funded by the pool's own balances under a cap, and a market route is kept beside it. The analogue's limit: the society's members own the society and set its rules at a general meeting; the pool's depositors own nothing and the cap is a committee's rule, which is why the standby route is part of the move and not an option beside it.

---

## VA-106 synergy line

Does the one move also serve an earlier requirement, with a mechanism? Nine candidates:

- **R1 (design) — yes.** The funding is a property of the pool as the limit is a property of the account; the same construction one level up. Mechanism: the cap reads the same ledger of balances the rule reads.
- **R2 (value) — yes.** The price condition (the limit's cost below the tariff) is held on the cost side: the funding line the price was set against is now fixed at the measured deposit cost rather than at a convention. Mechanism: the yearly rate review reads the funding term's price.
- **R3 (scale) — yes.** The cap is a release-order reading: each stage's drawn book against the pool's balances joins the stage readings; at the cap, release pauses. Mechanism: one figure added to the release track's sitting.
- **R6 (buy) — yes.** The receipts share clears the drawn balance and returns the funds to the pool; the split is what keeps the drawn book a tenth of the pool. Mechanism: the same clearance event, read at the pool level as turnover.
- **R9 (lock-out) — yes.** The outcome ledger is the standby route's tape. Mechanism: WP-6's monthly cut, no new write.
- **R4 (conviction) — no.** The history and the display do not move.
- **R5 (use) — no.** The funded event and the accepted term are unchanged.
- **R7 (access) — no.** The element is unchanged.
- **R8 (accumulate) — no.** The schedule and the store are unchanged.

Five earlier requirements served with a mechanism. The Phase 3 moat test asks that at least one VA-106 line name two or more other requirements: this line names five. Read across the ten lines at the consistency audit (named in the close).

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per year unless stated; every ⚠ is T4. Internal actors are read at the bank's level, as at C8 and C9.

| Actor | Behaviour needed | How often | Effect on own book | What it gains | What it costs | Best alternative and its surplus | Arithmetic (VA-157) | Surplus at scale | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|---|---|
| The business owner | nothing — the funding is the pool's; no term, notice or act | — | — | the same limit, price, split and schedule | nothing | — | central: £0 − £0 − £0 = **£0** · pessimistic: **£0** | flat | **nil by design** — no behaviour needed |
| The depositors as a class (the pool's credit balances) | nothing — the balances are held under the account contract at the pool's rate as today | — | — | — | — | — | central: **£0** · pessimistic: **£0** | flat | **nil by design** |
| Treasury (internal) | computes the measured deposit cost daily; supplies the line at that price under the signed term; holds the cap reading; administers the standby route | daily; monthly; yearly | neutral at the bank's level (a transfer price moves income between two internal books) | at the bank's level: the line's room above the operating bar, 5.66 per £1,000 — the surplus a convention at Bank Rate would remove (the line at 19.2% does not clear the gate and is not run) | ⚠ 100–200 h a year inside existing people = ⚠ £10–20k; the route's upkeep ⚠ £0.3–0.6m | price the line at Bank Rate — bank-level surplus 0 (the line does not run) | central: gain £25.5m (5.66 × £4.5bn) − cost £0.45m − £0 = **£25.0m** · pessimistic: gain £2.2m (0.66 × £3.4bn) − cost £0.61m − £0 = **£1.6m** | rises with the book | **PASS** |
| The asset and liability committee (internal) | signs the funding term; sets and reads the cap; opens the route on the trigger | once; monthly; on trigger | neutral | the drawn book stably funded under the net stable funding ratio by construction; one funding decision made once rather than at every rate sitting | ⚠ 10–20 h a year inside existing sittings | sign nothing — the convention stands; the line's margin is the committee's to change at any sitting | central: gain £6.4m (a quarter of the treasury row's gain, attributed to the signature that lets it act) − cost £0.003m − £0 = **£6.4m** · pessimistic: gain £0.4m − cost £0.004m − £0 = **£0.4m** | rises with the book | **PASS** |
| The standby route's agents (administrator, trustee, legal — external, commodity vendors) | document and administer the vehicle; refresh yearly | once; yearly | adds (fee income) | ⚠ £1–3m once; ⚠ £0.3–0.6m a year | their own cost, inside their fees | any other client — the same fees | central: gain £0.45m − cost £0.30m − £0 = **£0.15m** · pessimistic: gain £0.30m − cost £0.25m − £0 = **£0.05m** | flat | **PASS** — a commodity vendor; no VA-99 business case owed |
| The bank's limit-engine team (internal) | produces the tape monthly from WP-6 | monthly, automated | neutral | nothing new (the cut is the calibration's) | ⚠ 20–40 h once to write the cut; ⚠ £1–3k a year of compute | not produce: the route cannot open | central: gain £0.02m (a share of the route's readiness) − cost £0.005m − £0 = **£0.015m** · pessimistic: gain £0.005m − cost £0.005m − £0 = **£0** | flat | **PASS** (nil at the pessimistic corner, forced by the small size of the task) |
| Note investors and a rating agency | none in the design — actors of the failure path only (on the trigger) | — | — | — | — | — | — | — | not actors of the architecture; named because the existence test is read against them |

**Read plainly.** Every row PASSES or is nil by design. The design needs no one outside the bank to do anything until the trigger, and on the trigger it needs a class with many members.

---

## Actor tracks (VA-102)

No new external actor class this challenge in the design; one internal holder gains a behaviour (treasury) and one gains a decision (the committee); the standby route's agents are commodity vendors. **(1) Where does each track open?** The customer's track is unchanged. The release track (C3) gains one monthly reading (the cap) and one state (release paused at the cap). The pricing track (C2) gains one input (the funding term's price at the yearly review). A funding track opens at the committee's signature and carries three states: term signed; route documented; route open. **(2) Where a transition carries no product by decision, what activity does the work?** The daily price and the monthly tape are automated activities (AOM v10 3a); the cap reading and the trigger are committee activities (3c). **(3) What drives each counterparty?** Treasury and the committee are read at the bank's level (the row above); the agents by fee.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** PC-2 added: levelled-line funding, the cap and the standby route. No component removed; no other component amended. The release track gains the cap reading; the pricing track gains the funding term's price.

**Earlier requirements this same move also serves (VA-106).** R1, R2, R3, R6, R9 with mechanisms; R4, R5, R7, R8 no, with reasons (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — strengthened on one line.** The funding line's basis (the pool's deposit cost, C1) is now held by a term and a cap rather than assumed; the four removed operations stay removed; property holder of "funded" is treasury (a track row). RC rises ⚠ 0.05–0.18 | re-verified: at-scale margin on the selected customer 30.3% at the set price |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — strengthened.** The price condition's cost side is fixed; the KMC and the price do not move. The TAM data object narrows by one named block (the cap, G18) at the worst corner only — v4 written at this record | re-verified: 30.3% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — strengthened.** The cap joins the stage readings; release pauses at the cap without any limit being cut. SC gains the route's set-up (⚠ £1–3m once) inside the 0–1 band (unrounded 0.92 at the high corner). Stage 1 margin at the set price 2.8% at the AOM v10 fixed layer (spread count below) | re-verified: Stage 1 2.8% at the set price |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — unchanged.** The history and the display do not move; a paused release shows the shadow limit as at C3 | re-verified: 30.3%; cap line carried |
| R5 (C5 record v1.1) | use routine; routine disruption; Madrian and Shea; default funding; switch-off and reversal; the loss gap; CONC 5.2A timing | **re-verified — unchanged.** The funded event is the same; its funding source is the pool's balances as at C1. Loss gate at the set price 4.45% (floor high 107.47) | re-verified: 30.3%; loss gate 4.45% |
| R6 (C6 record v1) | lifecycles; CVTs; buy block type; Prelec and Loewenstein; mutation gate; price structure; representative example; R2 and R3 interactions | **re-verified — one position extended.** The price is the same; the yearly review now reads the funding term's price and the deposit beta. The fixed-against-linked question stays carried with R10's mechanism attached | re-verified: 30.3% at the set price (25.6% / 32.6% at the band's ends) |
| R7 (C7 record v1) | access routines; gateway class; Farrell and Saloner; PP-1; conformance; desk position; G15 | **re-verified — unchanged.** The element is unchanged; the standard's operator is scored at SR1 and is not a supply-side hold. S1, S3, F-5, F-6 carried unchanged | re-verified: 30.3% |
| R8 (C8 record v1) | extended routine; store of value; Sharpe 1990; WP-1 v2; SCIS; position-holding; the £8 cap line | **re-verified — unchanged.** The schedule and the store do not move; the SCIS design finding stands (2 · 4 · 6). The undrawn commitment the seasoned limit raises is inside the cap at every corner (⚠ 1.9–3.6 undrawn per £1 drawn is a capital figure, not a funding one) | re-verified: 30.3%; SCIS 2 · 4 · 6 carried |
| R9 (C9 record v1) | key resource; Dierickx and Cool; WP-6; FIS; position-holding; the loss-band re-test | **re-verified — strengthened.** The ledger gains a second use (the tape) with no new write; the FIS stands (5 · 6 · 7); the loss-band re-test is repeated at the C10 floor below | re-verified: 30.3%; FIS 5 · 6 · 7 carried |

No FAILED row. **Function-gate re-run (at C10):** every earlier requirement re-run in full on the cumulative BFF — `bank-credit-facility-consistency-audit-C10-2026-09-21.md` and `bank-credit-facility-verify-C10-2026-09-21.md`; both written the same day, after this record closed; the audit reads COHERES with one route-back (the C3 trial band, H1) and four soft items; the verification reads SOUND 87.7, validation-maturity pre-operational. Filenames entered in the changelog.

---

## Financial check — the floor on four layers, the ceiling as a price, the cap and the position-holding table

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn; at the worst corner of the cap ⚠ £5.0bn. **Component set the verdict was computed on (VA-74):** WP-1 v2 (amended C8), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, WP-6 (C9), CP-1 (amended C2, C4, C6), CP-2 (amended C8), PC-1 (resolved C6), PC-2 (new C10), PP-1 (C7).

**Pricing note.** F3 does not reprice. The ceiling stays the R2 KMC resolved to the C6 price (140; band ⚠ 135–142.5). R10 changes no price and no exposure; it fixes where the funding line's figure comes from and adds a route.

**What R10 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v10 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| compute the measured deposit cost and the line's price | HQ, daily, automated | e.funding_price on q.pool_credit_balances | 365 | ⚠ £0 (one arithmetic line in a computation treasury already runs) | ⚠ £0–1k | 0.00 |
| read the cap (drawn book ÷ pool credit balances) at the committee | HQ, monthly | e.cap_reading | 12 | ⚠ 1–2 h inside existing sittings | inside RC | 0.00 |
| produce the tape from WP-6 | HQ, monthly, automated | e.tape_cut on q.outcome_rows and q.balance_rows | 12 | ⚠ £100–250 of compute per cut | ⚠ £1–3k | 0.00 |
| maintain the standby route — administrator, trustee, legal refresh, no issuance | HQ, yearly | e.route_upkeep | 1 | ⚠ £0.3–0.6m (T2, published programme fee schedules) | ⚠ £0.3–0.6m | 0.05–0.18 (RC) |
| treasury's administration of the term and the route | HQ, yearly | e.route_upkeep | 1 | ⚠ 100–200 h inside treasury's existing people | inside RC | 0.00 |
| review the trigger and the cap threshold | HQ, quarterly | e.trigger_review | 4 | ⚠ 2–5 h inside existing sittings | inside RC | 0.00 |
| set up the standby route — vehicle, documents, first tape, arranger | HQ, once, before Stage 3 | e.route_setup | 1 | ⚠ £1–3m once, amortised over five years | ⚠ £0.2–0.6m | 0.04–0.18 (in SC, inside the 0–1 band) |
| **R10 total, unrounded** | | | | | **⚠ £0.5–1.2m operating and amortised set-up** | **⚠ 0.09–0.36** |

*Runner's call on the upkeep figure.* A documented but unissued master trust carries an administrator, a trustee, a yearly legal refresh and the tape; no rating fee and no note interest. ⚠ £0.3–0.6m is judged from published fee schedules of UK programmes (T2). Threshold: above ⚠ £1.0m a year the RC addition is 0.18–0.29 and the R10 addition is booked at ⚠ 0.5; the margin at the worst corner falls to 30.1%. Convergence: the first year's invoices after set-up.

**The four-layer floor at C10 (AOM v10 section 6).**

```
PVC  40.02–83.25   funding 15–30 (C10: the band is what the funding term holds — position-holding table) · expected loss 20–40 (C9: the calibration) · computing and payments 2.02–5.12 (C10: +0.00, the daily price and the tape) · exceptions and write-off 3.00–8.13 (C10: +0.00)
RC    2.07–5.22    C10: +0.05–0.18 — the standby route's upkeep (external administrator, trustee, legal refresh); treasury's hours inside existing people
SC    0–1          unchanged — the route's set-up (⚠ £1–3m once) sits inside the band; unrounded 0.03–0.74 → 0.07–0.92
IC   13–18         unchanged — no exposure change at R10; no capital relief sought
FLOOR 55.09–107.47  (C9: 55.04–107.29; C8: 55.04–107.28; C7: 54.04–106.28; C6: 54.04–106.27; C5: 54.04–106.26; C4: 54.03–106.20; C3: 54–106)
```

**Carrying check.**

```
CARRYING CHECK — R10
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v4 KMC-OD-STD-TARIFF)
  the price (C6)                        140.00 — band ⚠ 135.00–142.50 (F3 does not reprice)
  floor                                  55.09–107.47
  operating bar = floor × 1.25           68.86–134.34
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  price against the operating bar        140.00 − 134.34 = 5.66 at the set price · 0.66 at the band's low end · 8.16 at its top
  carries                                true at every point of the band
  margin worst corner (price − floor high) ÷ floor high
                                         30.3% at 140 · 25.6% at 135 · 32.6% at 142.5
  margin best corner (price − floor low) ÷ floor low
                                         154.1% at 140
  conventional additions used (RD-030)   R10 line ⚠ 1–3 removed (the bureau, scoring and aggregator feeds; booked here by number); added ⚠ 0.05–0.18 on the rounded layers (⚠ 0.09–0.36 unrounded); cumulative ⚠ 1.10–1.47 rounded (⚠ 0.60–2.17 unrounded); remaining ⚠ 6.53 at the high corner
  max payable to any holder (VA-164)     5.66 at central; 0 at the pessimistic corner; paid: 0.05–0.18 to the route's agents (commodity vendors)
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C10.yaml`).** By hand: **30.3% at the worst corner at the set price; 25.6% at the band's low end; 32.6% at its top; 154.1% at the best corner. PASS on the 25% gate at every point of the band.** R10 moves the worst-corner margin by 0.2 points (30.27% against C9's 30.49%). `fit_margin.py` is run on the at-C10 model; its output is in the verifier r10.

**The at-scale price hold (carried from C9).** The price of 14.0% holds at scale because the floor's high corner is 107.47 and the operating bar 134.34, both under the set price and the band's low end; R10 is what fixes the largest line of that floor. Across the rate cycle: a one-point rise in Bank Rate at a deposit beta of ⚠ 0.3–0.5 adds ⚠ 3–5 per £1,000 (worst-corner margin 26.8–24.7% — PASS to BORDERLINE at the edge); a two-point rise adds ⚠ 6–10 (23.4–19.2% — BORDERLINE); the yearly review (PC-1) is where the price answers it. A one-point fall lowers the floor by the same figures.

**Binding gate — by driving (VA-84).** Eighteen gates driven at C10: the seventeen of C9 and (18) the cap. Ordered by margin at the set price:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.45%** at the set price (4.05% at the band's low end; 4.65% at its top); the loss line is 67.47 + 10L and the bar is 112.00; zero margin at 7.25%; assumed ⚠ 2–4%; surplus 0.45 points at the assumed high corner. **First to fail.** R9 holds this band; R10 does not act on it.
2. the default-funded loss gap (C5) — on the same line; ⚠ 0.3–0.5 of the 0.45 points; unmeasured. Nil surplus at the top of that band, as at C8 and C9.
3. the price condition's room — 5.66 at the set price; 0.66 at the band's low end.
4. the rate against the lowest published EAR — 0.54 points (C6).
5. **the funding line (new reading, G-funding)** — the 25% margin fails if the line's funding cost exceeds **3.45%** at the set price (the funding line at 34.53 with every other layer at its high corner: 77.47 + 34.53 = 112.00 = 140 ÷ 1.25; 3.05% at the band's low end, 3.65% at its top; zero margin at 6.25%); the measured deposit cost is ⚠ 1.5–3.0%; surplus ⚠ 0.45–1.95 points above the assumed band, the same surplus as the loss gate leaves at its high corner; R10 is what holds it (position-holding table). Reads daily from the funding term.
6. the average seasoned uplift (G16, C8) — ⚠ 15–30%; threshold ⚠ 38% at the band's low end.
7. the calibration cohort minimum (G17, C9) — ⚠ 2,300–28,000 rows per cell against ⚠ 500.
8. **the cap (new, G18)** — the drawn book at or under ⚠ 10% of the pool's credit balances: 3.4–11.4% across the corners; surplus ⚠ £3.0bn at central; binds at the worst corner (⚠ £5.7bn drawn against ⚠ £50bn of balances) and cuts the book to ⚠ £5.0bn — a volume gate, not a cost gate; the per-£1,000 margin is unchanged by it. Reads monthly at the committee. Threshold for review ⚠ 8% for two quarters.
9. G15 — the platforms' display (C7), unchanged.
10. the connected share, unchanged.
11. the non-empty history share, unchanged.
12. the use gates — switch-off, funding-query, charge-query, display-query, seasoning-query rates (C5–C9), unchanged.
13–18. carried from C9 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, including default-funded draws and the seasoned uplift, with the rule's parameters re-fitted yearly, on a book funded inside its own pool
  threshold:    4.45% at the set price (4.05% at the band's low end · 4.65% at its top) — the 25% margin fails above it at the worst corner; zero margin at 7.25%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.45 points at the assumed high corner; the default-funded gap (C5) may consume ⚠ 0.3–0.5 of it; R9 holds the band (failure value ⚠ 4.5–6.0%); R10 holds the funding line beside it (failure value 4.0% and 4.6–5.0%) — two independent lines, each with its own hold
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the calibration is the first lever before the pivot
  reads at:     the Stage 1 12-month reading (the pool, and the first calibration run); the first replica's 24-month reading (the held-out cohort test); the funding term's daily price from Stage 1
```

**Independence (VA-97).** SHOWN at R10 for the first time in Function 3: the funding line and the loss line are independent inputs to the floor — the deposit cost is set by the depositors and the policy rate, the loss by the borrowers and the rule — and R10's hold acts on the funding line only. A failure of R9 (loss drift) and a failure of R10 (a repricing) are separate events with separate readings: the held-out cohort's loss (C9) and the funding term's daily price against the measured deposit cost (C10). Free readings named: the measured deposit cost (a rate, read daily); the drawn share of the pool's balances (a ratio, read monthly); the number of quarters the transfer price exceeded the trigger (a count). All three are readable from Stage 1; none is a transform of the loss gate.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts); at the cap's worst corner ⚠ £5.0bn. At Stage 1 (⚠ £0.4–1.9bn): floor 56.86–136.15 (the AOM v10 3c fixed layer of ⚠ £13.55m spread on the Stage 1 count, ⚠ £0.6m ÷ £0.4bn = 1.5 per £1,000 above the C3 people figure this line first carried; plus the tape's compute; the route's upkeep starts at Stage 2 when the route is set up); worst-corner margin at the set price (140 − 136.15) ÷ 136.15 = **2.8%**; −0.8% at the band's low end; 4.7% at its top. The simulation, which also applies the ⚠ 80% seasoning call to the year-one drawn balance and the cost of capital, prints −1.2% (`bank-credit-facility-fin-sim-2026-09-21.md`). Both readings say the same thing: Stage 1 does not carry the 25% margin at any point of the band — as at C3 to C9. At Stage 1 the drawn book is ⚠ 0.4–3.8% of the pool's balances; the cap is far from binding; funding is the pool's own from the first release.

**Working capital timing.** Unchanged from C6. The route's set-up (⚠ £1–3m) is a Stage 2 outlay on the path (fin-sim).

**The conventional line, priced.** The counterfactual's R10 line is ⚠ 1–3 per £1,000: bureau data, a scoring vendor and aggregator feeds bought to underwrite and monitor a conventional facility book (T4, patterned on published bureau price lists per account and per enquiry at ⚠ 228,000–760,000 accounts). The form does not carry it — the limit rule reads the account line and the ledger and nothing bought; the signal's ⚠ 0.1–0.3 is inside computing since C1. Removed here by number; R10's own addition is ⚠ 0.05–0.18 rounded.

**The hold-up resistance score (HRS) — registry row "F3 barrier scores".** The registry states the thresholds and not the terms; the terms below are the runner's, patterned on the SCIS and FIS, and are recorded for the WS1 feedback log. Scored for every supplier input in the value chain; the key input first.

| Input | Asset ownership (0–2) | Alternative availability (0–3) | Replacement time (0–2) | HRS conservative · central · optimistic | Reading |
|---|---|---|---|---|---|
| **deposit funding (the key input)** | 2 — the pool's balances are the bank's own liabilities | 1 conservative (the master trust, at a price that fails the margin) · 2 central (the trust and a warehouse line, both above the deposit cost) · 2 optimistic | 1 conservative (⚠ 12–18 months from a standing start) · 2 central and optimistic (under 12 months with the route documented and the tape maintained) | **4 · 6 · 6 without the design commitment; 5 · 6 · 6 with it** | conservative corner between NCR (3) and pass (5): the design commitment is required and is made (below) |
| the core platform's daily balance row | 2 — the bank's own ledger | 2 — any core produces the row; the engine reads it through the account line's feed | 1 — an adapter change, 12–18 months inside a core replacement | **5 · 5 · 6** | pass; the core platform as a whole scores 3 (2 · 1 · 0) and is the bank's standing constraint, not the line's |
| the fraud and conduct signal (bureau) | 0 | 3 — three bureaus | 2 — a contract switch of 3–6 months | **5 · 5 · 5** | pass |
| the standard's operator | 0 — public | 2 — the bank's own channel under PSRs 2017 reg. 69; the standard is public and any reader may implement it | 2 — a version change is absorbed by the bank's existing programme; the element is one field | **4 · 4 · 4** | between the lines; a standing constraint carried from C7 with the design commitment that the element is carried on the bank's own channel as well as through the directory; not a supplier with power — a public order compels the publication |
| model validation | 2 — the bank's own function | 3 — several external firms | 2 — under 12 months | **7 · 7 · 7** | pass |
| labour (the engine team, the cells, HQ) | 2 | 3 — the labour market | 2 | **7 · 7 · 7** | pass |
| cloud batch compute | 0 | 3 — three providers | 2 — a job moved in months | **5 · 5 · 5** | pass |
| collection agents and solicitors (write-off) | 0 | 3 — many firms | 2 — contracts under a year | **5 · 5 · 5** | pass |

**The design commitment that takes the key input from 4 to 5 at the conservative corner.** Four parts, each a build item or a standing activity in the AOM v10: (i) the tape is produced monthly from WP-6 from Stage 1, so the route's data history is as long as the form's; (ii) the programme documents are drafted before Stage 3 and refreshed yearly (the upkeep line); (iii) the cap (G18) keeps the opening size of the route under ⚠ £1bn at the worst corner, a size the public market has placed in one programme (T2); (iv) the trigger is a standing quarterly review. With the four in place the replacement time is under 12 months and the score is 5. Without them the score is 4 and the requirement would not pass the registry's line — stated so that the commitment is read as load, not as decoration.

**The score, read plainly.** The key input passes at every corner with the commitment because the input is owned and the route is ready; it is one point above the line at the conservative corner because the only alternative to the pool's funding costs more than the margin can bear. That is the finding, not a softening: R10 makes the funding replaceable for the venture's existence and cannot make it replaceable at the same price, because no market lends to a bank at its own deposit cost.

**Position-holding table (registry F3 row).** Every model assumption that depends on R10 holding; the requirement it holds because of; the failure value as a band; where it lives in the fit model.

| Assumption in the model | Holds because of | Value if R10 holds | Failure value (band) | In the fit model as |
|---|---|---|---|---|
| The funding line at the pool's deposit cost (PVC) | R10 — the line is funded inside its pool under a signed term at the measured deposit cost, with the market route beside it | ⚠ 1.5–3.0% = 15–30 per £1,000 | ⚠ 4.0% (Bank Rate — a transfer-price convention at the policy rate; FACT for the rate, T4 for the convention) = 40 per £1,000; floor high 107.47 → 117.47 | `position_holding.funding_at_bank_rate` |
| The same line, on the market route | R10 — the route is the alternative when the pool's price is overridden | as above | ⚠ 4.6–5.0% (SONIA + 0.6–1.0%, T2) = 46–50 per £1,000; floor high 117.47 → 123.47–127.47 | `position_holding.funding_at_market` |
| The route's upkeep without issuance (RC) | R10 — the route is maintained, not used | ⚠ £0.3–0.6m a year = 0.05–0.18 | ⚠ £1–2m a year if the route is opened and stays open (rating, servicing reports, note administration) = 0.18–0.59; RC 2.07–5.22 → 2.20–5.63 | `position_holding.route_running_cost` |
| The drawn book against the pool's balances (volume) | R10 — the cap | ⚠ 3.4–11.4% used; the book ⚠ £3.4–5.7bn | the pool's balances fall by ⚠ 20–40% (a deposit outflow) and the cap binds at ⚠ £3.0–4.0bn; the per-£1,000 margin is unchanged; the PCO objective is read in the fin-sim | `position_holding.cap_binds` (a volume assumption; no floor change) |

**Re-test at the failure value (by hand; the script's figure in r10).** *Funding at Bank Rate:* floor high 117.47; margin (140 − 117.47) ÷ 117.47 = **19.2% — BORDERLINE**; at the band's low end (135) **14.9% — FAIL**. *Funding at the market:* floor high 123.47–127.47; margin **13.4% — FAIL** at 4.6% and **9.8% — FAIL** at 5.0%; at 135, 9.3% and 5.9%. *Route running cost:* floor high 107.88; margin **29.8% — PASS**. *Cap binds:* margin unchanged at 30.3%; the book ⚠ £3.0–4.0bn. **The loss band, re-tested regardless of the FIS (C9's finding, at the C10 floor):** at ⚠ 4.5% the floor high is 112.47 and the margin **24.5% — BORDERLINE**; at ⚠ 5.0% it is 117.47 and **19.2% — BORDERLINE**; at ⚠ 6.0% it is 127.47 and **9.8% — FAIL**. **What the re-test says, unsoftened:** the margin depends on R10 holding the funding line at the pool's deposit cost. The market route holds the venture's existence and not its margin: at the market's price the design fails the gate at every point of the band. The design has two independent holds on the two largest lines of the floor (R9 on the loss, R10 on the funding) and a failure of either takes the margin below the gate. The HRS passes with the commitment, so the registry row does not require the verifier to re-test; the verifier r10 re-tests regardless and reports it.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Customer of record declared; one run; the routine positioned in named ✓ (VA-154).
- F3 ordering — the value chain mapped and the key input identified at SR1 before any theory ✓. VA-23 at Diagnose — the block tested is the at-scale supplier's power, not a pilot's ✓.
- Interim value chain mapped with eight inputs ranked by cost × volume; the five diagnostic questions answered; the block named as one operation (the line's funding priced by a convention outside the line) ✓ (SR1). Seven other candidates excluded by reason ✓. The shelf check at launch run — no supplier binds ✓. VA-92 existence test with the affordability screen stated first — max payable 4.71 per £1,000 at the set price, 0.71 at the band's low end; the route exists at ⚠ 0.09–0.36 ✓. VA-101 applied — the limit is of the world (a deposit franchise is cheaper than wholesale money), with the value resting on it stated ✓.
- ToC — parameter named ✓; theory named with researcher, year and paper ✓ (Klein, Crawford and Alchian 1978; supported by Drechsler, Savov and Schnabl 2017); contrast theories named (Williamson 1985; Diamond and Dybvig 1983) and answered ✓; fragile-findings check ✓; context and outcome as states ✓; hypothesis with falsification condition on the theory and four named assumptions ✓.
- Strategy — one sentence; exactly one structural decision ✓; mutation gate emitted before the strategy; six mutations (A–F), two not available; justification mode false ✓; supplier-power approach named (structural bypass) ✓; the architectural decision test passed (the move, not its outcomes; the route inside the move, not beside it) ✓; the at-scale test with the cap's worst corner stated ✓; R1 continuity ✓; R9, R2 and R6 interactions ✓; structural not contractual ✓.
- Productising — structural against contractual scarcity of the input ✓; the customer sees nothing, with the paused release named ✓; data-protection and prudential positions stated with what a ruling would settle ✓; at-scale test with the volume and no person added ✓.
- Cumulative BFF (C1–C10) read cold as one product; central mechanism named; the evolution test run and passed; components listed with the new one ✓ (parent's instruction; the challenge skill's F3 note overridden as at C8 and C9 and recorded in the WS1 feedback log).
- Considered and not chosen — ten entries with reasons ✓ (VA-4). Synthesis check with the analogue's limit ✓ (VA-1).
- VA-106 line, nine candidates, five served, four "no" with reasons; the Phase 3 moat test's condition met on this line (five other requirements named) ✓. VA-103 table, nine rows, no FAILED row; the function-gate re-run line printed ✓. VA-127 table, two arithmetic lines per row; every row PASS or nil by design; no FAIL to force ✓. VA-102 three questions answered ✓. VA-82 classified ✓.
- No forward references (VA-80) ✓ — the audit and the verification were named as not yet written with the rule that names them, and entered by filename once written. Launch constraints absent (VA-23) ✓. Completeness contract (VA-73) ✓.
- Conventional cost line named (⚠ 1–3, removed by number) with the reason; the cap line printed with the rounded and unrounded figures ✓ (F3 rule).
- Binding gate by driving ✓ (18 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162). Independence SHOWN ✓ (VA-97).
- Position-holding table — four assumptions, each with the requirement it holds because of, the failure value as a band and its place in the fit model ✓; re-test at the failure value by hand, unsoftened (19.2% BORDERLINE at Bank Rate; 13.4% / 9.8% FAIL at the market; the loss band repeated) ✓ (registry F3 row).
- **F3 barrier score (HRS): 4 · 6 · 6 without the design commitment; 5 · 6 · 6 with it — PASS at every corner with the commitment, which is made** ✓. The HRS terms are the runner's; recorded for WS1.
- Verdict order (VA-95) ✓ — `check_verdict_order.py` on the verdict record with R10 added. Loop-gate branch (VA-153): no FAIL on the design's FIT. Loop-backs (VA-151): 0.
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r10-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v10 and AOM v10 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v10 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. The release track carries the cap reading at a sitting it already holds; the pricing track carries the funding term's price at a review it already holds ✓ (VA-102). **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at central (21,900 at the high corner) on ⚠ 100,000 drawn accounts per cell; 14 handlers (band 13–15) — unchanged by R10, which adds no cell activity. Result: PROVISIONAL (one build item).

**Financial check.** Margin 30.3% at the worst corner at the set price (25.6% / 32.6% at the band's ends), 154.1% best, by hand; PASS at every point; `fit_margin.py` run on the at-C10 model (verifier r10). Carrying check: carries; room 5.66 at the set price, 0.66 at the band's low end. Binding gate: the loss rate, unmeasured, threshold 4.45% at the set price; R9 holds the band; R10 holds the funding line (threshold 3.45%); at R10's failure values the margin is BORDERLINE (19.2% at Bank Rate) and FAIL (13.4–9.8% at the market). Conventional additions ⚠ 1.10–1.47 of ⚠ £8 rounded. **Phase II capital gate (Function 3 close):** at the conservative scenario the margin is 30.3% against the 60% line — **BORDERLINE** (25–59%); the binding input is the loss rate: the conservative corner clears 60% only if the loss band's high corner is ⚠ 2.0% (floor high 87.47) with every other layer at its high corner, or if the funding line is at 1.5% and the loss at ⚠ 2.6%; what tightens the reading is the Stage 1 twelve-month loss reading. At central (floor 81.28) the margin is 72.2% — PASS. Printed in full in the fin-sim. Result: PROVISIONAL.

**What was decided about each check that did not pass.**
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- The margin's dependence on R10 (the position-holding re-test) — **design finding**: the funding line is held by the pool funding and by nothing else at the same price; the market route holds existence, not margin. Owner: the runner, at the C10 consistency audit (the moat test reads it beside the SCIS finding and the R9 finding). Convergence: the funding term's first year of daily readings from Stage 1.
- The margin's dependence on R9 (C9) — **design finding, carried**; re-tested at the C10 floor above, unsoftened.
- The Phase II gate at BORDERLINE — **finding of the function close**: the conservative corner is 30.3% against 60%; owner: the runner at the fin-sim and the summary; convergence: the Stage 1 twelve-month loss reading, which is the one input that can move the conservative corner past the line.
- The pool's credit balances (⚠ £50–100bn) — **unmeasured input**; owner: treasury; convergence: the first cap reading at Stage 1.
- The measured deposit cost (⚠ 1.5–3.0%) and the deposit beta (⚠ 0.3–0.5) — **unmeasured inputs**; owner: treasury; convergence: the funding term's first four quarters.
- The route's set-up (⚠ £1–3m) and upkeep (⚠ £0.3–0.6m) — **unmeasured inputs**; owner: treasury; convergence: the arranger's quote before Stage 3 and the first year's invoices; threshold ⚠ £1.0m a year on the upkeep.
- The route's all-in price on opening (⚠ SONIA + 0.6–1.0%) — **unmeasured input**, unobservable until the trigger; owner: treasury; falsification condition in SR2.
- The cap's worst-corner bind (⚠ £5.0bn against the proxy's ⚠ £5.7bn) — **structural limit, new at C10**: the line's size is bounded by the pool's balances; the deposit franchise is Case A's resource and R10 cannot enlarge it. Owner: the Studio Director (a Case A question by number).
- The funding term's signature and the cap — **build items**; owner: treasury and the asset and liability committee; convergence: before the first release (Stage 1).
- The standby route's documents and the first tape — **build items**; owner: treasury and the engine team; convergence: before Stage 3.
- The prudential and data-protection positions on the route — **standing constraints, designed for**, with what a ruling would settle named (nothing new); owner: treasury and the data-protection function.
- The HRS terms undefined in the registry — **method finding** for the WS1 feedback log; owner: the Head of R&D.
- The fixed-against-linked price question (C6) — **carried question**, with R10's mechanism attached; owner: Tom.
- C9's and earlier carried items — carried unchanged; the SCIS design finding carried.

```
GATE VERDICT — on the cumulative architecture C1 to C10
  logical limb:      PASS            checks failed: 0 (HRS 5 · 6 · 6 with the design commitment; 4 at the conservative corner without it)
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     margin 30.3% worst corner at the set price (25.6% at the band's low end / 32.6% at its top) / 154.1% best (by hand; `fit_margin.py` output in verifier r10) · binding gate the loss rate on the pool: surplus 0.45 points at the assumed high corner, unmeasured; R9 holds the band · the funding line: threshold 3.45%, measured ⚠ 1.5–3.0%, R10 holds it — at its failure values 19.2% (Bank Rate, BORDERLINE), 13.4–9.8% (the market, FAIL) · conventional additions used ⚠ 1.10–1.47 of ⚠ £8 rounded (⚠ 0.60–2.17 unrounded); remaining ⚠ 6.53
  price:             14.0% simple a year on the daily drawn balance = £140 per £1,000 drawn (band ⚠ 135–142.5); no fee; collected from receipts (C6, unchanged; F3 does not reprice)
  partner:           none new; the standby route's agents are commodity vendors
  decisions:         45 unmeasured inputs (39 carried, 6 new), 18 build items (14 carried, 4 new), 1 standing-constraint set (1 new row: the prudential and data-protection positions on the route), 4 structural limits (3 carried; the cap's worst-corner bind, new), 1 carried question (fixed against variable, C6, with R10's mechanism attached), 3 design findings (the SCIS, carried; the margin's dependence on R9, carried; the margin's dependence on R10, new), 1 method finding (the HRS terms), 1 function-close finding (the Phase II gate BORDERLINE); 0 actor-level FAIL
  capacity figure:   20,400 exception hours per cell a year at central (21,900 at the high corner), 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15) at 1,400–1,600 productive hours — unchanged by R10   VA-91
  independence:      SHOWN — the funding line and the loss line are independent inputs with separate holds (R10, R9) and separate readings; three free readings named, all readable from Stage 1   VA-97
  gates driven:      18; first to fail on evidence: the loss rate, margin 0.45 points at the set price; second: the default-funded gap on the same line; third: the price condition's room (5.66); the funding line fifth (surplus ⚠ 1.0–2.5 points); the cap eighth (a volume gate; binds at the worst corner)   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r10-2026-09-21.md   VA-90
  inherited:         R9, R8, R7, R6, R5, R4, R3, R2, R1 PROVISIONAL — R10 cannot exceed them; F1 and F2 closed PROVISIONAL with conditions carried   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design's FIT; the position-holding re-test's BORDERLINE and FAIL are at the failure values, not the design value — recorded as a design finding with owner and convergence; the model files are build items   VA-153
  launch constraints:none inside SR1–SR3 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn (⚠ £5.0bn at the cap's worst corner); at the Stage 1 count the worst-corner margin is 2.8% at the set price, −0.8% at the band's low end (AOM v10 fixed layer); the cap is far from binding at Stage 1   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; the funding line is a second, independent input to the margin with its own gate (3.45%) and its own hold   VA-160
  function gate:     F3 (C8–C10) — CLOSES PROVISIONAL at this record: SCIS 2 · 4 · 6 (C8, below the line — design finding), FIS 5 · 6 · 7 (C9), HRS 5 · 6 · 6 with the commitment (C10); the function-gate re-run (the consistency audit and the verification) written after this record and entered in VA-103 and the changelog
  Phase II gate:     BORDERLINE — 30.3% at the conservative scenario against 60%; binding input the loss rate; what tightens it: the Stage 1 twelve-month loss reading; central 72.2% PASS
  VERDICT:           PROVISIONAL
```

**R10 failure test.** Would R10 have failed? Three conditions. First, the venture has no answer if the supplier raises its price by 40% tomorrow: it has — the price is a reading under a signed term, and above the market's price the route opens. Second, the move is diversification or a contract: it is not — the input is owned by construction and the route is a vehicle the bank owns; the term records a price, it does not set one. Third, the alternative does not exist or is unaffordable: it exists (three public precedents) and costs ⚠ 0.09–0.36 against a screen of 4.71. R10 stands. What it does not do is stated in the same breath: the route holds the venture's existence, not its margin, and the margin's dependence on the pool's price is the finding this record carries.

---

## Carried items (VA-82)

- **Forward-referenced:** none — R10 is the last requirement. The consistency audit and the verification are the function-gate re-run (VA-103), written after this record and entered in the changelog.
- **Unmeasured inputs (new at C10, 6):** the pool's credit balances; the measured deposit cost; the deposit beta; the route's set-up cost; the route's upkeep; the route's all-in price on opening. **Carried from C1–C9 (39):** unchanged.
- **Build items (new at C10, 4):** the funding term and the cap; the standby route's documents; the first tape; the trigger's quarterly review. **Carried (14):** the CTM and AOM model files; the accrual ledger; the charge-first split; the representative example and APR basis; default funding's authorisation, notice and record; the term and the CONC 4.7 information; the limit-history placement; the release order's instrumentation; the element's population rule; the conformance test; the seasoning input and schedule in the engine; the 15th handler line at the high corner; the ledger and the calibration run; the held-out cohort design.
- **Standing constraints (new at C10):** the UK Securitisation Regulation's retained interest and the Article 28 processor contract on the route — designed for, with what a ruling would settle named (nothing new). C9's and earlier: unchanged.
- **Structural limits (carried, 3; new, 1):** the C1 limit rule's exposure model; the Stage 1 margin below 25% at every point of the band; the unconnected account's single conviction moment; **new at C10:** the line's size is bounded by the pool's balances — the cap binds at the worst corner and R10 cannot enlarge the deposit franchise (Case A's resource, by number).
- **Design findings:** the SCIS below the pass line (C8, carried); the margin's dependence on R9 (C9, carried); **new at C10:** the margin's dependence on R10 — the funding line is held at the pool's price by the pool funding and by nothing else; the market route holds existence, not margin.
- **Method finding (new at C10):** the HRS terms are not defined in the registry; the runner's decomposition is used and recorded for WS1.
- **Function-close finding (new at C10):** the Phase II gate reads BORDERLINE at the conservative scenario; the binding input is the loss rate.
- **Carried question (C6):** a fixed rate against a Bank Rate–linked rate — with R10's mechanism attached (the funding line moves with the deposit beta, not with Bank Rate).
- **TAM data object:** v4 written at this record — the cap (G18) named as a block at the worst corner; the C8, C9 and C10 records, the at-C8 to at-C10 fit models and the fin-sim added as consumers; the checking script run (verifier r10).
- **F2 audit and verification items:** S1, S3, F-5, F-6 carried to the C7 record's next regeneration; F-3, F-4 carried — all read at the C10 audit.
- **Carried to pilot-instance design after R10 (VA-23):** none — the route's set-up before Stage 3 and the term's signature before Stage 1 are path events (fin-sim), not launch constraints in the design.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Customer of record declared; one run per customer of record (VA-154) | PASS — one | header |
| F3 ordering — the value chain before theory; VA-23 at Diagnose | PASS | SR1 |
| Interim value chain mapped and ranked; key input named; five diagnostic questions; the block as one operation | PASS — deposit funding; the line's funding priced by a convention outside the line | SR1 |
| Other candidate inputs excluded by reason | PASS — seven | SR1 |
| Shelf check for any supplier binding at launch | PASS — none binds | SR1 |
| VA-92 existence test with the affordability screen first | PASS — max payable 4.71 (0.71 at the band's low end); the route exists at ⚠ 0.09–0.36; three public precedents | SR1 |
| VA-99 business case on every enabler except a commodity vendor | PASS — the route's agents are commodity vendors; no other enabler | SR1, VA-127 |
| VA-101 — the limit is of the world; value resting on it stated | PASS — a deposit franchise is cheaper than wholesale money; the funding line | SR1 |
| ToC parameter, theory (researcher, year, paper), context, outcome | PASS — Klein, Crawford and Alchian 1978; Drechsler, Savov and Schnabl 2017 | SR2 |
| Contrast theory named; fragile-findings check | PASS — Williamson 1985; Diamond and Dybvig 1983; none on the list | SR2 |
| Hypothesis with falsification condition; named assumptions | PASS — four | SR2 |
| Mutation gate before the strategy; ≥ 2 genuine mutations; justification mode false | PASS — six | SR3 |
| Exactly one structural move; supplier-power approach named | PASS — PC-2; structural bypass | SR3 |
| Architectural decision test — the move, not its outcomes | PASS | SR3 |
| Genuine replaceability, not reduced dependency ("if the supplier raised prices by 40% tomorrow") | PASS — the price is a reading; above the market's the route opens; the gap to the market's price is stated as the finding | SR3, Financial |
| R1 continuity; structural not contractual; at-scale test | PASS | SR3 |
| Cumulative BFF read cold; central mechanism named; the evolution test (mandatory at C10) | PASS — in kind, not in count | BFF |
| Considered and not chosen with reasons (VA-4) | PASS — ten | Considered |
| Synthesis check with the analogue's limit (VA-1) | PASS — the building-society funding limit | Synthesis |
| VA-106 line — every requirement; "no" with reason; Phase 3 moat condition (≥ 2 other requirements on one line) | PASS — five served, four no; condition met | VA-106 |
| VA-127 — one row per behaviour; two arithmetic lines; FAIL rows forced | PASS — seven rows; none to force | VA-127 |
| VA-102 — tracks opened at arrival; counterparty drivers | PASS — a funding track, three states | VA-102 |
| VA-103 — every earlier requirement re-verified; FIT per row; function-gate re-run line | PASS — nine rows; the function-gate re-run entered by filename in the changelog | VA-103 |
| VA-80 — no forward references | PASS | throughout |
| VA-23 — no launch constraints in the design | PASS | throughout |
| VA-73 — completeness contract | PASS | throughout |
| Conventional line named and removed; cap line printed (F3 rule, RD-030) | PASS — ⚠ 1–3 removed by number; 6.53 remaining | Financial |
| ABC bottom-up, every line with driver and volume (RD-031) | PASS — seven lines | Financial |
| Four-layer floor printed; each layer with tier and basis | PASS — 55.09–107.47 | Financial |
| Carrying check printed | PASS — carries | Financial |
| Margin ≥ 25% at the worst corner | PASS — 30.3% (25.6% at the band's low end) | Financial |
| Binding gate by driving (VA-84) | PASS — 18 gates; the loss rate first; the funding line fifth | Financial |
| Independence (VA-97) | SHOWN — two independent lines with separate holds and readings | Financial |
| Spread count (VA-162) | PASS — printed; Stage 1 2.8% at the AOM v10 fixed layer | Financial |
| Shared input (VA-160) | PASS — the loss rate; the funding line independent | close |
| Position-holding assumption named (F3) — table; each assumption in the fit model; re-test at the failure value | PASS — four assumptions; re-test 19.2% / 13.4% / 9.8% on the funding line, and the loss band repeated, printed unsoftened | Financial |
| **F3 barrier score — HRS ≥ 5 pass; ≤ 3 NCR** | **PASS with the design commitment — 5 conservative · 6 central · 6 optimistic (4 conservative without it); terms undefined in the registry — method finding** | Financial |
| Three-limb close; GATE VERDICT block (VA-89, VA-91) | PASS — printed, with the function gate and the Phase II line | close |
| Capacity figure, one number (VA-91) | PASS — 20,400 (21,900 at the high corner) | close |
| Verdict composition (VA-95); `check_verdict_order.py` | PASS — PROVISIONAL; IN ORDER (verifier r10) | close |
| Loop-backs (VA-151); loop-gate branch (VA-153) | PASS — 0; no FIT FAIL at the design value | close |
| Carried items classified (VA-82) | PASS | Carried |
| Verification artefact exists (VA-90) | PASS — verifier r10 | close |
| Incremental write (VA-88) | PASS | header |
| WS1 feedback capture (autonomous mode) | recorded in the WS1 feedback log's F3 section | — |
| House-style checker run | recorded in the status file | — |

---

## Quality check

- Does the strategy manufacture replaceability, or only reduce risk? **Manufactures it** — the input is owned by construction and a market route is held ready; the price cannot be set from inside above the market's, and the input cannot be withheld from outside.
- Could an incumbent adopt it without adopting the new BFF? **No** — a conventional facility book has no pool of its own: its borrowers are a selected subset of the bank's customers and its funding is whatever treasury allocates; the pool funding the pool needs a line that is a property of every account with enough flow (C1) and a split that turns the balances over (C6).
- Is the evolution test genuine? **Yes** — the C10 form is a pool with its own parameters, funding, growth and reach; the C1 form is a rule on one account; the difference is in kind.
- Is the input distinct from R9's resource? **Yes** — R9 holds what a rival cannot get (the outcome ledger); R10 holds what a supplier cannot reprice or withhold (the pool's funding). The ledger serves R10 as the tape; the tape is not the resource.
- Confidence: **Medium-high** on the mechanism (the pool's balances exceed its drawn balances by ⚠ 9–29 times; master trusts exist; the deposit channel is well documented); **medium** on the price the route would open at (T2, unobservable until the trigger) and on the deposit beta (T4); the margin's dependence on the pool's price is stated and is the finding this record carries.

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15, C5 G1–G10, C6 H1–H12, C7 I1–I13, C8 J1–J13, C9 K1–K8)

- L1 — Klein, B., Crawford, R. G. and Alchian, A. A. (1978), "Vertical Integration, Appropriable Rents, and the Competitive Contracting Process", *Journal of Law and Economics* 21(2): 297–326.
- L2 — Drechsler, I., Savov, A. and Schnabl, P. (2017), "The Deposits Channel of Monetary Policy", *Quarterly Journal of Economics* 132(4): 1819–1876.
- L3 — Williamson, O. E. (1985), *The Economic Institutions of Capitalism*, Free Press. Contrast.
- L4 — Diamond, D. W. and Dybvig, P. H. (1983), "Bank Runs, Deposit Insurance, and Liquidity", *Journal of Political Economy* 91(3): 401–419. Contrast.
- L5 — Building Societies Act 1986, s.7 (the funding limit — at least 50% of funds from members' shares). FACT. Synthesis check.
- L6 — Public UK revolving master-trust and small-business securitisation programmes: Penarth Master Issuer plc (credit-card receivables); Delamare Cards MTN Issuer plc (credit-card receivables); SBOLT 2016-1 (small-business loans, 2016). Existence test, programme timetables and fee schedules from their public offering documents. T2.
- L7 — Bank of England: Bank Rate 4.0% from August 2025 (FACT); SONIA published daily (T1).
- L8 — UK Finance, Business Finance Review, and Bank of England Bankstats — small and medium-sized business deposit balances across UK banks. T2, approximate; the bank's share is T4.
- L9 — UK Securitisation Regulation (as retained and amended, 2024) — risk retention of at least 5% of the material net economic interest; the PRA's significant-risk-transfer rules. FACT.
- L10 — Regulated Covered Bonds Regulations 2008 (SI 2008/346), eligible property. FACT. Mutation E.
- L11 — Bank of England, Term Funding Scheme with additional incentives for SMEs — drawdown window closed 31 October 2021. FACT. Mutation D.
- L12 — Capital Requirements Regulation, Part Six, Title IV (net stable funding ratio) — available-stable-funding factors of 90–95% for retail and small-business deposits. FACT.
- L13 — UK GDPR Articles 4(5), 28 and Recital 26; the ICO's guidance on pseudonymisation and processor contracts. Read for the position at Productizing.
- L14 — Published credit-bureau price lists for business-account monitoring and enquiry products, September 2026. T2, for the conventional R10 line.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | Created at R10 by the runner (Path C, mode 3, autonomous). PROVISIONAL, capped by R1–R9 (VA-95). Object-after to 23 September 2026 17:00. Third and last requirement of Function 3; F3 closes PROVISIONAL. HRS 5 · 6 · 6 with the design commitment (4 at the conservative corner without it). Position-holding re-test on the funding line printed unsoftened (BORDERLINE at Bank Rate, FAIL at the market) and carried as a design finding. Phase II gate BORDERLINE at the conservative scenario. Function-gate re-run: not yet at this version. House-style checker run on this file: result recorded in the status file. |
| v1 — correction | 21 September 2026 | The funding-line gate (G-funding) first printed as 3.99% did not reproduce (funding at 39.9 gives a margin of 19.3%, not 25%). Corrected to 3.45% at the set price with every other layer at its high corner (3.05% at 135; 3.65% at 142.5; zero margin at 6.25%); surplus above the measured deposit cost ⚠ 0.45–1.95 points. Found by the verifier r10; no other figure moves. |
| v1 — S4 closed | 21 September 2026 | Spread count (VA-162) re-stated on the AOM v10 3c fixed layer (⚠ £13.55m) in place of the C3 people figure (⚠ £12.95m): Stage 1 worst-corner margin 4.0% → 2.8% at the set price (−0.8% / 4.7% at the band's ends); the simulation's −1.2% after seasoning and the cost of capital cited beside it. S4 of the C10 consistency audit. The at-scale margin, the floor and the verdict are unchanged — Stage 1 was not carrying the gate before and does not now. |
| v1 — H1 closed | 21 September 2026 | Route-back H1 executed: C3 record v2 (`bank-credit-facility-c3-v2-2026-09-21.md`) re-sets the trial band's continue line to ≤ ⚠ 4.45% at £140 (4.05% at ⚠ £135), borderline 4.45–5.0%, kill > ⚠ 5.0% unchanged; the CTM v10 release-track row (v10.1) and the function status file carry the same values. No design change; the C10 verdict and margin are unaffected. |
| v1 — function-gate re-run | 21 September 2026 | The consistency audit C10 (`bank-credit-facility-consistency-audit-C10-2026-09-21.md`) and the verification (`bank-credit-facility-verify-C10-2026-09-21.md`) written after this record and the financial simulation (`bank-credit-facility-fin-sim-2026-09-21.md`). Audit: COHERES, one route-back (H1 — the C3 trial band's continue line ⚠ 4.8% is above the 4.45% gate at the C10 floor; re-set in the C3 record, not patched here), four soft items (S1 funding gate at the quarterly sitting; S2 the recurring fixed layer's ⚠ 1.06 reserve; S3 R7–R8 tension resolved at R9; S4 two Stage 1 figures). Verification: SOUND 87.7 (completeness 90.0, consistency 65, discipline 95.8, synthesis 100), validation-maturity pre-operational; three premature details (the 90-day cut, the yearly run, the before-Stage-3 date) to be recast as convergence items. No figure in this record moves. |
