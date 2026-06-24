"""Standalone export of the FINAL Deliverable 2 chart.

Reproduces the single submitted visualisation (public EV charging plugs per
10,000 residents across the 34 Greater Sydney LGAs) from the raw data and
saves a high-resolution PNG and a vector PDF into ``final_chart/``.

Run from the project root:
    python scripts/make_final_chart.py
"""
from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

EV_CSV = "ev_20251216.csv"
ABS_XLSX = "data/abs_regional_population_lga_2024_25.xlsx"
OUT_DIR = Path("final_chart")

INK = "#1a1a2e"
MUTED = "#c7ccd6"
ACCENT = "#e63946"
INNER = "#2a6f97"

GREATER_SYDNEY_RAW = [
    "Bayside", "Blacktown", "Blue Mountains", "Burwood", "Camden",
    "Campbelltown", "Canada Bay", "Canterbury-Bankstown", "Central Coast",
    "Cumberland", "Fairfield", "Georges River", "Hawkesbury", "Hornsby",
    "Hunters Hill", "Inner West", "Ku-ring-gai", "Lane Cove", "Liverpool",
    "Mosman", "North Sydney", "Northern Beaches", "Parramatta", "Penrith",
    "Randwick", "Ryde", "Strathfield", "Sutherland Shire", "Sydney",
    "The Hills Shire", "Waverley", "Willoughby", "Wollondilly", "Woollahra",
]
_DROP = {
    "council", "city", "shire", "municipality", "municipal", "regional",
    "district", "of", "the", "area", "nsw", "vic", "tas", "qld",
}


def norm_lga(name: str) -> str:
    if not isinstance(name, str):
        return ""
    s = name.lower().strip().replace("&", "and")
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.split(",")[0].replace("-", " ")
    s = re.sub(r"[^a-z\s]", " ", s)
    return " ".join(t for t in s.split() if t and t not in _DROP).strip()


def build_table() -> pd.DataFrame:
    gs_keys = {norm_lga(x) for x in GREATER_SYDNEY_RAW}

    ev = pd.read_csv(EV_CSV)
    ev["plugs"] = pd.to_numeric(ev["Number_of_plugs"], errors="coerce")
    ev = ev.dropna(subset=["LGANAME"]).copy()
    ev["lga_key"] = ev["LGANAME"].map(norm_lga)

    raw = pd.read_excel(ABS_XLSX, sheet_name="Table 1", header=None)
    rows = []
    for _, r in raw.iterrows():
        code = r[0]
        if isinstance(code, (int, float)) and not pd.isna(code) and code >= 10000:
            if isinstance(r[1], str) and pd.notna(r[3]):
                rows.append((r[1].strip(), float(r[3])))
    pop = pd.DataFrame(rows, columns=["lga_name", "erp_2025"])
    pop["lga_key"] = pop["lga_name"].map(norm_lga)

    by_lga = ev.groupby("lga_key").agg(plugs=("plugs", "sum")).reset_index()
    full = pop.merge(by_lga, on="lga_key", how="left")
    full["plugs"] = full["plugs"].fillna(0)
    full["region"] = np.where(full["lga_key"].isin(gs_keys),
                              "Greater Sydney", "Rest of NSW")
    full["plugs_per_10k"] = full["plugs"] / full["erp_2025"] * 10_000
    return full


def make_chart(full: pd.DataFrame) -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans"})
    gs = (full[full["region"] == "Greater Sydney"]
          .sort_values("plugs_per_10k", ascending=True).reset_index(drop=True))
    metro_avg = gs["plugs"].sum() / gs["erp_2025"].sum() * 10_000

    colours = np.where(gs["plugs_per_10k"] < metro_avg, ACCENT, MUTED)
    colours[gs["plugs_per_10k"].idxmax()] = INNER

    fig, ax = plt.subplots(figsize=(10, 9.5))
    ax.barh(gs["lga_name"], gs["plugs_per_10k"], color=colours,
            edgecolor="white", linewidth=0.5)

    for y, v in enumerate(gs["plugs_per_10k"]):
        ax.text(v + 0.15, y, f"{v:.1f}", va="center", ha="left",
                fontsize=8.5, color=INK)

    ax.axvline(metro_avg, color=INK, linewidth=1.1, linestyle="--", alpha=0.8)
    ax.text(metro_avg + 0.15, 0.4, f"Greater Sydney average\n{metro_avg:.1f} per 10,000",
            fontsize=8.5, color=INK, va="bottom")

    fig.text(0.013, 0.975,
             "Sydney's high-population outer suburbs are starved of public EV charging",
             fontsize=15.5, fontweight="bold", color=INK, ha="left")
    fig.text(0.013, 0.945,
             "Public EV charging plugs per 10,000 residents, 34 Greater Sydney LGAs (2025)",
             fontsize=11, color="#444", ha="left")

    ax.annotate(
        "Outer & south-western suburbs:\nlarge populations, very few public plugs",
        xy=(gs["plugs_per_10k"].iloc[3], 3), xytext=(5.4, 6.2),
        fontsize=9, color=ACCENT, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.3))

    ax.set_xlabel("Public charging plugs per 10,000 residents")
    ax.set_xlim(0, gs["plugs_per_10k"].max() * 1.12)
    ax.spines[["top", "right"]].set_visible(False)
    ax.xaxis.grid(True, color="#e9e9ee", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)

    fig.text(0.013, 0.012,
             "Source: Transport for NSW public EV charging stations (Data.NSW, accessed 16 Dec 2025); "
             "ABS Regional Population 2024-25, ERP by LGA (cat. 3218.0).\n"
             "'Greater Sydney' = ABS GCCSA (ASGS Ed. 3). Each LGA's plug count divided by its 2025 "
             "estimated resident population. Author's own analysis.",
             fontsize=7.5, color="#666", ha="left")

    plt.subplots_adjust(top=0.90, bottom=0.085, left=0.18, right=0.97)
    OUT_DIR.mkdir(exist_ok=True)
    png = OUT_DIR / "deliverable2_final_chart.png"
    pdf = OUT_DIR / "deliverable2_final_chart.pdf"
    fig.savefig(png, dpi=300)
    fig.savefig(pdf)
    plt.close(fig)
    print(f"Saved {png} (300 dpi) and {pdf}")


if __name__ == "__main__":
    make_chart(build_table())
