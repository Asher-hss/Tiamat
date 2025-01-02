import os
from openai import OpenAI
from openai.types.chat.chat_completion_assistant_message_param import(
    ChatCompletionAssistantMessageParam
)

from tiamat.llm.base_llm import BaseLLM
from typing import Dict, Optional, List
class openai_llm(BaseLLM):
    def __init__(
        self,
        api_key: str,
        model: Optional[str] = None,
        model_config: Optional[Dict[str, any]] = None,
        url: Optional[str] = None,
    ):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.url = url or os.getenv("OPENAI_URL")
        self.model = model
        self._client = OpenAI(
            timeout=180,
            max_retries=3,
            base_url=self.url,
            api_key=self.api_key,
        )
    
    def generate(self, messages: List[ChatCompletionAssistantMessageParam]):
        response = self._client.chat.completions.create(
            messages=messages,
            model = self.model,
            ** self.model_config
        )
        return response
    