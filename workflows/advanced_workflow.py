from langgraph.graph import StateGraph, END

from workflows.workflow_state import WorkflowState

from agents.planning_agent import PlanningAgent
from agents.risk_agent import RiskAgent
from agents.resource_agent import ResourceAgent
from agents.scrum_agent import ScrumAgent
from agents.report_agent import ReportAgent


class AdvancedWorkflow:

    def __init__(self):

        self.planning_agent = PlanningAgent()

        self.risk_agent = RiskAgent()

        self.resource_agent = ResourceAgent()

        self.scrum_agent = ScrumAgent()

        self.report_agent = ReportAgent()

        self.graph = StateGraph(WorkflowState)

        self.build_graph()

    def planning_node(self, state):

        result = self.planning_agent.generate_plan(
            state["user_input"]
        )

        state["project_plan"] = result

        return state

    def risk_node(self, state):

        result = self.risk_agent.analyze_risks(
            state["project_plan"]
        )

        state["risks"] = result

        return state

    def resource_node(self, state):

        result = self.resource_agent.allocate_resources(
            state["project_plan"]
        )

        state["resources"] = result

        return state

    def scrum_node(self, state):

        result = self.scrum_agent.generate_standup(
            state["project_plan"]
        )

        state["scrum_updates"] = result

        return state

    def report_node(self, state):

        result = self.report_agent.generate_report(
            state["project_plan"]
        )

        state["report"] = result

        return state

    def build_graph(self):

        self.graph.add_node(
            "planning",
            self.planning_node
        )

        self.graph.add_node(
            "risk",
            self.risk_node
        )

        self.graph.add_node(
            "resource",
            self.resource_node
        )

        self.graph.add_node(
            "scrum",
            self.scrum_node
        )

        self.graph.add_node(
            "report",
            self.report_node
        )

        self.graph.set_entry_point(
            "planning"
        )

        self.graph.add_edge(
            "planning",
            "risk"
        )

        self.graph.add_edge(
            "risk",
            "resource"
        )

        self.graph.add_edge(
            "resource",
            "scrum"
        )

        self.graph.add_edge(
            "scrum",
            "report"
        )

        self.graph.add_edge(
            "report",
            END
        )

        self.workflow = self.graph.compile()

    def execute(self, user_input):

        initial_state = {

            "user_input": user_input,

            "project_plan": "",

            "risks": "",

            "resources": "",

            "scrum_updates": "",

            "report": "",

            "context": ""
        }

        return self.workflow.invoke(
            initial_state
        )