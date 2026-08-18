## Project Status

Work in progress — additional features under active development.

**Live Demo:** [RAG Chatbot](https://rag-chatbot-szco.onrender.com)

## Screenshot
<img width="1710" height="863" alt="Screenshot 2026-07-19 at 7 25 44 PM" src="https://github.com/user-attachments/assets/cca78716-1f43-45a4-9a09-1f87d50eeea7" />

## PDF RAG Chatbot

A conversational AI chatbot that answers questions about uploaded PDF documents using Retrieval-Augmented Generation (RAG). Built with Flask, LangChain, and Google Gemini.

## Credits
Frontend template adapted from [autochat-bot](https://github.com/paramsgit/autochat-bot) by paramsgit (MIT License)

## Features

- Upload PDF documents via a web interface
- Automatically ingests and chunks PDF content into a pgvector vector store
- Ask questions about the uploaded PDF through a chat interface
- Answers grounded strictly in document content — no hallucinated facts
- Persistent conversation memory per session using LangGraph

## Tech Stack

- **Backend:** Python, Flask
- **AI / RAG:** LangChain, LangGraph, Google Gemini (gemini-3.5-flash + gemini-embedding-001)
- **Vector Store:** pgvector
- **PDF Processing:** PyPDF, LangChain Text Splitters
- **Frontend:** HTML, CSS, Jinja2

## How It Works

1. User uploads a PDF via the home page
2. The PDF is loaded, split into chunks (1000 tokens, 200 overlap), and embedded using Gemini Embeddings
3. Chunks are stored in a pgvector vector store
4. User asks a question via the chat interface
5. The RAG agent retrieves the top 5 relevant chunks via similarity search
6. Gemini generates a response grounded in the retrieved context
7. Conversation history is maintained per session using LangGraph's InMemorySaver


