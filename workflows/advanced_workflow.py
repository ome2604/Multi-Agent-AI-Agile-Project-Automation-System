from agents.planning_agent import PlanningAgent
from agents.risk_agent import RiskAgent
from agents.scrum_agent import ScrumAgent
from agents.resource_agent import ResourceAgent
from agents.report_agent import ReportAgent

from rag.context_builder import ContextBuilder

from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

from monitoring.logging_config import logger


class WorkflowManager:

    def __init__(self):

        logger.info("Initializing Workflow Manager")

        self.planning_agent = PlanningAgent()

        self.risk_agent = RiskAgent()

        self.scrum_agent = ScrumAgent()

        self.resource_agent = ResourceAgent()

        self.report_agent = ReportAgent()

        self.context_builder = ContextBuilder()

        self.short_memory = ShortTermMemory()

        self.long_memory = LongTermMemory()

    def execute_workflow(self, project_goal):

        logger.info("Starting Multi-Agent Workflow")

        retrieved_context = self.context_builder.build_context(
            project_goal
        )

        self.short_memory.save(
            "latest_user_request",
            project_goal
        )

        plan = self.planning_agent.generate_plan(
            project_goal,
            context=retrieved_context
        )

        self.long_memory.save(
            "project_plan",
            plan
        )

        risks = self.risk_agent.analyze_risks(
            plan
        )

        self.long_memory.save(
            "risks",
            risks
        )

        resources = self.resource_agent.allocate_resources(
            plan
        )

        self.long_memory.save(
            "resources",
            resources
        )

        scrum = self.scrum_agent.generate_standup(
            plan
        )

        self.long_memory.save(
            "scrum_updates",
            scrum
        )

        report = self.report_agent.generate_report(
            plan
        )

        self.long_memory.save(
            "final_report",
            report
        )

        logger.info(
            "Enterprise workflow completed successfully"
        )

        return {

            "retrieved_context": retrieved_context,

            "plan": plan,

            "risks": risks,

            "resources": resources,

            "scrum": scrum,

            "report": report,

            "short_memory": self.short_memory.get_all(),

            "long_memory": self.long_memory.load_all()
        }