import subprocess

class Evaluator:
    def __init__(self, problem_id, log_file):
        self.problem_id = problem_id
        self.log_file = log_file

    def _extract_generated_code(self):
        with open(self.log_file, "r") as log:
            return    # TODO: implement

    def run_test(self):
        generated_code = self._extract_generated_code()
        subprocess.call(["python", f"test_{self.problem_id}.py", generated_code])