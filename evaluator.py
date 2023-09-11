import json
import os
import subprocess

class Evaluator:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_filepath = os.path.join("logs", log_file)
        self.problem_id = self._extract_problem_id()


    def _extract_problem_id(self):
        return self.log_file.split("_")[0]


    def _extract_generated_code(self):
        with open(self.log_filepath, "r") as log:
            data = json.load(log)

        if not data or not data["response"] or data["response"] == "Error generating code":
            return None

        return data["response"]


    def run_test(self):
        generated_code = self._extract_generated_code()

        if generated_code:
            test_filepath = os.path.join("tests", f"test_{self.problem_id}.py")
            abs_log_filepath = os.path.abspath(self.log_filepath)
            subprocess.call(["python", test_filepath, generated_code, abs_log_filepath])