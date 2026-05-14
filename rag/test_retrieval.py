from rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What are the sprint risks?"
)

print("\nRetrieved Context:\n")

for result in results:

    print(result)
    print("\n-----------------\n")