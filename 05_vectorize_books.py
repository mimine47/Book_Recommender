# 05_vectorize_books.py
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

books_df = pd.read_csv("books_with_thumbnails.csv")

description = books_df["description"].tolist()
isbns = books_df["isbn13"].tolist()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30,
    length_function=len
)

docs = []
for isbn, desc in zip(isbns, description):
    chunks = splitter.split_text(desc)
    for i, chunk in enumerate(chunks):
        docs.append({"isbn13": isbn, "chunk_id": i, "text": chunk})

# Create embeddings
embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
documents = [Document(page_content=doc["text"], metadata={"isbn13": doc["isbn13"], "chunk_id": doc["chunk_id"]}) for doc in docs]

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_fn,
    persist_directory="books_chroma_db"
)
vector_db.persist()
print("✅ Vector database created and persisted.")

