import json
import os
import re
import timeout_decorator
from utils import write_test_results_to_log

class Evaluator:
    def __init__(self, log_file, log_directory):
        self.log_file = log_file
        self.log_filepath = os.path.join(log_directory, log_file)
        self.problem_id = self._extract_problem_id()


    def _extract_problem_id(self):
        return self.log_file.split("_")[0]


    def _extract_generated_code(self):
        with open(self.log_filepath, "r") as log:
            data = json.load(log)

        if not data or not data["response"] or data["response"] == "Error generating code":
            return None

        return data["response"]


    def _extract_name_from_namespace(self, generated_code):
        function_name = r"def\s+(\w+)\s*\("
        match = re.search(function_name, generated_code)

        if match:
            return match.group(1)
        else:
            return None


    @timeout_decorator.timeout(5)
    def run_test(self, tests):
        generated_code = self._extract_generated_code()

        if not generated_code:
            results = "Tests unsuccessful due to error in code generation"
            write_test_results_to_log(self.log_filepath, results)
            return
            
        function_name = self._extract_name_from_namespace(generated_code)
        namespace = {}
        exec(generated_code, namespace)

        test_function = namespace[function_name]

        for test in tests:
            result = test_function(*test["inputs"])
            assert result == test["output"], f"result {result} != {test['output']} (expected)"
