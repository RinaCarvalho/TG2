# TODO: Everywhere: document methods (docstrings)

import time

from prompt_generator import PromptGenerator
from prompt_constants import Technique, Variation
from code_generator import CodeGenerator
from utils import extract_prompt_from_problem, write_to_jsonl, list_problem_ids

model = "gpt-4"
language = "Python 3"
problem_id = None
prompt_type = "0-shot"
log_path = "logs/GPT_4_t1_v2"
technique=Technique.FEW_SHOT
variation=Variation.INACCURACY
samples = 1


def generate_code_for_problem(problem_id, prompt_type, technique, variation, model, language, log_path, samples):
    prompt = extract_prompt_from_problem(problem_id=problem_id, prompt_type=prompt_type)
    
    if prompt:
        prompt_gen = PromptGenerator(prompt=prompt, problem=problem_id, technique=technique, variation=variation)
        prompt_series = prompt_gen.generate_prompt_series()
        prompt = prompt_gen.generate_modified_prompt()
        code_gen = CodeGenerator(model=model, language=language)
        code_gen.generate_code(prompt_series, prompt, samples, log_path)


if __name__ == "__main__":
    write_to_jsonl()

    if problem_id:
        generate_code_for_problem(problem_id, prompt_type, technique, variation, model, language, log_path, samples)
    else:
        problem_ids = list_problem_ids()
        for problem_id in problem_ids:
            generate_code_for_problem(problem_id, prompt_type, technique, variation, model, language, log_path, samples)
            time.sleep(20)  # For GPT-4 rate limit
