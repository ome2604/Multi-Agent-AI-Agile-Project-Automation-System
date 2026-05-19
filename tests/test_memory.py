from memory.short_term_memory import ShortTermMemory

memory = ShortTermMemory()

memory.add_message(
    "user",
    "Build AI ecommerce platform"
)

print(memory.get_messages())