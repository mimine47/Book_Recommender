# 01_prepare_books.py
import pandas as pd

# Load cleaned books dataset
books = pd.read_csv("/content/books_cleaned.csv")

# Select a subset for initial processing
books_list = books["isbn13_title"].tolist()[:2000]

# Save this subset if needed
pd.DataFrame(books_list, columns=["isbn13_title"]).to_csv("books_subset.csv", index=False)
print("✅ Books subset saved.")

