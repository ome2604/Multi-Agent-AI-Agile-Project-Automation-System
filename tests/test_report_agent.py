from agents.report_agent import ReportAgent

agent = ReportAgent()

response = agent.invoke(
    """
    Generate stakeholder report for AI ecommerce platform.
    """
)

print("\n===== REPORT AGENT OUTPUT =====\n")
print(response)