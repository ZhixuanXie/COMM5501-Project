"""Core analysis for COMM5501 Deliverable 2.

Combines the NSW public EV charging-station CSV with ABS LGA population to
compute public charging plugs per 10,000 residents, split by Greater Sydney
vs Rest of NSW. Prints join coverage and headline numbers so the chart design
can be validated against the raw data.
"""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

EV_CSV = "ev_20251216.csv"
ABS_XLSX = "data/abs_regional_population_lga_2024_25.xlsx"

# ABS Greater Sydney GCCSA (1GSYD) constituent LGAs, ASGS Edition 3.
# Source: ABS Australian Statistical Geography Standard (ASGS) GCCSA.
GREATER_SYDNEY_RAW = [
    "Bayside", "Blacktown", "Blue Mountains", "Burwood", "Camden",
    "Campbelltown", "Canada Bay", "Canterbury-Bankstown", "Central Coast",
    "Cumberland", "Fairfield", "Georges River", "Hawkesbury", "Hornsby",
    "Hunters Hill", "Inner West", "Ku-ring-gai", "Lane Cove", "Liverpool",
    "Mosman", "North Sydney", "Northern Beaches", "Parramatta", "Penrith",
    "Randwick", "Ryde", "Strathfield", "Sutherland Shire", "Sydney",
    "The Hills Shire", "Waverley", "Willoughby", "Wollondilly", "Woollahra",
]

# Tokens that only describe the type of governance area, not its identity.
_DROP_TOKENS = {
    "council", "city", "shire", "municipality", "municipal", "regional",
    "district", "of", "the", "area", "nsw", "vic", "tas", "qld",
}


def norm_lga(name: str) -> str:
    """Normalise an LGA label to a comparable key (handles CSV vs ABS forms)."""
    if not isinstance(name, str):
        return ""
    s = name.lower().strip()
    s = s.replace("&", "and")
    s = re.sub(r"\(.*?\)", " ", s)        # drop "(nsw)" style qualifiers
    s = s.split(",")[0]                    # "sydney, council of the city of"
    s = s.replace("-", " ")               # "canterbury-bankstown" -> two words
    s = re.sub(r"[^a-z\s]", " ", s)
    tokens = [t for t in s.split() if t and t not in _DROP_TOKENS]
    return " ".join(tokens).strip()


GREATER_SYDNEY = {norm_lga(x) for x in GREATER_SYDNEY_RAW}


def load_charging() -> pd.DataFrame:
    df = pd.read_csv(EV_CSV)
    df["plugs"] = pd.to_numeric(df["Number_of_plugs"], errors="coerce")
    df = df.dropna(subset=["LGANAME"])
    df["lga_key"] = df["LGANAME"].map(norm_lga)
    return df


def load_population() -> pd.DataFrame:
    # Table 1 = NSW LGAs. Real header is split over rows; data starts at row 6.
    raw = pd.read_excel(ABS_XLSX, sheet_name="Table 1", header=None)
    rows = []
    for _, r in raw.iterrows():
        code = r[0]
        if isinstance(code, (int, float)) and not pd.isna(code) and code >= 10000:
            name = r[1]
            erp_2025 = r[3]
            if isinstance(name, str) and pd.notna(erp_2025):
                rows.append((int(code), name.strip(), float(erp_2025)))
    pop = pd.DataFrame(rows, columns=["lga_code", "lga_name", "erp_2025"])
    pop["lga_key"] = pop["lga_name"].map(norm_lga)
    return pop


def main() -> None:
    ev = load_charging()
    pop = load_population()

    print(f"Charging rows: {len(ev):,}; total plugs: {ev['plugs'].sum():,.0f}")
    print(f"ABS NSW LGAs: {len(pop)}; total ERP 2025: {pop['erp_2025'].sum():,.0f}")

    by_lga = (
        ev.groupby("lga_key")
        .agg(sites=("plugs", "size"), plugs=("plugs", "sum"))
        .reset_index()
    )

    merged = by_lga.merge(pop, on="lga_key", how="left", indicator=True)
    unmatched = merged[merged["_merge"] == "left_only"]
    print("\n--- JOIN COVERAGE ---")
    matched_plugs = merged.loc[merged["_merge"] == "both", "plugs"].sum()
    print(f"Matched LGAs: {(merged['_merge']=='both').sum()} / {len(merged)}")
    print(f"Plugs matched to a population: {matched_plugs:,.0f} "
          f"({matched_plugs/ev['plugs'].sum()*100:.1f}% of all plugs)")
    if len(unmatched):
        print("UNMATCHED charging LGA keys (and their plug counts):")
        for _, r in unmatched.sort_values("plugs", ascending=False).iterrows():
            print(f"   '{r['lga_key']}'  plugs={r['plugs']:.0f}")

    # Region split + per-capita on matched LGAs.
    full = pop.merge(by_lga, on="lga_key", how="left")
    full["plugs"] = full["plugs"].fillna(0)
    full["sites"] = full["sites"].fillna(0)
    full["region"] = full["lga_key"].apply(
        lambda k: "Greater Sydney" if k in GREATER_SYDNEY else "Rest of NSW"
    )
    full["plugs_per_10k"] = full["plugs"] / full["erp_2025"] * 10_000

    grp = full.groupby("region").agg(
        lgas=("lga_key", "size"),
        population=("erp_2025", "sum"),
        plugs=("plugs", "sum"),
    )
    grp["plugs_per_10k"] = grp["plugs"] / grp["population"] * 10_000
    print("\n--- REGION AGGREGATE (plugs per 10,000 residents) ---")
    print(grp.to_string())
    gs = grp.loc["Greater Sydney", "plugs_per_10k"]
    rn = grp.loc["Rest of NSW", "plugs_per_10k"]
    print(f"\nGreater Sydney is {gs/rn:.2f}x Rest of NSW on plugs per 10k.")

    print("\n--- LGAs with ZERO public plugs (population >= 5,000) ---")
    zero = full[(full["plugs"] == 0) & (full["erp_2025"] >= 5000)]
    print(f"{len(zero)} populated LGAs have no public charging plug recorded.")
    print(zero.sort_values("erp_2025", ascending=False)
          [["lga_name", "erp_2025", "region"]].head(15).to_string(index=False))

    print("\n--- Most under-served LGAs (pop >= 20,000), lowest plugs per 10k ---")
    big = full[full["erp_2025"] >= 20000].sort_values("plugs_per_10k")
    print(big[["lga_name", "region", "erp_2025", "plugs", "plugs_per_10k"]]
          .head(15).to_string(index=False))

    # Within Greater Sydney: inner/affluent vs outer-western suburbs.
    gs_df = full[full["region"] == "Greater Sydney"].copy()
    print("\n--- WITHIN GREATER SYDNEY: best served (plugs per 10k) ---")
    print(gs_df.sort_values("plugs_per_10k", ascending=False)
          [["lga_name", "erp_2025", "plugs", "plugs_per_10k"]]
          .head(8).to_string(index=False))
    print("\n--- WITHIN GREATER SYDNEY: worst served (plugs per 10k) ---")
    print(gs_df.sort_values("plugs_per_10k")
          [["lga_name", "erp_2025", "plugs", "plugs_per_10k"]]
          .head(10).to_string(index=False))

    # Inequality summary across Greater Sydney LGAs.
    gs_sorted = gs_df.sort_values("plugs_per_10k")
    half = len(gs_sorted) // 2
    bottom = gs_sorted.head(half)
    top = gs_sorted.tail(half)
    print("\n--- Greater Sydney inequality ---")
    print(f"Bottom half LGAs: {len(bottom)} LGAs, "
          f"{bottom['erp_2025'].sum():,.0f} residents, "
          f"{bottom['plugs'].sum():.0f} plugs, "
          f"{bottom['plugs'].sum()/bottom['erp_2025'].sum()*10000:.2f} per 10k")
    print(f"Top half LGAs:    {len(top)} LGAs, "
          f"{top['erp_2025'].sum():,.0f} residents, "
          f"{top['plugs'].sum():.0f} plugs, "
          f"{top['plugs'].sum()/top['erp_2025'].sum()*10000:.2f} per 10k")

    full.to_csv("data/lga_charging_access.csv", index=False)
    print("\nWrote data/lga_charging_access.csv")


if __name__ == "__main__":
    main()
