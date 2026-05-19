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

        try:

            retrieved_context = self.context_builder.build_context(
                project_goal
            )

            self.short_memory.save(
                "latest_user_request",
                project_goal
            )

            plan = self.safe_agent_execution(
                self.planning_agent.generate_plan,
                project_goal,
                retrieved_context
            )

            risks = self.safe_agent_execution(
                self.risk_agent.analyze_risks,
                plan
            )

            resources = self.safe_agent_execution(
                self.resource_agent.allocate_resources,
                plan
            )

            scrum = self.safe_agent_execution(
                self.scrum_agent.generate_standup,
                plan
            )

            report = self.safe_agent_execution(
                self.report_agent.generate_report,
                plan
            )

            self.long_memory.save(
                "project_plan",
                plan
            )

            self.long_memory.save(
                "risks",
                risks
            )

            self.long_memory.save(
                "resources",
                resources
            )

            self.long_memory.save(
                "scrum_updates",
                scrum
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

        except Exception as error:

            logger.exception(
                f"Workflow execution failed: {error}"
            )

            return {

                "status": "FAILED",

                "error": str(error),

                "message": "Enterprise workflow failure handled gracefully."
            }

    def safe_agent_execution(
        self,
        agent_method,
        *args
    ):

        try:

            return agent_method(*args)

        except Exception as error:

            logger.exception(
                f"Agent execution failed: {error}"
            )

            return f"""
            Agent Failure Recovery Activated.

            Error:
            {error}
            """