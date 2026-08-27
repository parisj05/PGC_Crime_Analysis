import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("cleaned/cleandata.csv")
df["OccurredOn"] = pd.to_datetime(df["OccurredOn"])

output_dir = Path("visualizations/sq2_geography")
output_dir.mkdir(parents=True, exist_ok=True)

division_incidents = (
    df.groupby("Division")["CaseNumber"]
    .nunique()
    .sort_values(ascending=True)
)

print("\nUnique Incidents by Division:")
print(division_incidents.sort_values(ascending=False).to_string())

plt.figure(figsize=(10, 6))
plt.barh(division_incidents.index, division_incidents.values)
plt.xlabel("Unique Incidents")
plt.ylabel("Police Division")
plt.title("Crime Incidents by Police Division")
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_division.png", dpi=300)
plt.close()

municipality_incidents = (
    df.groupby("Municipality")["CaseNumber"]
    .nunique()
    .sort_values(ascending=True)
)

print("\nUnique Incidents by Municipality:")
print(municipality_incidents.sort_values(ascending=False).to_string())

plt.figure(figsize=(10, 10))
plt.barh(municipality_incidents.index, municipality_incidents.values)
plt.xlabel("Unique Incidents")
plt.ylabel("Municipality")
plt.title("Crime Incidents by Municipality")
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_municipality.png", dpi=300)
plt.close()

beat_incidents = (
    df.dropna(subset=["Beat"])
    .groupby("Beat")["CaseNumber"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nTop 10 Beats:")
print(beat_incidents.head(10).to_string())

top_beats = beat_incidents.head(10).sort_values(ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(top_beats.index, top_beats.values)
plt.xlabel("Unique Incidents")
plt.ylabel("Police Beat")
plt.title("Top 10 Police Beats by Crime Incidents")
plt.tight_layout()
plt.savefig(output_dir / "top_10_beats.png", dpi=300)
plt.close()

reporting_area_incidents = (
    df.dropna(subset=["ReportingArea"])
    .groupby("ReportingArea")["CaseNumber"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nTop 10 Reporting Areas:")
print(reporting_area_incidents.head(10).to_string())

top_reporting_areas = (
    reporting_area_incidents
    .head(10)
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_reporting_areas.index.astype(str),
    top_reporting_areas.values
)
plt.xlabel("Unique Incidents")
plt.ylabel("Reporting Area")
plt.title("Top 10 Reporting Areas by Crime Incidents")
plt.tight_layout()
plt.savefig(output_dir / "top_10_reporting_areas.png", dpi=300)
plt.close()

zip_incidents = (
    df.dropna(subset=["PostalCode"])
    .groupby("PostalCode")["CaseNumber"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nTop 10 ZIP Codes:")
print(zip_incidents.head(10).to_string())

top_zips = (
    zip_incidents
    .head(10)
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_zips.index.astype(str),
    top_zips.values
)
plt.xlabel("Unique Incidents")
plt.ylabel("ZIP Code")
plt.title("Top 10 ZIP Codes by Crime Incidents")
plt.tight_layout()
plt.savefig(output_dir / "top_10_zip_codes.png", dpi=300)
plt.close()

print("\nGeographic analysis complete.")
print(f"Charts saved to: {output_dir}")