from agents.planning_agent import PlanningAgent

agent = PlanningAgent()

response = agent.invoke(
    """
    Create a sprint plan for an AI-powered ecommerce platform.
    """
)

print("\n===== PLANNING AGENT OUTPUT =====\n")
print(response)