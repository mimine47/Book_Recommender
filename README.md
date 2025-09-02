---

````markdown
# 📚 Book Recommender System Using LLMs and Vector Search

An **intelligent book recommendation system** leveraging Large Language Models, vector embeddings, and an interactive UI for semantic search and personalized book discovery.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [References](#references)

---

## Project Overview

This project enables users to enter **natural language queries** (e.g., "books about magic") and receive **highly relevant book recommendations** with thumbnails and metadata. 

It integrates:
- **Falcon-7B-Instruct**: For generating engaging book descriptions.
- **all-MiniLM-L6-v2 embeddings**: For semantic similarity search.
- **Chroma vector database**: For persistent, fast vector search.
- **Gradio**: For an interactive gallery-based frontend.

---

## Features

- Semantic search based on **meaning**, not just keywords.
- Automatic **LLM-generated book descriptions**.
- Persistent **vector search database** using Chroma.
- **Interactive frontend** with thumbnails, title, and author information.
- Batch processing and optimized memory usage for large datasets.

---

## Dataset

- `books_cleaned.csv` → Original metadata (title, authors, ISBN, ratings, publisher, etc.)
- `books_with_descriptions.csv` → LLM-generated book descriptions.
- `books_with_thumbnails.csv` → Added book cover thumbnails from Google Books API.
- `final_books_df.csv` → Final merged dataset for search.

**Metadata Schema:**
| Column | Description |
|--------|-------------|
| bookID | Internal unique ID |
| title | Book title |
| authors | Author(s) |
| average_rating | Average rating |
| isbn | ISBN-10 |
| isbn13 | ISBN-13 |
| language_code | Language |
| num_pages | Page count |
| ratings_count | Number of ratings |
| text_reviews_count | Number of reviews |
| publication_date | Date of publication |
| publisher | Publisher |
| isbn13_title | ISBN13 + Title (merge key) |
| description | LLM-generated short description |
| thumbnail | URL of book cover |

---

## Installation

```bash
# Clone repository
git clone https://github.com/mimine47/book-recommender.git
cd book-recommender

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
````

---

## Usage

### Launch the interactive Gradio app

```bash
python interface.py
```

* Open your browser at `http://localhost:7860`.
* Enter a query like `"fantasy books with magic"` and click **Find Books**.
* Recommended books will appear in a gallery with thumbnails and metadata.

### Example: Search Pipeline

```python
from interface import search_books, db, books_df

query = "books about love"
results_df = search_books(query, db, books_df, k=5)
print(results_df)
```

---

## Code Structure

| Script                     | Purpose                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `generate_descriptions.py` | LLM-based description generation with Falcon-7B-Instruct    |
| `merge_metadata.py`        | Merge original book metadata with generated descriptions    |
| `chunk_text.py`            | Split descriptions into overlapping chunks for embeddings   |
| `create_vector_db.py`      | Generate embeddings and persist vector database with Chroma |
| `fetch_thumbnails.py`      | Download book cover thumbnails via Google Books API         |
| `search_pipeline.py`       | Combines vector search with metadata lookup                 |
| `interface.py`             | Interactive Gradio frontend for recommendations             |

---

## Future Improvements

* Parallelize description generation for speed.
* Add caching for API calls.
* Implement collaborative filtering with content-based recommendations.
* Advanced filtering: language, rating, publication date.
* Mobile-responsive interface.
* Scalability: distributed embedding computation, database partitioning, load balancing.

---

## Author

**Mohamed Amine Mammar El Hadj**

Deep Learning Developer & Software Developer with experience in vector search and AI applications.

* [LinkedIn](https://www.linkedin.com/in/mohamed-amine-mammar-el-hadj-715a41295)
* [GitHub](https://github.com/mimine47)
* Email: [mohamedamine.devtech@gmail.com](mailto:mohamedamine.devtech@gmail.com)

---

## References

1. Falcon-7B-Instruct Model Documentation, Technology Innovation Institute
2. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks, Reimers & Gurevych, 2019
3. LangChain: Building Applications with LLMs, Harrison Chase et al.
4. Chroma: Open-source embedding database documentation
5. Google Books API Documentation, Google Developers

---

```

---

