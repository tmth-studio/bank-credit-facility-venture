# Cell index — Credit facility line — Case B business-case evidence workbook

Workbook: `bank-credit-facility-business-case-evidence.xlsx` · built from the model data file on 2026-09-22 · currency GBP.

Cite a figure in the business case as its name in this table, for example `margin_of_safety` or `cost_per_transaction`. Every name is also a defined name inside the workbook. Values are at the base scenario; the workbook recomputes them live.

## Results

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `scenario` | '1 Master'!$B$4 | 1 | Scenario switch: 1 base, 2 all-low, 3 all-high |
| `tam` | '2 Customers'!$B$5 | 760,000 | Total addressable market, households or customers |
| `units` | '2 Customers'!$B$6 | 3 | Number of operating units at scale |
| `customers_per_unit` | '2 Customers'!$B$9 | 76,000 | Customer base per operating unit at steady state |
| `transactions_per_unit` | '2 Customers'!$B$10 | 1,520,002 | Transactions per operating unit per month at steady state |
| `transactions_venture` | '2 Customers'!$B$11 | 4,560,005 | Transactions across the venture per month at steady state |
| `revenue_per_unit` | '2 Customers'!$E$15 | 17,733,403 | Revenue per operating unit per month at interim prices |
| `cogs_per_unit` | '2 Customers'!$G$15 | 2,850,003 | Cost of goods per operating unit per month |
| `headcount_per_unit` | '3 HR'!$D$20 | 11 | Headcount per operating unit |
| `hr_cost_per_unit` | '3 HR'!$F$20 | 54,587 | Staff cost per operating unit per month |
| `ho_staff_cost` | '3 HR'!$D$27 | 572,926 | Head-office staff cost per month |
| `capital_per_unit` | '4 Depreciation'!$F$5 | 0 | Capital assets per operating unit |
| `depreciation_per_unit` | '4 Depreciation'!$G$5 | 0 | Depreciation per operating unit per month |
| `capital_head_office` | '4 Depreciation'!$F$8 | 0 | Head-office capital assets |
| `depreciation_head_office` | '4 Depreciation'!$G$8 | 0 | Head-office depreciation per month |
| `running_per_unit` | '5 Running'!$E$10 | 4,911,422 | General running cost per operating unit per month |
| `running_head_office` | '5 Running'!$E$20 | 495,834 | Head-office running cost per month |
| `startup_per_unit` | '6 Start-up'!$B$7 | 0 | Start-up cost per operating unit (one-time plus working capital) |
| `startup_charge_per_unit` | '6 Start-up'!$B$9 | 0 | Start-up charge per operating unit per month |
| `development_head_office` | '6 Start-up'!$B$21 | 8,759,500 | Head-office development cost, one-time |
| `development_charge_per_month` | '6 Start-up'!$B$22 | 145,992 | Head-office development charge per month |
| `book_per_unit` | '7 Returns'!$B$4 | 1,520,001,600 | Loan book one operating unit carries (balance outstanding) |
| `book_capital_per_unit` | '7 Returns'!$B$5 | 174,496,184 | Capital the venture holds against one unit's book |
| `returns_per_unit` | '7 Returns'!$B$8 | 1,963,082 | Investment return required per operating unit per month |
| `returns_head_office` | '7 Returns'!$B$10 | 98,544 | Investment return required at head office per month |
| `book_at_scale` | '7 Returns'!$B$11 | 4,560,004,800 | Loan book at scale — balance outstanding across every unit |
| `book_capital_at_scale` | '7 Returns'!$B$12 | 523,488,551 | Capital held against the book at scale |
| `tax_per_unit` | '8 Tax'!$B$5 | 490,771 | Tax per operating unit per month |
| `tax_head_office` | '8 Tax'!$B$6 | 24,636 | Tax at head office per month |
| `unit_own_cost` | '9 Unit costs'!$B$12 | 10,269,865 | Operating unit's own costs per month, before head office |
| `ho_costs` | '9 Unit costs'!$B$13 | 1,337,932 | Head-office costs per month |
| `ho_total` | '9 Unit costs'!$B$15 | 1,337,932 | Head-office costs plus target profit per month |
| `ho_allocated_per_unit` | '9 Unit costs'!$B$16 | 445,977 | Head office allocated per operating unit per month |
| `whole_cost_per_unit` | '9 Unit costs'!$B$17 | 10,715,842 | Whole cost per operating unit per month |
| `cost_per_transaction` | '9 Unit costs'!$B$18 | 7.05 | Whole cost per transaction — the cost floor |
| `margin_of_safety` | '10 Pricing'!$B$6 | 65.5% | Margin of safety at the interim price, base scenario |
| `interim_price` | '10 Pricing'!$B$5 | 11.67 | Interim price per transaction |
| `verdict` | '10 Pricing'!$B$8 | PASS | Verdict on the margin of safety: PASS, BORDERLINE or FAIL |
| `required_price` | '10 Pricing'!$B$9 | 8.81 | Required price per transaction at the target margin of safety |
| `price_uplift_to_target` | '10 Pricing'!$B$10 | 75.5% | Price uplift needed to reach the target margin of safety (required ÷ interim) |
| `margin_from_failure` | '10 Pricing'!$B$11 | 50.5% | Margin of safety less the 15% floor, in percentage points |
| `price_fall_to_floor` | '10 Pricing'!$B$12 | 3.56 | Price fall per transaction that takes the margin of safety to the 15% floor |
| `required_price_product_1` | '10 Pricing'!$C$15 | 8.81 | Required price at the target margin of safety — Drawn balance, per £1,000 carried for one month |
| `binding_input` | '10 Pricing'!$B$54 | Running cost, operating unit — Expected credit loss on the drawn balance | The input whose adverse end lowers the margin of safety most |
| `margin_of_safety_worst_corner` | '10 Pricing'!$B$55 | 14.5% | Margin of safety with every banded input at its adverse end |
| `unit_surplus` | '11 Unit P&L'!$B$17 | 7,017,561 | Surplus per operating unit per month at the interim price |
| `unit_surplus_at_required` | '11 Unit P&L'!$C$17 | 2,678,961 | Surplus per operating unit per month at the required price |
| `venture_surplus_per_month` | '12 Venture P&L'!$D$20 | 21,052,682 | Venture surplus per month at scale, interim price |
| `venture_surplus_per_year` | '12 Venture P&L'!$D$21 | 252,632,180 | Venture surplus per year at scale, interim price |
| `venture_revenue_per_month` | '12 Venture P&L'!$D$5 | 53,200,208 | Venture revenue per month at scale |
| `year1_sales` | '13 Sales'!$N$12 | 142,523,357 | Sales in year one, the units open in year one |
| `year1_volume` | '13 Sales'!$N$14 | 12,216,253 | Transactions in year one |
| `loan_repayment_per_month` | '14 Cash flow'!$B$7 | 0 | Monthly loan repayment |
| `lowest_closing_balance` | '14 Cash flow'!$B$29 | 1,284,269 | Lowest closing cash balance in year one |
| `lowest_closing_balance_stress` | '14 Cash flow'!$B$30 | 189,231 | Lowest closing cash balance in year one under the revenue stress test |
| `closing_balance_month12` | '14 Cash flow'!$B$31 | 63,034,353 | Closing cash balance at the end of year one |
| `cash_needed` | '14 Cash flow'!$B$32 | 0 | Extra cash needed to keep the balance at or above zero |
| `cash_needed_stress` | '14 Cash flow'!$B$33 | 0 | Extra cash needed under the stress test |
| `forecast_loan_book_year_1` | '15 Roll-out'!$B$11 | 1,097,441,155 | Loans to customers at the end of year 1 |
| `forecast_loan_book_year_2` | '15 Roll-out'!$C$11 | 4,389,764,621 | Loans to customers at the end of year 2 |
| `forecast_loan_book_year_3` | '15 Roll-out'!$D$11 | 4,560,004,800 | Loans to customers at the end of year 3 |
| `forecast_loan_book_year_4` | '15 Roll-out'!$E$11 | 4,560,004,800 | Loans to customers at the end of year 4 |
| `forecast_loan_book_year_5` | '15 Roll-out'!$F$11 | 4,560,004,800 | Loans to customers at the end of year 5 |
| `forecast_revenue_year_1` | '16 Forecast P&L'!$B$5 | 142,523,357 | Forecast revenue, year 1 |
| `forecast_operating_profit_year_1` | '16 Forecast P&L'!$B$15 | 58,034,353 | Forecast operating profit, year 1 |
| `forecast_profit_after_tax_year_1` | '16 Forecast P&L'!$B$22 | 43,525,765 | Forecast profit after tax, year 1 |
| `forecast_revenue_year_2` | '16 Forecast P&L'!$C$5 | 581,797,475 | Forecast revenue, year 2 |
| `forecast_operating_profit_year_2` | '16 Forecast P&L'!$C$15 | 312,287,928 | Forecast operating profit, year 2 |
| `forecast_profit_after_tax_year_2` | '16 Forecast P&L'!$C$22 | 234,215,946 | Forecast profit after tax, year 2 |
| `forecast_revenue_year_3` | '16 Forecast P&L'!$D$5 | 638,402,496 | Forecast revenue, year 3 |
| `forecast_operating_profit_year_3` | '16 Forecast P&L'!$D$15 | 344,200,939 | Forecast operating profit, year 3 |
| `forecast_profit_after_tax_year_3` | '16 Forecast P&L'!$D$22 | 258,150,704 | Forecast profit after tax, year 3 |
| `forecast_revenue_year_4` | '16 Forecast P&L'!$E$5 | 638,402,496 | Forecast revenue, year 4 |
| `forecast_operating_profit_year_4` | '16 Forecast P&L'!$E$15 | 344,200,939 | Forecast operating profit, year 4 |
| `forecast_profit_after_tax_year_4` | '16 Forecast P&L'!$E$22 | 258,150,704 | Forecast profit after tax, year 4 |
| `forecast_revenue_year_5` | '16 Forecast P&L'!$F$5 | 638,402,496 | Forecast revenue, year 5 |
| `forecast_operating_profit_year_5` | '16 Forecast P&L'!$F$15 | 344,200,939 | Forecast operating profit, year 5 |
| `forecast_profit_after_tax_year_5` | '16 Forecast P&L'!$F$22 | 258,150,704 | Forecast profit after tax, year 5 |
| `forecast_revenue_total` | '16 Forecast P&L'!$G$5 | 2,639,528,320 | Forecast revenue over years one to 5 |
| `forecast_operating_profit_total` | '16 Forecast P&L'!$G$15 | 1,402,925,097 | Forecast operating profit over years one to 5 |
| `forecast_profit_after_tax_total` | '16 Forecast P&L'!$G$22 | 1,052,193,823 | Forecast profit after tax over years one to 5 |
| `forecast_closing_cash_year_1` | '17 Forecast cash flow'!$B$22 | 63,034,353 | Forecast closing cash, end of year 1 |
| `forecast_closing_cash_year_2` | '17 Forecast cash flow'!$C$22 | 360,813,692 | Forecast closing cash, end of year 2 |
| `forecast_closing_cash_year_3` | '17 Forecast cash flow'!$D$22 | 626,942,649 | Forecast closing cash, end of year 3 |
| `forecast_closing_cash_year_4` | '17 Forecast cash flow'!$E$22 | 885,093,353 | Forecast closing cash, end of year 4 |
| `forecast_closing_cash_year_5` | '17 Forecast cash flow'!$F$22 | 1,143,244,057 | Forecast closing cash, end of year 5 |
| `forecast_lowest_closing_cash` | '17 Forecast cash flow'!$B$24 | 63,034,353 | Lowest year-end cash balance across the forecast |
| `forecast_funding_needed` | '17 Forecast cash flow'!$B$25 | 0 | Extra funding needed to keep year-end cash at or above zero across the forecast |
| `forecast_net_assets_year_1` | '18 Forecast balance sheet'!$B$13 | 174,512,009 | Forecast net assets, end of year 1 |
| `forecast_loan_outstanding_year_1` | '18 Forecast balance sheet'!$B$9 | 0 | Loan outstanding, end of year 1 |
| `forecast_deposits_year_1` | '18 Forecast balance sheet'!$B$11 | 971,454,911 | Deposits funding the book, end of year 1 |
| `forecast_book_capital_year_1` | '18 Forecast balance sheet'!$B$17 | 125,986,245 | Capital held against the book, end of year 1 |
| `forecast_net_assets_year_2` | '18 Forecast balance sheet'!$C$13 | 786,686,689 | Forecast net assets, end of year 2 |
| `forecast_loan_outstanding_year_2` | '18 Forecast balance sheet'!$C$9 | 0 | Loan outstanding, end of year 2 |
| `forecast_deposits_year_2` | '18 Forecast balance sheet'!$C$11 | 3,885,819,642 | Deposits funding the book, end of year 2 |
| `forecast_book_capital_year_2` | '18 Forecast balance sheet'!$C$17 | 503,944,978 | Capital held against the book, end of year 2 |
| `forecast_net_assets_year_3` | '18 Forecast balance sheet'!$D$13 | 1,064,380,966 | Forecast net assets, end of year 3 |
| `forecast_loan_outstanding_year_3` | '18 Forecast balance sheet'!$D$9 | 0 | Loan outstanding, end of year 3 |
| `forecast_deposits_year_3` | '18 Forecast balance sheet'!$D$11 | 4,036,516,249 | Deposits funding the book, end of year 3 |
| `forecast_book_capital_year_3` | '18 Forecast balance sheet'!$D$17 | 523,488,551 | Capital held against the book, end of year 3 |
| `forecast_net_assets_year_4` | '18 Forecast balance sheet'!$E$13 | 1,322,531,670 | Forecast net assets, end of year 4 |
| `forecast_loan_outstanding_year_4` | '18 Forecast balance sheet'!$E$9 | 0 | Loan outstanding, end of year 4 |
| `forecast_deposits_year_4` | '18 Forecast balance sheet'!$E$11 | 4,036,516,249 | Deposits funding the book, end of year 4 |
| `forecast_book_capital_year_4` | '18 Forecast balance sheet'!$E$17 | 523,488,551 | Capital held against the book, end of year 4 |
| `forecast_net_assets_year_5` | '18 Forecast balance sheet'!$F$13 | 1,580,682,374 | Forecast net assets, end of year 5 |
| `forecast_loan_outstanding_year_5` | '18 Forecast balance sheet'!$F$9 | 0 | Loan outstanding, end of year 5 |
| `forecast_deposits_year_5` | '18 Forecast balance sheet'!$F$11 | 4,036,516,249 | Deposits funding the book, end of year 5 |
| `forecast_book_capital_year_5` | '18 Forecast balance sheet'!$F$17 | 523,488,551 | Capital held against the book, end of year 5 |
| `all_checks` | '19 Check'!$D$17 | ALL CHECKS PASS | ALL CHECKS PASS when every check row passes |

## Line items (tabs 3 to 6 — the amounts entered for each asset, running cost, start-up and development line)

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `line_ho_role_limit_engine_and_data_team` | '3 HR'!$D$24 | 291,675 | Staff cost per month, head office — Limit engine and data team × 25 |
| `line_ho_role_model_risk` | '3 HR'!$D$25 | 145,830 | Staff cost per month, head office — Model risk × 10 |
| `line_ho_role_product` | '3 HR'!$D$26 | 135,421 | Staff cost per month, head office — Product × 13 |
| `line_running_expected_credit_loss_on_the_drawn_balance` | '5 Running'!$C$5 | 2.50 | Running cost amount, operating unit (per_transaction) — Expected credit loss on the drawn balance |
| `line_running_computing_and_payments_in_the_account_line` | '5 Running'!$C$6 | 0.30 | Running cost amount, operating unit (per_transaction) — Computing and payments in the account line |
| `line_running_write_off_administration_and_legal` | '5 Running'!$C$7 | 0.42 | Running cost amount, operating unit (per_transaction) — Write-off administration and legal |
| `line_running_cell_tooling_case_system_and_telephony` | '5 Running'!$C$8 | 23,750 | Running cost amount, operating unit (per_unit_month) — Cell tooling — case system and telephony |
| `line_running_shared_trainer` | '5 Running'!$C$9 | 2,083 | Running cost amount, operating unit (per_unit_month) — Shared trainer |
| `line_ho_running_technology_run_the_limit_engine` | '5 Running'!$C$15 | 166,667 | Running cost per month, head office — Technology run — the limit engine |
| `line_ho_running_fraud_monitoring_on_funded_events` | '5 Running'!$C$16 | 104,167 | Running cost per month, head office — Fraud monitoring on funded events |
| `line_ho_running_other_head_office_people_the_all_people_total_less_the_named_teams` | '5 Running'!$C$17 | 37,500 | Running cost per month, head office — Other head-office people (the all-people total less the named teams) |
| `line_ho_running_standby_securitisation_route_annual_upkeep` | '5 Running'!$C$18 | 37,500 | Running cost per month, head office — Standby securitisation route — annual upkeep |
| `line_ho_running_reserve_against_the_assumed_head_office_count` | '5 Running'!$C$19 | 150,000 | Running cost per month, head office — Reserve against the assumed head-office count |
| `line_development_stage_0_back_test_on_the_bank_s_own_account_history` | '6 Start-up'!$B$12 | 550,000 | Development cost, head office, one-time — Stage 0 back-test on the bank's own account history |
| `line_development_outcome_ledger_build` | '6 Start-up'!$B$13 | 200,000 | Development cost, head office, one-time — Outcome ledger build |
| `line_development_seasoning_schedule_build` | '6 Start-up'!$B$14 | 30,000 | Development cost, head office, one-time — Seasoning schedule build |
| `line_development_credit_line_element_build_and_conformance_test` | '6 Start-up'!$B$15 | 75,000 | Development cost, head office, one-time — Credit-line element build and conformance test |
| `line_development_funding_term` | '6 Start-up'!$B$16 | 39,500 | Development cost, head office, one-time — Funding term |
| `line_development_migration_notices_to_the_accounts_moving_to_the_levelled_line` | '6 Start-up'!$B$17 | 575,000 | Development cost, head office, one-time — Migration notices to the accounts moving to the levelled line |
| `line_development_stage_readings_at_each_release_gate` | '6 Start-up'!$B$18 | 90,000 | Development cost, head office, one-time — Stage readings at each release gate |
| `line_development_standby_securitisation_route_documentation_and_set_up` | '6 Start-up'!$B$19 | 2,000,000 | Development cost, head office, one-time — Standby securitisation route — documentation and set-up |
| `line_development_carrying_cost_of_the_pool_overlays_during_release` | '6 Start-up'!$B$20 | 5,200,000 | Development cost, head office, one-time — Carrying cost of the pool overlays during release |

## Forecast inputs (tab 15 — units open, head-office share and equity raised, by year)

| Name | Cell | Base value | Meaning |
|---|---|---|---|
| `in_forecast_units_open_year_1` | '15 Roll-out'!$B$5 | 0.76 | Operating units open at the end of year 1 |
| `in_forecast_head_office_share_year_1` | '15 Roll-out'!$B$8 | 100.0% | Share of the at-scale head office staffed and run in year 1 |
| `in_forecast_equity_raised_year_1` | '15 Roll-out'!$B$9 | 5,000,000 | Equity raised in year 1 |
| `in_forecast_units_open_year_2` | '15 Roll-out'!$C$5 | 3 | Operating units open at the end of year 2 |
| `in_forecast_head_office_share_year_2` | '15 Roll-out'!$C$8 | 100.0% | Share of the at-scale head office staffed and run in year 2 |
| `in_forecast_equity_raised_year_2` | '15 Roll-out'!$C$9 | 0 | Equity raised in year 2 |
| `in_forecast_units_open_year_3` | '15 Roll-out'!$D$5 | 3 | Operating units open at the end of year 3 |
| `in_forecast_head_office_share_year_3` | '15 Roll-out'!$D$8 | 100.0% | Share of the at-scale head office staffed and run in year 3 |
| `in_forecast_equity_raised_year_3` | '15 Roll-out'!$D$9 | 0 | Equity raised in year 3 |
| `in_forecast_units_open_year_4` | '15 Roll-out'!$E$5 | 3 | Operating units open at the end of year 4 |
| `in_forecast_head_office_share_year_4` | '15 Roll-out'!$E$8 | 100.0% | Share of the at-scale head office staffed and run in year 4 |
| `in_forecast_equity_raised_year_4` | '15 Roll-out'!$E$9 | 0 | Equity raised in year 4 |
| `in_forecast_units_open_year_5` | '15 Roll-out'!$F$5 | 3 | Operating units open at the end of year 5 |
| `in_forecast_head_office_share_year_5` | '15 Roll-out'!$F$8 | 100.0% | Share of the at-scale head office staffed and run in year 5 |
| `in_forecast_equity_raised_year_5` | '15 Roll-out'!$F$9 | 0 | Equity raised in year 5 |

## Inputs (tab 1, Master Control)

| Name | Cell | Base | Low | High | Tier | Source |
|---|---|---|---|---|---|---|
| `in_market_total_reachable_population` | '1 Master'!$B$7 | 950,000 | 850,000 | 1,050,000 | 4 | ⚠ AOM v10 §0 — accounts on the levelled line after migration; a public-source estimate of the bank's SME account base |
| `in_market_non_viable_share` | '1 Master'!$B$8 | 20.0% | 15.0% | 25.0% | 4 | ⚠ assumed — accounts with no observed flow, so no limit can be computed (C1 record, the flow-coverage input) |
| `in_market_unit_population` | '1 Master'!$B$9 | 316,667 | 316,667 | 316,667 | 4 | ⚠ AOM v10 §3b — one cell per ⚠ 333,000 accounts; 950,000 ÷ 3 cells |
| `in_market_penetration_steady_state` | '1 Master'!$B$10 | 30.0% | 30.0% | 30.0% | 4 | ⚠ AOM v10 §0 — drawn accounts as a share of accounts with a limit (228,000 of 760,000); the balance band below carries the uncertainty |
| `in_market_transactions_per_customer_per_month` | '1 Master'!$B$11 | 20 | 15 | 25 | 4 | ⚠ AOM v10 §0 — average drawn balance £15–25k per drawn account; book £3.4–5.7bn |
| `in_product_0_share` | '1 Master'!$B$12 | 1 | 1 | 1 |  |  |
| `in_product_0_price` | '1 Master'!$B$13 | 11.6667 | 11.25 | 11.875 | 3 | C6 record — 14.0% simple on the daily drawn balance = £140 per £1,000 a year (band ⚠ 135–142.5), no fee; ÷ 12 |
| `in_product_0_cogs` | '1 Master'!$B$14 | 1.875 | 1.25 | 2.5 | 4 | ⚠ C10 record — funding at the measured deposit cost 1.5–3.0% a year on the drawn balance (£15–30 per £1,000); ÷ 12 |
| `in_hr_available_hours` | '1 Master'!$B$15 | 125 | 116.7 | 133.3 | 4 | ⚠ AOM v10 §3b — 1,400–1,600 productive hours a year per handler; ÷ 12 |
| `in_role_exception_handler_monthly_cost` | '1 Master'!$B$16 | 4,792 | 4,167 | 5,417 | 4 | ⚠ AOM v10 §3b — handlers £50–65k a year all-in; ÷ 12 |
| `in_role_cell_lead_monthly_cost` | '1 Master'!$B$17 | 6,667 | 5,833 | 7,500 | 4 | ⚠ AOM v10 §3b — leads £70–90k a year all-in; ÷ 12 |
| `in_ho_role_limit_engine_and_data_team_monthly_cost` | '1 Master'!$B$18 | 11,667 | 10,000 | 13,333 | 4 | ⚠ AOM v10 §3c — 25 people, £3–4m a year; per person per month |
| `in_ho_role_model_risk_monthly_cost` | '1 Master'!$B$19 | 14,583 | 12,500 | 16,667 | 4 | ⚠ AOM v10 §3c — 10 people, £1.5–2m a year; per person per month |
| `in_ho_role_product_monthly_cost` | '1 Master'!$B$20 | 10,417 | 8,333 | 12,500 | 4 | ⚠ AOM v10 §3c — 13 people, £1.3–1.95m a year; per person per month |
| `in_running_expected_credit_loss_on_the_drawn_balance_amount` | '1 Master'!$B$21 | 2.5 | 1.6667 | 3.3333 | 4 | ⚠ C1 record — loss rate on the flow-underwritten pool 2–4% a year (£20–40 per £1,000); ÷ 12; unmeasured until Stage 0's back-test |
| `in_running_computing_and_payments_in_the_account_line_amount` | '1 Master'!$B$22 | 0.2975 | 0.1683 | 0.4267 | 4 | ⚠ AOM v10 §6 — computing 2.02–5.12 per £1,000 a year; ÷ 12 |
| `in_running_write_off_administration_and_legal_amount` | '1 Master'!$B$23 | 0.4167 | 0.25 | 0.5833 | 4 | ⚠ AOM v10 §6 — write-off administration and legal £3–7 per £1,000 a year; ÷ 12 |
| `in_running_cell_tooling_case_system_and_telephony_amount` | '1 Master'!$B$24 | 23,750 | 19,167 | 28,333 | 4 | ⚠ AOM v10 §3b — tooling £0.23–0.34m a year per cell; ÷ 12 |
| `in_running_shared_trainer_amount` | '1 Master'!$B$25 | 2,083 | 1,667 | 2,500 | 4 | ⚠ AOM v10 §3b — one trainer £20–30k a year shared across the cells; ÷ 12 |
| `in_ho_running_technology_run_the_limit_engine_amount` | '1 Master'!$B$26 | 166,667 | 83,333 | 250,000 | 4 | ⚠ AOM v10 §3c — £1–3m a year; ÷ 12 |
| `in_ho_running_fraud_monitoring_on_funded_events_amount` | '1 Master'!$B$27 | 104,167 | 41,667 | 166,667 | 4 | ⚠ AOM v10 §3c — £0.5–2m a year; ÷ 12 |
| `in_ho_running_other_head_office_people_the_all_people_total_less_the_named_teams_amount` | '1 Master'!$B$28 | 37,500 | 25,000 | 50,000 | 4 | ⚠ fin-sim input rc_people_gbp £7.6–13.55m a year (AOM v10 §3c all-people cost) less the six lines named here; ÷ 12 |
| `in_ho_running_standby_securitisation_route_annual_upkeep_amount` | '1 Master'!$B$29 | 37,500 | 25,000 | 50,000 | 4 | ⚠ C10 record — a documented, never-issued master trust kept current, £0.3–0.6m a year (external); ÷ 12 |
| `in_ho_running_reserve_against_the_assumed_head_office_count_amount` | '1 Master'!$B$30 | 150,000 | 0 | 300,333 | 4 | ⚠ AOM v10.1 §6 — a named reserve of 1.06 per £1,000 at the conservative corner on a £3.4bn book, released when the insider's count is read (S2 of the C10 audit); ÷ 12 |
| `in_ho_dev_stage_0_back_test_on_the_bank_s_own_account_history_cost` | '1 Master'!$B$31 | 550,000 | 300,000 | 800,000 | 4 | ⚠ C3 record — the shadow run and back-test, £0.3–0.8m, no customer and no release |
| `in_ho_dev_outcome_ledger_build_cost` | '1 Master'!$B$32 | 200,000 | 100,000 | 300,000 | 4 | ⚠ C9 record — £0.1–0.3m once |
| `in_ho_dev_seasoning_schedule_build_cost` | '1 Master'!$B$33 | 30,000 | 20,000 | 40,000 | 4 | ⚠ C8 record — £20–40k once |
| `in_ho_dev_credit_line_element_build_and_conformance_test_cost` | '1 Master'!$B$34 | 75,000 | 50,000 | 100,000 | 4 | ⚠ C7 record — £50–100k once |
| `in_ho_dev_funding_term_cost` | '1 Master'!$B$35 | 39,500 | 26,000 | 53,000 | 4 | ⚠ C5 and C6 records — £26–53k once |
| `in_ho_dev_migration_notices_to_the_accounts_moving_to_the_levelled_line_cost` | '1 Master'!$B$36 | 575,000 | 300,000 | 850,000 | 4 | ⚠ C2 record — £0.3–0.85m once |
| `in_ho_dev_stage_readings_at_each_release_gate_cost` | '1 Master'!$B$37 | 90,000 | 45,000 | 135,000 | 4 | ⚠ C3 record — £45–135k once |
| `in_ho_dev_standby_securitisation_route_documentation_and_set_up_cost` | '1 Master'!$B$38 | 2,000,000 | 1,000,000 | 3,000,000 | 4 | ⚠ C10 record — £1–3m once, documented before Stage 3 and never issued |
| `in_ho_dev_carrying_cost_of_the_pool_overlays_during_release_cost` | '1 Master'!$B$39 | 5,200,000 | 0 | 10,400,000 | 4 | ⚠ C3 record — capital held against the Stage 1 book (£0–19m, 12 months) and each replica (£0–50m, 6 months) at 12–15%; a charge for capital held, not a payment |
| `in_startup_working_capital_months` | '1 Master'!$B$40 | 0 | 0 | 1 | 4 | the charge is collected as the first slice of each receipts share from month one (C6), so the cell carries no working capital; one month held at the adverse end |
| `in_startup_investment_period_months` | '1 Master'!$B$41 | 60 | 36 | 60 | 4 | the one-offs are spread over the five-year forecast; 36 months held at the adverse end |
| `in_finance_cost_of_capital` | '1 Master'!$B$42 | 13.5% | 12.0% | 15.0% | 3 | ⚠ FIT model at C10 — cost of equity 12–15% on the capital held against the book (a bank's target return on tangible equity, public results) |
| `in_finance_tax_rate` | '1 Master'!$B$43 | 25.0% | 25.0% | 25.0% |  |  |
| `in_finance_ho_target_ebit` | '1 Master'!$B$44 | 0.0% | 0.0% | 0.0% |  |  |
| `in_finance_target_margin` | '1 Master'!$B$45 | 25.0% | 25.0% | 25.0% |  |  |
| `in_book_balance_per_transaction` | '1 Master'!$B$46 | 1,000 | 1,000 | 1,000 | 1 | by definition — one transaction is £1,000 of drawn balance carried for one month |
| `in_book_capital_share_of_balance` | '1 Master'!$B$47 | 11.5% | 10.7% | 12.2% | 2 | 75% risk weight (CRR Art. 123, FACT) × ⚠ 12% total capital × (1 + 10% conversion on undrawn (Basel 3.1, PRA PS9/24, FACT) × ⚠ 1.9–3.6 undrawn per drawn); the rest of the book is funded by the pool's own credit balances (C10) |
| `in_cashflow_year1_units` | '1 Master'!$B$48 | 0.76 | 0.76 | 0.76 |  |  |
| `in_cashflow_year1_head_office_share` | '1 Master'!$B$49 | 100.0% | 100.0% | 100.0% |  |  |
| `in_cashflow_opening_balance` | '1 Master'!$B$50 | 0 | 0 | 0 |  |  |
| `in_cashflow_loan_amount` | '1 Master'!$B$51 | 0 | 0 | 0 |  |  |
| `in_cashflow_loan_rate_annual` | '1 Master'!$B$52 | 0.0% | 0.0% | 0.0% |  |  |
| `in_cashflow_loan_term_months` | '1 Master'!$B$53 | 12 | 12 | 12 |  |  |
| `in_cashflow_other_equity` | '1 Master'!$B$54 | 5,000,000 | 5,000,000 | 5,000,000 |  |  |
| `in_cashflow_stress_revenue_reduction` | '1 Master'!$B$55 | 10.0% | 10.0% | 10.0% |  |  |

## Sensitivity (one input at a time to its adverse end, worst first)

| Input | End | Margin of safety | Change |
|---|---|---|---|
| Running cost, operating unit — Expected credit loss on the drawn balance | high | 48.0% | -17.5% |
| Drawn balance, per £1,000 carried for one month — cost of goods per transaction | high | 52.0% | -13.5% |
| Drawn balance, per £1,000 carried for one month — price | low | 59.6% | -5.9% |
| Cost of capital (annual) | high | 61.3% | -4.2% |
| Running cost, operating unit — Write-off administration and legal | high | 61.7% | -3.8% |
| Start-up working capital (months of unit running cost) | high | 61.9% | -3.6% |
| Running cost, operating unit — Computing and payments in the account line | high | 62.5% | -3.0% |
| Transactions per customer per month | low | 62.8% | -2.7% |
| Share of the book the venture funds with its own capital | high | 63.0% | -2.5% |
| Development cost, head office, one-time — Carrying cost of the pool overlays during release | high | 64.7% | -0.8% |
| Running cost, head office, per month — Reserve against the assumed head-office count | high | 64.7% | -0.8% |
| Share of reachable population that is not viable | high | 64.9% | -0.5% |
| Investment recovery period (months) | low | 65.0% | -0.5% |
| Running cost, head office, per month — Technology run — the limit engine | high | 65.1% | -0.4% |
| Running cost, head office, per month — Fraud monitoring on funded events | high | 65.2% | -0.3% |
| Head office — Limit engine and data team — monthly cost per person | high | 65.3% | -0.2% |
| Available hours per person per month | low | 65.3% | -0.2% |
| Development cost, head office, one-time — Standby securitisation route — documentation and set-up | high | 65.3% | -0.2% |
| Head office — Product — monthly cost per person | high | 65.3% | -0.1% |
| Head office — Model risk — monthly cost per person | high | 65.4% | -0.1% |
| Exception handler — monthly cost per person | high | 65.4% | -0.1% |
| Running cost, operating unit — Cell tooling — case system and telephony | high | 65.4% | -0.1% |
| Running cost, head office, per month — Other head-office people (the all-people total less the named teams) | high | 65.4% | -0.1% |
| Running cost, head office, per month — Standby securitisation route — annual upkeep | high | 65.4% | -0.1% |
| Development cost, head office, one-time — Migration notices to the accounts moving to the levelled line | high | 65.4% | -0.0% |
| Development cost, head office, one-time — Stage 0 back-test on the bank's own account history | high | 65.4% | -0.0% |
| Development cost, head office, one-time — Outcome ledger build | high | 65.5% | -0.0% |
| Cell lead — monthly cost per person | high | 65.5% | -0.0% |
| Development cost, head office, one-time — Stage readings at each release gate | high | 65.5% | -0.0% |
| Running cost, operating unit — Shared trainer | high | 65.5% | -0.0% |
| Development cost, head office, one-time — Credit-line element build and conformance test | high | 65.5% | -0.0% |
| Development cost, head office, one-time — Funding term | high | 65.5% | -0.0% |
| Development cost, head office, one-time — Seasoning schedule build | high | 65.5% | -0.0% |
| Reachable population (whole venture) | low | 65.5% | +0.0% |

Binding input: **Running cost, operating unit — Expected credit loss on the drawn balance**. Margin of safety at the worst corner (every input adverse): **14.5%**. Verdict at base: **PASS** (65.5% against a 25% gate).
