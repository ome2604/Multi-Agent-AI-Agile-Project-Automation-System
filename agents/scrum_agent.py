from agents.base_agent import BaseAgent

class ScrumAgent(BaseAgent):

    def __init__(self):

        super().__init__("Scrum Assistant Agent")

    def generate_scrum_summary(self, sprint_context):

        prompt = f"""

        You are a Scrum Assistant Agent.

        Generate:
        - standup summary
        - sprint retrospective
        - blockers
        - priorities

        Sprint Context:
        {sprint_context}
        
        """

        return self.invoke(prompt)