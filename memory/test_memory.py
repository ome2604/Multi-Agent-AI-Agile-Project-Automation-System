from memory.state_manager import StateManager


state = StateManager()

# Short-term memory
state.short_term.save(
    "active_sprint",
    "Sprint 3"
)

# Long-term memory
state.long_term.save(
    "project_name",
    "AI Agile Automation Platform"
)

# Conversation memory
state.conversation.add_message(
    "user",
    "What are current sprint risks?"
)

print("\nSHORT TERM MEMORY:\n")

print(
    state.short_term.get_all()
)

print("\nLONG TERM MEMORY:\n")

print(
    state.long_term.load_all()
)

print("\nCONVERSATION MEMORY:\n")

print(
    state.conversation.get_history()
)