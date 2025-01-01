from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, field_validator
from typing import Any, List, Optional, Dict
from tiamat.tools.base_tool import BaseTool
class BaseAgent(ABC, BaseModel):
    id: str
    name: str
    tool_manager: Any
    config: Optional[Dict[str, any]] = Field(default=dict)
    max_iter: Optional[int] = Field(default=3)
    llm: Any = None
    memory: Any = None
    @abstractmethod
    def act(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def think(self, *args, **kwargs) -> Any:
        pass
    
    @field_validator("tools")
    def validate_tools(cls, tools: List[Any]) -> List[BaseTool]:
        validated_tools = []
        for tool in tools:
            if not isinstance(tool, BaseTool):
                raise ValueError(f"Tool {tool} is not an instance of BaseTool")
            validated_tools.append(tool)
        return validated_tools