from openai import OpenAI

from app.core.config import settings

client = OpenAI(api_key=settings.llm_secret_key, base_url="https://api.kluster.ai/v1")


class LLMHandler:
    def analyze_agenda(self, agenda) -> str:
        initial_context = (
            f"Eres un asistente que se encarga de llevar mi agenda. "
            f"Y mi agenda es: {str(agenda)}"
        )
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            max_tokens=100,
            temperature=0.7,
            messages=[
                {"role": "system", "content": initial_context},
                {"role": "user", "content": "¿Que planes tengo hoy?"},
            ],
        )

        return response.choices[0].message.content
