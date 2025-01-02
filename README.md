# RAGify
Retrieval-Augmented Generation using Local LLM

## Overview
This project demonstrates how to implement Retrieval-Augmented Generation (RAG) using a local language model. It reads PDF documents, splits them into text chunks, creates embeddings with FAISS, retrieves relevant chunks based on semantic similarity, and uses a local LLM (Groq) to generate responses.

## Features
1. **PDF Processing**: Extracts text from any number of PDF documents.
2. **Chunking**: Splits large text into manageable chunks.
3. **Embedding & Indexing**: Generates embeddings for chunks and stores them in an FAISS index.
4. **Semantic Search**: Retrieves the most relevant chunks based on a user query.
5. **LLM Integration**: Routes relevant text chunks into a local Large Language Model to generate a final answer.

## Installation
1. Clone this repository.  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your environment variables by creating a ```.env``` file
   ```bash
   GROQ_API_KEY=<your_groq_api_key>
   ```
## Usage

1. Run the Streamlit app:
```bash
streamlit run main.py
```
2. Upload your PDF documents.
3. Ask questions, and the model will provide answers based on the content of the uploaded documents.

## Contributing
Issues and pull requests are welcome. Feel free to suggest enhancements or report bugs.

## LICENSE
This project is licensed under the MIT License.