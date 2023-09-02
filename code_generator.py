import os
import openai

from datetime import datetime

# TODO: Enable other LLMs than Openai's

class CodeGenerator:
    def __init__(self, model):
        self.model = model
        openai.api_key = os.getenv("OPENAI_API_KEY")


    def _log_api_call(self, prompt_series, prompt, response):
        now = datetime.now()
        timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")
        log_file = f"{timestamp}__{prompt_series}.log"
        log_filepath = os.path.join("logs", log_file)

        with open(log_filepath, "a") as log:
            log.write("Prompt ==================\n")
            log.write(f"{prompt}\n\n")
            log.write("Response ================\n")
            log.write(f"{response}\n\n")

    
    def generate_code(self, prompt_series, prompt):
        # chat completion only for now
        # only openai for now
        try:
            completion = openai.ChatCompletion.create(
                model = self.model,
                messages = prompt
            )
            response = completion.choices[0].message
            self._log_api_call(prompt_series, prompt, response)

        except:
            response = None
            self._log_api_call(prompt_series, prompt, "Error generating code")
        
        return response
