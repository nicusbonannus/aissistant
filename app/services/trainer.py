from app.services.llm_handler import LLMHandler


class Trainer:
    def generate_routine(self, description: str, try_new_exes: bool):
        """
        Generate a training routine based on the provided description.
        """
        temperature = 0.8 if try_new_exes else 0.0

        return LLMHandler(temperature=temperature).generate_routine(
            muscles_groups=description
        )
