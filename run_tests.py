from evaluator import Evaluator
from utils import extract_tests_from_problem, write_test_results_to_log

log_file = "HE4_t0_v0__2023_09_08_03_05_26.json"

if __name__ == "__main__":
    evaluator = Evaluator(log_file=log_file)
    tests = extract_tests_from_problem(evaluator.problem_id)
    try:
        evaluator.run_test(tests)
        results = "Tests passed successfully"

    except AssertionError as e:
        results = f"Test failed: {e}"

    finally:
        write_test_results_to_log(evaluator.log_filepath, results)
