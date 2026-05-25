import pandas as pd

# Load CLEANED dataset (IMPORTANT)
df = pd.read_csv("../output/cleaned_amazon.csv")

# Ensure numeric conversion (safety)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["discount_amount"] = pd.to_numeric(df["discount_amount"], errors="coerce")

print("Dataset Shape:")
print(df.shape)

# Average rating
print("\nAverage Product Rating:")
print(df["rating"].mean())

# Top rated products
print("\nTop 5 Highest Rated Products:")
top_rated = df.sort_values(by="rating", ascending=False)

print(top_rated[["product_name", "rating"]].head())

# Fix NaN issue for discount sorting
print("\nTop 5 Highest Discount Products:")
top_discount = df.sort_values(by="discount_amount", ascending=False)

print(top_discount[["product_name", "discount_amount"]].head())