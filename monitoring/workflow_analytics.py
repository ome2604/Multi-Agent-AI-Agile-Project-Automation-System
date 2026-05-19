from monitoring.logging_config import logger


class WorkflowAnalytics:

    def generate_summary(
        self,
        workflow_output
    ):

        metrics = workflow_output.get(
            "workflow_metrics",
            {}
        )

        tokens = workflow_output.get(
            "token_usage",
            {}
        )

        logger.info(
            f"""
            WORKFLOW ANALYTICS SUMMARY

            Metrics:
            {metrics}

            Token Usage:
            {tokens}
            """
        )