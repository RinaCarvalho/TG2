import os
import openai
import json

from datetime import datetime

# TODO: Enable other LLMs than Openai's

class CodeGenerator:
    def __init__(self, model, language):
        self.model = model
        self.language = language
        openai.api_key = os.getenv("OPENAI_API_KEY")


    def _log_api_call(self, prompt_series, prompt, response):
        now = datetime.now()
        timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")
        log_file = f"{prompt_series}__{timestamp}.json"
        log_filepath = os.path.join("logs", log_file)
        
        log_entry = {
            "prompt": prompt,
            "response": response
        }

        with open(log_filepath, "a") as log:
            log.write(json.dumps(log_entry))

    
    def generate_code(self, prompt_series, prompt, n_samples = 1):
        # chat completion only for now
        # only openai for now

        for i in range(n_samples):
            try:
                completion = openai.ChatCompletion.create(
                    model = self.model,
                    messages = [
                        {"role": "system",
                        "content": f"You are a programming assistant, responsible for generating code in {self.language}.\
                                    Your responses must consist only of code, without additional text."},
                        {"role": "user", "content": prompt}
                    ]
                )
                response = completion.choices[0].message.content
                self._log_api_call(prompt_series, prompt, response)

            except:
                response = None
                self._log_api_call(prompt_series, prompt, "Error generating code")
