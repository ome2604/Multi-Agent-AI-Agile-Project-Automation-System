from tools.tavily_tool import search_web
from tools.scraper_tool import scrape_website

class ToolManager:

    def web_search(self, query):

        return search_web(query)

    def scrape(self, url):

        return scrape_website(url)