import os
import openai

class CodeEvaluator:
    def __init__(self, model, language, prompt):
        self.model = model
        self.language = language
        self.prompt = prompt

        openai.api_key = os.getenv("OPENAI_API_KEY")

    