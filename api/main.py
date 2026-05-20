from fastapi import FastAPI
from orchestrator.workflow_manager import WorkflowManager
import asyncio

app = FastAPI()

workflow = WorkflowManager()


@app.get("/")
def home():

    return {
        "status": "Enterprise AI System Running"
    }


@app.post("/execute")
async def execute_workflow(request: dict):

    result = await workflow.execute_workflow(
        request["goal"]
    )

    return result