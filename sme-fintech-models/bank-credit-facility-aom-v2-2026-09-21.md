# Business bank credit facility line — activity and operating model (AOM), v2, at C2

**Venture:** the credit facility line of a large UK SME bank (Case B), Path C mode 3 — see `../bank-credit-facility-c2-v1-2026-09-21.md`. **v2 written at R2** (21 Sep 2026), runner-drafted under the propose-and-confirm rule. **v1** (`bank-credit-facility-aom-v1-2026-09-18.md`) is retained unchanged as the C1 record. **Update mode:** only the rows R2 adds or changes are new; every other row is carried from v1 with its C1 trace. **Scale:** the incumbent's own volume, a red field — `⚠ [average drawn SME balance £]`; public proxy used throughout: own base ⚠ 950,000 business accounts (PCO S11), ⚠ 80% with six months of flow so carrying a limit (⚠ 760,000), ⚠ 30% drawn at any time (⚠ 228,000), ⚠ £15–25k average drawn, so a drawn book of ⚠ £3.4–5.7bn. New at C2: the overdraft accounts inside that base — 950,000 × 11–17% (SME Finance Monitor overdraft use, TAM data object) = ⚠ 104,500–161,500, of which ⚠ 40–70% on the standard tariff = ⚠ 41,800–113,050 (the selected customer). **Naming note:** the model file `bank-credit-facility-aom-model-at-C2.yaml` is a build item; this document is the record and section 0 carries the quantities and events every driver resolves to. **Every cost line traces resource → activity → driver → volume.** No cost line is a share of revenue. Every ⚠ figure is Tier 4 until the insider corrects it. The bank is not named.

**Defined terms.** As in the CTM v2: *flow*, *standing limit*, *draw*, *receipts share*, *account line*, *standard tariff*, *migration*, *price condition*. *Exception cell* — the smallest operating unit of people in the form: the team that handles accounts whose flow has stopped, whose limit rule has been overridden by a fraud or conduct signal, or whose holder has declined migration or queried the saving statement.

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
  q.productive_hours_fte:  1500          # hours a year one handler works on cases; T3, the runner's seat judgement
  q.undrawn_per_drawn:     [1.5, 2.5]    # undrawn limit per £1 drawn; T4
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
actors:
  a.limit_engine · a.account_line · a.treasury · a.exception_handler · a.cell_lead · a.model_risk
  a.product_conduct · a.pricing_committee (C2) · a.customer
floors:
  f.cell_min_people: 12 handlers + 1 lead — reason: the C2 rows add ⚠ 1,000 hours a year to a cell that v1 sized at 11 handlers with no slack
```

## 1 · Actors

| Actor | Role in the form | Level |
|---|---|---|
| The business (customer) | holds its account; draws; is repaid from by the receipts share; **accepts or declines migration (C2)** | customer |
| The account line (Case A) | holds the flow and the balance; the ledger the limit engine reads; **produces the saving statement (C2)** | internal dependency — not designed here |
| The limit engine | computes every account's standing limit daily from the flow by a rule; no person decides an account | HQ, automated |
| The exception cell | the people who act when the flow stops, a signal fires, a customer disputes, **a customer declines migration or queries the saving statement (C2)** | LMU |
| Model risk and credit oversight | owns the limit rule as a model; sets the risk appetite the rule expresses; reports to the board's risk committee | HQ |
| Product, conduct and compliance | the account terms, the CCA-regulated agreement for sole traders under £25,000, Consumer Duty outcomes; **the modifying agreement or variation notice at migration (C2)** | HQ |
| **The pricing committee** | **holds the price condition (PC-1) as a constraint on the Payment product; the price itself is `[REQUIRES C6]`** | **HQ, existing function (C2)** |
| Treasury | funds the drawn book from the account line's deposits; holds capital against drawn and undrawn exposure | HQ, existing function |
| PRA and FCA | permissions and capital unchanged; the rule is a model under SS1/23 | external, unchanged |

## 2 · Ops map — the three flows

**Money.** Deposits on the account line fund the drawn book (treasury). A draw moves money from the limit to the account balance. Each receipt into the account is split: the receipts share reduces the drawn balance; the rest stays with the customer. Interest is taken with the share (structure `[REQUIRES C6]`; level bounded by PC-1). A write-off leaves the book when an account's flow has stopped and the exception cell has closed it. **New at C2:** at migration the drawn overdraft balance moves onto the limit as a draw — no money moves, the ledger reclassifies the balance; the overdraft's renewal fee event stops.

**Information.** The ledger (account line) → the limit engine → the standing limit shown in the account (CP-1). Signals (fraud, conduct, flow-stop) → the exception cell. The rule's performance (loss by cohort) → model risk → the rule. **New at C2:** the ledger → the saving statement once a year (what the overdraft cost in the year before migration; what the limit cost since) → the customer; a decline or a query → the exception cell; the tariff the customer paid → the pricing committee (the reference for PC-1).

**Product.** The standing limit is the product. It exists on every account with enough flow before any need arises. The draw and the receipts share are the customer's only two actions. **New at C2:** for the selected customer the product replaces the overdraft on the same account — migration is the one event that retires the old product.

**What the conventional form performs that this form does not.** The application; the per-application credit decision; the security process; the annual review (**including the overdraft's annual renewal, C2**); the collections operation. Each is named so its absence is a design, not an omission.

## 3 · Activity table — LMU first (one exception cell), then HQ

Every row names the flow it serves (money · information · product), its performer, and a driver that resolves to section 0.

### 3a · Making — the limit, the draw and the migration (stream: Making; level: per account, automated)

| Activity | Flow | Performer | Driver | Volume at scale | Unit cost ⚠ | Note |
|---|---|---|---|---|---|---|
| read the account's flow and compute the standing limit | information | a.limit_engine | e.daily_recompute | ⚠ 760,000 × 365 | compute ⚠ £1–2 per account a year | a rule, not a decision (C1) |
| show the limit and the receipts share in the account | information | a.account_line | q.accounts_with_limit | ⚠ 760,000 | inside the account line's existing cost | CP-1 (C1) |
| execute a draw | money | a.account_line | e.draw | ⚠ 680,000 | ⚠ £0.5 per draw | WP-2 (C1) |
| split each receipt by the receipts share | money | a.account_line | e.receipt | ⚠ 228,000 × ⚠ 300 | ⚠ £0.01 per receipt | WP-3 (C1) |
| fund the drawn balance | money | a.treasury | q.drawn_book_gbp | ⚠ £3.4–5.7bn | ⚠ 1.5–3.0% a year | the deposit cost of the account line (C1) |
| absorb expected loss | money | the book | q.drawn_book_gbp × loss rate | ⚠ 2.0–4.0% of drawn | — | the critical assumption; the binding gate (C1, tested at C2) |
| **retire the overdraft and reclassify its drawn balance as a draw on the limit; issue the modifying agreement or variation notice** | **product** | **a.account_line, with a.product_conduct** | **e.migration** | **⚠ 104,500–161,500, once** | **⚠ £1–3 per account (notice, agreement, ledger change)** | **WP-4 (C2). One-off ⚠ £0.1–0.5m; outside the annual floor; a scaling cost carried to C3 by number** |
| **produce the saving statement** | **information** | **a.account_line** | **e.saving_statement** | **⚠ 104,500–161,500 a year** | **⚠ £0.1 per statement** | **CP-1 amended (C2). ⚠ £10–16k a year, inside the computing line** |

Per drawn account, the automated activities cost ⚠ £2–5 a year on a ⚠ £15–25k balance — ⚠ £0.1–0.3 per £1,000 drawn, rounded up to £2–5 per £1,000 in the FIT model to hold a margin for the computing and payment cost the account line would allocate. The C2 rows add ⚠ £0.003 per £1,000 a year (the statement) and nothing else to the annual line; the rounding absorbs them.

### 3b · Making — exceptions (stream: Making; level: LMU — one exception cell)

| Activity | Flow | Performer | Driver | Volume per cell a year ⚠ | Hours each ⚠ | Hours a year ⚠ |
|---|---|---|---|---|---|---|
| contact an account whose flow has stopped with a balance drawn; agree a clearing plan or close | money | a.exception_handler | e.flow_stop | 2,000 | 4 | 8,000 |
| review an account where a fraud or conduct signal has overridden the rule | information | a.exception_handler | e.signal | 3,000 | 2 | 6,000 |
| handle a customer dispute on the limit or the share | product | a.exception_handler | e.dispute | 1,000 | 1 | 1,000 |
| close and write off | money | a.exception_handler | e.write_off | 1,000 | 1 | 1,000 |
| **explain the saving statement to a customer who queries it** | **information** | **a.exception_handler** | **e.saving_query** | **2,000** | **0.5** | **1,000** |
| **Cell total, recurring** | | | **q.cell_drawn_accounts = 100,000** | | | **⚠ 17,000** |
| *explain migration to a customer who declines or asks; record the decline (one-off, launch year only)* | *product* | *a.exception_handler* | *e.migration_decline* | *4,600–7,100, once* | *0.5* | *2,300–3,600, once* |

**Capacity figure used throughout (VA-91): ⚠ 17,000 exception hours per cell a year; ⚠ 38,800 hours at scale (2.28 cells on ⚠ 228,000 drawn accounts).** One cell is ⚠ 12 handlers at 1,500 productive hours (18,000 hours, so ⚠ 1,000 hours of slack against the 17,000) with a cell lead; the trainer is shared across cells. At scale: ⚠ 2.3 cells, ⚠ 28 handlers and 3 leads, ⚠ 30 people with the shared trainer. The one-off migration row is ⚠ 5,300–8,200 hours across all cells in the launch year — ⚠ 3.5–5.5 people for one year — and sits with the migration cost in the scaling layer, C3 by number. It is not in the capacity figure.

### 3c · HQ functions (level: HQ; stream: Making support, Delivering, Selling)

| Function | Flow | People ⚠ | Cost a year ⚠ £m | Driver |
|---|---|---|---|---|
| limit engine and data team — builds and runs the rule, the data pipeline, the monitoring | information | 25 | 3.0–4.0 | fixed per HQ |
| model risk and credit oversight — validates the rule, sets appetite, reports loss by cohort | information | 10 | 1.5–2.0 | fixed per HQ |
| product, conduct and compliance — account terms, the CCA agreement under £25,000, Consumer Duty; **the migration agreements and the saving statement's conduct standard (C2, +2 people)** | product | 12 | 1.2–1.8 | fixed per HQ |
| **pricing committee — holds PC-1; sets the price `[REQUIRES C6]`** | **money** | **existing function, no new people** | **0** | **fixed per HQ (C2)** |
| technology run cost — computing, storage, the payment systems inside the account line allocated to the limit | information | — | 1.0–3.0 | q.accounts_with_limit |
| fraud monitoring allocation | information | — | 0.5–2.0 | q.accounts_with_limit |
| **HQ running cost (the RC layer)** | | **⚠ 47** | **⚠ 7.2–12.8** | |
| exception cells (from 3b; counted in the PVC layer, not here) | money · information · product | 30 | 1.8–2.4 | q.drawn_accounts |
| **All people in the form** | | **⚠ 77** | **⚠ 9.0–15.2** | ≈ ⚠ 0.16–0.45% of the drawn book, stated for scale only — no cost line is derived from it |

**Correction at v2.** v1 counted the exception cells in both 3b (the PVC exceptions line) and 3c (the RC line). v2 counts them once, in PVC. The RC layer falls from ⚠ £8.5–14.5m to ⚠ £7.2–12.8m; the rounded RC figure per £1,000 (section 6) is unchanged.

Headcount check: the conventional form at this volume employs relationship managers (a portfolio of ⚠ 200–300 clients each below £2m turnover, CMA 2016 and judged), credit underwriters, security administrators and a collections and recoveries function (FCA SME collections review 2022 covered 11 banks). None of those roles exists in this form. The insider corrects the conventional headcount; no public source carries it.

### 3d · Activities the conventional form performs and this form removes (for the drop, not the floor)

| Conventional activity | Zone | Cost evidence |
|---|---|---|
| assess an application on financial statements, credit history and security | Making | US benchmark $3,000–4,000 per small loan (ProSight, T3); judged UK bank cost per person-decision ⚠ £500–1,500 (bank-conventional-model-object.yaml, 14 Sep 2026); "the transaction cost of a $100,000 loan is comparable to that of a $1m loan" (Mills and McCarthy, HBS 2014) |
| take and perfect security | Making | ⚠ £200–800 per facility |
| annual review of each facility, **including the overdraft's annual renewal and its fee event (C2)** | Making | ⚠ £200–500 per facility a year |
| collections and recoveries | Delivering | FCA 2022 review; ⚠ £5–15 per £1,000 drawn |
| relationship management allocated to lending | Selling | ⚠ £240–360 per client a year below £2m (judged, from Glassdoor pay and a judged portfolio) |

## 4 · Role support (every performer has a supervisor, a trainer and a quality reviewer)

| Performer | Supervisor | Trainer | Quality reviewer |
|---|---|---|---|
| exception handler | cell lead | cell lead, with the product team's conduct standard; **the migration and saving-statement scripts are part of the handbook (C2)** | model risk (samples closed cases monthly); **conduct samples migration declines quarterly (C2)** |
| cell lead | head of exceptions (one across cells) | head of exceptions | model risk |
| limit engine (the rule) | head of the engine team | — (a rule; the team is trained by the engine team's own onboarding) | model risk (independent validation under SS1/23) |
| account line (the ledger, the statement) | head of the account line (Case A) | — (a system) | second-line operational risk (existing) |
| product, conduct and compliance | head of product | second-line compliance (the conduct standard) | second-line compliance (existing) |
| **pricing committee** | **the chief financial officer's function (existing)** | **— (a committee of existing officers)** | **second-line compliance and internal audit (existing); the condition is a documented control** |
| treasury | head of treasury (existing) | — | asset and liability committee (existing) |

PASS: no performer lacks a supervisor, a trainer or a reviewer.

## 5 · LMU sizing — one exception cell

| Item | Value ⚠ |
|---|---|
| drawn accounts covered | 100,000 (q.cell_drawn_accounts) |
| drawn balance covered | £1.5–2.5bn |
| people | 12 handlers + 1 lead + 1 trainer (shared across cells) |
| fixed cost a year | £0.8–1.05m (12 handlers ⚠ £50–65k loaded; lead ⚠ £70–90k; trainer share ⚠ £20–30k; tooling and premises ⚠ £0.1–0.15m) |
| contribution from the balance covered at the ⚠ 7.5–12% price paid today on the whole book | £110–300m of revenue |
| stand-up time | ⚠ 6–10 weeks (the handbook is the training; the rule is already running) |

The cell covers its cost from a fraction of a per cent of the revenue on the balance it covers. PASS on contribution. The price used here is the whole book's price paid today (C1), not the selected customer's KMC; the C2 fit model carries the KMC.

## 6 · Cost floor derivation (per £1,000 of average drawn balance, per year, at scale — the FIT input)

| Layer | £ per £1,000 a year ⚠ | Derivation |
|---|---|---|
| PVC — funding | 15–30 | deposit cost ⚠ 1.5–3.0% (Bank Rate 4.0% from August 2025, FACT); unchanged by migration — the balance was already funded |
| PVC — expected loss | 20–40 | ⚠ 2.0–4.0% on a flow-underwritten pool; the critical assumption. At C2 the migrated pool is an observed-conduct pool (the bank has seen its overdraft behaviour), which cannot raise the rate above the flow-underwritten assumption; the band is held, not lowered — the insider's figure replaces it |
| PVC — computing and payments | 2–5 | 3a, rounded up; the saving statement adds ⚠ £0.003 |
| PVC — exceptions and write-off handling | 3–8 | 3b: ⚠ £1.8–2.4m across 2.3 cells ÷ £3.4–5.7bn = £0.32–0.71, plus write-off administration and legal ⚠ £3–7 = £3.3–7.7, rounded |
| **PVC** | **40–83** | unchanged from C1 |
| RC | 2–5 | 3c: ⚠ £7.2–12.8m ÷ £3.4–5.7bn = £1.26–3.76, rounded to the C1 band (the double count removed; the +2 conduct people added) |
| SC | not designed until C3 | the one-off migration cost (⚠ £0.1–0.5m notices; ⚠ 5,300–8,200 handler hours) is recorded here by number and not in the annual floor |
| IC — capital on drawn | 10.8–13.5 | 75% risk weight (regulatory retail SME, standardised, FACT) × ⚠ 12% total capital × ⚠ 12–15% cost of equity |
| IC — capital on undrawn | 1.6–3.4 | q.undrawn_per_drawn ⚠ 1.5–2.5 × 10% credit conversion factor (Basel 3.1, PRA PS9/24, from 1 January 2027, FACT) × 75% × 12% × 12–15%; an overdraft limit already carried this treatment, so migration adds nothing |
| **IC** | **12–17** | rounded |
| **Cost floor at C2 (PVC + RC + IC)** | **54–105** | scaling cost excluded — indicative; the C2 design adds no annual cost line that survives rounding |

**What R2 changed in the floor: nothing that survives rounding.** The migration is a one-off; the statement is ⚠ £0.003 per £1,000; the extra exception hours are ⚠ £0.02–0.05 per £1,000 inside the 3–8 band. The floor a C2 price must clear is ⚠ 54–105 per £1,000 a year. The KMC it is measured against is ⚠ £150–300 (TAM data object, KMC-OD-STD-TARIFF).

Conventional form on the same unit, all ⚠, unchanged from v1: application form ⚠ 60–154; roadmap form (v1 section 7) ⚠ 63–164 blended, ⚠ 57–133 on the pre-approved segment. On the selected customer's own alternative — the standard-tariff overdraft — the price paid is ⚠ 150–300, and the conventional cost behind it is the roadmap form's ⚠ 57–133 plus the tariff's margin; the gap between what the customer pays and what the form costs is what R2 selects.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. Runner-drafted, PROVISIONAL on the object-after PCO. |
| v1.1 | 18 September 2026 | Baseline correction (roadmap form). |
| v2 | 21 September 2026 | R2 update. Section 0 added: every driver now resolves to a named quantity, event or actor (RD-031). Every activity row names its flow. Migration (WP-4), the saving statement (CP-1) and the pricing committee (PC-1) added; two exception rows added (saving query, recurring; migration decline, one-off); capacity figure restated once at ⚠ 17,000 hours per cell; cells resized to 12 handlers. Double count of the exception cells between 3b and 3c removed. Floor recomputed on four layers: ⚠ 54–105, unchanged. |
