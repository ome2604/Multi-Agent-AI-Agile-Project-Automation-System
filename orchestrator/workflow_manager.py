from agents.planning_agent import PlanningAgent
from agents.risk_agent import RiskAgent
from agents.scrum_agent import ScrumAgent
from agents.resource_agent import ResourceAgent
from agents.report_agent import ReportAgent

from monitoring.logging_config import logger


class WorkflowManager:

    def __init__(self):

        logger.info("Initializing Workflow Manager")

        self.planning_agent = PlanningAgent()
        self.risk_agent = RiskAgent()
        self.scrum_agent = ScrumAgent()
        self.resource_agent = ResourceAgent()
        self.report_agent = ReportAgent()

    def execute_workflow(self, project_goal):

        logger.info("Starting Multi-Agent Workflow")

        plan = self.planning_agent.generate_plan(
            project_goal
        )

        risks = self.risk_agent.analyze_risks(
            plan
        )

        resources = self.resource_agent.allocate_resources(
            plan
        )

        scrum = self.scrum_agent.generate_standup(
            plan
        )

        report = self.report_agent.generate_report(
            plan
        )

        return {
            "plan": plan,
            "______________________________________________"
            "risks": risks,
            "______________________________________________"
            "resources": resources,
            "______________________________________________"
            "scrum": scrum,
            "______________________________________________"
            "report": report
        }