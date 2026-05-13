from orchestrator.workflow_manager import WorkflowManager

workflow = WorkflowManager()

result = workflow.execute_workflow(
    "Build an AI-powered ecommerce platform"
)

print("\n===== FINAL MULTI-AGENT OUTPUT =====\n")

for key, value in result.items():

    print(f"\n===== {key.upper()} =====\n")

    print(value)