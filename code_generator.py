import os
import openai
import json
import time

from datetime import datetime
from utils import remove_fluff_from_code

# TODO: Enable other LLMs than Openai's

class CodeGenerator:
    def __init__(self, model, language):
        self.model = model
        self.language = language
        openai.api_key = os.getenv("OPENAI_API_KEY")


    def _log_api_call(self, prompt_series, prompt, response, log_path):
        now = datetime.now()
        timestamp = now.strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]
        log_file = f"{prompt_series}__{timestamp}.json"
        log_filepath = os.path.join(log_path, log_file)

        response = remove_fluff_from_code(response)
        
        log_entry = {
            "prompt": prompt,
            "response": response
        }

        with open(log_filepath, "a") as log:
            log.write(json.dumps(log_entry))

    
    def generate_code(self, prompt_series, prompt, n_samples = 1, log_path = "logs"):
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
                self._log_api_call(prompt_series, prompt, response, log_path)

                print(prompt_series)

            except:
                response = None
                self._log_api_call(prompt_series, prompt, "Error generating code", log_path)

            finally:
                if self.model == 'gpt-4':
                    time.sleep(3)  # Due to rate limit
