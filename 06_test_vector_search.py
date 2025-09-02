# 06_test_vector_search.py
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding_fn = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma(
    persist_directory="books_chroma_db",
    embedding_function=embedding_fn
)

query = "books about magic"
results = db.similarity_search(query, k=5)

for r in results:
    print(f"ISBN: {r.metadata['isbn13']}, Chunk: {r.metadata['chunk_id']}")
    print(r.page_content[:200], "\n")

