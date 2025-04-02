import openai


class LLMHandler:
    def analyze_agenda(self):
        response = openai.Completion.create(
            engine="text-davinci-003",  # O el modelo que corresponda
            prompt="¿Cómo puedo usar DeepSeek-V3?",
            max_tokens=100,
            temperature=0.7,
        )

        return response.choices[0].text.strip()
