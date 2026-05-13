from typing import TypedDict
from langgraph.graph import StateGraph, END

class GraphState(TypedDict):
    message: str

def node_function(state):
    print("Processing:", state["message"])
    return state

workflow = StateGraph(GraphState)

workflow.add_node("start_node", node_function)

workflow.set_entry_point("start_node")

workflow.add_edge("start_node", END)

app = workflow.compile()

result = app.invoke({
    "message": "Enterprise AI Workflow Running"
})

print(result)