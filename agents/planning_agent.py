from agents.base_agent import BaseAgent
from tools.tool_manager import ToolManager

class PlanningAgent(BaseAgent):

    def __init__(self):

        super().__init__("Planning Agent")

        self.tools = ToolManager()

    def generate_plan(self, project_goal):

        web_research = self.tools.web_search(
            f"Best Agile practices for {project_goal}"
        )

        prompt = f"""

        You are an enterprise Agile Planning Agent.

        Web Research:
        {web_research}

        Responsibilities:
        - break project into milestones
        - generate sprint plans
        - define dependencies

        Project:
        {project_goal}

        Generate:
        1. Milestones
        2. Sprint Plan
        3. Dependencies
        4. Estimated Timeline
        
        """

        return self.invoke(prompt)