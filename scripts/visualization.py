import pandas as pd
import os

# Load dataset
df = pd.read_csv("../dataset/amazon.csv")

print("DATA LOADED SUCCESSFULLY")

# Clean price columns (VERY IMPORTANT)
df["actual_price"] = (
    df["actual_price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["discounted_price"] = (
    df["discounted_price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert to numeric
df["actual_price"] = pd.to_numeric(df["actual_price"], errors="coerce")
df["discounted_price"] = pd.to_numeric(df["discounted_price"], errors="coerce")

# Create discount column
df["discount_amount"] = df["actual_price"] - df["discounted_price"]

# Preview
print("\nFIRST 5 ROWS:")
print(df[["actual_price", "discounted_price", "discount_amount"]].head())

# Create output folder safely
os.makedirs("../output", exist_ok=True)

# Save file
output_path = "../output/cleaned_amazon.csv"
df.to_csv(output_path, index=False)

print("\nCLEANED FILE SAVED AT:", output_path)