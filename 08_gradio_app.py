# 08_gradio_app.py
import gradio as gr
from 07_search_pipeline import recommend_books

with gr.Blocks() as demo:
    gr.Markdown("# 📚 Book Recommender")
    with gr.Row():
        user_query = gr.Textbox(label="Enter a description or keyword:", placeholder="e.g., books about magic")
        submit_btn = gr.Button("Find Books")
    output_gallery = gr.Gallery(label="Recommended Books", columns=3, rows=2)

    submit_btn.click(fn=recommend_books, inputs=user_query, outputs=output_gallery)

# Launch interface
demo.launch(server_port=7860, server_name="0.0.0.0")

