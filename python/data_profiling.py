import pandas as pd

df = pd.read_csv("raw/rawdataset.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")
print(df.head())

print("\nUnique Case Numbers:")
print(df["CaseNumber"].nunique())

print("\nDuplicate Case Numbers:")
print(df["CaseNumber"].duplicated().sum())

print("\nMost Common Case Numbers:")
print(df["CaseNumber"].value_counts().head(10))

print("\nDuplicate Rows:")
print(df[df.duplicated(keep=False)].sort_values("CaseNumber").head(20))

print("\nCase Number Format Examples:")
print(df["CaseNumber"].value_counts().tail(20))

print("\nCase Numbers Containing 'Copy':")
print(df[df["CaseNumber"].str.contains("Copy", case=False, na=False)])

print("\nCase Number Lengths:")
print(df["CaseNumber"].str.len().value_counts().sort_index())

print("\nOffenses Per Case:")
print(df.groupby("CaseNumber").size().describe())

print("\nCopy Case Summary:")
print(
    df[df["CaseNumber"].str.contains("Copy", case=False, na=False)]
    [["CaseNumber", "OccurredOn", "Offense", "Offense_IBR_Code", "LocationType", "Division", "Beat", "ReportingArea", "Municipality"]]
    .sort_values(["OccurredOn", "Offense"])
)

print("\nCopy Case Counts:")
print(df[df["CaseNumber"].str.contains("Copy", case=False, na=False)]["CaseNumber"].value_counts())

print("\nDate Range:")
print("Earliest:", df["OccurredOn"].min())
print("Latest:", df["OccurredOn"].max())

print("\nDate Examples:")
print(df["OccurredOn"].head(10).to_string(index=False))

print("\nYear Prefix From Case Number:")
print(df["CaseNumber"].str[:2].value_counts().sort_index())
print("\nUnique Offenses:")
print(df["Offense"].nunique())

print("\nMost Common Offenses:")
print(df["Offense"].value_counts().head(20))

print("\nCrime Against Categories:")
print(df["Offense_IBR_CrimeAgainst"].value_counts(dropna=False))

print("\nOffense Completion:")
print(df["OffenseCompleted"].value_counts())

print("\nUnique IBR Codes:")
print(df["Offense_IBR_Code"].nunique())

print("\nGeographic Variables:")

print("\nDivisions:")
print(df["Division"].value_counts(dropna=False))

print("\nBeats:")
print("Unique:", df["Beat"].nunique())
print(df["Beat"].value_counts(dropna=False).head(20))

print("\nReporting Areas:")
print("Unique:", df["ReportingArea"].nunique())
print(df["ReportingArea"].value_counts(dropna=False).head(20))

print("\nMunicipalities:")
print(df["Municipality"].value_counts(dropna=False))

print("\nPostal Codes:")
print("Unique:", df["PostalCode"].nunique())
print(df["PostalCode"].value_counts(dropna=False).head(20))