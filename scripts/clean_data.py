import pandas as pd

# Load dataset
df = pd.read_csv("dataset/amazon.csv")

# Remove missing values
df = df.dropna()

# Clean discounted_price column
df["discounted_price"] = df["discounted_price"].str.replace("₹", "")
df["discounted_price"] = df["discounted_price"].str.replace(",", "")
df["discounted_price"] = df["discounted_price"].astype(float)

# Clean actual_price column
df["actual_price"] = df["actual_price"].str.replace("₹", "")
df["actual_price"] = df["actual_price"].str.replace(",", "")
df["actual_price"] = df["actual_price"].astype(float)
# Clean discount_percentage column
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "")
df["discount_percentage"] = df["discount_percentage"].astype(float)

# Convert rating column to float
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Check data types again


# Check data types
print(df.dtypes)
# Create new column
df["discount_amount"] = df["actual_price"] - df["discounted_price"]

# Show first 5 rows
print(df[["actual_price", "discounted_price", "discount_amount"]].head())
# Save cleaned dataset
df.to_csv("output/cleaned_amazon.csv", index=False)

print("\nCleaned dataset saved successfully!")