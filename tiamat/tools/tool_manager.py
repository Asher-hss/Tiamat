from typing import Dict, Type
from tools.base_tool import BaseTool

class ToolManager:
    """
    Manager for handling tools.
    """

    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}

    def register_tool(self, tool_name: str, tool: BaseTool):
        """
        Register a tool with the manager.
        :param tool_name: Unique name for the tool.
        :param tool: The tool instance.
        """
        if not isinstance(tool, BaseTool):
            raise TypeError(f"The tool must be an instance of BaseTool, got {type(tool)}")
        self.tools[tool_name] = tool

    def get_tool(self, tool_name: str) -> BaseTool:
        """
        Retrieve a tool by its name.
        :param tool_name: The name of the tool.
        :return: The tool instance.
        """
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return self.tools[tool_name]

    def call_tool(self, tool_name: str, *args, **kwargs) -> Any:
        """
        Call a specific tool's execute method.
        :param tool_name: The name of the tool to execute.
        :return: The result of the tool's execution.
        """
        tool = self.get_tool(tool_name)
        return tool.execute(*args, **kwargs)

    def list_tools(self) -> Dict[str, str]:
        """
        List all registered tools with their descriptions.
        :return: A dictionary of tool names and descriptions.
        """
        return {name: tool.description() for name, tool in self.tools.items()}
