# Customer Support AI Agent - Setup & Usage Guide

## Before setting up the AI agent, ensure you have the following:

- Python 3.8+ installed on your system
- Cohere API key (Sign up at https://cohere.com if you don’t have one)
- ChromaDB and required Python libraries installed

### Step 1: Clone or Extract the Project

- If you received a ZIP file, extract it to your preferred directory.
- If using GitHub, clone the repository:

`git clone <repository-url>`
`cd customer-support-ai`

### Step 2: Install Dependencies

- Ensure you have Python installed. Then, run the following command to install the required libraries:

` pip install cohere chromadb `

###  Step 3: Obtain and Configure Your Cohere API Key

- Sign up for Cohere: Visit Cohere's website. Create an account (free tier is available). Generate an API key from the Cohere Dashboard.
- Update agent.py: Open agent.py in a text editor.
Locate this line:
`COHERE_API_KEY = "api_key"`
Replace `api_key` with your actual Cohere API Key.
- Save the file.

### Step 4: Load Knowledge Base into ChromaDB
-Before running the chatbot, we need to store the product and policy data in ChromaDB (type this in CMD: `python retriever.py`)

You should see:

✅ Data successfully loaded into ChromaDB!
#### This means the knowledge base is ready.

### Step 5: Run the Chatbot

- Start the AI agent using(CMD): `python main.py`

You will see:
`🤖 Ask a question (or type 'exit' to quit):`

#### Now, you can ask questions like:

`"How much is the iPhone 15 Pro?"`
`"What are your shipping options?"`

#### To exit the chatbot, type: `exit`


# 🎉 Your AI Agent is ready! If you need help, feel free to reach out. 🚀

