from rag.context_builder import ContextBuilder

builder = ContextBuilder()

context = builder.build_context(
    "What are the major project risks?"
)

print("\nGenerated Context:\n")

print(context)