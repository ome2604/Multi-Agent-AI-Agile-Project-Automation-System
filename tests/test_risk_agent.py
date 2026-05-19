from agents.risk_agent import RiskAgent

agent = RiskAgent()

response = agent.invoke(
    """
    Analyze risks for an AI ecommerce platform.
    """
)

print("\n===== RISK AGENT OUTPUT =====\n")
print(response)