import time

from monitoring.logging_config import logger


class MetricsCollector:

    def __init__(self):

        self.agent_metrics = {}

    def start_timer(self):

        return time.time()

    def stop_timer(
        self,
        agent_name,
        start_time
    ):

        end_time = time.time()

        latency = round(
            end_time - start_time,
            2
        )

        if agent_name not in self.agent_metrics:

            self.agent_metrics[agent_name] = {

                "calls": 0,

                "total_latency": 0
            }

        self.agent_metrics[agent_name]["calls"] += 1

        self.agent_metrics[agent_name]["total_latency"] += latency

        logger.info(
            f"""
            METRICS UPDATE

            Agent:
            {agent_name}

            Latency:
            {latency} seconds
            """
        )

        return latency

    def get_metrics(self):

        analytics = {}

        for agent, data in self.agent_metrics.items():

            average_latency = round(

                data["total_latency"] / data["calls"],

                2
            )

            analytics[agent] = {

                "calls": data["calls"],

                "average_latency": average_latency
            }

        return analytics