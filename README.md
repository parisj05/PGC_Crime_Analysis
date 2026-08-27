# Prince George's County Crime Incident Analysis

## What Changed. Where. Why.

A decision-oriented crime analysis project examining incident patterns across Prince George's County, Maryland.

**Audience:** Police Department Crime & Safety Analysts  
**Geographic Scope:** Prince George's County, Maryland  
**Time Period:** August 18, 2024 – August 16, 2026  
**Focus:** Crime Incident Patterns

## Main Question

How do crime incident patterns vary across Prince George's County, and what trends could help identify public-safety needs?

This analysis focuses on:

- What changed?
- Where did it change?
- What types of incidents are driving the change?

## Analysis

### 1. Time & Offense

Examines how crime incidents and offense types change over time.

- Monthly incident volume
- Offense frequency
- Top offense types
- Monthly offense trends
- Unusual increases or decreases
- Day-of-week patterns
- Time-of-day patterns

### 2. Geography

Examines where incidents are concentrated across Prince George's County.

- Police Division
- Beat
- Reporting Area
- Municipality
- ZIP Code
- Geographic concentration
- Interactive dashboard visualizations

### 3. Context

Examines the circumstances surrounding reported incidents.

- Time of day
- Day of week
- Month
- Location type
- Offense type by location
- Person vs. property crimes
- Completed vs. attempted offenses

## Key Findings So Far

The cleaned dataset contains **48,501 records** representing crime incidents across the study period.

The largest offense categories are:

1. Theft from Auto
2. Other Theft
3. Stolen Vehicle
4. Assault (No Weapon)
5. DV Assault (No Weapon)

Property-related incidents account for the majority of records.

Crime activity also varies substantially by:

- Month
- Hour
- Police division
- Municipality
- Beat
- Reporting area
- Location type

The analysis is designed to identify patterns that may help prioritize public-safety resources and further investigation.

## Dataset

The original dataset contained:

- **50,095 records**
- **13 variables**
- **19 offense types**
- **19 IBR codes**
- **9 police divisions**
- **128 beats**
- **491 reporting areas**
- **26 municipalities**
- **54 ZIP codes**

### Important Variables

| Variable | Description |
|---|---|
| `CaseNumber` | Incident identifier |
| `OccurredOn` | Date and time of incident |
| `Offense` | Type of offense |
| `Offense_IBR_Code` | Standardized offense classification |
| `Offense_IBR_CrimeAgainst` | Person or property classification |
| `OffenseCompleted` | Whether the offense was completed |
| `LocationType` | Location where the incident occurred |
| `ReportingAgency` | Reporting agency |
| `PostalCode` | ZIP code |
| `Division` | Police division |
| `Beat` | Police beat |
| `ReportingArea` | Police reporting area |
| `Municipality` | Municipality |

## Data Preparation

The dataset was profiled and cleaned using Python.

### Duplicate Records

The raw dataset contained **1,594 exact duplicate rows**.

After removal:

**50,095 → 48,501 records**

Repeated `CaseNumber` values were retained because a single case can contain multiple offense records.

### Date Cleaning

`OccurredOn` was converted from text to a datetime field.

Additional analytical variables were created:

- `Year`
- `Month`
- `MonthName`
- `DayOfWeek`
- `Hour`

All original date values successfully converted.

### Case Number Validation

The dataset contained 16 malformed case numbers such as:

- `Copy of 24`
- `Copy of 25`
- `Copy of 26`

After duplicate removal, 11 remained.

These records were retained because they contained usable analytical information. A `ValidCaseNumber` field identifies standard versus malformed case numbers.

### Missing Data

Missing geographic and classification values were identified rather than automatically removed.

The largest missing-data issue was `ReportingArea`.

Original missing values included:

- `ReportingArea`: 3,192
- `PostalCode`: 102
- `Beat`: 1
- `Offense_IBR_CrimeAgainst`: 61

Most missing `ReportingArea` values occurred in **Division II**, indicating that missing geographic information is concentrated rather than evenly distributed.

## Project Structure

```text
PGC_Crime_Analysis/
│
├── index.html
├── style.css
│
├── python/
│   ├── data_profiling.py
│   ├── data_cleaning.py
│   ├── sq1_time_offense.py
│   ├── sq2_geography.py
│   └── sq3_context.py
│
├── cleaned/
│   └── cleandata.csv
│
├── raw/
│   └── original dataset
│
├── visualizations/
│   ├── sq1_time_offense/
│   ├── sq2_geography/
│   └── sq3_context/
│
└── README.md
