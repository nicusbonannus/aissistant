from openai import OpenAI

from app.core.config import settings

client = OpenAI(api_key=settings.llm_secret_key, base_url="https://api.kluster.ai/v1")


class LLMHandler:
    def analyze_agenda(self, agenda) -> str:
        initial_context = (
            f"Eres un asistente que se encarga de llevar mi agenda. "
            f"Me gusta trabajar de 9 a 18, con una hora de almuerzo entre la 12 y las 14hs."
            f"Me levanto a las 6.40, no me gusta hacer cosas despues de las 20hs"
            f"Y mi agenda es: {str(agenda)}. "
        )
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            max_tokens=400,
            temperature=0.7,
            messages=[
                {"role": "system", "content": initial_context},
                {
                    "role": "user",
                    "content": "¿En que momento mañana puedo ir a la ferreteria?",
                },
            ],
        )

        return response.choices[0].message.content
