import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("cleaned/cleandata.csv")
df["OccurredOn"] = pd.to_datetime(df["OccurredOn"])
location_cleaning = {
    "Residence/Home": "Residence / Home",
    "Parking Lot/Garage": "Parking Lot / Garage",
    "Highway/Road/Alley": "Highway / Road / Alley",
    "Commercial/Office Building": "Commercial / Office Building",
    "Department/Discount Store": "Department / Discount Store",
    "Service/Gas Station": "Service / Gas Station",
    "Grocery/Supermarket": "Grocery / Supermarket",
    "Other/Unknown": "Other / Unknown",
    "Drug Store/Doctors Office/Hospital": "Drug Store / Doctors Office",
    "School-Elementary/Secondary": "Elementary / Secondary School",
    "Park/Playground": "Park / Playground",
    "Bar/Night Club": "Bar / Night Club",
    "Hotel/Motel/Etc.": "Hotel / Motel",
    "Field/Woods": "Field / Woods",
    "Bank/Savings and Loan": "Bank / Savings and Loan",
    "Church/Synagogue/Temple": "Church / Synagogue / Temple",
    "Government/Public Building": "Government / Public Building",
    "Airport / Bus / Train Terminal": "Airport / Bus / Train Terminal",
    "Air/Bus/Train Terminal": "Airport / Bus / Train Terminal",
    "Gambling Facility/Casino/Race Track": "Gambling Facility - Casino, Race Track, etc.",
    "Arena/Stadium/Fairgrounds/Coliseum": "Arena / Stadium / Fairgrounds / Coliseum",
    "College / University": "College / University",
    "School-College/University": "College / University",
    "Jail/Prison/Penitentiary/Corrections Facility": "Jail / Prison / Penitentiary / Corrections Facility",
    "Shelter-Mission/Homeless": "Mission / Homeless Shelter",
    "Dock/Wharf/Freight/Modal Terminal": "Dock / Wharf / Freight / Modal Terminal"
}

df["LocationType"] = df["LocationType"].replace(location_cleaning)

output_dir = Path("visualizations/sq3_context")
output_dir.mkdir(parents=True, exist_ok=True)

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_incidents = (
    df.groupby("DayOfWeek")["CaseNumber"]
    .nunique()
    .reindex(day_order)
)

print("\nUnique Incidents by Day of Week:")
print(day_incidents.to_string())

plt.figure(figsize=(10, 6))
plt.bar(day_incidents.index, day_incidents.values)
plt.xlabel("Day of Week")
plt.ylabel("Unique Incidents")
plt.title("Crime Incidents by Day of Week")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_day_of_week.png", dpi=300)
plt.close()

hour_incidents = (
    df.groupby("Hour")["CaseNumber"]
    .nunique()
    .reindex(range(24), fill_value=0)
)

print("\nUnique Incidents by Hour:")
print(hour_incidents.to_string())

plt.figure(figsize=(12, 6))
plt.plot(hour_incidents.index, hour_incidents.values, marker="o")
plt.xlabel("Hour of Day")
plt.ylabel("Unique Incidents")
plt.title("Crime Incidents by Hour of Day")
plt.xticks(range(24))
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_hour.png", dpi=300)
plt.close()

month_incidents = (
    df.groupby("Month")["CaseNumber"]
    .nunique()
    .reindex(range(1, 13), fill_value=0)
)

month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

print("\nUnique Incidents by Month:")
print(month_incidents.to_string())

plt.figure(figsize=(12, 6))
plt.bar(month_names, month_incidents.values)
plt.xlabel("Month")
plt.ylabel("Unique Incidents")
plt.title("Crime Incidents by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "incidents_by_month.png", dpi=300)
plt.close()

location_incidents = (
    df.groupby("LocationType")["CaseNumber"]
    .nunique()
    .sort_values(ascending=False)
)

print("\nUnique Incidents by Location Type:")
print(location_incidents.to_string())

top_locations = location_incidents.head(10).sort_values(ascending=True)

plt.figure(figsize=(10, 7))
plt.barh(top_locations.index, top_locations.values)
plt.xlabel("Unique Incidents")
plt.ylabel("Location Type")
plt.title("Top 10 Location Types by Crime Incidents")
plt.tight_layout()
plt.savefig(output_dir / "top_10_location_types.png", dpi=300)
plt.close()

top_offenses = (
    df.groupby("Offense")["CaseNumber"]
    .nunique()
    .nlargest(5)
    .index
)

offense_location = (
    df[df["Offense"].isin(top_offenses)]
    .groupby(["LocationType", "Offense"])["CaseNumber"]
    .nunique()
    .reset_index()
)

pivot = offense_location.pivot(
    index="LocationType",
    columns="Offense",
    values="CaseNumber"
).fillna(0)

top_location_rows = (
    pivot.sum(axis=1)
    .nlargest(10)
    .index
)

pivot_top = pivot.loc[top_location_rows]

print("\nTop Location Types for Top 5 Offenses:")
print(pivot_top.to_string())

pivot_top.plot(
    kind="bar",
    figsize=(14, 7)
)

plt.xlabel("Location Type")
plt.ylabel("Unique Incidents")
plt.title("Top 5 Offenses Across Major Location Types")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_dir / "top_offenses_by_location.png", dpi=300)
plt.close()

print("\nContextual analysis complete.")
print(f"Charts saved to: {output_dir}")