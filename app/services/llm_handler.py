from langchain.agents import AgentType, initialize_agent
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from app.core.config import settings

# client = OpenAI(api_key=settings.llm_secret_key, base_url="https://api.kluster.ai/v1")


class DiscountInput(BaseModel):
    price: float = Field(..., description="Precio original del producto")
    percentage: float = Field(..., description="Porcentaje de descuento a aplicar")


def calculate_discount(price: float, percentage: float) -> float:
    return price * (1 - percentage / 100)


discount_tool = StructuredTool(
    name="Calculadora de descuentos",
    description="Calcula el precio final despues de aplicar un descuento",
    func=calculate_discount,
    args_schema=DiscountInput,
)


class LLMHandler:
    def __init__(self):
        self._llm = ChatOpenAI(
            model=settings.LLM_MODEL_NAME,
            max_tokens=400,
            temperature=0.7,
            api_key=settings.LLM_SECRET_KEY,
            base_url=settings.LLM_PROVIDER_URL,
        )

    def find_spot(self, agenda, event_description: str) -> str:
        initial_context = f"{settings.LLM_SYSTEM_PROMPT} Mi agenda es: {str(agenda)}."
        message = f"¿En que momento mañana puedo hacer este evento:{event_description}?"
        messages = [
            SystemMessage(content=initial_context),
            HumanMessage(message),
        ]

        response = self._llm.invoke(messages)

        return response.content

    def analyze_agenda(self, agenda_events: list) -> str:
        initial_context = (
            f"{settings.LLM_SYSTEM_PROMPT} Mi agenda es: {str(agenda_events)}."
        )
        messages = [
            SystemMessage(content=initial_context),
            HumanMessage(
                "Resumi mi agenda, decime si es un dia cargado, un dia cargado tiene mas de 2 eventos."
            ),
        ]

        response = self._llm.invoke(messages)

        return response.content

    def tool_example(self, price: float, discount: float) -> float:
        agent = initialize_agent(
            tools=[discount_tool],
            llm=self._llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )

        question = f"Si un producto cuesta ${price} y tiene un {discount}% de descuento, cual es el precio final?"
        response = agent.run(question)
        return response
