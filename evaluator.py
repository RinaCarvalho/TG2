import json
import os
import re
import timeout_decorator
from utils import write_test_results_to_log, extract_problem_id

class Evaluator:
    def __init__(self, log_file, log_directory):
        self.log_file = log_file
        self.log_filepath = os.path.join(log_directory, log_file)
        self.problem_id = extract_problem_id(self.log_file)


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


    @timeout_decorator.timeout(15)
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

            if self.problem_id == "MBPP160":
                if result is not None:
                    x, y = result
                    a, b, n = test["inputs"]
                    assert type(result) == tuple, f"result is not a tuple"
                    assert a*x + b*y == n, f"result {result} is not a valid tuple"
                else:
                    assert result == test["output"], f"result {result} != {test['output']} (expected)"
            elif self.problem_id == "YTDL1":
                assert result == test["output"] or result == test["output"][:-1], f"result {result} != {test['output']} (expected)"
            else:
                assert result == test["output"], f"result {result} != {test['output']} (expected)"
