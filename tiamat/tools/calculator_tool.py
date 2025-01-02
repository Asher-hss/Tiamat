from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):
    """
    A simple calculator tool that adds two numbers.
    """

    def execute(self, x: int, y: int) -> int:
        return x + y

    def description(self) -> str:
        return "A tool to add two numbers."
