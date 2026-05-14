from rag.retriever import Retriever


class ContextBuilder:

    def __init__(self):

        self.retriever = Retriever()

    def build_context(self, query):

        retrieved_docs = self.retriever.retrieve(query)

        context = "\n".join(retrieved_docs)

        return context