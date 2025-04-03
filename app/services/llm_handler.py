from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from app.core.config import settings

# client = OpenAI(api_key=settings.llm_secret_key, base_url="https://api.kluster.ai/v1")


class LLMHandler:
    def __init__(self):
        self._llm = ChatOpenAI(
            model_name=settings.LLM_MODEL_NAME,
            max_tokens=400,
            temperature=0.7,
            openai_api_key=settings.LLM_SECRET_KEY,
            openai_api_base=settings.LLM_PROVIDER_URL,
        )

    def analyze_agenda(self, agenda) -> str:
        initial_context = f"{settings.LLM_SYSTEM_PROMPT} Mi agenda es: {str(agenda)}."
        messages = [
            SystemMessage(content=initial_context),
            HumanMessage("¿En que momento mañana puedo ir a la ferreteria?"),
        ]

        response = self._llm(messages)

        return response.content
