# 07_search_pipeline.py
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load books with thumbnails
books_df = pd.read_csv("books_with_thumbnails.csv")

embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="books_chroma_db", embedding_function=embedding_fn)

def search_books(query: str, k: int = 10):
    results = db.similarity_search(query, k=k)
    matched_books = []
    for r in results:
        isbn = r.metadata.get("isbn13", None)
        if isbn:
            try:
                match = books_df[books_df["isbn13"] == int(isbn)]
            except ValueError:
                match = books_df[books_df["isbn13"].astype(str) == str(isbn)]
            if not match.empty:
                for _, row in match.iterrows():
                    matched_books.append(row.to_dict())
    return pd.DataFrame(matched_books)

def recommend_books(query):
    df = search_books(query)
    gallery_items = []
    for _, row in df.iterrows():
        caption = f"{row['title']} by {row['authors']}"
        gallery_items.append((row['thumbnail'], caption))
    return gallery_items

