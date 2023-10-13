import csv
import json
import os
import re
from problems import data

problem_file_path = 'problems.jsonl'


def write_to_jsonl():
    with open(problem_file_path, "w") as jsonl_file:
        for problem_data in data:
            # Convert the dictionary to a JSON string
            json_str = json.dumps(problem_data)
            # Write the JSON string as a line in the JSONL file
            jsonl_file.write(json_str + "\n")


def extract_problem_id(log_file):
    return log_file.split("_")[0]


def extract_prompt_from_problem(problem_id, prompt_type):
    with open(problem_file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            if data.get("problem_id") == problem_id:
                prompts = data.get("prompts", [])
                for prompt in prompts:
                    return prompt[prompt_type]


def extract_examples_from_problem(problem_id, variation_examples):
    for problem in data:
        if problem['problem_id'] == problem_id:
            return problem[variation_examples]


def extract_tests_from_problem(problem_id):
    for problem in data:
        if problem['problem_id'] == problem_id:
            return problem['tests']
        
    return None


def remove_fluff_from_code(response):
    start_pattern = r'```(python(\\n)?)?'
    end_pattern = r'```'

    start_match = re.search(start_pattern, response)

    if start_match:
        end_match = re.search(end_pattern, response[start_match.end():])

        if end_match:
            start_pos = start_match.end()
            end_pos = start_match.end() + end_match.start()
            code_snippet = response[start_pos:end_pos]

            return code_snippet

    return response


def write_test_results_to_log(log_filepath, results):
    with open(log_filepath, "r") as log_file:
        log = log_file.read()
        data = json.loads(log)

    data["test_results"] = results

    with open(log_filepath, "w") as log:
        log.write(json.dumps(data, indent = 4))


def compile_results(logs_dir):
    results = {}

    for subdir in os.listdir(logs_dir):
        subdir_path = os.path.join(logs_dir, subdir)
        results[subdir] = {}
        for log_file in os.listdir(subdir_path):
            log_file_path = os.path.join(subdir_path, log_file)
            with open(log_file_path, 'r') as f:
                log_data = json.load(f)
                problem_id = extract_problem_id(log_file)
                if problem_id not in results[subdir]:
                    results[subdir][problem_id] = 0
                if log_data['test_results'] == "Tests passed successfully":
                    results[subdir][problem_id] += 1
    return results


def write_results_to_csv(results):
    with open("result_compilation.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        header = ['Problem'] + list(results.keys())
        csv_writer.writerow(header)

        for problem_id in set(problem for problems in results.values() for problem in problems.keys()):
            row = [problem_id]
            for subdir in results.keys():
                if problem_id in results[subdir]:
                    row.append(results[subdir][problem_id])
                else:
                    row.append("-")
            csv_writer.writerow(row)

    print("Results have been saved.")
