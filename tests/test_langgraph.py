from workflows.advanced_workflow import AdvancedWorkflow

workflow = AdvancedWorkflow()

result = workflow.execute(
    "Build an AI-powered ecommerce platform"
)

print("\n===== LANGGRAPH WORKFLOW OUTPUT =====\n")

print(result)