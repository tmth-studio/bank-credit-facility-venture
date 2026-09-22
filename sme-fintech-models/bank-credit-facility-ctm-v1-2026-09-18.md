# Business bank credit facility line — customer transformation map (CTM), v1, at C1

**Venture:** the credit facility line of a large UK SME bank (Case B — term loan and overdraft), Path C mode 3 — see `../bank-credit-facility-c1-v1-2026-09-18.md`. **Created at R1** (18 Sep 2026), runner-drafted, PROVISIONAL on a PCO that is object-after to 20 Sep 2026 17:00. **Customer:** the business with fewer than 50 employees that holds its account at the bank and needs working money. **Naming note:** the challenge skills name this file `bank-credit-facility-ctm-model-at-C1.yaml` and generate the views from it; this run wrote a document, so this file is the record and the model file is a build item. Every state change is traced to a requirement; anything a later requirement owns is flagged `[REQUIRES C[N]+]`, not designed. The bank is not named. Every ⚠ figure is Tier 4 until the insider corrects it.

**Defined terms.** *Flow* — the receipts and payments the bank observes in the customer's account. *Standing limit* — the amount the customer may draw at any time, recomputed from the flow, without an application. *Draw* — a transfer from the limit to the account balance, made by the customer. *Receipts share* — the fixed fraction of each receipt that repays the drawn balance until it is cleared. *Account line* — Case A of the levelled line, the account that holds and moves money (the Kept design occupies it).

## 1 · Component register (Flow Register format)

| ID | Product | Component | Introduced at | Carries |
|---|---|---|---|---|
| WP-1 | Working | the standing limit — computed from the flow by the limit engine, shown in the account, recomputed daily | C1 | the customer's "I can see what I can draw" state; the bank's exposure decision, which no person makes |
| WP-2 | Working | the draw — the customer moves money from the limit to the balance in the account, no application | C1 | the customer's "I have the money" state; the term loan and the overdraft dissolve into one running facility (a term-shaped draw is a draw with a fixed receipts share) |
| WP-3 | Working | the receipts share — a term of the account agreement under which a fixed fraction of each receipt repays the drawn balance | C1 | the customer's "it repays itself from what comes in" state; the bank's collections operation, which no longer exists as an operation |
| CP-1 | Communications | the limit statement — the standing limit and the receipts share, visible in the account before any need arises | C1 (named; the customer's conviction that it is real belongs to C4) | the "aware" state only |
| — | Communications | how a customer who has never borrowed comes to trust the limit enough to draw | `[REQUIRES C4+]` | not designed |
| — | Payment | the price — the interest and any fee on the drawn balance, and how it is presented | `[REQUIRES C6]` | not designed; the mode-3 ceiling is the price paid today |
| — | Partner | the accountant, the accounting software or the platform through which the customer meets the limit | `[REQUIRES C7]` | not designed |
| — | Working | the limit for an account with less than ⚠ six months of flow — the start-up | `[REQUIRES C2]` | not designed; the excluded population is sized at R2 |

## 2 · The customer's journey — the business (four phases)

Sparse states; a component sits on each transition; a transition with no component carries a flag.

### Phase 1 — Becoming

| From state | To state | Component | Change (cognitive / emotive / behavioural) | Requirement |
|---|---|---|---|---|
| holds an account; borrows nowhere, or applies and is refused, or puts in personal money | aware that the account carries a standing limit | CP-1 | cognitive | C1 |
| aware | convinced the limit is real and the receipts share is bearable | — `[REQUIRES C4+]` | emotive | not designed at F1 |
| convinced | draws for the first time | WP-2 | behavioural | C1 |

### Phase 2 — Consuming (core delivery — the phase R1 changes)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| needs working money this week | has the money in the account | WP-2 — the draw, within the standing limit, no application, no decision event | behavioural | C1 |
| drawn | drawn balance falls as receipts arrive | WP-3 — the receipts share | behavioural (nothing to do) | C1 |
| flow grows or shrinks | standing limit rises or falls | WP-1 — recomputed daily from the flow | cognitive (the customer sees the limit move with the business) | C1 |
| flow stops | limit falls to zero; drawn balance stays; the exception cell contacts the customer | WP-1 and the exception activity (AOM 3b) | behavioural | C1 |

### Phase 3 — Paying (the phase R3 changes; the price is C6)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| drawn | pays interest on the drawn balance, taken with the receipts share | — `[REQUIRES C6]` — structure not designed; the mode-3 ceiling is the price paid today | behavioural | not designed at F1 |

### Phase 4 — Repeating

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| cleared | draws again when needed; the limit was never withdrawn | WP-1 | behavioural | C1 |
| the business grows | the limit grows with the flow; no new application at any size below the form's ceiling | WP-1 | cognitive | C1; the ceiling of the form is `[REQUIRES C2]` |

## 3 · User and partner tracks (property holders who are not the customer — VA-71)

### Account line track (the bank's own account, Case A) — internal holder, C1

| State | Component | Holder | Note |
|---|---|---|---|
| the flow is observed and held as a record | the account ledger | the bank (the Kept design on Case A; a dependency, not designed here) | the limit engine reads the ledger; nothing in this design changes the account |
| the receipts share is a term of the account agreement | WP-3 | the bank's account terms; for a sole trader or a partnership of two or three persons borrowing under £25,000 the agreement is regulated under the Consumer Credit Act 1974 (s.16B exempts business credit above £25,000; a limited company is never a CCA borrower) | a compliance line, not a decision |

### Limit engine track (the bank's own operators) — internal holder, C1

| State | Component | Holder | Note |
|---|---|---|---|
| the limit is computed by a rule from the flow; no person decides an account | WP-1 | the limit engine team and the model-risk reviewer (AOM 3c) | the rule is a model under the bank's model-risk standard; the PRA's SS1/23 applies |
| an account whose flow stops is handled by a person | exception activity (AOM 3b) | the exception cell | the only human contact in the form |

### Regulator track — C1, unchanged

| State | Component | Holder | Note |
|---|---|---|---|
| the bank holds Part 4A permission to lend and accept deposits | — | PRA and FCA | no new permission is needed; capital under the standardised approach (75% regulatory retail SME) |

### Partner track — flagged

| State | Component | Holder | Note |
|---|---|---|---|
| who brings the customer to the limit | — | `[REQUIRES C7]` | not designed |

## 4 · State changes traced to requirements (the traceability check)

| State change | Component | Requirement | Status |
|---|---|---|---|
| refused or self-funding → aware of a standing limit | CP-1 | C1 | carried |
| aware → convinced | — | C4+ | flagged |
| needs money → has money, no application | WP-2 | C1 | carried |
| drawn → repaid from receipts, no collections operation | WP-3 | C1 | carried |
| flow changes → limit changes | WP-1 | C1 | carried |
| flow stops → exception contact | AOM 3b | C1 | carried |
| drawn → pays a price | — | C6 | flagged |
| no flow history → a limit | — | C2 | flagged |

Every C1 transition carries a component or a flag. No transition is carried by a component that a later requirement has not yet designed.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. Runner-drafted, PROVISIONAL on the object-after PCO. |
