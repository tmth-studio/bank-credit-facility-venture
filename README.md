# A business bank's credit facility line — venture design record

The full design record for a standing credit facility on a business current account: a limit computed daily from the account's own cash flow, drawn without an application, repaid as a share of receipts, priced at £140 per £1,000 drawn a year with no fee.

The bank is not named anywhere in these files. Every figure only the bank holds is written as a red field — `⚠ [description]` — for the bank to fill in. All other figures are from public sources, cited in each record.

**Status (22 September 2026):** architecture complete, C1 to C10. Verified SOUND 87.7 at C10. Financial simulation: PASS at the central and optimistic scenarios; BORDERLINE at the conservative scenario (30.3% against a 60% gate). The one input that moves the gate is the loss rate on a flow-underwritten pool, which the bank can read from its own history without any customer or release.

## Read in this order

1. `bank-credit-facility-architecture-summary-2026-09-21.md` — two pages: what it is, what it earns, what would stop it
2. `bank-deposits-lending-pco-v1-2026-09-18.md` — the opportunity statement: customer, outcome, the cost the conventional form pays
3. `bank-credit-facility-c1-v2-2026-09-18.md` to `bank-credit-facility-c10-v1-2026-09-21.md` — the ten challenges, one record each (C3 has a v2; read it, v1 is kept for the audit trail)
4. `bank-credit-facility-fin-sim-2026-09-21.md` — the financial simulation at scale and on the monthly path to scale
5. `bank-credit-facility-consistency-audit-C10-2026-09-21.md` and `bank-credit-facility-verify-C10-2026-09-21.md` — the whole-architecture audit and the independent verification

## The models folder

`sme-fintech-models/` holds the working models behind the records:

- `bank-credit-facility-ctm-v10-2026-09-21.md` — the customer transformation model (how the customer's routine changes, state by state); v1 to v9 are the history
- `bank-credit-facility-aom-v10-2026-09-21.md` — the at-scale operating model (every activity, resource, driver and volume; the cost floor is derived here)
- `bank-credit-facility-fit-model-at-C10.yaml` and `bank-credit-facility-fit-verifier-r10-2026-09-21.md` — the cost floor against the price at each challenge
- `bank-credit-facility-tam-model.yaml` — the addressable volume and its survival by segment
- `bank-credit-facility-counterfactual.md` — what the conventional form costs at scale, for comparison
- `bank_credit_facility_fin_sim.py` and `bank-credit-facility-fin-sim-outputs.json` — the simulation script and its output
- `bank-credit-facility-f1-status.md` — the one-page status of every requirement, gate and open item

## Filling in the red fields

Search any file for `⚠` to find every figure the bank holds. The first to fill is the loss rate by account-conduct band: it sets the verdict. After it, in order: the share of accounts with six months or more of flow, the share of overdraft users on the standard tariff, the acceptance rate, and each cost line.

## Method

Designed under the Integrated Venture Engine (IVE) method. The design records follow its ten requirements: three that make the economics work (R1–R3), four that make the customer's routine work (R4–R7), three that hold the market position (R8–R10).

© Tough Minds, Tender Hearts Ltd 2026. All rights reserved. Runner-drafted; object-after review to 23 September 2026 17:00.
