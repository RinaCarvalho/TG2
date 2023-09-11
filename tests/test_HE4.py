# test mean average deviation

def run_tests(script_string):
    namespace = {}
    exec(script_string, namespace)

    calculate_mad = namespace['calculate_mad']

    assert calculate_mad([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert calculate_mad([-3.2, -1, 0.5, 2.5]) == 1.8


if __name__ == "__main__":
    import sys
    from utils import write_test_results_to_log

    if len(sys.argv) > 2:
        script_string = sys.argv[1]
        log_filepath = sys.argv[2]

        try:
            run_tests(script_string)
            results = "Tests passed successfully"
            write_test_results_to_log(log_filepath, results)

        except AssertionError as e:
            results = f"Test failed: {e}"
            write_test_results_to_log(log_filepath, results)
            sys.exit(1)
