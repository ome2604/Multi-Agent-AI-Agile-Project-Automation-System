from agents.planning_agent import PlanningAgent
from agents.risk_agent import RiskAgent
from agents.scrum_agent import ScrumAgent
from agents.resource_agent import ResourceAgent
from agents.report_agent import ReportAgent

class AgentRouter:

    def __init__(self):

        self.planning_agent = PlanningAgent()
        self.risk_agent = RiskAgent()
        self.scrum_agent = ScrumAgent()
        self.resource_agent = ResourceAgent()
        self.report_agent = ReportAgent()