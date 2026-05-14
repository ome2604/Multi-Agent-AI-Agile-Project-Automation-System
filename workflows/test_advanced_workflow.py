from workflows.advanced_workflow import AdvancedWorkflow


workflow = AdvancedWorkflow()

result = workflow.execute(
    "Build an AI-powered project management platform."
)

print("\nFINAL WORKFLOW OUTPUT:\n")

print(result)