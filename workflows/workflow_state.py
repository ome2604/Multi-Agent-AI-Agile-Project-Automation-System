from typing import TypedDict


class WorkflowState(TypedDict):

    user_input: str

    project_plan: str

    risks: str

    resources: str

    scrum_updates: str

    report: str

    context: str