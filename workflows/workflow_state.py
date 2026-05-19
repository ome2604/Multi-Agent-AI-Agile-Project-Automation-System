from typing import TypedDict


class WorkflowState(TypedDict):

    user_input: str

    retrieved_context: str

    project_plan: str

    risks: str

    resources: str

    scrum_updates: str

    report: str

    short_memory: dict

    long_memory: dict

    tool_outputs: dict