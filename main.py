# TODO: Everywhere: document methods (docstrings)

from prompt_generator import PromptGenerator
from prompt_constants import Technique, Variation
from code_generator import CodeGenerator
from utils import extract_prompt_from_problem, write_to_jsonl

model = "gpt-3.5-turbo"
language = "Python"
problem_id = "YTDL1"
prompt_type = "0-shot"
log_path = "logs/GPT_35_t1_v0"

if __name__ == "__main__":
    write_to_jsonl()
    prompt = extract_prompt_from_problem(problem_id=problem_id, prompt_type=prompt_type)

    if prompt:
        prompt_gen = PromptGenerator(prompt=prompt, problem=problem_id, technique=Technique.FEW_SHOT, variation=Variation.NONE)
        prompt_series = prompt_gen.generate_prompt_series()
        prompt = prompt_gen.generate_modified_prompt()
        code_gen = CodeGenerator(model=model, language=language)
        code_gen.generate_code(prompt_series, prompt, 1, log_path)
