import os
import requests
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
        # self.palm_key = os.getenv("PALM_API_KEY")
        self.gcloud_token = os.getenv("GCLOUD_ACCESS_TOKEN")
        self.google_project_id = os.getenv("PROJECT_ID")


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
            if "gpt" in self.model:
                try:
                    data = self._call_OpenAI_API(prompt)
                except:
                    data = "Error generating code"

                if self.model == 'gpt-4':
                    time.sleep(3)  # Due to rate limit

            else:   # Palm
                response = self._call_PaLM_API(prompt)

                if response.status_code == 200:
                    # Request was successful
                    formatted_response = response.json()
                    data = formatted_response["predictions"][0]["content"]
                else:
                    # Request failed
                    data = response.text

            self._log_api_call(prompt_series, prompt, data, log_path)
            print(prompt_series)


    def _call_OpenAI_API(self, prompt):
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
        return response
    

    def _call_PaLM_API(self, prompt):
        url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{self.google_project_id}/locations/us-central1/publishers/google/models/{self.model}:predict"
        headers = {
            "Authorization": f"Bearer {self.gcloud_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "instances": [
                {
                    "prefix": f"Consider the following problem and generate code in {self.language}" + prompt
                }
            ],
            "parameters": {
                "temperature": 0.5,
                "maxOutputTokens": 1024
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response
