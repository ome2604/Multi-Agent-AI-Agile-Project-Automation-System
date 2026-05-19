from agents.scrum_agent import ScrumAgent

agent = ScrumAgent()

response = agent.invoke(
    """
    Generate sprint standup summary.
    """
)

print("\n===== SCRUM AGENT OUTPUT =====\n")
print(response)