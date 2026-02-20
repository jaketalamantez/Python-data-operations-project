import pandas as pd

df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna("UNKNOWN")

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Basic validation
print("Rows:", len(df))
print("Missing values:\n", df.isnull().sum())

# Save outputs
df.to_csv("clean_data.csv", index=False)
df.to_json("clean_data.json", orient="records", indent=2)

print("Cleaning complete.")