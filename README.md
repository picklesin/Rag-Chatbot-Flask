# PDF RAG Chatbot

A conversational AI chatbot that answers questions about uploaded PDF documents using Retrieval-Augmented Generation (RAG). Built with Flask, LangChain, and Google Gemini.

## Features

- Upload PDF documents via a web interface
- Automatically ingests and chunks PDF content into a ChromaDB vector store
- Ask questions about the uploaded PDF through a chat interface
- Answers grounded strictly in document content — no hallucinated facts
- Persistent conversation memory per session using LangGraph

## Tech Stack

- **Backend:** Python, Flask
- **AI / RAG:** LangChain, LangGraph, Google Gemini (gemini-3.5-flash + gemini-embedding-001)
- **Vector Store:** ChromaDB
- **PDF Processing:** PyPDF, LangChain Text Splitters
- **Frontend:** HTML, CSS, Jinja2

## How It Works

1. User uploads a PDF via the home page
2. The PDF is loaded, split into chunks (1000 tokens, 200 overlap), and embedded using Gemini Embeddings
3. Chunks are stored in a ChromaDB vector store
4. User asks a question via the chat interface
5. The RAG agent retrieves the top 5 relevant chunks via similarity search
6. Gemini generates a response grounded in the retrieved context
7. Conversation history is maintained per session using LangGraph's InMemorySaver

## Setup

1. Clone the repository
2. Create a virtual environment and install dependencies:
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file in the root directory:

GOOGLE_API_KEY=your_api_key_here

4. Run the application:
```bash
   flask run
```

## Project Status

Work in progress — frontend styling and additional features under active development.