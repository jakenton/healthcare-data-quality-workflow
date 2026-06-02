"""
01_inject_data_quality_issues.py

Purpose: Create a realistic messy healthcare operations dataset from the original Kaggle healthcare dataset.

Why this matters: Real healthcare analytics work often begins with data that is not ready for reporting. Analysts commonly need to identify and fix
    - Missing values
    - Duplicate records
    - Inconsistent naming conventions
    - Extra spaces
    - Missing financial values

Input: data/raw/healthcare_dataset.csv

Output: data/messy/healthcare_dataset_messy.csv
"""

# %%
# Import pandas for working with tabular data.
# Import numpy for random selection of rows.

from pathlib import Path

import numpy as np
import pandas as pd

# %%
# -------------------------------------------------------------------------
# Set a random seed so the messy dataset is reproducible.
# This means the same rows will be modified each time the script runs.
# -------------------------------------------------------------------------

np.random.seed(42)

# %%
# -------------------------------------------------------------------------
# Define file paths.
# Path(__file__) means "start from the location of this Python script."
# .parents[1] moves up one folder to the main project folder.
# -------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parents[1]

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "healthcare_dataset.csv"
MESSY_FILE = PROJECT_ROOT / "data" / "raw" / "healthcare_dataset_messy.csv"

# %%
# -------------------------------------------------------------------------
# Load the raw healthcare dataset.
# -------------------------------------------------------------------------

df = pd.read_csv(RAW_FILE)

print("Raw dataset loaded successfully!")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

# %%
# -------------------------------------------------------------------------
# Create a copy of the raw dataset.
# The copy will be modified, not the original
# -------------------------------------------------------------------------

messy_df = df.copy()

# %%
# ------------------------------------------------------------------------------------------
# Helper function: Select a random set of row indexes base on a perfcentage of the dataset
# ------------------------------------------------------------------------------------------

def get_random_indexes(dataframe, percent):
    """
    Select random row indexes from a dataframe.

    Parameters:
        dataframe:
            The dataframe rows are selected from.

        percent:
            The percentage of rows to select.
            Example: 0.03 means 3%.
    
    Returns:
        A list of randomly selected row indexes.
    """

    row_count = len(dataframe)
    sample_size = int(row_count * percent)

    return np.random.choice(
        dataframe.index,
        size=sample_size,
        replace=False
    )

# %%
# --------------------------------------------------------------------------------------------------
# Issue 1: Missing Doctor values
# Real-world reason: A provider may be unassigned, missing from an export, or not mapped correctly.
# --------------------------------------------------------------------------------------------------

missing_doctor_indexes = get_random_indexes(messy_df, 0.03)

messy_df.loc[missing_doctor_indexes, "Doctor"] = np.nan

print(f"Missing Doctor values added: {len(missing_doctor_indexes):,}")

# %%
# --------------------------------------------------------------------------------------------------
# Issue 2: Missing Hospital values
# Real-world reason: Facility information may be missing during multi-site data aggregation.
# --------------------------------------------------------------------------------------------------

missing_hospital_indexes = get_random_indexes(messy_df, 0.02)

messy_df.loc[missing_hospital_indexes, "Hospital"] = np.nan

print(f"Missing Hospital values added: {len(missing_hospital_indexes):,}")

# %%
# --------------------------------------------------------------------------------------------------
# Issue 3: Hospital naming variations
# Real-world reason: The same facility may appear with slightly different names across systems.
# --------------------------------------------------------------------------------------------------

hospital_variation_indexes = get_random_indexes(messy_df, 0.05)

for idx in hospital_variation_indexes:
        hospital = messy_df.loc[idx, "Hospital"]

        if pd.notna(hospital):
              variation_type = np.random.choice(["upper", "inc", "comma_inc"])

              if variation_type == "upper":
                    messy_df.loc[idx, "Hospital"] = hospital.upper()

              elif variation_type == "inc":
                    messy_df.loc[idx, "Hospital"] = hospital.replace("Inc", "Incorporated")
                
              elif variation_type == "comma_inc":
                    messy_df.loc[idx, "Hospital"] = hospital.replace("Inc", "Inc.")

print(f"Hospital naming variations added: {len(hospital_variation_indexes):,}")

# %%
# --------------------------------------------------------------------------------------------------
# Issue 4: Insurance Provider variations
# Real-world reason: Insurance names are often entered differently across systems or departments.
# --------------------------------------------------------------------------------------------------

insurance_variation_indexes = get_random_indexes(messy_df, 0.05)

insurance_variations = {
      "UnitedHealthcare": ["UNITEDHEALTHCARE", "United Healthcare", "UHC"],
      "Blue Cross": ["BLUE CROSS", "blue cross", "BlueCross"],
      "Aetna": ["AETNA", "aetna"],
      "Cigna": ["CIGNA", "cigna"],
      "Medicare": ["MEDICARE", "medicare"]
}

for idx in insurance_variation_indexes:
      insurer = messy_df.loc[idx, "Insurance Provider"]

      if insurer in insurance_variations:
            messy_df.loc[idx, "Insurance Provider"] = np.random.choice(
                  insurance_variations[insurer]
            )

print(f"Insurance Provider variations added: {len(insurance_variation_indexes):,}")
                                              
                                              
                                              # %%
# --------------------------------------------------------------------------------------------------
# Issue 5: Leading and trailing spaces
# Real-world reason: Extra spaces commonly appear in exported text fields and can break matching.
# --------------------------------------------------------------------------------------------------

space_indexes = get_random_indexes(messy_df, 0.05)

space_columns = ["Insurance Provider", "Admission Type", "Test Results"]

for idx in space_indexes:
      column = np.random.choice(spaces_columns)
      value = messy_df.loc[idx, column]

      if pd.notna(value):
            messy_df.loc[idx, column] = "f {value} "

print(f"Leading/trailing spaces added: {len(space_indexes):,}")

# ----------------------------------------------------------------------------------------------
# Issue 6: Missing Billing Amount values
# Real-world reason: Billing fields may be black if charges are pending or failed to export.
# # --------------------------------------------------------------------------------------------

missing_billing_indexes = get_random_indexes(messy_df, 0.01)

messy_df.loc[missing_billing_indexes, "Billing Amount"] = np.nan

print(f"Missing Billing Amount values added: {len(missing_billing_indexes):,}")

# ----------------------------------------------------------------------------------------------------
# Issue 7: Duplicate records
# Real-world reason: Duplicate records can appear when exports are combined or accidentally appended.
# ----------------------------------------------------------------------------------------------------

duplicate_indexes = get_random_indexes(messy_df, 0.02)

duplicate_rows = messy_df.loc[duplicate_indexes].copy()

messy_df = pd.concat(
      [messy_df, duplicate_rows],
      ignore_index=True
)

print(f"Duplicate records added: {len(duplicate_rows):,}")

# %%
# Save the messy dataset.

MESSY_FILE.parent.mkdir(parents=True, exist_ok=True)

messy_df.to_csv(MESSY_FILE, index= False)

print("Messy dataset saved successfully!")
print(f"Output file: {MESSY_FILE}")
print(f"Final rows: {messy_df.shape[0]:,}")
print(f"Final columns: {messy_df.shape[1]:,}")

# %%
# Create a simple summary of the injected issues

summary = {
      "Original Rows": len(df),
      "Final Rows After Duplicates": len(messy_df),
      "Missing Doctor Added": len(missing_doctor_indexes),
      "Missing Hospital Added": len(missing_hospital_indexes),
      "Hospital Naming Variations Added": len(hospital_variation_indexes),
      "Insurance Provder Variations Added": len(insurance_variation_indexes),
      "Rows With Extra Spaces Added": len(space_indexes),
      "Missing Billing Amount Added": len(missing_billing_indexes),
      "Duplicate Records Added": len(duplicate_rows)
}

summary_df = pd.DataFrame(
      summary.items(),
      columns=["Data Quality Issue," "Count"]
)

print(summary_df)