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
        pass
