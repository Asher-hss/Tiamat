from abc import ABC, abstractmethod
from typing import List, Any

class BaseMemory(ABC):
    """
    Abstract Base Class for a memory module.
    Defines the interface for storing and retrieving memory.
    """

    @abstractmethod
    def save(self, data: Any) -> None:
        """
        Save data to memory.
        :param data: Data to be saved.
        """
        pass

    @abstractmethod
    def retrieve(self) -> List[Any]:
        """
        Retrieve all stored memory.
        :return: List of all stored data.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Clear all memory.
        """
        pass