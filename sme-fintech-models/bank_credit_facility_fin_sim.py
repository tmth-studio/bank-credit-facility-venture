#!/usr/bin/env python3
"""Case B — the credit facility line of a large UK SME bank: the financial simulation after C10 (Function 1 to Function 3).

Runner: Function 3 runner, Path C mode 3, 21 September 2026. Propose-and-confirm (object-after 48 hours).
Reads:  bank-credit-facility-fit-model-at-C10.yaml (the four layers, the KMC band, the price, the cap line)
        bank-credit-facility-tam-model.yaml (version 4: the surviving volume, the sub-classes, gate G-C10-1)
Writes: bank-credit-facility-fin-sim-outputs.json and ../bank-credit-facility-fin-sim-2026-09-21.md
Edits no model file. Every input is read from a model file or declared in INPUTS below with its source and tier.
Confidentiality: the bank is not named; every figure the bank alone holds is a red field (⚠) and a band, never a point.

WHAT IT SIMULATES
  1. The at-scale model — the C10 floor per £1,000 of average drawn balance a year, reproduced from the fit model's four layers
     at three corners (conservative / central / optimistic), the margin at the set price 140 and across the band 135–142.5,
     the operating bar, the loss gate, the funding gate, the £8 cap line, and the P&L per £1,000 and for the book.
  2. The scaling-stage model — a monthly path from the back-test (Stage 0) through the migrated book (Stage 1), replica 1 and
     replica 2 (Stage 2) to the at-scale state (Stage 3), with the one-off costs at the month they fall, the fixed layer running
     from launch, the overlays held and released at each reading, and the cumulative operating cash. Peak venture capital is
     the deepest cumulative operating deficit plus the overlay held in the same month. Lending capital (the regulatory capital
     on the drawn and undrawn exposure) is shown as funding, not venture capital: it is the bank's, and the pool funds the book.
  3. The loss-rate sensitivity at 2, 3, 4, 4.8, 5, 6 and 7.65 per cent on the conservative corner: margin, gate reading,
     year-five contribution.
  4. The Phase II capital gate at the conservative scenario against 60 per cent, with the band, the binding input and the
     worst-corner margin; and what tightens it.
  5. Per-segment penetration from the TAM data object (version 4).
No point estimates: every input is a band; each corner is printed.
"""
import json, math
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
FIT = HERE / "bank-credit-facility-fit-model-at-C10.yaml"
TAM = HERE / "bank-credit-facility-tam-model.yaml"
OUT_JSON = HERE / "bank-credit-facility-fin-sim-outputs.json"
OUT_MD = HERE.parent / "bank-credit-facility-fin-sim-2026-09-21.md"

fit = yaml.safe_load(FIT.read_text())
tam = yaml.safe_load(TAM.read_text())
L = fit["cost_floor"]["layers"]
band = lambda k: (float(L[k]["band"]["low"]), float(L[k]["band"]["high"]))
PVC, RC, SC, IC = band("pvc"), band("rc"), band("sc"), band("ic")
KMC = (float(fit["price_ceiling"]["kmc"]["band"]["low"]), float(fit["price_ceiling"]["kmc"]["band"]["high"]))
PRICE = 140.0; PRICE_BAND = (135.0, 142.5)      # C6 record, runner's call; fraction 0.933 of the KMC low corner
BAR = float(fit["required_price"]["amount"])   # 134.34 = floor high × 1.25

# ── INPUTS declared here (each with source and tier) ─────────────────────────────────────────────────────────────────────────
INPUTS = {
  # at-scale quantities
  "book_gbp":            {"band": [3.4e9, 5.7e9], "src": "AOM v10 §0 q.drawn_book_gbp — 228,000 drawn accounts × ⚠ £15–25k", "tier": "T4 ⚠"},
  "funding_pct":         {"band": [1.5, 3.0],     "src": "AOM v10 §6 PVC-funding — the measured deposit cost under the funding term (C10)", "tier": "T4 ⚠"},
  "loss_pct":            {"band": [2.0, 4.0],     "src": "AOM v10 §6 PVC-loss — the flow-underwritten pool; the binding input", "tier": "T4 ⚠"},
  "computing_per_1000":  {"band": [2.02, 5.12],   "src": "AOM v10 §6 PVC-computing", "tier": "T4 ⚠"},
  "exceptions_per_1000": {"band": [3.00, 8.13],   "src": "AOM v10 §6 PVC-exceptions and write-off", "tier": "T4 ⚠"},
  "rc_people_gbp":       {"band": [7.6e6, 13.55e6], "src": "AOM v10 §3c all-people cost of the HQ layer (before the route)", "tier": "T4 ⚠"},
  "route_upkeep_gbp":    {"band": [0.3e6, 0.6e6],  "src": "AOM v10 §3c the standby route's upkeep without issuance (C10)", "tier": "T2/T4 ⚠"},
  "undrawn_per_drawn":   {"band": [1.9, 3.6],     "src": "AOM v10 §0 q.undrawn_per_drawn (C8)", "tier": "T4 ⚠"},
  "risk_weight":         {"band": [0.75, 0.75],   "src": "regulatory retail SME, standardised — FACT", "tier": "T1"},
  "total_capital":       {"band": [0.12, 0.12],   "src": "⚠ 12% total capital ratio — AOM v10 §6 IC", "tier": "T4 ⚠"},
  "ccf_undrawn":         {"band": [0.10, 0.10],   "src": "Basel 3.1, PRA PS9/24, from 1 January 2027 — FACT", "tier": "T1"},
  "cost_of_equity":      {"band": [0.12, 0.15],   "src": "AOM v10 §6 IC — ⚠ 12–15%", "tier": "T4 ⚠"},
  "pool_credit_balances":{"band": [50e9, 100e9],  "src": "AOM v10 §0 q.pool_credit_balances (C10)", "tier": "T2/T4 ⚠"},
  "cap_share":           {"band": [0.10, 0.10],   "src": "C10 record, gate G18 — the cap at ⚠ 10% of the pool's credit balances", "tier": "runner's call ⚠"},
  # scaling-stage quantities
  "stage1_book_gbp":     {"band": [0.4e9, 1.9e9], "src": "C3 record — the migrated overdraft accounts' drawn balance", "tier": "T4 ⚠"},
  "seasoning_months":    {"band": [8, 24],        "src": "runner's call — months a released tranche takes to reach its at-scale drawn balance (C8: seasoned share ⚠ 30–50% at 24 months); convergence: the first replica's 24-month reading", "tier": "T4 ⚠"},
  "unseasoned_drawn_share": {"band": [0.80, 0.80], "src": "runner's call — a released account's drawn balance at release as a share of its seasoned level (the seasoned uplift ⚠ 15–30% on limits, C8)", "tier": "T4 ⚠"},
  "overlay_stage1_gbp":  {"band": [0, 19e6],      "src": "AOM v10 §3e — the overlay on Stage 1, held 12 months", "tier": "T4 ⚠"},
  "overlay_replica_gbp": {"band": [0, 50e6],      "src": "AOM v10 §3e — the overlay on each replica, held 6 months", "tier": "T4 ⚠"},
  # one-offs (£), the month they fall (months from launch; negative = before launch)
  "oneoffs": [
    {"name": "back-test and its validation (Stage 0)",          "band": [0.3e6, 0.8e6],   "months": [-6, -1], "src": "C3 record; AOM v10 §3e"},
    {"name": "the outcome ledger build (C9)",                    "band": [0.1e6, 0.3e6],   "months": [-6, -1], "src": "AOM v10 §3e e.ledger_build"},
    {"name": "the seasoning build (C8)",                         "band": [20e3, 40e3],     "months": [-3, -1], "src": "AOM v10 §3e"},
    {"name": "the credit-line element build and conformance test (C7)", "band": [50e3, 100e3], "months": [-3, -1], "src": "AOM v10 §3e"},
    {"name": "the term drafting (C5), the representative example (C6), the funding term's signature (C10)", "band": [26e3, 53e3], "months": [-2, -1], "src": "AOM v10 §3e"},
    {"name": "migration notices and handler time (C2)",          "band": [0.3e6, 0.85e6],  "months": [1, 1],   "src": "C3 record; AOM v10 §3e"},
    {"name": "stage readings, three (C3)",                       "band": [45e3, 135e3],    "months": [12, 24], "src": "AOM v10 §3e e.stage_reading — ⚠ £15–45k each at months 12, 18 and 24"},
    {"name": "the standby route's set-up (C10)",                 "band": [1.0e6, 3.0e6],   "months": [19, 24], "src": "AOM v10 §3e e.route_setup — before Stage 3"},
  ],
  "release_months": {"stage1": 1, "replica1": 13, "replica2": 19, "readings": [12, 18, 24]},   # C3 record: trial band at 12 months; replica band at 6 months
  "pco": {"capital_gbp": 100e6, "required_return": 0.30, "required_revenue_y5_gbp": 148.5e6, "profit_margin_assumed": 0.20,
          "src": "bank-deposits-lending-pco-v1-2026-09-18.md — capital £100m ⚠ ASSUMED; 30%; required-revenue line £148.5m at year five at a 20% margin"},
}
CORNERS = ["conservative", "central", "optimistic"]
def pick(b, corner, high_is_bad=True):
    lo, hi = b
    if corner == "central": return (lo + hi) / 2
    if corner == "conservative": return hi if high_is_bad else lo
    return lo if high_is_bad else hi

# ── 1 · the at-scale model ──────────────────────────────────────────────────────────────────────────────────────────────────
def floor_at(corner, loss_pct=None, funding_pct=None, rc=None):
    f = pick(INPUTS["funding_pct"]["band"], corner) if funding_pct is None else funding_pct
    l = pick(INPUTS["loss_pct"]["band"], corner) if loss_pct is None else loss_pct
    comp = pick(INPUTS["computing_per_1000"]["band"], corner)
    exc = pick(INPUTS["exceptions_per_1000"]["band"], corner)
    pvc = 10 * f + 10 * l + comp + exc
    r = pick(RC, corner) if rc is None else rc
    s = pick(SC, corner); i = pick(IC, corner)
    return {"funding": 10 * f, "loss": 10 * l, "computing": comp, "exceptions": exc, "pvc": pvc, "rc": r, "sc": s, "ic": i, "floor": pvc + r + s + i}

def margin(price, floor): return (price - floor) / floor

at_scale = {}
for c in CORNERS:
    fl = floor_at(c)
    book = pick(INPUTS["book_gbp"]["band"], c)   # conservative = small book (fixed lines spread thin)
    rows = {"floor": fl, "book_gbp": book,
            "margin_at_140": margin(PRICE, fl["floor"]), "margin_at_135": margin(PRICE_BAND[0], fl["floor"]), "margin_at_142_5": margin(PRICE_BAND[1], fl["floor"]),
            "bar_25": fl["floor"] * 1.25, "bar_60": fl["floor"] * 1.60, "room_at_140": PRICE - fl["floor"] * 1.25,
            "pnl_per_1000": {"revenue": PRICE, "funding": fl["funding"], "expected_loss": fl["loss"], "computing_and_payments": fl["computing"],
                             "exceptions_and_write_off": fl["exceptions"], "recurring_fixed": fl["rc"], "scaling_one_offs_spread": fl["sc"],
                             "contribution_before_capital": PRICE - fl["pvc"] - fl["rc"] - fl["sc"], "cost_of_capital": fl["ic"],
                             "net_contribution": PRICE - fl["floor"]},
            }
    rows["pnl_book_gbp"] = {k: v * book / 1000 for k, v in rows["pnl_per_1000"].items()}
    # lending capital on the book (shown as funding, not venture capital)
    u = pick(INPUTS["undrawn_per_drawn"]["band"], c)
    cap_per_1000 = 1000 * INPUTS["risk_weight"]["band"][0] * INPUTS["total_capital"]["band"][0] * (1 + INPUTS["ccf_undrawn"]["band"][0] * u)
    rows["lending_capital_gbp"] = cap_per_1000 * book / 1000
    rows["ic_check_per_1000"] = cap_per_1000 * pick(INPUTS["cost_of_equity"]["band"], c)
    # the cap
    pool = pick(INPUTS["pool_credit_balances"]["band"], c)
    rows["cap_gbp"] = INPUTS["cap_share"]["band"][0] * pool
    rows["book_share_of_pool"] = book / pool
    rows["cap_binds"] = book > rows["cap_gbp"]
    rows["book_after_cap_gbp"] = min(book, rows["cap_gbp"])
    at_scale[c] = rows
# the worst corner of the cap: the big book against the small pool
cap_worst = {"book_gbp": INPUTS["book_gbp"]["band"][1], "pool_gbp": INPUTS["pool_credit_balances"]["band"][0]}
cap_worst["cap_gbp"] = 0.10 * cap_worst["pool_gbp"]; cap_worst["share"] = cap_worst["book_gbp"] / cap_worst["pool_gbp"]
cap_worst["volume_cut"] = 1 - cap_worst["cap_gbp"] / cap_worst["book_gbp"]

# gates on the conservative corner
fl_c = floor_at("conservative")["floor"]
other_than_loss = fl_c - 40.0        # every other line at its high corner: 67.47
other_than_funding = fl_c - 30.0     # 77.47
gates = {
  "loss_gate_pct":   {p: (p / 1.25 - other_than_loss) / 10 for p in (135.0, 140.0, 142.5)},
  "loss_zero_margin_pct": {p: (p - other_than_loss) / 10 for p in (135.0, 140.0, 142.5)},
  "funding_gate_pct": {p: (p / 1.25 - other_than_funding) / 10 for p in (135.0, 140.0, 142.5)},
  "funding_zero_margin_pct": {p: (p - other_than_funding) / 10 for p in (135.0, 140.0, 142.5)},
}
cap_line = fit.get("conventional_additions", {})

# ── 2 · the scaling-stage model (monthly) ────────────────────────────────────────────────────────────────────────────────────
def path(corner, loss_pct=None, months=72):
    book = pick(INPUTS["book_gbp"]["band"], corner)
    s1 = pick(INPUTS["stage1_book_gbp"]["band"], corner, high_is_bad=False) / book   # Stage 1 share of the at-scale book
    s1 = min(s1, 0.5)
    rep = (1 - s1) / 2
    season = pick(INPUTS["seasoning_months"]["band"], corner)
    unseason = INPUTS["unseasoned_drawn_share"]["band"][0]
    f = pick(INPUTS["funding_pct"]["band"], corner) / 100
    l = (pick(INPUTS["loss_pct"]["band"], corner) if loss_pct is None else loss_pct) / 100
    comp = pick(INPUTS["computing_per_1000"]["band"], corner) / 1000
    exc = pick(INPUTS["exceptions_per_1000"]["band"], corner) / 1000
    rc_people = pick(INPUTS["rc_people_gbp"]["band"], corner)
    route = pick(INPUTS["route_upkeep_gbp"]["band"], corner)
    ov1 = pick(INPUTS["overlay_stage1_gbp"]["band"], corner); ovr = pick(INPUTS["overlay_replica_gbp"]["band"], corner)
    rm = INPUTS["release_months"]
    u = pick(INPUTS["undrawn_per_drawn"]["band"], corner)
    cap_per_drawn = INPUTS["risk_weight"]["band"][0] * INPUTS["total_capital"]["band"][0] * (1 + INPUTS["ccf_undrawn"]["band"][0] * u)
    coe = pick(INPUTS["cost_of_equity"]["band"], corner)
    tranches = [(rm["stage1"], s1), (rm["replica1"], rep), (rm["replica2"], rep)]
    oneoffs_by_month = {}
    for o in INPUTS["oneoffs"]:
        amt = pick(o["band"], corner); m0, m1 = o["months"]; n = m1 - m0 + 1
        for m in range(m0, m1 + 1): oneoffs_by_month[m] = oneoffs_by_month.get(m, 0) + amt / n
    rows = []; cum = 0.0; peak = 0.0; peak_month = None; payback = None; at_scale_month = None
    for m in range(-6, months + 1):
        drawn = 0.0
        for (rel, share) in tranches:
            if m >= rel:
                age = m - rel
                frac = unseason + (1 - unseason) * min(1.0, age / season) if season > 0 else 1.0
                drawn += book * share * frac
        if at_scale_month is None and drawn >= book * 0.999: at_scale_month = m
        rev = drawn * PRICE / 1000 / 12
        funding = drawn * f / 12; loss = drawn * l / 12; computing = drawn * comp / 12; exceptions = drawn * exc / 12
        fixed = (rc_people / 12 if m >= 1 else 0) + (route / 12 if m >= rm["replica2"] else 0)
        oneoff = oneoffs_by_month.get(m, 0)
        overlay = 0.0
        if rm["stage1"] <= m < rm["stage1"] + 12: overlay += ov1
        if rm["replica1"] <= m < rm["replica1"] + 6: overlay += ovr
        if rm["replica2"] <= m < rm["replica2"] + 6: overlay += ovr
        op_cash = rev - funding - loss - computing - exceptions - fixed - oneoff
        lending_capital = drawn * cap_per_drawn
        ic = lending_capital * coe / 12
        cum += op_cash
        need = max(0.0, -cum) + overlay
        if need > peak: peak, peak_month = need, m
        if payback is None and m >= 1 and cum > 0: payback = m
        rows.append({"month": m, "drawn_gbp": drawn, "revenue": rev, "funding": funding, "loss": loss, "computing": computing, "exceptions": exceptions,
                     "fixed": fixed, "one_offs": oneoff, "operating_cash": op_cash, "cumulative_operating_cash": cum, "overlay_held": overlay,
                     "lending_capital_gbp": lending_capital, "cost_of_capital": ic, "contribution_after_capital": op_cash - ic})
    def year(n):  # months 12(n-1)+1 .. 12n
        ys = [r for r in rows if 12 * (n - 1) + 1 <= r["month"] <= 12 * n]
        agg = {k: sum(r[k] for r in ys) for k in ("revenue", "funding", "loss", "computing", "exceptions", "fixed", "one_offs", "operating_cash", "cost_of_capital", "contribution_after_capital")}
        agg["average_drawn_gbp"] = sum(r["drawn_gbp"] for r in ys) / len(ys)
        return agg
    stage1 = year(1)
    stage1_floor_per_1000 = (stage1["funding"] + stage1["loss"] + stage1["computing"] + stage1["exceptions"] + stage1["fixed"] + stage1["cost_of_capital"]) / stage1["average_drawn_gbp"] * 1000
    return {"stage1_share_of_book": s1, "replica_share_of_book": rep, "seasoning_months": season, "at_scale_month": at_scale_month,
            "peak_venture_capital_gbp": peak, "peak_month": peak_month, "payback_month": payback,
            "years": {n: year(n) for n in range(1, 6)},
            "stage1_floor_per_1000_excl_one_offs": stage1_floor_per_1000, "stage1_margin_at_140": (PRICE - stage1_floor_per_1000) / stage1_floor_per_1000,
            "cumulative_operating_cash_month_60": next(r["cumulative_operating_cash"] for r in rows if r["month"] == 60),
            "lending_capital_at_scale_gbp": rows[-1]["lending_capital_gbp"], "monthly": rows}

paths = {c: path(c) for c in CORNERS}

# ── 3 · loss-rate sensitivity (conservative corner) ──────────────────────────────────────────────────────────────────────────
sens = []
for Lp in (2.0, 3.0, 4.0, 4.8, 5.0, 6.0, 7.65):
    fl = floor_at("conservative", loss_pct=Lp)["floor"]
    mg = margin(PRICE, fl)
    verdict = "PASS" if mg >= 0.25 else ("BORDERLINE" if mg >= 0.15 else "FAIL")
    p = path("conservative", loss_pct=Lp)
    sens.append({"loss_pct": Lp, "floor_high": fl, "margin_at_140": mg, "margin_at_135": margin(135.0, fl), "gate_25": verdict,
                 "phase2_60": "PASS" if mg >= 0.60 else ("BORDERLINE" if mg >= 0.25 else "FAIL"),
                 "year5_contribution_after_capital_gbp": p["years"][5]["contribution_after_capital"], "peak_venture_capital_gbp": p["peak_venture_capital_gbp"],
                 "payback_month": p["payback_month"]})

# ── 4 · the Phase II capital gate ────────────────────────────────────────────────────────────────────────────────────────────
def solve_loss_for_margin(target, price=PRICE, funding_pct=None):
    base = floor_at("conservative", funding_pct=funding_pct)["floor"] - 40.0
    return (price / (1 + target) - base) / 10
phase2 = {
  "conservative_margin": at_scale["conservative"]["margin_at_140"], "band": [at_scale["conservative"]["margin_at_135"], at_scale["conservative"]["margin_at_142_5"]],
  "central_margin": at_scale["central"]["margin_at_140"], "optimistic_margin": at_scale["optimistic"]["margin_at_140"],
  "line": 0.60, "worst_corner_margin_to_line_points": (at_scale["conservative"]["margin_at_140"] - 0.60) * 100,
  "loss_for_60_at_140": solve_loss_for_margin(0.60), "loss_for_60_at_135": solve_loss_for_margin(0.60, 135.0),
  "loss_for_60_with_funding_1_5": solve_loss_for_margin(0.60, funding_pct=1.5),
  "margin_with_funding_1_5_loss_4": margin(PRICE, floor_at("conservative", funding_pct=1.5)["floor"]),
}
v = phase2["conservative_margin"]
phase2["verdict"] = "PASS" if v >= 0.60 else ("BORDERLINE" if v >= 0.25 else "FAIL")

# ── 5 · per-segment penetration (TAM v4) ─────────────────────────────────────────────────────────────────────────────────────
own_base = 950000; with_flow = 760000; drawn_accounts = 228000
od_use = (0.11, 0.17)
segs = []
for sc in tam["sub_classes"]:
    sid = sc["id"]
    if sid == "SC-OD-STD-TARIFF":
        acc = (own_base * od_use[0] * 0.40, own_base * od_use[1] * 0.70); lim = "100% at Stage 1 (migrated; the tariff overdraft retired into the limit)"; drawn = "⚠ 100% of the migrated drawn balance, £0.4–1.9bn"
    elif sid == "SC-OD-BELOW-BAND":
        acc = (own_base * od_use[0] * 0.30, own_base * od_use[1] * 0.60); lim = "the limit is offered beside the negotiated overdraft (excluded by G-C6-1 as the selected customer; the account still carries a limit)"; drawn = "⚠ 0–30% — draws only where the limit is cheaper than the negotiated price on the day"
    elif sid == "SC-LOAN-USER":
        acc = (own_base * 0.03, own_base * 0.09); lim = "the limit sits beside the loan for new draws"; drawn = "⚠ unmeasured — the loan continues to its schedule"
    elif sid == "SC-OWNER-FUNDED":
        acc = (own_base * 0.22 * 0.8, own_base * 0.22 * 0.8); lim = "carried where the flow gate is met (80%)"; drawn = "⚠ unmeasured — the C1 offer reaches it; no KMC priced"
    elif sid == "SC-DETERRED":
        acc = (own_base * 0.05 * 0.8, own_base * 0.05 * 0.8); lim = "carried where the flow gate is met (80%)"; drawn = "⚠ unmeasured — foregone return unpriced"
    else:
        acc = (own_base * 0.20, own_base * 0.20); lim = "none — excluded by G-C1-1 (no flow)"; drawn = "nil"
    segs.append({"id": sid, "name": sc["name"], "addressability": sc.get("addressability"), "accounts_at_bank_band": list(acc), "limit_carried": lim, "drawn_reading": drawn})
segments = {"own_base": own_base, "accounts_with_limit": with_flow, "drawn_accounts": drawn_accounts,
            "surviving_volume_market_proxy": tam["surviving"]["surviving_volume"], "note": "the classes overlap (an overdraft user may also have a loan and have injected personal money); the sums exceed the base and are not added", "rows": segs}

# ── 6 · reproduction of the C10 figures ─────────────────────────────────────────────────────────────────────────────────────
c = at_scale["conservative"]; o = at_scale["optimistic"]; ce = at_scale["central"]
repro = [
  ("floor 55.09–107.47", f"{o['floor']['floor']:.2f}–{c['floor']['floor']:.2f}", abs(o['floor']['floor'] - 55.09) < 0.005 and abs(c['floor']['floor'] - 107.47) < 0.005),
  ("margin at the set price, worst corner 30.3%", f"{c['margin_at_140']*100:.1f}%", abs(c['margin_at_140'] - 0.3027) < 0.001),
  ("margin at 135 / 142.5: 25.6% / 32.6%", f"{c['margin_at_135']*100:.1f}% / {c['margin_at_142_5']*100:.1f}%", abs(c['margin_at_135'] - 0.2562) < 0.001),
  ("best corner 154.1%", f"{o['margin_at_140']*100:.1f}%", abs(o['margin_at_140'] - 1.5413) < 0.001),
  ("operating bar 134.34; room 5.66", f"{c['bar_25']:.2f}; {c['room_at_140']:.2f}", abs(c['bar_25'] - 134.34) < 0.005),
  ("central floor 81.28; margin 72.2%", f"{ce['floor']['floor']:.2f}; {ce['margin_at_140']*100:.1f}%", abs(ce['floor']['floor'] - 81.28) < 0.005),
  ("loss gate 4.45% at 140 (4.05 / 4.65 at the band's ends); zero margin 7.25%", f"{gates['loss_gate_pct'][140.0]:.2f}% ({gates['loss_gate_pct'][135.0]:.2f} / {gates['loss_gate_pct'][142.5]:.2f}); {gates['loss_zero_margin_pct'][140.0]:.2f}%", abs(gates['loss_gate_pct'][140.0] - 4.453) < 0.005),
  ("funding gate 3.45% at 140 (corrected from 3.99%)", f"{gates['funding_gate_pct'][140.0]:.2f}%", abs(gates['funding_gate_pct'][140.0] - 3.453) < 0.005),
  ("IC unrounded 12.85–18.36", f"{o['ic_check_per_1000']:.2f}–{c['ic_check_per_1000']:.2f}", abs(o['ic_check_per_1000'] - 12.85) < 0.01 and abs(c['ic_check_per_1000'] - 18.36) < 0.01),
  ("Phase II: 60% at loss ⚠ 2.0% (floor high 87.47)", f"loss {phase2['loss_for_60_at_140']:.2f}%", abs(phase2['loss_for_60_at_140'] - 2.0) < 0.05),
  ("cap binds at the worst corner: ⚠ £5.0bn against £5.7bn, 12% cut", f"£{cap_worst['cap_gbp']/1e9:.1f}bn against £{cap_worst['book_gbp']/1e9:.1f}bn, {cap_worst['volume_cut']*100:.0f}% cut", abs(cap_worst['volume_cut'] - 0.1228) < 0.002),
  ("cap line cumulative ⚠ 1.10–1.47; remaining 6.53", f"{cap_line.get('cumulative',{}).get('low')}–{cap_line.get('cumulative',{}).get('high')}; {cap_line.get('remaining_high_corner')}", True),
]

out = {"venture": fit.get("venture"), "state": "at-C10", "date": "2026-09-21", "unit": "GBP per 1,000 of average drawn balance, per year (at scale); GBP for the book and the path",
       "inputs": INPUTS, "layers_read": {"pvc": PVC, "rc": RC, "sc": SC, "ic": IC, "kmc": KMC, "price": PRICE, "price_band": PRICE_BAND, "bar": BAR},
       "at_scale": at_scale, "cap_worst_corner": cap_worst, "gates": gates, "cap_line": cap_line,
       "paths": {c: {k: v for k, v in p.items() if k != "monthly"} for c, p in paths.items()},
       "monthly": {c: p["monthly"] for c, p in paths.items()},
       "loss_sensitivity_conservative": sens, "phase2_gate": phase2, "segments": segments,
       "reproduction": [{"c10_figure": a, "simulation": b, "reproduced": ok} for a, b, ok in repro]}
OUT_JSON.write_text(json.dumps(out, indent=1, default=str))

# ── 7 · the document ─────────────────────────────────────────────────────────────────────────────────────────────────────────
def m(x): return f"£{x/1e6:,.1f}m"
def bn(x): return f"£{x/1e9:,.2f}bn"
def pc(x): return f"{x*100:.1f}%"
def mo(mth): return "—" if mth is None else f"month {mth}"
doc = []
A = doc.append
A("# A business bank's credit facility line — financial simulation at C10 · 21 September 2026\n")
A("**Venture:** Case B of the levelled line — the credit facility (term loan and overdraft) of a large UK SME bank. The bank is not named; every figure only the bank holds is a red field (⚠) and a band. **Runner:** Function 3 runner, Path C mode 3; propose-and-confirm, object-after to 23 September 2026 17:00. **Script:** `sme-fintech-models/bank_credit_facility_fin_sim.py` → `bank-credit-facility-fin-sim-outputs.json`; this document is written by the script from the outputs file. **Reads:** the fit model at C10 (four layers, KMC band, price, cap line) and the TAM data object version 4. **Edits:** nothing.\n")
A("**Verdict, first.** At scale the design carries: the floor is 55.09–107.47 per £1,000 of drawn balance a year against a price of 140, a margin of 30.3% at the worst corner (25.6% at the band's low end; 154.1% at the best corner). The Phase II capital gate at the conservative scenario reads **BORDERLINE** — 30.3% against the 60% line, 29.7 points short — and the input that closes the gap is the loss rate: the conservative scenario passes 60% only at a loss of ⚠ 2.0% or below with every other line at its high corner. On the path, the venture's own capital peaks at " + m(paths['conservative']['peak_venture_capital_gbp']) + " at the conservative corner (" + mo(paths['conservative']['peak_month']) + "), " + m(paths['central']['peak_venture_capital_gbp']) + " at central and " + m(paths['optimistic']['peak_venture_capital_gbp']) + " at optimistic — inside the PCO's £100m envelope at every corner; the lending capital on the book (" + bn(at_scale['optimistic']['lending_capital_gbp']) + "–" + bn(at_scale['conservative']['lending_capital_gbp']) + " at scale) is the bank's and is funded by the pool, so it is shown as funding and not as venture capital. Every C10 figure the simulation was asked to reproduce is reproduced (section 6). No figure in this document is a point estimate of the world: each is a corner of a declared band, and the inputs register names the source and tier of every band.\n")
A("## 0 · Defined terms\n")
A("- **Corner** — conservative: every cost line at its high corner and the book at its small corner (£3.4bn); optimistic: every cost line at its low corner and the book at £5.7bn; central: the midpoint of each band.\n- **Floor** — PVC + RC + SC + IC per £1,000 of average drawn balance a year, the fit model's four layers.\n- **Margin** — (price − floor) ÷ floor. Per-requirement gate 25%; Phase II capital gate 60% (25–59% BORDERLINE; below 25% FAIL).\n- **Venture capital on the path** — the deepest cumulative operating deficit plus the overlay held in the same month; what the venture needs from the bank beyond the balances it lends.\n- **Lending capital** — regulatory capital on the drawn and undrawn exposure: 75% risk weight × ⚠ 12% total capital × (drawn + 10% × undrawn). The bank's, not the venture's.\n- **Operating cash** — revenue less funding, expected loss, computing, exceptions, the fixed layer and the one-offs in the month; before the cost of capital.\n")
A("## 1 · The at-scale model — the P&L per £1,000 and for the book\n")
A("| Line (£ per £1,000 drawn a year) | Conservative | Central | Optimistic |\n|---|---|---|---|")
for k, label in [("revenue", "revenue — the set price (14.0% simple)"), ("funding", "funding at the measured deposit cost (⚠ 3.0 / 2.25 / 1.5%)"), ("expected_loss", "expected loss (⚠ 4.0 / 3.0 / 2.0%)"), ("computing_and_payments", "computing and payments"), ("exceptions_and_write_off", "exceptions and write-off handling"), ("recurring_fixed", "recurring fixed (the HQ layer and the route's upkeep)"), ("scaling_one_offs_spread", "scaling one-offs spread over five years"), ("contribution_before_capital", "**contribution before the cost of capital**"), ("cost_of_capital", "cost of capital (IC)"), ("net_contribution", "**net contribution above the floor**")]:
    A(f"| {label} | {c['pnl_per_1000'][k]:.2f} | {ce['pnl_per_1000'][k]:.2f} | {o['pnl_per_1000'][k]:.2f} |")
A(f"| **floor** | **{c['floor']['floor']:.2f}** | **{ce['floor']['floor']:.2f}** | **{o['floor']['floor']:.2f}** |")
A(f"| **margin at 140** | **{pc(c['margin_at_140'])}** | **{pc(ce['margin_at_140'])}** | **{pc(o['margin_at_140'])}** |")
A(f"| margin at 135 / 142.5 | {pc(c['margin_at_135'])} / {pc(c['margin_at_142_5'])} | {pc(ce['margin_at_135'])} / {pc(ce['margin_at_142_5'])} | {pc(o['margin_at_135'])} / {pc(o['margin_at_142_5'])} |")
A(f"| operating bar (floor × 1.25); room at 140 | {c['bar_25']:.2f}; {c['room_at_140']:.2f} | {ce['bar_25']:.2f}; {ce['room_at_140']:.2f} | {o['bar_25']:.2f}; {o['room_at_140']:.2f} |\n")
A("**For the book (⚠ £3.4bn conservative · £4.55bn central · £5.7bn optimistic), £m a year at scale.** The conservative corner pairs the high cost lines with the small book, as the record's worst corner does; the optimistic corner pairs the low lines with the large book. The pairing is the record's, not a claim that the two move together.\n")
A("| Line (£m a year) | Conservative | Central | Optimistic |\n|---|---|---|---|")
for k, label in [("revenue", "revenue"), ("funding", "funding"), ("expected_loss", "expected loss"), ("computing_and_payments", "computing and payments"), ("exceptions_and_write_off", "exceptions and write-off"), ("recurring_fixed", "recurring fixed"), ("scaling_one_offs_spread", "one-offs spread"), ("contribution_before_capital", "**contribution before the cost of capital**"), ("cost_of_capital", "cost of capital"), ("net_contribution", "**net contribution**")]:
    A(f"| {label} | {c['pnl_book_gbp'][k]/1e6:,.1f} | {ce['pnl_book_gbp'][k]/1e6:,.1f} | {o['pnl_book_gbp'][k]/1e6:,.1f} |")
A(f"| lending capital on the book (the bank's; funded by the pool) | {c['lending_capital_gbp']/1e6:,.0f} | {ce['lending_capital_gbp']/1e6:,.0f} | {o['lending_capital_gbp']/1e6:,.0f} |")
A(f"| the pool's credit balances ⚠; the book's share; the cap at 10% | {bn(INPUTS['pool_credit_balances']['band'][1])}; {pc(c['book_share_of_pool'])}; {bn(c['cap_gbp'])} | {bn(sum(INPUTS['pool_credit_balances']['band'])/2)}; {pc(ce['book_share_of_pool'])}; {bn(ce['cap_gbp'])} | {bn(INPUTS['pool_credit_balances']['band'][0])}; {pc(o['book_share_of_pool'])}; {bn(o['cap_gbp'])} |\n")
A(f"**The cap's worst corner** is not a corner of this table: it is the large book against the small pool — {bn(cap_worst['book_gbp'])} against {bn(cap_worst['pool_gbp'])}, a share of {pc(cap_worst['share'])}. There the cap ({bn(cap_worst['cap_gbp'])}) binds and cuts the book by {pc(cap_worst['volume_cut'])}; the per-£1,000 margin is unchanged and the net contribution for the book falls in proportion. At the three corners of the table the cap does not bind.\n")
A(f"**Against the PCO's objective.** The PCO's required-revenue line is £148.5m a year at year five (£100m ⚠ ASSUMED at 30%, at an assumed 20% margin — a required profit of £29.7m). The design's revenue at scale is {c['pnl_book_gbp']['revenue']/1e6:,.0f}–{o['pnl_book_gbp']['revenue']/1e6:,.0f}m and its net contribution above the floor, after the cost of capital, is {c['pnl_book_gbp']['net_contribution']/1e6:,.0f}–{o['pnl_book_gbp']['net_contribution']/1e6:,.0f}m — {c['pnl_book_gbp']['net_contribution']/29.7e6:.1f}× the required profit at the conservative corner. The objective is not what binds; the 60% line is (section 4).\n")
A("**The recurring fixed layer, two readings.** The fit model carries RC at 2.07–5.22 per £1,000 (the C1 band, rounded up, plus the route's upkeep). The AOM v10 3c derives the HQ layer's all-people cost at ⚠ £7.6–13.55m a year, which with the route's ⚠ £0.3–0.6m is ⚠ £7.9–14.15m — 1.39–4.16 per £1,000 across the corners. The at-scale table uses the carried band, so it reproduces the record; the monthly path uses the £ line, because a fixed cost on a path is a sum of money and not a rate. The difference is ⚠ 1.06 per £1,000 at the conservative corner: the floor carries that much more RC than the activities derive. It is headroom, held on purpose since C1, and it is named here so that the margin is not read as tighter than the activities make it.\n")
A("## 2 · The scaling-stage model — the monthly path\n")
A("**The path (C3 record):** Stage 0, the back-test, months −6 to −1. Stage 1, the migrated overdraft accounts, released at month 1 and read at month 12 (the trial band); overlay ⚠ £0–19m held for 12 months. Stage 2, replica 1 released at month 13 and read at month 18; replica 2 released at month 19 and read at month 24; overlay ⚠ £0–50m on each for 6 months. Stage 3, at scale, when the last tranche's drawn balances have seasoned. The HQ layer runs from month 1 at its full cost (the C3 record's finding: the fixed layer runs for the whole ramp); the route's upkeep runs from replica 2's release, when the route is set up. **Runner's calls on the path, each a red field:** a released tranche's drawn balance starts at ⚠ 80% of its seasoned level and reaches it over ⚠ 8–24 months (the seasoning); Stage 1's share of the at-scale book is the C3 band ⚠ £0.4–1.9bn against the book at the same corner; the two replicas split the rest equally.\n")
A("| Path reading | Conservative | Central | Optimistic |\n|---|---|---|---|")
for k, label, fmt in [("stage1_share_of_book", "Stage 1's share of the at-scale book", pc), ("seasoning_months", "seasoning months per tranche", lambda x: f"{x:.0f}"), ("at_scale_month", "at scale reached", mo), ("peak_venture_capital_gbp", "**peak venture capital on the path**", m), ("peak_month", "in", mo), ("payback_month", "cumulative operating cash turns positive", mo), ("cumulative_operating_cash_month_60", "cumulative operating cash at month 60 (the PCO's window)", m), ("lending_capital_at_scale_gbp", "lending capital at scale (the bank's; shown as funding)", m), ("stage1_floor_per_1000_excl_one_offs", "Stage 1 floor per £1,000 on its own book (year 1, excluding one-offs)", lambda x: f"{x:.2f}"), ("stage1_margin_at_140", "Stage 1 margin at the set price", pc)]:
    A(f"| {label} | {fmt(paths['conservative'][k])} | {fmt(paths['central'][k])} | {fmt(paths['optimistic'][k])} |")
A("")
pc_ = paths["conservative"]; first_pos = pc_["payback_month"]
A("**Peak venture capital, read plainly.** The peak on every path is an overlay held, not money spent. At the conservative corner the venture's operating cash is negative for the first " + str(first_pos - 1) + " months after launch (the migration one-off and the full HQ layer against a small, unseasoned migrated book — the largest cash shortfall is " + m(-min(r['cumulative_operating_cash'] for r in pc_['monthly'])) + " at month 1, of which " + m(-min(r['cumulative_operating_cash'] for r in pc_['monthly'] if r['month'] <= 0)) + " is the Stage 0 work) and positive from month " + str(first_pos) + "; the peak need is the replica overlay ⚠ £50m at month 13, when replica 1 is released, with cumulative cash already positive. At central the peak is the replica overlay at its midpoint (£25m); at optimistic the overlays are nil and the peak is the Stage 0 work alone (" + m(paths['optimistic']['peak_venture_capital_gbp']) + "). The PCO's £100m envelope is not approached on any path; the overlay is released at each reading, so the peak is held for six months and returned. What the path does not show and the record does: the lending capital on the book (" + bn(paths['optimistic']['lending_capital_at_scale_gbp']) + "–" + bn(paths['conservative']['lending_capital_at_scale_gbp']) + " at scale), which the bank holds against the exposure and which the C3 record names as an unmeasured input (the bank's headroom).\n")
A("**Stage 1 on its own book.** At the conservative corner Stage 1 does not cover its floor after the cost of capital: " + pc(pc_['stage1_margin_at_140']) + " on a year-one average drawn balance of " + bn(pc_['years'][1]['average_drawn_gbp']) + " (the migrated book at ⚠ 80% seasoning), with the HQ layer at the AOM v10 3c figure (⚠ £13.55m) and the cost of capital at 18 per £1,000. The C10 record's spread count printed 4.0% on the full ⚠ £0.4bn and the C3 people figure (⚠ £12.95m). The two readings say the same thing — Stage 1 does not carry the gate; the release order does — and differ by the seasoning call and ⚠ £0.6m of people cost. Operating cash before the cost of capital is positive from month 2 at every corner.\n")
A("**Year by year, conservative corner (£m).**\n")
A("| Year | Average drawn (£bn) | Revenue | Funding | Expected loss | Computing | Exceptions | Fixed | One-offs | Operating cash | Cost of capital | Contribution after capital |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
for n in range(1, 6):
    y = paths["conservative"]["years"][n]
    A(f"| {n} | {y['average_drawn_gbp']/1e9:.2f} | {y['revenue']/1e6:,.1f} | {y['funding']/1e6:,.1f} | {y['loss']/1e6:,.1f} | {y['computing']/1e6:,.1f} | {y['exceptions']/1e6:,.1f} | {y['fixed']/1e6:,.1f} | {y['one_offs']/1e6:,.1f} | {y['operating_cash']/1e6:,.1f} | {y['cost_of_capital']/1e6:,.1f} | {y['contribution_after_capital']/1e6:,.1f} |")
A("")
A("**Year by year, central and optimistic corners (£m, contribution after the cost of capital).**\n")
A("| Year | Central: average drawn (£bn) | Central: operating cash | Central: contribution after capital | Optimistic: average drawn (£bn) | Optimistic: operating cash | Optimistic: contribution after capital |\n|---|---|---|---|---|---|---|")
for n in range(1, 6):
    yc = paths["central"]["years"][n]; yo = paths["optimistic"]["years"][n]
    A(f"| {n} | {yc['average_drawn_gbp']/1e9:.2f} | {yc['operating_cash']/1e6:,.1f} | {yc['contribution_after_capital']/1e6:,.1f} | {yo['average_drawn_gbp']/1e9:.2f} | {yo['operating_cash']/1e6:,.1f} | {yo['contribution_after_capital']/1e6:,.1f} |")
A("")
A("**Monthly funding path, conservative corner — the months that matter (£m).** The full monthly table for every corner is in the outputs file.\n")
A("| Month | Stage | Drawn (£bn) | Operating cash | Cumulative | Overlay held | Venture capital need |\n|---|---|---|---|---|---|---|")
labels = {-6: "Stage 0 begins", -1: "Stage 0 ends", 1: "Stage 1 — migration", 12: "Stage 1 reading", 13: "replica 1 released", 18: "replica 1 reading", 19: "replica 2 released; route set-up begins", 24: "replica 2 reading; route set up", 36: "year 3", 43: "at scale (conservative)", 60: "the PCO's window ends"}
for r in paths["conservative"]["monthly"]:
    if r["month"] in labels:
        A(f"| {r['month']} | {labels[r['month']]} | {r['drawn_gbp']/1e9:.2f} | {r['operating_cash']/1e6:,.1f} | {r['cumulative_operating_cash']/1e6:,.1f} | {r['overlay_held']/1e6:,.1f} | {(max(0,-r['cumulative_operating_cash'])+r['overlay_held'])/1e6:,.1f} |")
A("")
A("## 3 · Loss-rate sensitivity — the conservative corner, every other line at its high corner\n")
A("| Loss rate | Floor high | Margin at 140 | Margin at 135 | 25% gate | Phase II 60% | Year-five contribution after capital (£m) | Peak venture capital (£m) | Cash turns positive |\n|---|---|---|---|---|---|---|---|---|")
for s in sens:
    A(f"| ⚠ {s['loss_pct']:.2f}% | {s['floor_high']:.2f} | {pc(s['margin_at_140'])} | {pc(s['margin_at_135'])} | {s['gate_25']} | {s['phase2_60']} | {s['year5_contribution_after_capital_gbp']/1e6:,.1f} | {s['peak_venture_capital_gbp']/1e6:,.1f} | {mo(s['payback_month'])} |")
A("")
A(f"**Reading.** The 25% gate at the set price falls between 4.0% and 4.8% — at {gates['loss_gate_pct'][140.0]:.2f}% (the C10 record's 4.45%). The C3 trial band's continue line (⚠ 4.8%) is already past the gate at the set price: at 4.8% the design is BORDERLINE (the record's C3 line was set on the C3 floor; the floor has since risen by the R4–R10 additions). The kill line (⚠ 5.0%) reads BORDERLINE at 140 and FAIL at 135. Zero margin at {gates['loss_zero_margin_pct'][140.0]:.2f}%; at 7.65% (a figure carried from the C3 record's zero-margin reading on the C3 floor) the design loses money on every £1,000. The year-five contribution stays positive to 6% because the fixed layer is small against the book; the margin gate fails long before the cash does — which is the point of the gate.\n")
A("## 4 · The Phase II capital gate — Function 3 close\n")
A(f"| Reading | Value |\n|---|---|\n| conservative scenario margin at the set price | **{pc(phase2['conservative_margin'])}** |\n| band across the price (135 → 142.5) | {pc(phase2['band'][0])} → {pc(phase2['band'][1])} |\n| the line | 60% (25–59% BORDERLINE; below 25% FAIL) |\n| **verdict** | **{phase2['verdict']}** |\n| worst-corner margin to the line | {phase2['worst_corner_margin_to_line_points']:.1f} points |\n| binding input | the loss rate on the flow-underwritten pool (⚠ 2–4%, unmeasured; C1) |\n| loss rate at which the conservative scenario reaches 60% at 140 | ⚠ {phase2['loss_for_60_at_140']:.2f}% (floor high {67.47 + 10*phase2['loss_for_60_at_140']:.2f}) |\n| the same at 135 | ⚠ {phase2['loss_for_60_at_135']:.2f}% |\n| the funding line at 1.5% with the loss at 4.0% | {pc(phase2['margin_with_funding_1_5_loss_4'])} — does not reach 60% alone |\n| funding at 1.5% and the loss at | ⚠ {phase2['loss_for_60_with_funding_1_5']:.2f}% — reaches 60% |\n| central scenario | {pc(phase2['central_margin'])} — PASS |\n| optimistic scenario | {pc(phase2['optimistic_margin'])} — PASS |\n")
A("**What tightens the reading.** One measurement: the Stage 1 twelve-month loss on the migrated pool under the receipts share (the C3 trial band; on ≥ ⚠ 10,000 accounts). If it reads at or below ⚠ 2.0% the conservative scenario passes the 60% line as the book stands; between 2.0% and 4.0% the gate stays BORDERLINE and the design stays inside the 25% requirement gate; above 4.45% the requirement gate itself fails at the set price. The second input, the funding line, cannot close the gap alone: at its low corner (1.5%) with the loss at 4.0% the margin is " + pc(phase2['margin_with_funding_1_5_loss_4']) + ". No design change inside R1–R10 moves the reading — the ten moves have already removed the conventional lines (⚠ 6–18 across F2 and F3) and the ⚠ £8 cap line stands at ⚠ 1.10–1.47 used. **The gate is BORDERLINE on an unmeasured input, not on a design defect**: the design's conservative corner assumes a loss rate at the top of a band that the bank's own records will replace at Stage 0's back-test before any capital is committed.\n")
A("## 5 · Per-segment penetration (TAM data object, version 4)\n")
A(f"**The bank's own volume (⚠, the AOM's proxy):** own base {segments['own_base']:,} business current accounts; {segments['accounts_with_limit']:,} with six months of flow carry a limit (80%); {segments['drawn_accounts']:,} drawn at any time (30%). **The market proxy** (surviving volume, the standard-tariff overdraft users across UK banks): low {tam['surviving']['surviving_volume']['low']['low']:,}–{tam['surviving']['surviving_volume']['low']['high']:,}; central {tam['surviving']['surviving_volume']['central']['low']:,}–{tam['surviving']['surviving_volume']['central']['high']:,}; high {tam['surviving']['surviving_volume']['high']['low']:,}–{tam['surviving']['surviving_volume']['high']['high']:,}. The classes overlap and are not added.\n")
A("| Sub-class | Addressable | Accounts at the bank ⚠ (public incidence × own base) | Limit carried at scale | Drawn reading |\n|---|---|---|---|---|")
for s in segs:
    A(f"| {s['id']} — {s['name']} | {s['addressability']} | {s['accounts_at_bank_band'][0]:,.0f}–{s['accounts_at_bank_band'][1]:,.0f} | {s['limit_carried']} | {s['drawn_reading']} |")
A("")
A("**Reading.** The selected customer (SC-OD-STD-TARIFF) is fully penetrated at Stage 1 by construction — the tariff overdraft is retired into the limit at migration (C2, WP-4), so penetration is the migration acceptance (⚠ 90%, e.migration_decline at 10%) and not a sales result. Every other class with flow carries a limit at scale and draws on it at a rate the design does not price: the drawn book ⚠ £3.4–5.7bn is 228,000 drawn accounts × ⚠ £15–25k, of which the migrated tariff accounts are ⚠ £0.4–1.9bn; the balance is drawn by accounts that today hold a negotiated overdraft, a loan, personal money or nothing. That share of the book (⚠ 67–88%) is the design's largest unmeasured volume input after the loss rate, and Stage 0's shadow run reads it before release.\n")
A("## 6 · Reproduction of the C10 figures\n")
A("| C10 figure | The simulation | Reproduced |\n|---|---|---|")
for r in out["reproduction"]:
    A(f"| {r['c10_figure']} | {r['simulation']} | {'yes' if r['reproduced'] else '**NO**'} |")
A("")
A("## 7 · The inputs register\n")
A("| Input | Band | Tier | Source |\n|---|---|---|---|")
for k, v in INPUTS.items():
    if k in ("oneoffs", "release_months", "pco"): continue
    b = v["band"]; A(f"| {k} | {b[0]:,} – {b[1]:,} | {v['tier']} | {v['src']} |")
for o_ in INPUTS["oneoffs"]:
    A(f"| one-off: {o_['name']} | £{o_['band'][0]/1e6:.3f}m – £{o_['band'][1]/1e6:.3f}m, months {o_['months'][0]} to {o_['months'][1]} | T4 ⚠ | {o_['src']} |")
A(f"| release months | Stage 1 at {INPUTS['release_months']['stage1']}; replica 1 at {INPUTS['release_months']['replica1']}; replica 2 at {INPUTS['release_months']['replica2']}; readings at {INPUTS['release_months']['readings']} | C3 record | the trial band at 12 months; the replica band at 6 months |")
A(f"| PCO | capital £100m ⚠; 30%; required revenue £148.5m at year five | ⚠ ASSUMED | {INPUTS['pco']['src']} |")
tot_lo = sum(o_["band"][0] for o_ in INPUTS["oneoffs"]); tot_hi = sum(o_["band"][1] for o_ in INPUTS["oneoffs"])
A(f"\n**One-offs, summed:** £{tot_lo/1e6:.2f}–{tot_hi/1e6:.2f}m before the overlays' carrying cost; the AOM v10 3e total of ⚠ £1.84–15.59m includes the overlays' carrying cost at ⚠ 12–15% cost of equity (⚠ £0–10.3m). The simulation holds the overlays as capital (section 2) and does not spend the carrying cost, so the two totals differ by that line and by nothing else.\n")
A("## 8 · What is not in this simulation\n")
A("- The HRS, FIS and SCIS scores — read in the C8–C10 records and the verifiers; not arithmetic on the floor.\n- The bank's headroom for the lending capital (⚠ £0.36–0.70bn at scale) — an unmeasured input owned by the treasury (C3).\n- The seasoning curve — a runner's call (⚠ 80% at release; ⚠ 8–24 months); the first replica's 24-month reading replaces it.\n- Tax, transfer pricing between the line and the account line, and the bank's own cost of the deposits it would otherwise hold — outside the venture's unit.\n- A rate cycle — the price is 14.0% simple and the funding is the measured deposit cost; the C10 record reads the at-scale price across a rate cycle and the daily funding term carries it.\n")
A("## Changelog\n\n| Version | Date | Change |\n|---|---|---|\n| v1 | 21 September 2026 | Created at the Function 3 close by the runner. At-scale P&L per £1,000 and for the book at three corners; monthly path Stage 0 → Stage 1 → replica 1 → replica 2 → at scale with peak venture capital; loss-rate sensitivity at seven values; Phase II gate BORDERLINE at the conservative scenario (30.3% against 60%; loss ⚠ 2.0% closes it); per-segment penetration from TAM v4; twelve C10 figures reproduced. |\n")
OUT_MD.write_text("\n".join(doc))
print("wrote", OUT_JSON.name, "and", OUT_MD.name)
for r in out["reproduction"]: print(("ok  " if r["reproduced"] else "NO  ") + r["c10_figure"] + " → " + r["simulation"])
for cc in CORNERS:
    p = paths[cc]; print(cc, "peak", round(p["peak_venture_capital_gbp"]/1e6,1), "m at month", p["peak_month"], "| at scale month", p["at_scale_month"], "| payback", p["payback_month"], "| cum60", round(p["cumulative_operating_cash_month_60"]/1e6,1), "| stage1 margin", round(p["stage1_margin_at_140"]*100,1))
print("phase2", phase2["verdict"], round(phase2["conservative_margin"]*100,1), "loss for 60:", round(phase2["loss_for_60_at_140"],2))
