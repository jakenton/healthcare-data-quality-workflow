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
