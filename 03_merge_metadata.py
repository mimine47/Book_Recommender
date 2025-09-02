# 03_merge_metadata.py
import pandas as pd

books = pd.read_csv("/content/books_cleaned.csv")
descriptions = pd.read_csv("/content/books_with_descriptions.csv")

# Merge on isbn13_title
final_books_df = books.merge(
    descriptions,
    on="isbn13_title",
    how='inner'
)

final_books_df.to_csv("final_books_df.csv", index=False)
print("✅ Metadata merged with descriptions.")

