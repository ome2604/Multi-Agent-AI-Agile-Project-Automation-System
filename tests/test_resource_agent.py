from agents.resource_agent import ResourceAgent

agent = ResourceAgent()

response = agent.invoke(
    """
    Allocate resources for AI ecommerce platform.
    """
)

print("\n===== RESOURCE AGENT OUTPUT =====\n")
print(response)