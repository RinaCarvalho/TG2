# TODO: Everywhere: document methods (docstrings)

from prompt_generator import PromptGenerator
from code_generator import CodeGenerator
from utils import extract_prompt_from_problem, write_to_jsonl

model = "gpt-3.5-turbo"
language = "Python"
problem_id = "HE162"
prompt_type = "0-shot"

if __name__ == "__main__":
    write_to_jsonl()
    prompt = extract_prompt_from_problem(problem_id=problem_id, prompt_type=prompt_type)

    if prompt:
        prompt_gen = PromptGenerator(prompt=prompt, problem=problem_id)
        prompt_series = prompt_gen.generate_prompt_series()
        code_gen = CodeGenerator(model=model, language=language)
        code_gen.generate_code(prompt_series, prompt, 7)
