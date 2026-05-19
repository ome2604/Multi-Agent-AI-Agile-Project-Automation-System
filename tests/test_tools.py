from tools.tavily_tool import search_web

result = search_web(
    "Latest AI project management trends"
)

print("\n===== TOOL OUTPUT =====\n")

print(result)