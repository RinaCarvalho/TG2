import os
from evaluator import Evaluator
from utils import extract_tests_from_problem, write_test_results_to_log, write_to_jsonl

log_directory = "logs/GPT_4_t2_v0"

if __name__ == "__main__":
    write_to_jsonl()

    for log_file in os.listdir(log_directory):
        evaluator = Evaluator(log_file=log_file, log_directory=log_directory)
        tests = extract_tests_from_problem(evaluator.problem_id)

        if not tests:
            continue

        try:
            evaluator.run_test(tests)
            results = "Tests passed successfully"

        except AssertionError as e:
            results = f"Test failed: {e}"

        except Exception as e:
            results = f"Test failed: {e}"

        write_test_results_to_log(evaluator.log_filepath, results)
