import chromadb
import logging

# Suppress ChromaDB logging
logging.getLogger("chromadb").setLevel(logging.ERROR)

# Initialize ChromaDB persistent storage
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="support_knowledge")

# Load data from text files
def load_data():
    with open("data/products.txt", "r", encoding="utf-8") as f:
        product_data = f.read().split("\n\n")  # Splitting each product block
    
    with open("data/policies.txt", "r", encoding="utf-8") as f:
        policy_data = f.read().split("\n\n")  # Splitting each policy block

    # Add products to ChromaDB
    for i, text in enumerate(product_data):
        collection.add(ids=[f"product_{i}"], documents=[text])

    # Add policies to ChromaDB
    for i, text in enumerate(policy_data):
        collection.add(ids=[f"policy_{i}"], documents=[text])

    print("✅ Data successfully loaded into ChromaDB!")

# Retrieve relevant info based on user query
def retrieve_info(query):
    results = collection.query(query_texts=[query], n_results=1, include=["documents"])
    return results["documents"][0] if results["documents"] else "No relevant info found."

# Run only when script is executed directly
if __name__ == "__main__":
    load_data()
