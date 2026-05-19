import asyncio

from agents.base_agent import BaseAgent

from agents.planning_agent import PlanningAgent
from agents.risk_agent import RiskAgent
from agents.scrum_agent import ScrumAgent
from agents.resource_agent import ResourceAgent
from agents.report_agent import ReportAgent

from rag.context_builder import ContextBuilder

from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

from monitoring.logging_config import logger
from monitoring.audit_logger import AuditLogger


class WorkflowManager:

    def __init__(self):

        logger.info("Initializing Workflow Manager")

        self.audit_logger = AuditLogger()

        self.planning_agent = PlanningAgent()

        self.risk_agent = RiskAgent()

        self.scrum_agent = ScrumAgent()

        self.resource_agent = ResourceAgent()

        self.report_agent = ReportAgent()

        self.context_builder = ContextBuilder()

        self.short_memory = ShortTermMemory()

        self.long_memory = LongTermMemory()

    async def execute_workflow(
        self,
        project_goal
    ):

        logger.info(
            "Starting Async Multi-Agent Workflow"
        )

        self.audit_logger.log_workflow_start(

            "Enterprise Multi-Agent Workflow",

            project_goal
        )

        try:

            retrieved_context = self.context_builder.build_context(
                project_goal
            )

            self.short_memory.save(
                "latest_user_request",
                project_goal
            )

            plan = await self.planning_agent.generate_plan(
                project_goal,
                context=retrieved_context
            )

            risk_task = asyncio.create_task(

                self.risk_agent.analyze_risks(
                    plan
                )
            )

            resource_task = asyncio.create_task(

                self.resource_agent.allocate_resources(
                    plan
                )
            )

            scrum_task = asyncio.create_task(

                self.scrum_agent.generate_standup(
                    plan
                )
            )

            risks, resources, scrum = await asyncio.gather(

                risk_task,

                resource_task,

                scrum_task
            )

            report = await self.report_agent.generate_report(
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

            self.audit_logger.log_workflow_complete(

                "Enterprise Multi-Agent Workflow"
            )

            logger.info(
                "Async enterprise workflow completed"
            )

            return {

                "retrieved_context": retrieved_context,

                "plan": plan,

                "risks": risks,

                "resources": resources,

                "scrum": scrum,

                "report": report,

                "workflow_metrics":
                BaseAgent.metrics_collector.get_metrics(),

                "token_usage":
                BaseAgent.token_tracker.get_usage(),

                "short_memory":
                self.short_memory.get_all(),

                "long_memory":
                self.long_memory.load_all()
            }

        except Exception as error:

            self.audit_logger.log_error(

                "WorkflowManager",

                error
            )

            logger.exception(
                f"Workflow failed: {error}"
            )

            return {

                "status": "FAILED",

                "error": str(error)
            }