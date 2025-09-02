# 02_generate_descriptions.py
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from tqdm import tqdm

# Load books subset
books = pd.read_csv("books_subset.csv")
books_list = books["isbn13_title"].tolist()

# Load Falcon-7B-Instruct model
model_name = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.bfloat16
)
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto"
)

def generate_book_description(book_info, max_new_tokens=100):
    prompt = f"Write a short, engaging description for the book: {book_info}"
    sequences = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    return sequences[0]["generated_text"]

# Generate descriptions in batches
results = []
batch_size = 500

for start in tqdm(range(0, len(books_list), batch_size), desc="Batches"):
    batch = books_list[start:start + batch_size]
    for book in tqdm(batch, desc=f"Books {start+1}-{start+len(batch)}"):
        desc_text = generate_book_description(book, max_new_tokens=100)
        results.append({"isbn13_title": book, "description": desc_text})

# Save final descriptions
desc_df = pd.DataFrame(results)
desc_df.to_csv("books_with_descriptions.csv", index=False)
print("✅ Descriptions saved.")

