import pandas as pd
import os

# Load dataset
df = pd.read_csv("../dataset/amazon.csv")

print("DATA LOADED SUCCESSFULLY")
print("\nBEFORE CLEANING:")
print(df[["actual_price", "discounted_price"]].head())

# CLEAN PRICES (IMPORTANT FIX)
df["actual_price"] = (
    df["actual_price"].astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["discounted_price"] = (
    df["discounted_price"].astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Convert to numeric
df["actual_price"] = pd.to_numeric(df["actual_price"], errors="coerce")
df["discounted_price"] = pd.to_numeric(df["discounted_price"], errors="coerce")

# Drop bad rows (VERY IMPORTANT to remove NaN issue)
df = df.dropna(subset=["actual_price", "discounted_price"])

# Create discount column
df["discount_amount"] = df["actual_price"] - df["discounted_price"]

print("\nAFTER CLEANING:")
print(df[["actual_price", "discounted_price", "discount_amount"]].head())

# Create output folder
os.makedirs("../output", exist_ok=True)

# Save file
df.to_csv("../output/cleaned_amazon.csv", index=False)

print("\nCLEANED FILE SAVED SUCCESSFULLY")