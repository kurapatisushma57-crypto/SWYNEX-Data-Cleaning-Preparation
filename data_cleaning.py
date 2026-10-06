import pandas as pd

# Column names
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

# Load dataset
df = pd.read_csv (  
  "data/adult_dataset/adult.data",
    names=columns,
    skipinitialspace=True,
    na_values="?"
)

 # Handle missing values
categorical_columns = [
    "workclass",
    "occupation",
    "native_country"
]

for column in categorical_columns:
    df[column] = df[column].fillna("Unknown")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Show number of rows and columns
print("\nRows and columns:")
print(df.shape)

# Show column names
print("\nColumn names:")
print(df.columns)
# show missing values
print("\nMissing values:")
print(df.isnull().sum())
# after cleaning missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())
# Check duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())
# Remove duplicate records
df = df.drop_duplicates()
print("\nDuplicate records after cleaning:")
print(df.duplicated().sum())
# Check unique values in workclass
print("\nWorkclass values:")
print(df["workclass"].unique())
# Check unique education values
print("\nEducation values:")
print(df["education"].unique())
# Check data types
print("\nData types:")
print(df.dtypes)
# Final data quality check
print("\nFinal missing values:")
print(df.isnull().sum())

print("\nFinal duplicate count:")
print(df.duplicated().sum())
# Save cleaned dataset
output_file = "data/cleaned_dataset.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)