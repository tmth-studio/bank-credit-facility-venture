# Business bank credit facility line — activity and operating model (AOM), v1, at C1

**Venture:** the credit facility line of a large UK SME bank (Case B), Path C mode 3 — see `../bank-credit-facility-c1-v1-2026-09-18.md`. **Created at R1** (18 Sep 2026), runner-drafted, PROVISIONAL on a PCO that is object-after to 20 Sep 2026 17:00. **Scale:** the incumbent's own volume, a red field — `[average drawn SME balance £]`; public proxy used throughout: own base ⚠ 950,000 business accounts (PCO S11), ⚠ 80% with six months of flow so carrying a limit (⚠ 760,000), ⚠ 30% drawn at any time (⚠ 228,000), ⚠ £15–25k average drawn, so a drawn book of ⚠ £3.4–5.7bn. Cross-check: the UK SME bank lending stock is £198bn across 5.69m businesses, £34,800 a business (BBB 2025/26 and DBT 2025, FACT), with just under 20% of SMEs holding a loan (CMA 2016, FACT). **Naming note:** the model file `bank-credit-facility-aom-model-at-C1.yaml` is a build item; this document is the record. **Every cost line traces resource → activity → driver → volume.** Every ⚠ figure is Tier 4 until the insider corrects it. The bank is not named.

**Defined terms.** As in the CTM: *flow*, *standing limit*, *draw*, *receipts share*, *account line*. *Exception cell* — the smallest operating unit of people in the form: the team that handles accounts whose flow has stopped or whose limit rule has been overridden by a fraud or conduct signal.

## 1 · Actors

| Actor | Role in the form | Level |
|---|---|---|
| The business (customer) | holds its account; draws; is repaid from by the receipts share | customer |
| The account line (Case A) | holds the flow and the balance; the ledger the limit engine reads | internal dependency — not designed here |
| The limit engine | computes every account's standing limit daily from the flow by a rule; no person decides an account | HQ, automated |
| The exception cell | the people who act when the flow stops, a signal fires, or a customer disputes | LMU |
| Model risk and credit oversight | owns the limit rule as a model; sets the risk appetite the rule expresses; reports to the board's risk committee | HQ |
| Product, conduct and compliance | the account terms, the CCA-regulated agreement for sole traders under £25,000, Consumer Duty outcomes | HQ |
| Treasury | funds the drawn book from the account line's deposits; holds capital against drawn and undrawn exposure | HQ, existing function |
| PRA and FCA | permissions and capital unchanged; the rule is a model under SS1/23 | external, unchanged |

## 2 · Ops map — the three flows

**Money.** Deposits on the account line fund the drawn book (treasury). A draw moves money from the limit to the account balance. Each receipt into the account is split: the receipts share reduces the drawn balance; the rest stays with the customer. Interest is taken with the share (structure `[REQUIRES C6]`). A write-off leaves the book when an account's flow has stopped and the exception cell has closed it.

**Information.** The ledger (account line) → the limit engine → the standing limit shown in the account (CP-1). Signals (fraud, conduct, flow-stop) → the exception cell. The rule's performance (loss by cohort) → model risk → the rule.

**Product.** The standing limit is the product. It exists on every account with enough flow before any need arises. The draw and the receipts share are the customer's only two actions.

**What the conventional form performs that this form does not.** The application; the per-application credit decision (a person or a scorecard reading documents the applicant produced); the security process (guarantee, debenture, charge); the annual review; the collections operation. Each is named so its absence is a design, not an omission.

## 3 · Activity table — LMU first (one exception cell), then HQ

### 3a · Making — the limit and the draw (stream: Making; level: per account, automated)

| Activity | Performer | Driver | Volume at scale | Unit cost ⚠ | Note |
|---|---|---|---|---|---|
| read the account's flow and compute the standing limit | limit engine | every account with a limit, daily | ⚠ 760,000 accounts × 365 | compute ⚠ £1–2 per account a year | a rule, not a decision |
| show the limit and the receipts share in the account | account line front end | every account with a limit | ⚠ 760,000 | inside the account line's existing cost | CP-1 |
| execute a draw | account line ledger | draws a year, ⚠ 3 per drawn account | ⚠ 680,000 | ⚠ £0.5 per draw | WP-2 |
| split each receipt by the receipts share | account line ledger | receipts into drawn accounts | ⚠ 228,000 × ⚠ 300 a year | ⚠ £0.01 per receipt | WP-3 |
| fund the drawn balance | treasury | average drawn balance | ⚠ £3.4–5.7bn | ⚠ 1.5–3.0% a year | the deposit cost of the account line |
| absorb expected loss | the book | drawn balance × loss rate | ⚠ 2.0–4.0% of drawn | — | the critical assumption; see the run record |

Per drawn account, the automated activities cost ⚠ £2–5 a year on a ⚠ £15–25k balance — ⚠ £0.1–0.3 per £1,000 drawn, rounded up to £2–5 per £1,000 in the FIT model to hold a margin for the computing and payment cost the account line would allocate.

### 3b · Making — exceptions (stream: Making; level: LMU — one exception cell)

| Activity | Performer | Driver | Volume per cell a year ⚠ | Hours each ⚠ | Hours a year ⚠ |
|---|---|---|---|---|---|
| contact an account whose flow has stopped with a balance drawn; agree a clearing plan or close | exception handler | ⚠ 2% of drawn accounts | 2,000 | 4 | 8,000 |
| review an account where a fraud or conduct signal has overridden the rule | exception handler | ⚠ 3% of drawn accounts | 3,000 | 2 | 6,000 |
| handle a customer dispute on the limit or the share | exception handler | ⚠ 1% of drawn accounts | 1,000 | 1 | 1,000 |
| close and write off | exception handler | ⚠ 1% of drawn accounts | 1,000 | 1 | 1,000 |
| **Cell total** | | **100,000 drawn accounts** | | | **⚠ 16,000** |

One cell covers ⚠ 100,000 drawn accounts with ⚠ 16,000 hours a year — ⚠ 11 people at 1,500 productive hours, with a supervisor and a trainer. At ⚠ 228,000 drawn accounts the form needs ⚠ 2.3 cells: ⚠ 25 people. **Capacity figure used throughout (VA-91): ⚠ 16,000 exception hours per cell a year; ⚠ 36,500 hours at scale.**

### 3c · HQ functions (level: HQ; stream: Making support, Delivering, Selling)

| Function | People ⚠ | Cost a year ⚠ £m | Driver |
|---|---|---|---|
| limit engine and data team — builds and runs the rule, the data pipeline, the monitoring | 25 | 3.0–4.0 | fixed per HQ |
| model risk and credit oversight — validates the rule, sets appetite, reports loss by cohort | 10 | 1.5–2.0 | fixed per HQ |
| product, conduct and compliance — account terms, the CCA agreement under £25,000, Consumer Duty | 10 | 1.0–1.5 | fixed per HQ |
| exception cells (from 3b) | 25 | 1.5–2.0 | scales with drawn accounts |
| technology run cost — computing, storage, the payment systems inside the account line allocated to the limit | — | 1.0–3.0 | scales with accounts |
| fraud monitoring allocation | — | 0.5–2.0 | scales with accounts |
| **Running cost** | **⚠ 70** | **⚠ 8.5–14.5** | ≈ ⚠ 0.15–0.43% of the drawn book |

Headcount check: the conventional form at this volume employs relationship managers (a portfolio of ⚠ 200–300 clients each below £2m turnover, CMA 2016 and judged), credit underwriters, security administrators and a collections and recoveries function (FCA SME collections review 2022 covered 11 banks). None of those roles exists in this form. The insider corrects the conventional headcount; no public source carries it.

### 3d · Activities the conventional form performs and this form removes (for the drop, not the floor)

| Conventional activity | Zone | Cost evidence |
|---|---|---|
| assess an application on financial statements, credit history and security | Making | US benchmark $3,000–4,000 per small loan (ProSight, T3); judged UK bank cost per person-decision ⚠ £500–1,500 (bank-conventional-model-object.yaml, 14 Sep 2026); "the transaction cost of a $100,000 loan is comparable to that of a $1m loan" (Mills and McCarthy, HBS 2014) |
| take and perfect security | Making | ⚠ £200–800 per facility |
| annual review of each facility | Making | ⚠ £200–500 per facility a year |
| collections and recoveries | Delivering | FCA 2022 review; ⚠ £5–15 per £1,000 drawn |
| relationship management allocated to lending | Selling | ⚠ £240–360 per client a year below £2m (judged, from Glassdoor pay and a judged portfolio) |

## 4 · Role support (every performer has a supervisor, a trainer and a quality reviewer)

| Performer | Supervisor | Trainer | Quality reviewer |
|---|---|---|---|
| exception handler | cell lead | cell lead, with the product team's conduct standard | model risk (samples closed cases monthly) |
| limit engine (the rule) | head of the engine team | — | model risk (independent validation under SS1/23) |
| product and compliance | head of product | — | second-line compliance (existing) |

PASS: no performer lacks a supervisor, a trainer or a reviewer.

## 5 · LMU sizing — one exception cell

| Item | Value ⚠ |
|---|---|
| drawn accounts covered | 100,000 |
| drawn balance covered | £1.5–2.5bn |
| people | 11 handlers + 1 lead + 1 trainer (shared across cells) |
| fixed cost a year | £0.7–0.9m |
| contribution from the balance covered at the ⚠ 7.5–12% price paid today | £110–300m of revenue |
| stand-up time | ⚠ 6–10 weeks (the handbook is the training; the rule is already running) |

The cell covers its cost from a fraction of a per cent of the revenue on the balance it covers. PASS on contribution.

## 6 · Cost floor derivation (per £1,000 of average drawn balance, per year, at scale — the FIT input)

| Layer | £ per £1,000 a year ⚠ | Derivation |
|---|---|---|
| PVC — funding | 15–30 | deposit cost ⚠ 1.5–3.0% (Bank Rate 4.0% from August 2025, FACT) |
| PVC — expected loss | 20–40 | ⚠ 2.0–4.0% on a flow-underwritten pool; the critical assumption |
| PVC — computing and payments | 2–5 | 3a, rounded up |
| PVC — exceptions and write-off handling | 3–8 | 3b: ⚠ £1.5–2.0m across 2.3 cells ÷ £3.4–5.7bn = £0.3–0.6, plus write-off administration and legal ⚠ £3–7 |
| **PVC** | **40–83** | |
| RC | 2–5 | 3c: ⚠ £8.5–14.5m ÷ £3.4–5.7bn = £1.5–4.3, rounded |
| SC | not designed until C3 | — |
| IC — capital on drawn | 10.8–13.5 | 75% risk weight (regulatory retail SME, standardised, FACT) × ⚠ 12% total capital × ⚠ 12–15% cost of equity |
| IC — capital on undrawn | 1.6–3.4 | ⚠ 1.5–2.5 undrawn per 1 drawn × 10% credit conversion factor (Basel 3.1, PRA PS9/24, from 1 January 2027, FACT) × 75% × 12% × 12–15% |
| **IC** | **12–17** | rounded |
| **Cost floor (PVC + RC + IC)** | **54–105** | scaling cost excluded — indicative |

Conventional form on the same unit, blended small-business book, all ⚠: funding 15–30; expected loss 10–25 (a filtered, part-secured pool); capital 10–14; operating 25–85 (3d: the decision ⚠ £500–1,500 on a ⚠ £24k average small facility — the Bank Referral Scheme's average deal is £23,887, FACT — over a ⚠ 2–3 year life = 7–31; annual review 8–21; collections 5–15; relationship allocation 5–20). **Conventional floor ⚠ 60–154.** On a £10,000 facility the operating line alone is ⚠ £60–200 per £1,000, which is why the conventional gate refuses it.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 18 September 2026 | Created at R1. Runner-drafted, PROVISIONAL on the object-after PCO. |

## 7 · Baseline correction, 18 September 2026 (v1.1)

The insider confirmed that the bank operates pre-approved limits at scale (`[clients with a pre-approved limit]`), is digitising fulfilment end to end, and is extending pre-approval to newly joined clients. The comparison floor is therefore the **roadmap form**, not the application form in section 3d. Re-cut, per £1,000 of drawn balance a year, all ⚠: funding 15–30; expected loss 10–25; capital 10–14; the decision on the pre-approved segment 1–3 (7–31 on the segment with no conduct history); security 2–5; annual review 8–21; collections 5–15; relationship 5–20. **Roadmap-form floor ⚠ 63–164 blended; ⚠ 57–133 on the pre-approved segment.** The lines that are fixed per facility and remain in the roadmap form — security, review, collections, relationship — are ⚠ 20–61; the new form replaces them with the exception cells and the rule at ⚠ 5–13 (3b, 3c). The new form's own floor (section 6) is unchanged at ⚠ 54–105.
