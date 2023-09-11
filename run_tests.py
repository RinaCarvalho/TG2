from evaluator import Evaluator

log_file = "HE4_t0_v0__2023_09_08_03_05_26.json"

if __name__ == "__main__":
    evaluator = Evaluator(log_file=log_file)
    evaluator.run_test()
    pass