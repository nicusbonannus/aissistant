import asyncio

from langchain.agents import AgentType, initialize_agent
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from langchain_core.tracers.context import tracing_v2_enabled
from langchain_openai import ChatOpenAI
from langsmith import Client
from pydantic import BaseModel, Field, SecretStr

from app.core.config import settings


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
    def __init__(self, temperature: float = 0.1):
        self.client = Client()
        self._llm = ChatOpenAI(
            model=settings.LLM_MODEL_NAME,
            max_tokens=400,
            temperature=temperature,
            api_key=SecretStr(settings.LLM_SECRET_KEY),
            base_url=settings.LLM_PROVIDER_URL,
            verbose=True,
            streaming=True,
        )

    # deprecated
    def find_spot(self, agenda, event_description: str) -> str:
        initial_context = f"{settings.LLM_SYSTEM_PROMPT} Mi agenda es: {str(agenda)}."
        message = f"¿En que momento mañana puedo hacer este evento:{event_description}?"
        messages = [
            SystemMessage(content=initial_context),
            HumanMessage(message),
        ]

        with tracing_v2_enabled():
            response = self._llm.invoke(messages)

            return str(response.content)

    # deprecated
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

        with tracing_v2_enabled():
            response = self._llm.invoke(messages)

            return str(response.content)

    def tool_example(self, price: float, discount: float):
        agent = initialize_agent(
            tools=[discount_tool],
            llm=self._llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
        )

        question = f"Si un producto cuesta ${price} y tiene un {discount}% de descuento, cual es el precio final?"

        with tracing_v2_enabled():
            response = agent.run(question)
            return response

    async def generate_routine(self, description: str):
        messages = [
            SystemMessage(content=settings.LLM_SYSTEM_PROMPT),
            HumanMessage(
                f"Genera una rutina de gym para hoy enfocada en los siguientes musculos: {str(description)}. "
                f"No expliques los ejercicios."
            ),
        ]

        with tracing_v2_enabled():
            stream = self._llm.astream(messages)
            full_response = []
            async for chunk in stream:
                if hasattr(chunk, "content"):
                    content = chunk.content
                    yield content
                    full_response.append(content)
                    await asyncio.sleep(0.2)
