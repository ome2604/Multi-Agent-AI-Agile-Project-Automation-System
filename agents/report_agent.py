from agents.base_agent import BaseAgent

class ReportAgent(BaseAgent):

    def __init__(self):

        super().__init__("Report Agent")

    def generate_report(self, project_context):

        prompt = f"""

        You are an enterprise Report Agent.

        Generate:
        - stakeholder summary
        - sprint report
        - progress summary
        - delivery insights

        Project Context:
        {project_context}
        
        """

        return self.invoke(prompt)