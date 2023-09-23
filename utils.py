import json
from problems import data

problem_file_path = 'problems.jsonl'


def write_to_jsonl():
    with open(problem_file_path, "w") as jsonl_file:
        for problem_data in data:
            # Convert the dictionary to a JSON string
            json_str = json.dumps(problem_data)
            # Write the JSON string as a line in the JSONL file
            jsonl_file.write(json_str + "\n")


def extract_prompt_from_problem(problem_id, prompt_type):
    with open(problem_file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            if data.get("problem_id") == problem_id:
                prompts = data.get("prompts", [])
                for prompt in prompts:
                    return prompt[prompt_type]


def extract_tests_from_problem(problem_id):
    for problem in data:
        if problem['problem_id'] == problem_id:
            return problem['tests']
        
    return None


def write_test_results_to_log(log_filepath, results):
    with open(log_filepath, "r") as log_file:
        log = log_file.read()
        data = json.loads(log)

    data["test_results"] = results

    with open(log_filepath, "w") as log:
        log.write(json.dumps(data, indent = 4))
