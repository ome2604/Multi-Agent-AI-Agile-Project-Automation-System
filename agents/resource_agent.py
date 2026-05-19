from agents.base_agent import BaseAgent

class ResourceAgent(BaseAgent):

    def __init__(self):

        super().__init__("Resource Allocation Agent")

    async def allocate_resources(self, project_data):

        prompt = f"""

        You are a Resource Allocation Agent.

        Responsibilities:
        - assign tasks
        - balance workload
        - estimate completion
        - optimize productivity

        Project Data:
        {project_data}
        
        """

        return await self.invoke(prompt)