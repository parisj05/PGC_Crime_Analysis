import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("cleaned/cleandata.csv")
df["OccurredOn"] = pd.to_datetime(df["OccurredOn"])

output_dir = Path("visualizations/sq1_time_offense")
output_dir.mkdir(parents=True, exist_ok=True)

monthly_incidents = (
    df.groupby(df["OccurredOn"].dt.to_period("M"))["CaseNumber"]
    .nunique()
    .reset_index()
)

monthly_incidents.columns = ["Month", "UniqueIncidents"]

print("\nMonthly Incidents:")
print(monthly_incidents.to_string(index=False))

plt.figure(figsize=(12, 6))
plt.plot(
    monthly_incidents["Month"].astype(str),
    monthly_incidents["UniqueIncidents"]
)
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Unique Incidents")
plt.title("Monthly Crime Incidents in Prince George's County")
plt.tight_layout()
plt.savefig(output_dir / "monthly_incidents.png", dpi=300)
plt.close()

offense_incidents = (
    df.groupby("Offense")["CaseNumber"]
    .nunique()
    .sort_values(ascending=True)
)

print("\nUnique Incidents by Offense:")
print(offense_incidents.sort_values(ascending=False).to_string())

plt.figure(figsize=(10, 8))
plt.barh(offense_incidents.index, offense_incidents.values)
plt.xlabel("Unique Incidents")
plt.ylabel("Offense")
plt.title("Crime Incidents by Offense")
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_offense.png", dpi=300)
plt.close()

top_offenses = (
    df.groupby("Offense")["CaseNumber"]
    .nunique()
    .nlargest(5)
    .index
)

offense_monthly = (
    df[df["Offense"].isin(top_offenses)]
    .groupby(
        [df["OccurredOn"].dt.to_period("M"), "Offense"]
    )["CaseNumber"]
    .nunique()
    .reset_index()
)

offense_monthly.columns = [
    "Month",
    "Offense",
    "UniqueIncidents"
]

plt.figure(figsize=(12, 6))

for offense in top_offenses:
    data = offense_monthly[
        offense_monthly["Offense"] == offense
    ]

    plt.plot(
        data["Month"].astype(str),
        data["UniqueIncidents"],
        label=offense
    )

plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Unique Incidents")
plt.title("Monthly Trends for Top 5 Offenses")
plt.legend()
plt.tight_layout()
plt.savefig(output_dir / "top_5_offense_trends.png", dpi=300)
plt.close()

print("\nTop 5 Offenses:")
print(top_offenses.to_list())

monthly_incidents["Change"] = (
    monthly_incidents["UniqueIncidents"].diff()
)

monthly_incidents["PercentChange"] = (
    monthly_incidents["UniqueIncidents"].pct_change() * 100
)

print("\nMonthly Changes:")
print(monthly_incidents.to_string(index=False))

largest_increases = (
    monthly_incidents
    .dropna(subset=["PercentChange"])
    .nlargest(5, "PercentChange")
)

largest_decreases = (
    monthly_incidents
    .dropna(subset=["PercentChange"])
    .nsmallest(5, "PercentChange")
)

print("\nLargest Monthly Increases:")
print(largest_increases.to_string(index=False))

print("\nLargest Monthly Decreases:")
print(largest_decreases.to_string(index=False))

for year in [2025, 2026]:
    subset = df[
        (df["OccurredOn"].dt.year == year)
        & (df["OccurredOn"].dt.month.isin([1, 2, 3]))
    ]

    result = (
        subset.groupby(
            [subset["OccurredOn"].dt.month, "Offense"]
        )["CaseNumber"]
        .nunique()
        .reset_index()
    )

    result.columns = [
        "Month",
        "Offense",
        "UniqueIncidents"
    ]

    pivot = result.pivot(
        index="Offense",
        columns="Month",
        values="UniqueIncidents"
    ).fillna(0)

    pivot["Jan_to_Mar_Change"] = (
        pivot.get(3, 0) - pivot.get(1, 0)
    )

    print(
        f"\n{year} January to March Offense Changes:"
    )
    print(
        pivot
        .sort_values(
            "Jan_to_Mar_Change",
            ascending=False
        )
        .to_string()
    )