import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("output/cleaned_amazon.csv")

# Top 10 highest discount products
top_discount = df.sort_values(by="discount_amount", ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10,6))

plt.bar(top_discount["product_name"], top_discount["discount_amount"])

# Labels
plt.xlabel("Product Name")
plt.ylabel("Discount Amount")
plt.title("Top 10 Highest Discount Products")

# Rotate product names
plt.xticks(rotation=90)

# Adjust layout
plt.tight_layout()

# Save graph
plt.savefig("output/top_discount_products.png")

# Show graph
plt.show()
