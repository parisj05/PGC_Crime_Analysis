import pandas as pd

df = pd.read_csv("raw/rawdataset.csv")

df["OccurredOn"] = pd.to_datetime(df["OccurredOn"])
df["Year"] = df["OccurredOn"].dt.year
df["Month"] = df["OccurredOn"].dt.month
df["MonthName"] = df["OccurredOn"].dt.month_name()
df["DayOfWeek"] = df["OccurredOn"].dt.day_name()
df["Hour"] = df["OccurredOn"].dt.hour
print(df[["OccurredOn", "Year", "Month", "MonthName", "DayOfWeek", "Hour"]].head())
print(df["OccurredOn"].dtype)
print(df["OccurredOn"].head())
print(df["OccurredOn"].isna().sum())

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Rows before removing exact duplicates:", before)
print("Rows after removing exact duplicates:", after)
print("Exact duplicates removed:", before - after)

copy_cases = df[df["CaseNumber"].str.contains("Copy", case=False, na=False)]

print("Copy Case Records Remaining:", len(copy_cases))
print(copy_cases[["CaseNumber", "OccurredOn", "Offense", "Offense_IBR_Code", "LocationType",
                  "Division", "Beat", "ReportingArea", "Municipality"]].to_string(index=False))
df["ValidCaseNumber"] = df["CaseNumber"].str.match(r"^\d{2}-\d{7}$")

print("\nCaseNumber Validation:")
print(df["ValidCaseNumber"].value_counts())
print("\nInvalid CaseNumbers:")
print(df.loc[~df["ValidCaseNumber"], "CaseNumber"].value_counts())
print("\nMissing Values After Duplicate Removal:")
print(df.isnull().sum())

print("\nMissing ReportingArea by Division:")
print(df[df["ReportingArea"].isna()]["Division"].value_counts())

print("\nMissing PostalCode by Division:")
print(df[df["PostalCode"].isna()]["Division"].value_counts())

print("\nMissing Beat by Division:")
print(df[df["Beat"].isna()]["Division"].value_counts())



print("\nDivision Values:")
print(df["Division"].unique())

print("\nMunicipality Values:")
print(df["Municipality"].unique())

print("\nOffense Crime Against Missing:")
print(df[df["Offense_IBR_CrimeAgainst"].isna()][["Offense", "Offense_IBR_Code"]].value_counts())

print("\nBeat Missing Record:")
print(df[df["Beat"].isna()])


print("\nActual Minimum Date:")
print(df["OccurredOn"].min())

print("\nActual Maximum Date:")
print(df["OccurredOn"].max())

print("\nLatest 20 Records:")
print(df[["CaseNumber", "OccurredOn", "Offense"]].sort_values("OccurredOn", ascending=False).head(20).to_string(index=False))

df["Offense_IBR_CrimeAgainst"] = df["Offense_IBR_CrimeAgainst"].fillna("Unknown")

print("\nCrime Against Values After Cleaning:")
print(df["Offense_IBR_CrimeAgainst"].value_counts())

df["PostalCode"] = df["PostalCode"].astype("Int64")
df["ReportingArea"] = df["ReportingArea"].astype("Int64")

print("\nGeographic Data Types:")
print(df[["PostalCode", "ReportingArea"]].dtypes)

print("\nGeographic Missing Values:")
print(df[["PostalCode", "Beat", "ReportingArea"]].isna().sum())


print("\nOffense Values:")
print(df["Offense"].value_counts())

print("\nCrime Against Values:")
print(df["Offense_IBR_CrimeAgainst"].value_counts())

print("\nCompletion Values:")
print(df["OffenseCompleted"].value_counts())

print("\nDivision Values:")
print(df["Division"].value_counts())

print("\nMunicipality Values:")
print(df["Municipality"].value_counts())

print("\nFinal Dataset Shape:")
print(df.shape)

output_path = "cleaned/cleandata.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved to:", output_path)