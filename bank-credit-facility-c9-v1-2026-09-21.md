# A business bank's credit facility line — challenge nine (R9) record v1 · Path C, mode 3 · 21 September 2026

**Verdict, first:** PROVISIONAL. R9 asks what a rival with any budget cannot buy. At C8 the answer is the account's own record — but the record is per account, and a rival with enough consented feeds could reconstruct much of it. What no rival can reconstruct is the pool's record of outcomes under the form: how often a limit set by the rule at each multiple was drawn, how fast each draw cleared through the receipts share, and what was lost, by cohort (seasoning × flow band × release stage). That record exists only where the form has run, and the form has run only here. The one move makes it the rule's calibration source: the base multiple and the seasoning schedule are re-fitted yearly from the pool's own outcome ledger, with no external score in the limit rule. A rival can copy the rule's shape on day one and cannot copy its parameters until it has run its own line for its own release stages — ⚠ 27–54 months — on its own pool. Component: WP-6 — the outcome ledger and calibration. The verdict cannot exceed R1–R8 (VA-95). Margin at the worst corner 30.5% at the set price (25.8% at the band's low end; 32.8% at its top); best corner 154.4%. Conventional additions used against the ⚠ £8 cap: ⚠ 1.05–1.29 rounded through R9 (⚠ 0.50–1.81 unrounded); remaining ⚠ 6.71 at the high corner. The first-imitator score (FIS) is 5 conservative, 6 central, 7 optimistic — PASS at every corner. The position-holding re-test at the loss band's failure value is printed unsoftened: at ⚠ 5% the margin is 19.4% (BORDERLINE); at ⚠ 6% it is 10.0% (FAIL). The margin depends on R9 holding.

**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. **Entry:** `bank-credit-facility-c8-v1-2026-09-21.md` (R8, PROVISIONAL, object-after to 23 September 2026 17:00), and the C7 to C1 records (each PROVISIONAL); F1 closed PROVISIONAL at C3; F2 closed PROVISIONAL at C7 (audit PASS WITH CONDITIONS; verification 93.1 SOUND). **PCO:** `bank-deposits-lending-pco-v1-2026-09-18.md` — ratified by lapse 20 September 2026 17:00. **Mode:** 3 — just show me. **Runner:** Finrad, acting for Tom under the propose-and-confirm and derived-work rules; every call in this record that a runner can make is tagged *runner's call*. **Confidentiality:** the bank is not named; every internal figure is a red field `⚠ [name]`; public and generic sources only. Every ⚠ figure is Tier 4 until the insider corrects it.

**Written skeleton first (VA-88); every section filled in order; no section refers forward except by number (VA-80).**

**Research clusters not run: desk-based design, no fieldwork planned.**

**The F3 rule this record works under (Tom, 16 September 2026).** R8 to R10 make the at-scale price and cost hold. R9 does it by making one resource unavailable to a rival at any budget — the registry's test is VA-101's: could any competitor, with any budget, remove the limit? The conventional R9 line in the counterfactual (RD-030) is ⚠ 0 per £1,000: a conventional overdraft book carries no resource moat of its own — its relationship managers are the R1 line (removed at C1) and its bureau data is a supplier input (R10 by number). Nothing is removed at R9; the cap moves only by what the one move costs.

**F3 ordering (challenge skill).** Identify the resource first; the theory and the strategy follow from it. The key resource is named at SR1 before any theory is chosen. **VA-23 at Diagnose:** the block tested is the at-scale one — a rival at the bank's scale, not a pilot's.

**Customer of record (VA-154).** The business owner who holds the account (the migrated overdraft user and the never-borrowed customer with enough flow — one customer of record, one payer). The routine positioned in: the rule's own routine on the customer's account — set the limit, fund the event, clear it, record the outcome, re-set the limit. One run. No supplier binds at launch (the C10 shelf check is R10's by number).

**Sections in this record.** Defined terms. SR1 to SR3 with the mutation gate. Productizing. Cumulative business form factor (C1–C9). Considered and not chosen. Synthesis check. VA-106. Actor business cases and tracks. BFF delta with the re-verification of C1–C8. Financial check with the position-holding table and the first-imitator score. The close. Carried items. Checks run. Quality check. Sources. Changelog.

---

## 0 · Defined terms

- **Required core competency** — the capability the venture must have to deliver the value proposition: setting a standing limit on every account with enough flow, with no application, at a loss rate inside the band the price carries.
- **Key resource** — the asset that enables the competency and for which a rival has few or no alternatives: the pool's outcome ledger.
- **Outcome ledger (WP-6)** — the pool's record of every limit the rule set, every funded event, its clearance or its loss, and the multiple in force at the time, kept by cohort: seasoning (C8) × flow band (C1) × release stage (C3). Per-account rows are the customer's (C8: the seasoning line); the cohort aggregates are the bank's.
- **Calibration** — the yearly re-fit of the rule's parameters — the base multiple of flow by flow band and the seasoning schedule — from the outcome ledger, by the limit-engine team, validated by model risk (SS1/23) and approved at the release-track sitting. The published schedule (C8) is the calibration's current output.
- **Generic rule** — a limit rule whose parameters are set once from public or bought data (a bureau score, an industry loss table) and not re-fitted from the pool's own outcomes. The rival's rule on day one.
- **Replication lag** — the time a rival needs to hold a comparable ledger: ⚠ 27–54 months. *Runner's call*: ⚠ 0–12 months to build the form's split and seasoning field (without them there is no comparable outcome to record), then its own Stage 0 to Stage 2 on its own pool (C3's release order) — Stage 0 back-test ⚠ 3–6 months, Stage 1 twelve months, two replicas at six months each — ⚠ 27–42 months of stages.
- **First-imitator score (FIS)** — the registry's barrier score for R9: the compound rate of the resource (0–3), the replication lag (< 12 months 0; 12–36 months 1; > 36 months 2) and capital independence (0–2). Maximum 7; ≥ 5 pass; ≤ 3 NCR.
- **Time compression diseconomies** — Dierickx and Cool's term: an asset stock built faster costs more than proportionally, or cannot be built faster at all; a ledger of outcomes over 36 months cannot be bought in 12.

---

## SR1 — Required core competency and key resource

*Customer of record: the business owner who holds the account; the routine positioned in: the rule's own routine on the account — set, fund, clear, record, re-set.*

**(a) The required core competency.** Setting a standing limit on every account with enough flow, with no application, at a loss rate inside the band the price carries (⚠ 2–4% at C1; the binding gate at every challenge since). Everything the form does — the price below the tariff (C2), the release order (C3), the history (C4), the default funding (C5), the split (C6), the published line (C7), the seasoned limit (C8) — is delivered by a rule that sets the multiple of flow. The competency is setting that multiple right: high enough that the limit covers the customer's shortfalls, low enough that the loss stays inside the band.

**(b) The key resource.** The rule's parameters come from somewhere. At C1 they came from the back-test on the bank's own account history (Stage 0) — a history of overdraft conduct, not of conduct under the form. At C8 the seasoning schedule's figures are all Tier 4. What sets the multiple right, at scale, is the record of what happened when the rule set it: which limits were drawn, how fast the draws cleared through the receipts share, and what was lost — by seasoning, flow band and stage. That record is the outcome ledger. It exists only where the form has run.

**The four diagnostic questions.**

1. *If a rival wanted to replicate the venture, what single resource would be hardest to acquire?* Not the rule — the rule's shape is a page. Not the account data — the CMA Order made it readable by any authorised provider (C7). The outcome ledger: a rival can read what the account did; it cannot read what a limit set by this rule at this multiple did, because no such limit existed on the rival's book.
2. *Tacit, intangible, perishable or complex?* Intangible (data) and time-compressed: it accumulates at the rate the form runs, one cleared event at a time, and it cannot be bought at any price because no one else holds it.
3. *Does it exist in the world, or must the venture make it?* It does not exist; the form makes it. At C8 the seasoning field is written per account; the ledger is the same events kept by cohort with the multiple in force and the outcome. Nothing new is observed.
4. *Natural or manufactured scarcity?* Manufactured by the form's own operation: the scarcity is that the form has run here and nowhere else. It is not manufactured by a contract, a patent or an exclusive licence.

**The block, named as one operation.** The rule's parameters are set from outside the rule's own outcomes. At C8 the base multiple is the Stage 0 back-test's and the schedule is a set of Tier 4 figures; neither is re-fitted from what the rule did. A rival with a generic rule and the same feed starts level with the bank on parameters, because the bank's parameters are not yet the pool's. The C8 record left the calibration to R9 by number; this is it.

**Why this is not the other candidates.** *The limit engine* — 25 people and a computation; any bank at scale has one; a lead time, not a resource (skill failure pattern: "a resource a well-resourced competitor could acquire in 12–18 months by spending money"). *The account base* — Case A's resource, not the line's; and the feed made the base's data readable. *The seasoning record per account* — C8's store, the customer's, exportable; a rival that reads enough exports sees the per-account record and still cannot see what multiple was in force or what was lost on it. *The brand* — not a resource of the form. *Regulatory permission* — every UK bank holds it.

**VA-101 test at SR1.** Could any competitor, with any budget, remove the limit? A rival can buy the engine, the people and the feed. It cannot buy 36 months of the form running on a pool it does not have; it can only run its own line for its own ⚠ 27–54 months. The limit is of the world (time compression), not of the design. The value that rests on it: the loss band (⚠ 2–4%) at scale, which is the binding gate; stated in the position-holding table.

---

## SR2 — Lock-out theory of change

**Parameter the resource rests on.** An asset stock that can only be accumulated by operating cannot be bought, and accumulating it faster than the operation runs costs more than proportionally or is not possible.

**Theory.** Dierickx, I. and Cool, K. (1989), "Asset Stock Accumulation and Sustainability of Competitive Advantage", *Management Science* 35(12): 1504–1511. Assets that confer advantage are stocks accumulated by flows over time; a rival cannot buy the stock, only start the flow. Four properties make the stock hard to imitate: *time compression diseconomies* (the stock cannot be built faster by spending more), *asset mass efficiencies* (a larger stock accumulates faster — here, a larger ledger calibrates more precisely, which lowers loss, which raises the limit the rule can set, which produces more events), *interconnectedness* (the stock's value depends on other stocks the rival also lacks — the split, the release order, the seasoning field) and *causal ambiguity*. The mechanism used here is the first two. Supported by Arrow, K. J. (1962), "The Economic Implications of Learning by Doing", *Review of Economic Studies* 29(3): 155–173 — cost falls with cumulative output, and cumulative output is what a late entrant lacks.

**Contrast.** Barney, J. B. (1991), "Firm Resources and Sustained Competitive Advantage", *Journal of Management* 17(1): 99–120 — the resource-based view's four tests (valuable, rare, inimitable, non-substitutable). Descriptive: it says which resources confer advantage and not how to make one; Dierickx and Cool say how. A second contrast is the Open Banking premise (C7): account data is public by order. The theory survives it because the CMA Order covers what the account did, not what the lender's rule did on it — the ledger's outcome column (the multiple in force; cleared or lost) is not in any feed.

**Fragile-findings check.** Dierickx and Cool 1989 and Arrow 1962 are analytical models, not empirical findings; neither is on the fragile-findings list. Barney 1991 is a framework. No replication question arises.

**Context in which the mechanism holds.** The form runs on the pool (C3's release order). Every funded event and its outcome is recorded with the multiple in force (C6's split makes clearance an observed state). The rule's parameters are re-fitted from the ledger and validated (SS1/23). The rival's rule is generic or is fitted on the rival's own smaller, younger ledger.

**Outcome.** The bank's rule sets the multiple with a loss inside the band at a limit a generic rule cannot match without a higher loss — the winner's curse (C8, Sharpe 1990) now at the level of the pool: a rival that matches the bank's limit with generic parameters carries the loss the bank's calibration avoided. The outcome is a loss rate on the calibrated rule below the generic rule's by a measurable margin, and a rival that cannot offer the same limit at the same price for ⚠ 27–54 months.

**Hypothesis (falsifiable).** At the first replica's 24 months, the loss rate on limits set by the re-fitted parameters is at least ⚠ 0.5 points below the loss rate on a held-out cohort run on the Stage 0 parameters, at the same average multiple. Falsified if the difference is below ⚠ 0.2 points. **Falsification condition on the theory:** if within 36 months of Stage 3 a non-bank offers a standing, no-application line on the bank's accounts (read through the feed) at or below 14.0%, sustained for twelve months at a published loss inside the band, then a generic rule on public data was enough and the ledger conferred nothing.

**Named assumptions.** (1) The outcome column — the multiple in force and the cleared-or-lost state — is not reconstructible from consented feeds at a scale that calibrates: a rival needs ⚠ tens of thousands of accounts under a comparable rule, which it cannot get without running one — T4, from the mechanism; (2) the calibration's gain is in the loss rate, not only in the limit: re-fitted parameters lower loss at a given multiple by ⚠ 0.5–1.0 points on the uplift's drawn share — T4, from Arrow's learning curve applied to a credit rule; (3) the ledger's per-account rows stay the customer's (C8) and the cohort aggregates stay inside the bank's data-protection record without a new lawful basis — Article 6(1)(b) for the account rows, 6(1)(f) for the aggregates — *runner's call*; what a ruling would settle is whether cohort-level re-fitting is "compatible further processing" under Article 5(1)(b), which the design says it is because the purpose is the same limit.

---

## SR3 — Lock-out strategy

**The strategy in one sentence.** Make the pool's outcome ledger the rule's only calibration source — the base multiple and the seasoning schedule are re-fitted yearly from what the rule's own limits did — so that the rule's parameters exist only where the form has run.

```
MUTATION GATE — R9
baseline: the rule's parameters are set once — the base multiple from the Stage 0 back-test on overdraft history (C3), the seasoning schedule as Tier 4 figures (C8) — and are not re-fitted from what the rule did; a rival with a generic rule and the same feed starts level on parameters, and the bank's only lead is the time since release.
mutation_A: the calibration ledger — the outcome ledger (WP-6) kept by cohort with the multiple in force, from which the rule's parameters are re-fitted yearly; no external score in the limit rule; the bureau is read only by the fraud and conduct signal (C1) | reason_considered: it is the one asset the form creates that no rival holds, and it makes every C1–C8 figure tagged T4 a fitted value | verdict: adopted | reason_verdict: structural bypass — the scarcity is built by operating, not contracted; passes VA-101 (time compression is of the world); costs a build and a yearly run, no person and no capital
mutation_B: platform exclusivity — the published line (C7) carried only to platforms that agree not to carry a rival's line | reason_considered: exclusivity capture on the channel | verdict: rejected | reason_verdict: contractual, and it conflicts with R7's design (the element is an open-standard field any authorised reader may call); the CMA Order does not permit a bank to condition a reader's access
mutation_C: publish the cohort loss tables — make the ledger's aggregates public so that the bank's rule becomes the market's reference | reason_considered: raises the bank's standing; a "reference rate" position | verdict: rejected | reason_verdict: gives away the resource; a rival's generic rule would fit to the bank's tables at no cost
mutation_D: grow the account base — more accounts, a larger ledger | reason_considered: asset mass efficiencies act on it | verdict: rejected | reason_verdict: Case A's move, not the line's; the base is the account line's resource and the line does not set its growth
mutation_E: patent or register the rule | reason_considered: the conventional intellectual-property answer | verdict: not available | reason_verdict: a credit rule is a business method; not patentable in the UK (Patents Act 1977 s.1(2)(c)); a registered design covers appearance, not method; the shape of the rule is a page any rival may write
differsFromBaseline: true
justificationModeFlag: false
adoptedMutation: mutation_A — the calibration ledger (WP-6)
evolvedBFF: a bank whose credit facility is a standing property of every business account with enough flow — computed daily from the flow and from the account's own record of drawing and clearing, by a rule whose parameters are fitted only to what the rule's own limits did on this pool; priced below the tariff, released in stages, believed on its history, used without an act, paid from receipts, published wherever the account is read, seasoned by use, and calibrated on its own outcomes.
synthesisCheck: a motor insurer's own claims history for pricing, because the insurer's rate for a risk class is fitted to what that class cost the insurer, a record no rival holds and no rival can buy — a new entrant prices on the market's tables and carries the winner's curse until its own book has run for enough years.
```

**Lock-out approach.** Structural bypass — the highest of the three (substitute development, exclusivity capture, structural bypass). The resource is manufactured internally by the form's own operation and made inimitable by the time it takes to accumulate; no contract, no licence, no exclusivity holds it.

**The architectural decision test.** The single structural move is that the rule's parameters come from the ledger and nowhere else. Its removal makes the outcome impossible: with an external score in the rule, a rival buys the same score; with parameters set once, a rival's generic rule matches them on day one. What follows — a lower loss at a given multiple, a rival that cannot match the limit at the price — is evidence, not the strategy.

**R1 continuity.** R1's workaround removed the application and the underwriter and put a rule in their place. The competency that replaced underwriting is setting the multiple; R9 names what the competency runs on. The C1 rule's Stage 0 back-test was the first calibration; R9 makes calibration continuous.

**R8 interaction.** C8's seasoning schedule was published with Tier 4 figures. R9 replaces them with fitted values at each yearly run; the schedule stays published (the customer sees it), the figures move. The per-account record stays the customer's; the cohort aggregates are the bank's — the two halves of the same events.

**R10 interaction — by number only (VA-80).** The supplier inputs the rule reads (funding, the feed, the bureau for the signal) are R10's.

**Structural, not contractual.** No agreement with anyone makes the ledger scarce. A rival with any budget can start its own line tomorrow and hold a comparable ledger in ⚠ 27–54 months; it cannot hold one sooner.

---

## Productizing R9 — the strategy in the architecture

**WP-6 — the outcome ledger and calibration.** A new Working-product component in the Making stream's resource layer. It has two parts. *The ledger:* for every account with a limit, every daily limit set (the multiple in force, the flow band, the release stage), every funded event (C5), its clearance (C8's cleared event) or its stall or write-off, kept by cohort. No new observation: every row is a state the account line and the split already produce; the ledger keeps them with the multiple in force. *The calibration:* once a year the limit-engine team re-fits the base multiple by flow band and the seasoning schedule from the ledger; model risk validates the re-fit (SS1/23 — a change to a model's parameters is a model change); the release-track sitting approves it; the published schedule (C8) is updated. No external score enters the limit rule; the bureau is read only by the fraud and conduct signal, as at C1.

**Structural against contractual scarcity.** The ledger is scarce because of how the form is built: it is the by-product of a rule that sets limits and a split that clears them. It is not scarce because a contract says so. A rival's route to a comparable ledger is to run a comparable form for a comparable time.

**The calibration is a parameter change, not a rule change.** The rule's shape (C1: the multiple of monthly flow, six months of history, the kill band) does not change at a yearly run; the values do. Each run is logged with the ledger cut it was fitted on, so any limit can be traced to the parameters in force on its day (SS1/23 Principle 3). *Runner's call.*

**The customer sees the output, not the run.** The published schedule (C8) shows the current fitted values; the limit history (C4) shows each limit with its date. Nothing new is sent. A customer who asks why the schedule changed is answered by the exception cell from the published schedule and its date — inside the seasoning-query line C8 booked (⚠ 0.5–1.5% of drawn accounts a year; the calibration adds no separate query class, *runner's call*, threshold: if schedule-change queries exceed ⚠ 0.5% of drawn accounts in the quarter after a run, they are booked as a class).

**Data protection.** The per-account rows are processed for the account contract (UK GDPR Article 6(1)(b)); the cohort aggregates for the bank's legitimate interest in setting limits inside its appetite (Article 6(1)(f)), recorded in the Article 30 record. Personal data in the ledger: sole traders and partners are natural persons; companies are not. The design position is that cohort re-fitting is compatible further processing (Article 5(1)(b)) because the purpose — the limit on the account — is unchanged. What a ruling would settle: whether a re-fit that changes a natural person's limit is a decision under Article 22; the design says it is the same automated decision the customer accepted at C5, with the parameter changed, and the C5 term names the rule as automated.

**The at-scale test.** At ⚠ 760,000 accounts with a limit and ⚠ 228,000 drawn accounts, the ledger is ⚠ 0.7–2.7m funded-event rows a year plus ⚠ 277m daily limit rows (760,000 × 365); a table, not a person. The yearly re-fit is ⚠ 100–200 hours of the limit-engine team's 25 people; validation ⚠ 200–400 hours inside model risk's 10; approval one item at the release-track sitting. No person is added. The build is ⚠ 1,000–2,000 hours once = ⚠ £100–300k, in the SC layer.

**What the bank now has.** A rule whose parameters no rival can buy; a schedule whose figures are fitted, not assumed; and a loss band held by calibration rather than by hope.

---

## Cumulative business form factor (C1–C9)

**The architecture's central mechanism.** The standing limit as a property of the account — computed from the flow and from the account's own record by a rule fitted only to what its own limits did on this pool, present before any need, published wherever the account is read. Remove the calibration and the form returns to C8: a rule any rival can match on parameters the day it reads the feed.

**The evolved BFF.** A bank whose credit facility is a standing property of every business account with enough flow: the limit is computed daily from the flow and shown in the account before any need arises (C1); it is priced below the tariff the customer pays today and the existing overdraft is retired into it (C2); it is released in stages against a kill band, with the rule proven on history before it is trusted (C3); it is believed because the customer checks it against the twelve months of their own shortfalls it would have covered (C4); it is used without an act, because a payment that exceeds the balance is met from it under a term accepted once (C5); it is paid for only from the money that comes in, at one rate and no fee (C6); it is published wherever the account is read (C7); it grows with the account's own record of drawing and clearing (C8); and the rule that sets it is fitted, yearly, only to what its own limits did on this pool (C9).

**Components at C9.** WP-1 v2 (amended C8), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, **WP-6 (new C9 — the outcome ledger and calibration)**, CP-1 (amended C2, C4, C6), CP-2 (amended C8), PC-1 (resolved C6), PP-1 (C7). One new component; none removed.

---

## Considered / not chosen (VA-4)

- **Platform exclusivity (B)** — rejected at the mutation gate: contractual; conflicts with R7's open element; not permitted under the CMA Order.
- **Publishing the cohort tables (C)** — rejected: gives the resource away.
- **Growing the base (D)** — rejected: Case A's move.
- **Patent or registered design (E)** — not available: a business method.
- **An exclusive data licence with a bureau or an aggregator** — not chosen: exclusivity capture on a supplier's asset; a contract a rival can outbid; and it puts an external input in the limit rule the design keeps out.
- **A proprietary scoring model bought from a vendor** — not chosen: any rival buys the same vendor; a lead time, not a resource.
- **The exception cell's judgement as tacit knowledge** — not chosen: the cell decides nothing about a limit (C1, C4, C8); a tacit-knowledge resource in the cell would mean the cell had discretion, which the design removed.
- **Trade secrecy on the rule's parameters** — not chosen as the resource: the parameters are published in the schedule (C8) and shown per account (C4); the secret is not the values but their source, which is what R9 holds.
- **A network effect between accounts (a customer's suppliers on the same line)** — not chosen: it needs the supplier's account at the same bank, which the line does not set; and the mechanism is Case A's.

---

## Synthesis check (VA-1)

A motor insurer's own claims history: the insurer's rate for a risk class is fitted to what that class cost the insurer, year by year; a new entrant prices on the market's published tables and carries the winner's curse until its own book has run long enough to fit its own rates. The bank's rule is the same: the multiple by flow band and seasoning is fitted to what those cohorts cost the bank. The analogue's limit: an insurer's claims history is a private asset by market structure (no order makes it readable); the bank's account data is public by order (C7), so the resource here is narrower — only the outcome column is private — and the strategy is correspondingly narrower: it holds the calibration, not the data.

---

## VA-106 synergy line

Does the one move also serve an earlier requirement, with a mechanism? Eight candidates:

- **R1 (design) — yes.** The rule becomes complete in itself: its parameters come from its own outputs, so no external score is bought for the limit decision. Mechanism: the calibration reads the events the split writes.
- **R3 (scale) — yes.** The stage readings (C3) are the ledger's first cohort cuts; the kill band and the calibration read the same cohorts. Mechanism: the release track's cohort reading becomes the calibration's first input, and Stage 0's back-test is the first run.
- **R6 (buy) — yes.** The cleared event the charge-first split produces is the ledger's unit of outcome; the split makes clearance an observed state rather than an inferred one. Mechanism: the same event, no new write.
- **R8 (accumulate) — yes.** The seasoning schedule's Tier 4 figures become fitted values at the first run; the store of value is calibrated, not assumed. Mechanism: the yearly run rewrites the published schedule.
- **R2 (value) — no.** The price and the KMC do not move.
- **R4 (conviction) — no.** The per-account history is per account; the ledger is by cohort; CP-2 has no new line.
- **R5 (use) — no.** The accepted term is unchanged; the funded event is the same.
- **R7 (access) — no.** The element is unchanged.

Four earlier requirements served with a mechanism. R10 by number only (VA-80).

---

## Actor business cases (VA-127)

One row per behaviour the architecture needs from anyone but the venture. Prices per year unless stated; every ⚠ is T4.

| Actor | Behaviour needed | How often | Effect on own book | What it gains | What it costs | Best alternative and its surplus | Arithmetic (VA-157) | Surplus at scale | Verdict; force if not PASS |
|---|---|---|---|---|---|---|---|---|---|
| The business owner | nothing — the ledger is a by-product of drawing and clearing (C5, C6, C8) | — | — | a schedule whose figures are fitted to the pool; the same limit path | nothing | — | central: £0 − £0 − £0 = **£0** · pessimistic: **£0** | flat | **nil by design** — no behaviour needed |
| The bank's limit-engine team (internal) | builds the ledger and the calibration run; re-fits the parameters yearly; logs each run against its ledger cut | once; then yearly | adds (the rule's outputs kept with the multiple in force) | a rule whose parameters are the pool's: loss on the uplift's drawn share lower than the generic rule's by ⚠ 0.5–1.0 points (assumption 2) — ⚠ 10% of drawn-days × £3.4–5.7bn × 0.5–1.0% = ⚠ £1.7–5.7m a year | build ⚠ 1,000–2,000 h at ⚠ £100–150/h = ⚠ £100–300k once; run ⚠ 100–200 h a year = ⚠ £10–20k | leave the parameters as set at Stage 0: surplus £0 and the loss drifts with the pool (position-holding table) | central: gain £2.0m − cost £0.05m (build amortised £0.03m + run £0.02m) − £0 = **£1.95m** · pessimistic: gain £0.3m (⚠ 0.2 points on ⚠ 5% of drawn-days on £3.4bn) − cost £0.08m − £0 = **£0.22m** | rises with the ledger | **PASS** |
| The bank's model-risk function (internal) | validates each re-fit (SS1/23 — a parameter change is a model change); reads the held-out cohort | yearly | neutral (inside the existing inventory) | a documented calibration with a held-out test — the validation it would owe on any parameter change | ⚠ 200–400 h a year inside the ⚠ 10 model-risk people = ⚠ £20–40k | not validate: not available under SS1/23 | central: gain £0.02m (a finding avoided) − cost £0.03m − £0 = **−£0.01m** · pessimistic: gain £0.01m − cost £0.04m − £0 = **−£0.03m** | unchanged | **PROVISIONAL — forced by SS1/23** (as at C8) |
| The board risk committee (internal) | approves the re-fitted parameters as an item of the release-track sitting; holds the appetite line against the ledger | yearly | neutral | the appetite line held on the pool's own outcomes instead of Tier 4 figures | ⚠ 10–20 h inside existing sittings | approve nothing: the Stage 0 parameters stand and the loss drifts | central: gain £0.5m (a quarter of the engine row's loss gain, attributed to the approval that lets it act) − cost £0.002m − £0 = **£0.50m** · pessimistic: gain £0.1m − cost £0.003m − £0 = **£0.10m** | rises with the ledger | **PASS** |
| The bank's data-protection function (internal) | records the ledger's two processing purposes (Article 30); signs the compatible-purpose position | once; yearly review | neutral | a recorded basis for the cohort processing the bank already does for every Tier 1 model | ⚠ 20–40 h once = ⚠ £2–4k | not record: not available (Article 30 is a duty) | central: gain £0.05m (an enforcement finding avoided) − cost £0.003m − £0 = **£0.047m** · pessimistic: gain £0.01m − cost £0.004m − £0 = **£0.006m** | unchanged | **PASS** |
| The rival lender | none — the design needs nothing from it | — | — | — | — | — | — | — | not an actor of the architecture; named because the replication lag is measured against it |
| The account-information readers (C7 class) | none — the element is unchanged | — | — | — | — | — | central: **£0** · pessimistic: **£0** | unchanged | **nil** — no new behaviour |

**The model-risk row, forced.** As at C8: the validation costs more than the finding it avoids and is owed under SS1/23 regardless. Booked in RC inside the existing people (AOM v9 3c); it does not move the floor.

---

## Actor tracks (VA-102)

No new actor class this challenge; three internal holders gain a behaviour (the limit-engine team builds and runs the calibration; model risk validates it; the risk committee approves it) and one gains a record (data protection). **(1) Where does each track open?** The customer's track is unchanged — the ledger is written from states the track already has (funded → cleared → seasoned). The release track (C3) opens at Stage 0 and gains one yearly state: parameters re-fitted and approved. **(2) Where a transition carries no product by decision, what activity does the work?** The yearly run (AOM v9 3j) and the validation (3c); no product is sent. **(3) Counterparty drivers?** None external: the ledger, the run and the approval are the bank's.

---

## BFF delta and upstream re-verification (VA-103)

**What changed in the BFF at this requirement.** WP-6 added: the outcome ledger and the yearly calibration. WP-1 v2's schedule now carries fitted values. No component removed; no other component amended.

**Earlier requirements this same move also serves (VA-106).** R1, R3, R6, R8 with mechanisms; R2, R4, R5, R7 no, with reasons (above).

| Earlier requirement | Named checks on the BFF as it now stands | FIT |
|---|---|---|
| R1 (C1 record v2) | delivering-zone CLO; workaround; ABC floor; property holders; pointing test | **re-verified — strengthened on one line.** The rule's parameters now come from the rule's own outputs; the four removed operations stay removed; no external score is added to the limit decision. Property holder of "calibrated" is the limit-engine team (a track row). The computing line rises ⚠ 0.00–0.01 | re-verified: at-scale margin on the selected customer 30.5% at the set price |
| R2 (C2 record v1) | single KMC; ToC; one move; mutation gate; admissibility; elimination coverage; credibility; pointing; carrying; existence | **re-verified — unchanged.** The KMC, the price and the TAM data object do not move; the calibration selects nothing (v3 stands until C10 by number) | re-verified: 30.5% |
| R3 (C3 record v1) | CLO II; release order; back-test; stage bands; SC layer; overlay | **re-verified — strengthened.** The Stage 0 back-test is the first calibration; each stage reading is a ledger cut; the kill band reads the same cohorts. SC gains the ledger build (⚠ £100–300k once) inside the 0–1 band. Stage 1 margin at the set price 4.0% (spread count below) | re-verified: Stage 1 4.0% at the set price |
| R4 (C4 record v1) | efficacy ToC; credibility gap; Milgrom / Hoch and Deighton; CP-2; mutation gate; VA-81; VA-92; cap line | **re-verified — unchanged.** The history shows each limit with its date; a re-fit changes the limit on its day like any flow change. The signed display covers it (the yearly template review reads the schedule's new figures — a *runner's call*) | re-verified: 30.5%; cap line carried |
| R5 (C5 record v1.1) | use routine; routine disruption; Madrian and Shea; default funding; switch-off and reversal; the loss gap; CONC 5.2A timing | **re-verified — one position extended.** The CONC 5.2A assessment at acceptance covers the rule; the design says a re-fitted parameter is the same rule assessed. What a ruling would settle: whether a yearly re-fit that raises limits across a cohort needs a fresh assessment per account. Loss gate at the set price 4.47% (floor high 107.29) | re-verified: 30.5%; loss gate 4.47% |
| R6 (C6 record v1) | lifecycles; CVTs; buy block type; Prelec and Loewenstein; mutation gate; price structure; representative example; R2 and R3 interactions | **re-verified — unchanged.** The split is the same; the cleared event it produces is the ledger's unit. The price is the same | re-verified: 30.5% at the set price (25.8% / 32.8% at the band's ends) |
| R7 (C7 record v1) | access routines; gateway class; Farrell and Saloner; PP-1; conformance; desk position; G15 | **re-verified — unchanged.** The element carries the released limit; a re-fit changes the figure, not the element. S1, S3, F-5, F-6 carried unchanged | re-verified: 30.5% |
| R8 (C8 record v1) | extended routine; store of value; Sharpe 1990; WP-1 v2; SCIS; position-holding; the £8 cap line | **re-verified — strengthened.** The schedule's figures become fitted; the SCIS design finding stands (the calibration does not change the switching cost's size). The three C8 position-holding assumptions are unchanged; R9 adds three of its own | re-verified: 30.5%; SCIS 2 · 4 · 6 carried |

No FAILED row. **Function-gate re-run:** not at C9 (at C10 by number).

---

## Financial check — the floor on four layers, the ceiling as a price, the cap and the position-holding table

**Unit.** £1,000 of average drawn balance, per year, at scale. **Volume.** `⚠ [average drawn SME balance £]`; public proxy ⚠ £3.4–5.7bn. **Component set the verdict was computed on (VA-74):** WP-1 v2 (amended C8), WP-2 (amended C5), WP-3 (amended C6), WP-4, WP-5, WP-6 (new C9), CP-1 (amended C2, C4, C6), CP-2 (amended C8), PC-1 (resolved C6), PP-1 (C7).

**Pricing note.** F3 does not reprice. The ceiling stays the R2 KMC resolved to the C6 price (140; band ⚠ 135–142.5). R9 changes no price and no exposure; it changes where the rule's parameters come from.

**What R9 adds to the floor — activity by activity (ABC, RD-031).** Every line: resource → activity → driver that resolves to a named quantity in the AOM v9 section 0 → volume.

| Activity | Level | Driver | Volume ⚠ | Unit cost ⚠ | Cost a year ⚠ | Per £1,000 ⚠ |
|---|---|---|---|---|---|---|
| keep the daily limit row with the multiple in force | per account per day, automated | e.daily_recompute on q.accounts_with_limit | 760,000 × 365 = 277m rows | ⚠ £0.00001 (a field stored beside a computation already run) | ⚠ £3k | 0.00 |
| keep the outcome row (funded, cleared, stalled, written off) | per event, automated | e.cleared_event and e.funded_event on q.drawn_accounts | ⚠ 0.7–2.7m a year | ⚠ £0.001 | ⚠ £1–3k | 0.00 |
| run the calibration — re-fit the base multiple by flow band and the seasoning schedule on a held-out cut | HQ, yearly | e.calibration_run | 1 | ⚠ 100–200 h at ⚠ £100/h = ⚠ £10–20k, plus compute ⚠ £5–30k on 277m rows | ⚠ £15–50k | 0.00–0.01 |
| validate the re-fit (SS1/23) | HQ, yearly | e.ledger_validation | 1 | ⚠ 200–400 h inside the ⚠ 10 model-risk people | inside RC | 0.00 |
| approve the parameters at the release-track sitting | HQ, yearly | e.parameter_approval | 1 | ⚠ 10–20 h inside existing sittings | inside RC | 0.00 |
| record the two processing purposes (Article 30) | HQ, once then yearly | e.dp_record | 1 | ⚠ 20–40 h inside the existing conduct and data-protection people | inside RC | 0.00 |
| build the ledger and the calibration run | HQ, once | e.ledger_build | 1 | ⚠ 1,000–2,000 h at ⚠ £100–150/h = ⚠ £100–300k once, amortised over five years | ⚠ £20–60k | 0.00–0.02 (in SC, inside the 0–1 band) |
| **R9 total, unrounded** | | | | | **⚠ £0.04–0.12m operating and amortised build** | **⚠ 0.01–0.03** |

*Runner's call on the compute figure.* A yearly re-fit on ⚠ 277m limit rows and ⚠ 0.7–2.7m outcome rows is a batch job on the bank's existing data platform; ⚠ £5–30k is judged from published cloud batch prices at that row count. Threshold: above ⚠ £100k a year the computing line rises by a further 0.01–0.03 and the R9 addition is booked at ⚠ 0.05. Convergence: the first run's cost at Stage 1.

**The four-layer floor at C9 (AOM v9 section 6).**

```
PVC  40.02–83.25   funding 15–30 · expected loss 20–40 (C9: the band is what the calibration holds — position-holding table) · computing and payments 2.02–5.12 (C9: +0.00–0.01, the calibration run) · exceptions and write-off 3.00–8.13 (C9: +0.00)
RC    2.02–5.04    unchanged — the validation, the approval and the record sit inside the existing people
SC    0–1          unchanged — the ledger build (⚠ £100–300k once) sits inside the band; unrounded 0.72 → 0.74 at the high corner
IC   13–18         unchanged — no exposure change at R9
FLOOR 55.04–107.29  (C8: 55.04–107.28; C7: 54.04–106.28; C6: 54.04–106.27; C5: 54.04–106.26; C4: 54.03–106.20; C3: 54–106)
```

**Carrying check.**

```
CARRYING CHECK — R9
  KMC (ceiling)                         150–300 per £1,000 a year (unchanged, TAM v3 KMC-OD-STD-TARIFF)
  the price (C6)                        140.00 — band ⚠ 135.00–142.50 (F3 does not reprice)
  floor                                  55.04–107.29
  operating bar = floor × 1.25           68.80–134.11
  capital bar = PCO capital ÷ drawn book 26.05–43.68 (unchanged)
  binding bar                            operating, at both corners
  price against the operating bar        140.00 − 134.11 = 5.89 at the set price · 0.89 at the band's low end · 8.39 at its top
  carries                                true at every point of the band
  margin worst corner (price − floor high) ÷ floor high
                                         30.5% at 140 · 25.8% at 135 · 32.8% at 142.5
  margin best corner (price − floor low) ÷ floor low
                                         154.4% at 140
  conventional additions used (RD-030)   R9 line ⚠ 0 (nothing to remove); added ⚠ 0.01 on the rounded layers (⚠ 0.01–0.03 unrounded); cumulative ⚠ 1.05–1.29 rounded (⚠ 0.51–1.81 unrounded); remaining ⚠ 6.71 at the high corner
  max payable to any holder (VA-164)     5.89 at central; 0 at the pessimistic corner; paid: 0
```

**Margin of safety (the fit model, `sme-fintech-models/bank-credit-facility-fit-model-at-C9.yaml`).** By hand: **30.5% at the worst corner at the set price; 25.8% at the band's low end; 32.8% at its top; 154.4% at the best corner. PASS on the 25% gate at every point of the band.** R9 moves the worst-corner margin by less than a tenth of a point (30.49% against C8's 30.50%). `fit_margin.py` is run on the at-C9 model; its output is in the verifier r9.

**Binding gate — by driving (VA-84).** Seventeen gates driven at C9: the sixteen of C8 and (17) the calibration cohort minimum. Ordered by margin at the set price:

1. the loss rate on the flow-underwritten pool — the 25% margin fails above **4.47%** at the set price (4.07% at the band's low end; 4.67% at its top); the loss line is 67.29 + 10L and the bar is 112.00; zero margin at 7.27%; assumed ⚠ 2–4%; surplus 0.47 points at the assumed high corner. **First to fail.** R9 is the requirement that holds this band at scale (position-holding table): without the calibration the band is a Stage 0 figure applied to a pool that has moved.
2. the default-funded loss gap (C5) — on the same line; ⚠ 0.3–0.5 of the 0.47 points; unmeasured. Nil surplus at the top of that band, as at C8.
3. the price condition's room — 5.89 at the set price; 0.89 at the band's low end.
4. the rate against the lowest published EAR — 0.54 points (C6).
5. the average seasoned uplift (G16, C8) — ⚠ 15–30%; threshold ⚠ 38% at the band's low end. Now a fitted value from the first run.
6. **the calibration cohort minimum (new, G17)** — a cohort cell (seasoning × flow band × stage) needs ⚠ 500 outcome rows for its parameter to move; below it the cell inherits its neighbour's (*runner's call*). At Stage 0 the history holds overdraft outcomes, not the form's; the first run on the form's own outcomes is at Stage 1's twelve months, on ⚠ 46,000–71,000 drawn accounts × ⚠ 3–12 events = ⚠ 140,000–850,000 rows across ⚠ 30–60 cells — ⚠ 2,300–28,000 per cell, above the minimum at every corner. Reads at Stage 1's twelve months.
7. G15 — the platforms' display (C7), unchanged.
8. the connected share, unchanged.
9. the non-empty history share, unchanged.
10. the use gates — switch-off, funding-query, charge-query, display-query, seasoning-query rates (C5–C8), unchanged; schedule-change queries booked inside the seasoning-query line (threshold ⚠ 0.5% of drawn accounts in the quarter after a run).
11–17. carried from C8 unchanged.

```
BINDING GATE — the loss rate on the flow-underwritten pool (identified at C1; printed at every challenge after)
  gate:         the expected-loss line, on the pool as released, including default-funded draws and the seasoned uplift, with the rule's parameters re-fitted yearly
  threshold:    4.47% at the set price (4.07% at the band's low end · 4.67% at its top) — the 25% margin fails above it at the worst corner; zero margin at 7.27%
  this design:  ⚠ 2.0–4.0% assumed — surplus of 0.47 points at the assumed high corner; the default-funded gap (C5) may consume ⚠ 0.3–0.5 of it; R9 is what holds the band as the pool seasons — its failure value is ⚠ 4.5–6.0% (position-holding table)
  pivot:        > ⚠ 5% at the worst corner (C2's ruling, unchanged); the calibration is the first lever pulled before the pivot — a re-fit that cuts the multiple where the loss is
  reads at:     the Stage 1 12-month reading (the pool, and the first calibration run); the first replica's 24-month reading (the held-out cohort test — the R9 hypothesis)
```

**Independence (VA-97).** NOT shown — the margin is a transform of the loss gate; R9's gain is on the same line. Free counts named: the held-out cohort's loss against the re-fitted cohort's (a difference of two loss readings, not a count of acts — stated as such); the calibration run's row count per cell (a count). Both unmeasured.

**Spread count (VA-162).** At scale ⚠ £3.4–5.7bn (228,000 drawn accounts). At Stage 1 (⚠ £0.4–1.9bn): floor 56.86–134.63 (the C8 figure plus the computing addition); worst-corner margin at the set price (140 − 134.63) ÷ 134.63 = **4.0%**; 0.3% at the band's low end; 5.8% at its top. Stage 1 does not carry the 25% margin at any point of the band — as at C3 to C8. At Stage 1 the ledger holds overdraft outcomes only; the first run on the form's outcomes is at Stage 1's twelve months, so the Stage 1 parameters are Stage 0's.

**Working capital timing.** Unchanged from C6.

**The conventional line, priced.** The counterfactual's R9 line is ⚠ 0: a conventional overdraft book holds no resource a rival cannot buy — its underwriters and relationship managers are hired in the market (the R1 line, removed at C1), its bureau scores are bought (a supplier input, R10 by number), and its loss history is used to set appetite, not to fit a limit rule. Nothing is removed; the cap moves only by R9's own ⚠ 0.01–0.03.

**The first-imitator score (FIS) — registry row "F3 barrier scores".**

| Term | Conservative | Central | Optimistic | Basis |
|---|---|---|---|---|
| Compound rate (0–3) | 2 | 2 | 3 | the ledger grows by ⚠ 0.7–2.7m outcome rows a year and its precision rises with cohort size (asset mass efficiencies); the loss gain is bounded by the band, so the compounding is in precision, not in the margin; 3 where a lower loss lets the rule set a larger limit, which produces more events |
| Replication lag (< 12 months 0 · 12–36 months 1 · > 36 months 2) | 1 (⚠ 27 months) | 2 (⚠ 39 months) | 2 (⚠ 54 months) | ⚠ 0–12 months to build the split and the seasoning field plus ⚠ 27–42 months of the rival's own Stage 0 to Stage 2 |
| Capital independence (0–2) | 2 | 2 | 2 | money buys the engine, the people and the feed; it does not buy 36 months of the form running on a pool the rival does not have |
| **FIS (max 7; ≥ 5 pass; ≤ 3 NCR)** | **5 — pass** | **6 — pass** | **7 — pass** | |

**The score, read plainly.** The resource passes at every corner because a rival cannot buy it and cannot build it faster than the form runs. The conservative corner is one point above the line: a rival that already runs a comparable split and seasoning field (there is none known — desk check, T2) would score 1 on lag and the FIS would be 5 still. The score is not softened by the fact that a rival can *start*: it can, and it holds nothing comparable for ⚠ 27–54 months.

**Position-holding table (registry F3 row).** Every model assumption that depends on R9 holding; the requirement it holds because of; the failure value as a band; where it lives in the fit model.

| Assumption in the model | Holds because of | Value if R9 holds | Failure value (band) | In the fit model as |
|---|---|---|---|---|
| The expected-loss band on the pool at scale (PVC) | R9 — the rule's parameters are re-fitted yearly to what the rule's own limits did; a cohort whose loss rises has its multiple cut at the next run | ⚠ 2.0–4.0% | ⚠ 4.5–6.0% — a generic rule on Stage 0 parameters applied to a pool that has seasoned and grown for three years (*runner's call*: the drift a fixed-parameter rule shows between validations, judged from the SS1/23 rationale for yearly validation; T4) | `position_holding.loss_band` — PVC expected loss 20–40 → 45–60; floor high 107.29 → 112.29–127.29 |
| The average seasoned uplift on the book (IC) | R9 — the schedule's figures are fitted at the first run | ⚠ 15–30% | ⚠ 0–10% (too few rows to fit; the schedule is cut to the flow-only base) — IC 13–18 → 12–17; the failure is of the store (C8), not of the margin | `position_holding.uplift_fitted` |
| The validation cost inside existing people (RC) | R9 — the re-fit is validated by the bank's own model-risk function under SS1/23 | ⚠ 200–400 h inside the 10 people | an independent external validation each year, ⚠ £0.2–0.5m — RC 2.02–5.04 → 2.06–5.19 (+0.04–0.15) | `position_holding.validation_external` |

**Re-test at the failure value (by hand; the script's figure in r9).** *Loss band:* at ⚠ 4.5% the floor high is 112.29 and the margin (140 − 112.29) ÷ 112.29 = **24.7% — BORDERLINE**; at ⚠ 5.0% it is 117.29 and **19.4% — BORDERLINE**; at ⚠ 6.0% it is 127.29 and **10.0% — FAIL**. At the band's low end (135) the same three read 20.2%, 15.1% and 6.1%. *Uplift:* IC 12–17, floor high 106.29, margin **31.7% — PASS**. *Validation:* floor high 107.44, margin **30.3% — PASS**. **What the re-test says, unsoftened:** the margin depends on R9 holding. The first assumption is the binding gate itself; R9 is the requirement that keeps it inside the band as the pool moves, and without R9 the design is BORDERLINE at the band's midpoint and FAIL at its top. The FIS passes, so the registry row does not require the verifier to re-test; the verifier r9 re-tests regardless and reports it.

---

## The close — three checks (VA-89, VA-91)

**Logical check.**
- Customer of record declared; one run; the routine positioned in named ✓ (VA-154).
- F3 ordering — the key resource identified at SR1 before any theory ✓. VA-23 at Diagnose — the block tested is the at-scale rival's, not a pilot's ✓.
- Required core competency named (a) and key resource named (b); the four diagnostic questions answered; the block named as one operation (the rule's parameters set from outside its own outcomes) ✓ (SR1). Five other candidates excluded by reason ✓. VA-101 applied at SR1 — the limit is of the world (time compression), with the value resting on it stated ✓.
- ToC — parameter named ✓; theory named with researcher, year and paper ✓ (Dierickx and Cool 1989; supported by Arrow 1962); contrast theory named (Barney 1991) and the Open Banking premise answered ✓; fragile-findings check ✓; context and outcome as states ✓; hypothesis with falsification condition on the theory and three named assumptions ✓.
- Strategy — one sentence; exactly one structural decision ✓; mutation gate emitted before the strategy; five genuine mutations (A–E), one not available; justification mode false ✓; lock-out approach named (structural bypass) ✓; the architectural decision test passed (the move, not its outcomes) ✓; R1 continuity ✓; R8 interaction ✓; R10 by number ✓; structural not contractual ✓.
- Productising — structural against contractual scarcity ✓; parameter change not rule change, with traceability ✓; the customer sees the output ✓; data-protection positions stated with what a ruling would settle ✓; at-scale test with the volume and no person added ✓.
- Cumulative BFF (C1–C9) read cold as one product; central mechanism named; components listed with the new one ✓ (parent's instruction; the challenge skill's F3 note overridden as at C8 and recorded in the WS1 feedback log).
- Considered and not chosen — nine entries with reasons ✓ (VA-4). Synthesis check with the analogue's limit ✓ (VA-1).
- VA-106 line, eight candidates, four served, four "no" with reasons ✓. VA-103 table, eight rows, no FAILED row ✓. VA-127 table, two arithmetic lines per row; one PROVISIONAL row with the force named; two nil rows by design ✓. VA-102 three questions answered ✓. VA-82 classified ✓.
- No forward references (VA-80) ✓ — R10 by number only. Launch constraints absent (VA-23) ✓. Completeness contract (VA-73) ✓.
- Conventional cost line named (⚠ 0) with the reason nothing is removed; the cap line printed with the rounded and unrounded figures ✓ (F3 rule).
- Binding gate by driving ✓ (17 gates). Shared-input declaration ✓ (VA-160). Spread count ✓ (VA-162). Independence stated ✓ (VA-97).
- Position-holding table — three assumptions, each with the requirement it holds because of, the failure value as a band and its place in the fit model ✓; re-test at the failure value by hand, unsoftened (24.7% / 19.4% / 10.0% on the loss band) ✓ (registry F3 row).
- **F3 barrier score (FIS): 5 · 6 · 7 — PASS at every corner** ✓.
- Verdict order (VA-95) ✓ — `check_verdict_order.py` on the verdict record with R9 added. Loop-gate branch (VA-153): no FAIL on the design's FIT. Loop-backs (VA-151): 0.
- Incremental write ✓. Verification artefact ✓: `sme-fintech-models/bank-credit-facility-fit-verifier-r9-2026-09-21.md`.

Checks failed: 0. **PASS.**

**Operational check.** The CTM v9 and AOM v9 are written as documents; the model files are not (build item carried from C1) — FAIL on the run, disposed. Every AOM v9 activity names its flow and a driver that resolves to section 0 ✓; no cost line is a share of revenue ✓. The release track carries the yearly re-fit at a state it already had (the reading) ✓ (VA-102). **Capacity (VA-91 — the one figure):** ⚠ **20,400 exception hours per cell a year** at central (21,900 at the high corner) on ⚠ 100,000 drawn accounts per cell; 14 handlers (band 13–15) — unchanged by R9, which adds no cell activity. Result: PROVISIONAL (one build item).

**Financial check.** Margin 30.5% at the worst corner at the set price (25.8% / 32.8% at the band's ends), 154.4% best, by hand; PASS at every point; `fit_margin.py` run on the at-C9 model (verifier r9). Carrying check: carries; room 5.89 at the set price, 0.89 at the band's low end. Binding gate: the loss rate, unmeasured, threshold 4.47% at the set price; R9 is the requirement that holds the band; at its failure value the margin is BORDERLINE (19.4% at 5%) and FAIL (10.0% at 6%). Conventional additions ⚠ 1.05–1.29 of ⚠ £8 rounded. Result: PROVISIONAL.

**What was decided about each check that did not pass.**
- CTM and AOM model files absent — **build item**; owner: the Venture Architect seat; carried.
- The model-risk actor row — FAIL at both corners, **forced by SS1/23**; no input to measure.
- The margin's dependence on R9 (the position-holding re-test) — **design finding**: the binding gate is held by the calibration; the design has no second hold on the loss band. Owner: the runner, at the C10 consistency audit (the moat test reads it against the SCIS finding). Convergence: the held-out cohort test at the first replica's 24 months (the R9 hypothesis).
- The calibration's loss gain (⚠ 0.5–1.0 points on the uplift's drawn share) — **unmeasured input**; owner: model risk; convergence: the held-out cohort test.
- The loss-drift failure value (⚠ 4.5–6.0%) — **unmeasured input**; owner: model risk; convergence: the same test, read the other way (the held-out cohort's loss).
- The compute cost of a run (⚠ £5–30k) — **unmeasured input**; owner: the limit-engine team; convergence: the first run at Stage 1's twelve months; threshold ⚠ £100k.
- The rows per cohort cell (⚠ 2,300–28,000) — **unmeasured input**; owner: the limit-engine team; convergence: the first run.
- The replication lag (⚠ 27–54 months) — **unmeasured input**, by construction unobservable until a rival runs; owner: the runner (desk check for any comparable line, yearly); falsification condition in SR2.
- The schedule-change query rate — **unmeasured input** inside the seasoning-query line; owner: the cell lead; convergence: the quarter after the first run; threshold ⚠ 0.5%.
- The data-protection positions (Articles 5(1)(b), 6, 22, 30) and the SS1/23 position on a yearly re-fit — **standing constraints, designed for**, with what a ruling would settle named; owner: the data-protection and model-risk functions; convergence: the signed positions before the first run.
- The ledger and the calibration run — **build item**; owner: the limit-engine team; convergence: Stage 0 (the ledger keeps overdraft outcomes from the back-test onward).
- The held-out cohort design — **build item** (which accounts are held on Stage 0 parameters and for how long, so that the hypothesis can be read); owner: model risk; convergence: before Stage 1's twelve-month run.
- C8's and earlier carried items — carried unchanged; the SCIS design finding carried.

```
GATE VERDICT — on the cumulative architecture C1 to C9
  logical limb:      PASS            checks failed: 0 (FIS 5 · 6 · 7 pass at every corner)
  operational limb:  PROVISIONAL     checks failed: 1 build item (no model files)
  financial limb:    PROVISIONAL     margin 30.5% worst corner at the set price (25.8% at the band's low end / 32.8% at its top) / 154.4% best (by hand; `fit_margin.py` output in verifier r9) · binding gate the loss rate on the pool: surplus 0.47 points at the assumed high corner, unmeasured; R9 holds the band — at its failure value the margin is 24.7% at 4.5%, 19.4% at 5% (BORDERLINE), 10.0% at 6% (FAIL) · conventional additions used ⚠ 1.05–1.29 of ⚠ £8 rounded (⚠ 0.51–1.81 unrounded); remaining ⚠ 6.71
  price:             14.0% simple a year on the daily drawn balance = £140 per £1,000 drawn (band ⚠ 135–142.5); no fee; collected from receipts (C6, unchanged; F3 does not reprice)
  partner:           none new; none needed
  decisions:         39 unmeasured inputs (34 carried, 5 new), 14 build items (12 carried, 2 new), 1 standing-constraint set (1 new row: the data-protection and SS1/23 positions on the re-fit), 3 structural limits (carried; none new — the time-compression limit is the lock-out, not a failed check), 1 carried question (fixed against variable, C6), 2 design findings (the SCIS, carried; the margin's dependence on R9, new); 1 actor-level FAIL forced (SS1/23)
  capacity figure:   20,400 exception hours per cell a year at central (21,900 at the high corner), 100,000 drawn accounts (333,000 accounts with a limit) per cell = one replica; 14 handlers per cell (band 13–15) at 1,400–1,600 productive hours — unchanged by R9   VA-91
  independence:      NOT shown — the margin is a transform of the loss gate; R9's gain is on the same line; two free readings named and unmeasured   VA-97
  gates driven:      17; first to fail on evidence: the loss rate, margin 0.47 points at the set price; second: the default-funded gap on the same line; third: the price condition's room (5.89)   VA-84
  verification:      sme-fintech-models/bank-credit-facility-fit-verifier-r9-2026-09-21.md   VA-90
  inherited:         R8, R7, R6, R5, R4, R3, R2, R1 PROVISIONAL — R9 cannot exceed them; F1 and F2 closed PROVISIONAL with conditions carried   VA-95
  repairs:           none claimed
  loop_backs:        0 this requirement   VA-151
  loop-gate branch:  no FAIL on the design's FIT; the position-holding re-test's BORDERLINE and FAIL are at the failure value, not the design value — recorded as a design finding with owner and convergence; the model files are build items   VA-153
  launch constraints:none inside SR1–SR3 and this block   VA-23
  spread count:      at scale ⚠ £3.4–5.7bn; at the Stage 1 count the worst-corner margin is 4.0% at the set price, 0.3% at the band's low end; Stage 1 runs on Stage 0 parameters   VA-162
  shared input:      the loss rate — drives both the margin and the binding gate; R9's calibration acts on the same line; the price sets where on that line the gate sits   VA-160
  function gate:     F3 (C8–C10) — not yet; C10 by number
  VERDICT:           PROVISIONAL
```

**R9 failure test.** Would R9 have failed? Three conditions. First, a rival with any budget could buy or build the resource inside 18 months: it cannot — the ledger is built by operating and the shortest lag is ⚠ 27 months. Second, the scarcity is contractual: it is not — no contract holds it. Third, the resource is the same one the conventional form already uses: it is not — a conventional book sets appetite from its loss history and buys its scores; it does not fit a no-application limit rule to its own outcomes, because it has no such rule. R9 stands, and what it holds is the binding gate.

---

## Carried items (VA-82)

- **Forward-referenced (each by number only):**
  - the at-scale price hold; the yearly rate review; the funding line's movement with Bank Rate; the supplier inputs the rule reads (funding, the feed, the bureau for the signal) and their replaceability; the shelf check for any supplier binding at launch; the moat test on the SCIS finding and on the margin's dependence on R9 — R10
- **Unmeasured inputs (new at C9, 5):** the calibration's loss gain; the loss-drift failure value; the compute cost of a run; the rows per cohort cell; the replication lag (and, inside C8's seasoning-query line, the schedule-change query rate). **Carried from C1–C8 (34):** unchanged.
- **Build items (new at C9, 2):** the ledger and the calibration run; the held-out cohort design. **Carried (12):** the CTM and AOM model files; the accrual ledger; the charge-first split; the representative example and APR basis; default funding's authorisation, notice and record; the term and the CONC 4.7 information; the limit-history placement; the release order's instrumentation; the element's population rule; the conformance test; the seasoning input and schedule in the engine; the 15th handler line at the high corner.
- **Standing constraints (new at C9):** UK GDPR Articles 5(1)(b), 6(1)(b), 6(1)(f), 22 and 30 on the ledger's two processing purposes; PRA SS1/23 on a yearly parameter re-fit as a model change — designed for, with what a ruling would settle named. C8's and earlier: unchanged.
- **Structural limits (carried, 3):** the C1 limit rule's exposure model; the Stage 1 margin below 25% at every point of the band; the unconnected account's single conviction moment. **New at C9:** none.
- **Design findings:** the SCIS below the pass line (C8, carried); **new at C9:** the margin's dependence on R9 — the binding gate is held by the calibration and by nothing else.
- **Carried question (C6):** a fixed rate against a Bank Rate–linked rate.
- **TAM data object:** v3 stands; no narrowing at C9 (the calibration selects nothing). The C9 record is added as a consumer at v4 (C10 by number).
- **F2 audit and verification items:** S1, S3, F-5, F-6 carried to the C7 record's next regeneration; F-3, F-4 carried.
- **Carried to pilot-instance design after R10 (VA-23):** none new — the Stage 0 ledger on overdraft outcomes is a design state (C3), not a launch constraint.

---

## Checks run — Phase 2 registry rows

| Registry row | Result | Where |
|---|---|---|
| Customer of record declared; one run per customer of record (VA-154) | PASS — one | header |
| F3 ordering — resource before theory; VA-23 at Diagnose | PASS | SR1 |
| Required core competency and key resource named; four diagnostic questions; the block as one operation | PASS — the outcome ledger; parameters set from outside the rule's outcomes | SR1 |
| Other candidate resources excluded by reason | PASS — five | SR1 |
| VA-101 — the limit is of the world; value resting on it stated; validation paired | PASS — time compression; the loss band; the held-out test | SR1 |
| ToC parameter, theory (researcher, year, paper), context, outcome | PASS — Dierickx and Cool 1989 | SR2 |
| Contrast theory named; fragile-findings check | PASS — Barney 1991; none on the list | SR2 |
| Hypothesis with falsification condition; named assumptions | PASS — three | SR2 |
| Mutation gate before the strategy; ≥ 2 genuine mutations; justification mode false | PASS — five | SR3 |
| Exactly one structural move; lock-out approach named | PASS — WP-6; structural bypass | SR3 |
| Architectural decision test — the move, not its outcomes | PASS | SR3 |
| R1 continuity; structural not contractual | PASS | SR3 |
| Structural against contractual scarcity; at-scale test | PASS | Productizing |
| Cumulative BFF read cold; central mechanism named (parent's brief) | PASS | BFF |
| Considered and not chosen with reasons (VA-4) | PASS — nine | Considered |
| Synthesis check with the analogue's limit (VA-1) | PASS | Synthesis |
| VA-106 line — every requirement; "no" with reason | PASS — four served, four no | VA-106 |
| VA-127 — one row per behaviour; two arithmetic lines; FAIL rows forced | PASS — seven rows; one PROVISIONAL forced | VA-127 |
| VA-102 — tracks opened at arrival; dispositions; counterparty drivers | PASS — none new | VA-102 |
| VA-103 — every earlier requirement re-verified; FIT per row | PASS — eight rows | VA-103 |
| VA-80 — no forward references | PASS | throughout |
| VA-23 — no launch constraints in the design | PASS | throughout |
| VA-73 — completeness contract | PASS | throughout |
| Conventional line named and removed; cap line printed (F3 rule, RD-030) | PASS — ⚠ 0, nothing to remove; 6.71 remaining | Financial |
| ABC bottom-up, every line with driver and volume (RD-031) | PASS — seven lines | Financial |
| Four-layer floor printed; each layer with tier and basis | PASS — 55.04–107.29 | Financial |
| Carrying check printed | PASS — carries | Financial |
| Margin ≥ 25% at the worst corner | PASS — 30.5% (25.8% at the band's low end) | Financial |
| Binding gate by driving (VA-84) | PASS — 17 gates; the loss rate first | Financial |
| Independence (VA-97) | stated — NOT shown; free readings named | Financial |
| Spread count (VA-162) | PASS — printed; Stage 1 4.0% | Financial |
| Shared input (VA-160) | PASS — the loss rate | close |
| Position-holding assumption named (F3) — table; each assumption in the fit model; re-test at the failure value | PASS — three assumptions; re-test 24.7% / 19.4% / 10.0% on the loss band, printed unsoftened | Financial |
| **F3 barrier score — FIS ≥ 5 pass; ≤ 3 NCR** | **PASS — 5 conservative · 6 central · 7 optimistic** | Financial |
| Three-limb close; GATE VERDICT block (VA-89, VA-91) | PASS — printed | close |
| Capacity figure, one number (VA-91) | PASS — 20,400 (21,900 at the high corner) | close |
| Verdict composition (VA-95); `check_verdict_order.py` | PASS — PROVISIONAL; IN ORDER (verifier r9) | close |
| Loop-backs (VA-151); loop-gate branch (VA-153) | PASS — 0; no FIT FAIL at the design value | close |
| Carried items classified (VA-82) | PASS | Carried |
| Verification artefact exists (VA-90) | PASS — verifier r9 | close |
| Incremental write (VA-88) | PASS | header |
| House-style checker run | recorded in the f1-status file | — |

---

## Quality check

- Is the resource structurally scarce, not contractually? **Yes** — built by operating; no contract holds it.
- Could a well-resourced competitor acquire or build it in 18 months? **No** — the shortest lag is ⚠ 27 months, and money does not shorten it.
- Is the strategy something the current BFF cannot accommodate? **Yes** — a conventional overdraft book has no no-application rule to fit.
- Is the resource distinct from R10's supplier input? **Yes** — R9 holds what a rival cannot get; the supplier inputs the rule reads are R10's by number.
- Confidence: **Medium-high** on the mechanism (time compression is well established and the lag is arithmetic on C3's stages); **medium** on the size of the loss gain (assumption 2, T4); the dependence of the margin on R9 is stated and is the finding this record carries.

---

## Sources (in addition to PCO S1–S12, C1 C1–C12, C2 D1–D10, C3 E1–E13, C4 F1–F15, C5 G1–G10, C6 H1–H12, C7 I1–I13, C8 J1–J13)

- K1 — Dierickx, I. and Cool, K. (1989), "Asset Stock Accumulation and Sustainability of Competitive Advantage", *Management Science* 35(12): 1504–1511.
- K2 — Arrow, K. J. (1962), "The Economic Implications of Learning by Doing", *Review of Economic Studies* 29(3): 155–173.
- K3 — Barney, J. B. (1991), "Firm Resources and Sustained Competitive Advantage", *Journal of Management* 17(1): 99–120.
- K4 — Patents Act 1977, s.1(2)(c) — a scheme, rule or method for doing business is not an invention. FACT.
- K5 — UK GDPR, Articles 5(1)(b) (purpose limitation and compatible further processing), 6(1)(b) and 6(1)(f) (lawful bases), 22 (automated decisions) and 30 (records of processing); ICO guidance on lawful basis and on purpose limitation. Read for the positions at Productizing.
- K6 — Payment Services Regulations 2017, reg. 69, and the CMA Retail Banking Market Investigation Order 2017 — access for authorised account-information providers without discrimination. FACT (read for mutation B).
- K7 — PRA SS1/23, Model risk management principles for banks — Principle 3 (model development, implementation and use; traceability of parameters) and Principle 4 (independent validation of model changes). FACT.
- K8 — Published cloud batch-compute price lists (the three largest providers), September 2026 — the compute figure for a yearly re-fit on ⚠ 277m rows. T2.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 21 September 2026 | Created at R9 by the runner (Path C, mode 3, autonomous). PROVISIONAL, capped by R1–R8 (VA-95). Object-after to 23 September 2026 17:00. Second requirement of Function 3. FIS 5 · 6 · 7 PASS. Position-holding re-test on the loss band printed unsoftened (BORDERLINE at 5%, FAIL at 6%) and carried as a design finding. House-style checker run on this file: result recorded in the f1-status file. |
