import cohere
import os
from retriever import retrieve_info

# Initialize Cohere with your API key
COHERE_API_KEY = "api_key"  # Replace with your actual key
co = cohere.Client(COHERE_API_KEY)

# Generate AI response using retrieved info
def generate_response(user_query):
    retrieved_info = retrieve_info(user_query)

    prompt = f"""
    You are a helpful customer support assistant. 
    Answer the user's question based on the following retrieved information:

    Retrieved Info: {retrieved_info}
    User Question: {user_query}

    Response:
    """

    response = co.generate(
        model="command",  # Cohere’s model for conversational AI
        prompt=prompt,
        max_tokens=300,  # Maximum number of tokens to generate
    )

    return response.generations[0].text.strip()

# Run test query if executed directly
if __name__ == "__main__":
    while True:
        query = input("Ask a question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print("\n🤖 AI Response:", generate_response(query), "\n")

def chat():
    while True:
        user_input = input("Ask a question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break
        response = generate_response(user_input)  # Ensure this function exists
        print(f"\n🤖 AI Response: {response}\n")

