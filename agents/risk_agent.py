from agents.base_agent import BaseAgent

class RiskAgent(BaseAgent):

    def __init__(self):

        super().__init__("Risk Analysis Agent")

    def analyze_risks(self, project_context):

        prompt = f"""

        You are an enterprise Risk Analysis Agent.

        Analyze:
        - blockers
        - sprint risks
        - dependency issues
        - workload imbalance
        - delivery delays

        Context:
        {project_context}

        Generate:
        1. Risks
        2. Severity
        3. Mitigation Strategies

        """

        return self.invoke(prompt)