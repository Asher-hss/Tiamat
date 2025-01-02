from tiamat.agents.base_agent import BaseAgent
from typing import Any
class Agent(BaseAgent):
    def think(self, context):
        history = self.memory.retrieve()
        
        messages = history + [
            {"role": "user", "content": f"""
            Based on the following context, generate a JSON instruction for the next action:
            Context: {context}
            Response format:
            {{
                "action": "action_name",
                "params": {{}}
            }}
            """}
        ]

        response = self.llm.generate(messages) 

        self.memory.save({"role": "user", "content": context})
        self.memory.save({"role": "assistant", "content": response})

        return eval(response)
    
    def act(self, instruction: dict, *args, **kwargs) -> Any:
        """
        Execute the action specified by the instruction.
        """
        action = instruction.get("action")
        params = instruction.get("params", {})
        tool = next((t for t in self.tool_manager if t.__class__.__name__.lower() == action), None)
        
        if not tool:
            raise ValueError(f"Tool '{action}' not found in tool_manager")
        
        return tool.execute(**params)