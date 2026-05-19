from monitoring.logging_config import logger


class AuditLogger:

    def log_workflow_start(
        self,
        workflow_name,
        user_request
    ):

        logger.info({

            "event": "WORKFLOW_STARTED",

            "workflow": workflow_name,

            "request": user_request
        })

    def log_workflow_complete(
        self,
        workflow_name
    ):

        logger.info({

            "event": "WORKFLOW_COMPLETED",

            "workflow": workflow_name
        })

    def log_agent_execution(
        self,
        agent_name,
        status
    ):

        logger.info({

            "event": "AGENT_EXECUTION",

            "agent": agent_name,

            "status": status
        })

    def log_error(
        self,
        component,
        error
    ):

        logger.error({

            "event": "SYSTEM_ERROR",

            "component": component,

            "error": str(error)
        })

    def log_api_call(
        self,
        provider,
        status
    ):

        logger.info({

            "event": "API_CALL",

            "provider": provider,

            "status": status
        })