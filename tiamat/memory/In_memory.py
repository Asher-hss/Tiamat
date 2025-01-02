from typing import Dict, List
class InMemory:
    def __init__(self):
        self.storage: List[Dict[str, str]] = []

    def save(self, message: Dict[str, str]) -> None:
        """
        Save a single message to memory.
        :param message: A dictionary with 'role' and 'content' keys.
        """
        self.storage.append(message)

    def retrieve(self) -> List[Dict[str, str]]:
        """
        Retrieve all stored messages.
        :return: List of message dictionaries.
        """
        return self.storage

    def clear(self) -> None:
        """
        Clear all memory.
        """
        self.storage.clear()
