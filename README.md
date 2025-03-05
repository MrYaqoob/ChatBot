# Customer Support AI Agent

## Overview

This project is a simple Customer Support AI Agent that answers e-commerce-related questions using Retrieval-Augmented Generation (RAG). It retrieves relevant information from a knowledge base and generates accurate responses using the Cohere API.

## Approach

### Data Storage & Retrieval

- The knowledge base (product details & company policies) is stored in ChromaDB, a vector database.
- When a user asks a question, we use semantic search to find the most relevant document.

### Retrieval-Augmented Generation (RAG)

- The retrieved information is combined with the user’s query.
- This augmented prompt is sent to Cohere’s LLM, ensuring the response is based on actual company knowledge.

### Response Generation

- The AI generates a clear and accurate answer using the Cohere API.
- The chatbot runs in a command-line interface (CLI) for user interaction.

### Setup Instructions

- Install Dependencies
- Make sure you have Python installed. Then, install the required libraries: pip install cohere chromadb

### Load Knowledge Base into ChromaDB

- Before running the chatbot, load product and policy data into ChromaDB: python retriever.py

### Run the Chatbot

- Start the AI agent, type in CMD: python main.py
- Then, ask questions like: "How much is the iPhone 15 Pro?" & "What are your shipping options?"

## Example Conversations

🤖 Welcome to the Customer Support AI!

(For user)
Ask a question (or type 'exit' to quit): what is the price of sony headphones? and what is the shipping policies for that?

🤖 AI Response: The Sony WH-1000XM5 Headphones are currently priced at $399. Great choice! Regarding shipping policies, these headphones are currently in stock and ready to be shipped. Please ensure you verify the shipping address carefully and choose the appropriate shipping method preferred time frame. Unfortunately, I cannot provide specific information regarding shipping costs as it varies according to the destination and depends on the courier company. Therefore, it would be best to proceed to the checkout stage to receive more detailed shipping information. Feel free

## Technologies Used

- Python (Primary language)
- Cohere API (LLM for response generation)
- ChromaDB (Vector storage for retrieval)
- Command-Line Interface (CLI) (User interaction)

## Future Improvements

- Improve response formatting.
- Retrieve multiple relevant documents for better context.
- Deploy as a web API instead of CLI.
