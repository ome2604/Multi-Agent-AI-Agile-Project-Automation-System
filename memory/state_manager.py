from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory
from memory.conversation_memory import ConversationMemory


class StateManager:

    def __init__(self):

        self.short_term = ShortTermMemory()

        self.long_term = LongTermMemory()

        self.conversation = ConversationMemory()