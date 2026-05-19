import asyncio

from orchestrator.workflow_manager import WorkflowManager

from monitoring.workflow_analytics import WorkflowAnalytics


async def main():

    workflow = WorkflowManager()

    result = await workflow.execute_workflow(
        "Build an AI-powered ecommerce platform"
    )

    analytics = WorkflowAnalytics()

    analytics.generate_summary(result)

    print("\n===== ENTERPRISE WORKFLOW OUTPUT =====\n")

    for key, value in result.items():

        print(f"\n===== {key.upper()} =====\n")

        print(value)


asyncio.run(main())