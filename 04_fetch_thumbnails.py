# 04_fetch_thumbnails.py
import pandas as pd
import requests
import time

books_df = pd.read_csv("final_books_df.csv")

def fetch_thumbnail(isbn):
    if pd.isna(isbn):
        return "cover-not-found.jpg"
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    headers = {"User-Agent": "BookFetcher/1.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            try:
                return data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
            except (IndexError, KeyError):
                return "cover-not-found.jpg"
        elif response.status_code == 429:
            print("⚠️ Rate limit hit, waiting 30s...")
            time.sleep(30)
            return fetch_thumbnail(isbn)
        else:
            print(f"❌ Error {response.status_code} for ISBN {isbn}")
            return "cover-not-found.jpg"
    except requests.RequestException as e:
        print(f"❌ Request failed for ISBN {isbn}: {e}")
        return "cover-not-found.jpg"

for i, isbn in enumerate(books_df["isbn13"], start=1):
    books_df.at[i-1, "thumbnail"] = fetch_thumbnail(isbn)
    if i % 50 == 0:
        books_df.to_csv("books_with_thumbnails.csv", index=False)
        print(f"💾 Progress saved at {i}/{len(books_df)}")

books_df.to_csv("books_with_thumbnails.csv", index=False)
print("✅ All thumbnails fetched and saved!")

