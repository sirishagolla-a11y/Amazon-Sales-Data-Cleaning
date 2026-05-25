import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_amazon.csv")

# Basic dataset info
print("Dataset Shape:")
print(df.shape)

# Average rating
print("\nAverage Product Rating:")
print(df["rating"].mean())

# Highest rated products
print("\nTop 5 Highest Rated Products:")
top_rated = df.sort_values(by="rating", ascending=False)

print(top_rated[["product_name", "rating"]].head())

# Products with highest discounts
print("\nTop 5 Highest Discount Products:")
top_discount = df.sort_values(by="discount_amount", ascending=False)

print(top_discount[["product_name", "discount_amount"]].head())