# Business bank credit facility line — customer transformation map (CTM), v2, at C2

**Venture:** the credit facility line of a large UK SME bank (Case B — term loan and overdraft), Path C mode 3 — see `../bank-credit-facility-c2-v1-2026-09-21.md`. **v2 written at R2** (21 Sep 2026), runner-drafted under the propose-and-confirm rule. **v1** (`bank-credit-facility-ctm-v1-2026-09-18.md`) is retained unchanged as the C1 record. **Update mode:** only the rows R2 adds or changes are new; every other row is carried from v1 with its C1 trace. **Customer at C2 (selected at R2):** the established UK SME with observable account flow that currently pays a standard-tariff overdraft at 15–30% EAR for recurrent working-capital draws. **Naming note:** the challenge skill names the model file `bank-credit-facility-ctm-model-at-C2.yaml` and generates the views from it; this venture's pattern (C1) is a document, so this file is the record and the model file stays a build item — the runner's call, carried in the C2 record. Every state change is traced to a requirement by number; anything a later requirement owns is flagged `[REQUIRES C[N]+]`, not designed. The bank is not named. Every figure only the bank holds is a red field `⚠ [description]`. Every ⚠ figure is Tier 4 until the insider corrects it.

**Defined terms.** As in v1: *flow*, *standing limit*, *draw*, *receipts share*, *account line*. New at C2: *Standard tariff* — the published interest rate and fees a bank charges on a business overdraft that is not individually negotiated. *Migration* — the one-time move of a customer's existing arranged overdraft, and any balance drawn on it, into the standing limit and a draw with a receipts share. *Price condition* — the rule that the all-in price of the limit per £1,000 drawn stays below the standard-tariff cost the customer paid before migration; a condition, not a price — the price and its structure are C6's.

## 1 · Component register (Flow Register format)

| ID | Product | Component | Introduced at | Carries |
|---|---|---|---|---|
| WP-1 | Working | the standing limit — computed from the flow by the limit engine, shown in the account, recomputed daily | C1 | the customer's "I can see what I can draw" state; the bank's exposure decision, which no person makes |
| WP-2 | Working | the draw — the customer moves money from the limit to the balance in the account, no application | C1 | the customer's "I have the money" state |
| WP-3 | Working | the receipts share — a term of the account agreement under which a fixed fraction of each receipt repays the drawn balance | C1 | the customer's "it repays itself from what comes in" state; the bank's collections operation, which no longer exists as an operation |
| **WP-4** | Working | **the migration** — the customer's existing arranged overdraft is retired and any drawn overdraft balance becomes a draw on the standing limit with a receipts share; one event per overdraft account; the customer may decline and keep the overdraft | **C2** | the customer's "the money I already owe now sits on the limit, at less than I was paying" state; the retirement of the standard-tariff overdraft as a product on the account |
| CP-1 | Communications | the limit statement — the standing limit and the receipts share, visible in the account before any need arises | C1 (v2 amended at C2: the statement also shows, once a year, what the customer paid on the overdraft in the year before migration and what the limit cost in the year since) | the "aware" state (C1); the "I can see the saving" state (C2) |
| **PC-1** | Payment | **the price condition** — the all-in price of the limit per £1,000 drawn is held below the standard-tariff cost the customer paid before migration; a constraint the Payment product must satisfy | **C2 (condition only)** | the customer's "this costs me less than the overdraft did" state; the structure, the level and the presentation of the price are `[REQUIRES C6]` |
| — | Communications | how a customer who has never borrowed comes to trust the limit enough to draw | `[REQUIRES C4+]` | not designed |
| — | Payment | the price — the interest and any fee on the drawn balance, its structure and how it is presented | `[REQUIRES C6]` | not designed; PC-1 constrains it, nothing more |
| — | Partner | the accountant, the accounting software or the platform through which the customer meets the limit | `[REQUIRES C7]` | not designed |
| — | Working | the limit for an account with no flow history anywhere (new to trading) | excluded at C2 — recorded in the TAM data object as an excluded sub-class; no later requirement is named as its owner | not designed |

## 2 · The customer's journey — the business (four phases)

Sparse states; a component sits on each transition; a transition with no component carries a flag.

### Phase 1 — Becoming

| From state | To state | Component | Change (cognitive / emotive / behavioural) | Requirement |
|---|---|---|---|---|
| holds an account and pays a standard-tariff overdraft for recurrent draws (the selected customer); or borrows nowhere, or is refused, or puts in personal money | aware that the account carries a standing limit | CP-1 | cognitive | C1 |
| aware | convinced the limit is real and the receipts share is bearable | — `[REQUIRES C4+]` | emotive | not designed at F1 |
| convinced | draws for the first time (a customer with no overdraft); **or accepts migration of the existing overdraft (the selected customer)** | WP-2; **WP-4** | behavioural | C1; **C2** |

### Phase 2 — Consuming (core delivery — the phase R1 changed; R2 adds the value-realisation rows)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| needs working money this week | has the money in the account | WP-2 — the draw, within the standing limit, no application, no decision event | behavioural | C1 |
| drawn | drawn balance falls as receipts arrive | WP-3 — the receipts share | behavioural (nothing to do) | C1 |
| flow grows or shrinks | standing limit rises or falls | WP-1 — recomputed daily from the flow | cognitive | C1 |
| flow stops | limit falls to zero; drawn balance stays; the exception cell contacts the customer | WP-1 and the exception activity (AOM 3b) | behavioural | C1 |
| **pays the standard tariff on an arranged overdraft, renewed each year** | **the overdraft is retired; the drawn balance sits on the limit under a receipts share; no renewal, no fee event** | **WP-4** | **behavioural** | **C2** |
| **carries the drawn balance on the limit** | **sees, once a year, what the overdraft cost and what the limit cost — the saving is visible** | **CP-1 (amended)** | **cognitive** | **C2** |
| **carries the drawn balance on the limit** | **the all-in price stays below what the overdraft cost** | **PC-1 (condition); the price itself `[REQUIRES C6]`** | **emotive (relief from the tariff)** | **C2 — condition; C6 — price** |

### Phase 3 — Paying (the phase R3 changes; the price is C6)

| From state | To state | Component | Change | Requirement |
|---|---|---|---|---|
| drawn | pays interest on the drawn balance, taken with the receipts share | — `[REQUIRES C6]` — structure not designed; PC-1 bounds it from above | behavioural | not designed at F1 |

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

### Limit engine track (the bank's own operators) — internal holder, C1

| State | Component | Holder | Note |
|---|---|---|---|
| the limit is computed by a rule from the flow; no person decides an account | WP-1 | the limit engine team and the model-risk reviewer (AOM 3c) | the rule is a model under SS1/23 |
| an account whose flow stops is handled by a person | exception activity (AOM 3b) | the exception cell | the only human contact in the form |
| **a customer declines migration, or queries the saving statement** | **exception activity (AOM 3b, C2 rows)** | **the exception cell** | **C2 — the customer keeps the overdraft; the account carries both until the overdraft's next renewal** |

### Pricing track (the bank's own pricing function) — internal holder, new at C2

| State | Component | Holder | Note |
|---|---|---|---|
| **the price condition is set as a constraint on the Payment product** | **PC-1** | **the bank's pricing committee** | **C2 — the holder of "the price remains below the tariff" is the pricing committee, not the customer; the committee carries the condition; the price it sets is `[REQUIRES C6]`** |

### Regulator track — C1, unchanged

| State | Component | Holder | Note |
|---|---|---|---|
| the bank holds Part 4A permission to lend and accept deposits | — | PRA and FCA | no new permission; capital under the standardised approach |

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
| **pays the tariff on an overdraft → the overdraft is retired and the balance sits on the limit** | **WP-4** | **C2** | **carried** |
| **on the limit → sees the saving once a year** | **CP-1 (amended)** | **C2** | **carried** |
| **on the limit → the price stays below the tariff** | **PC-1 (condition)** | **C2 (condition); C6 (price)** | **carried as a condition; the price is flagged** |
| **declines migration → keeps the overdraft** | **AOM 3b (C2 row)** | **C2** | **carried** |
| drawn → pays a price | — | C6 | flagged |
| no flow history → a limit | — | excluded (TAM data object) | recorded, not carried |

Every C1 and C2 transition carries a component or a flag. No transition is carried by a component that a later requirement has not yet designed: PC-1 is a condition on the Payment product, not the product.

**Component set at C2 (for the margin-of-safety check, VA-74):** WP-1, WP-2, WP-3, WP-4, CP-1 (amended), PC-1 (condition).

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. |
| v2 | 21 September 2026 | R2 update. Added WP-4 (migration), PC-1 (price condition) and the amended CP-1; three Phase 2 rows, one Phase 1 row, one Phase 4 row; the pricing track; the migration row on the account line track; the decline row on the limit engine track. The new-to-trading row is now an excluded sub-class in the TAM data object, not a `[REQUIRES C2]` flag. |
