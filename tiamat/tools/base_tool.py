from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):
    """
    Abstract Base Class for tools.
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the tool's main function.
        :return: The result of the tool's operation.
        """
        pass

    @abstractmethod
    def description(self) -> str:
        """
        Return a description of the tool's functionality.
        """
        pass