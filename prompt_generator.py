import typo
import random
from prompt_constants import Technique, Variation, TYPO_LIST

class PromptGenerator:
    def __init__(self, prompt, problem, technique = Technique.ZERO_SHOT, variation = Variation.NONE):
        self.prompt = prompt
        self.problem = problem
        self.technique = technique.value
        self.variation = variation.value
    

    def generate_prompt_series(self):
        # problem here refers to the codename I have given the problem or sth
        return f"{self.problem}_t{self.technique}_v{self.variation}"
    
    def generate_modified_prompt(self):
        if self.variation == Variation.TYPO.value:
            self.prompt = self._generate_prompt_with_typos(self.prompt)

        return self.prompt

    def _generate_prompt_with_typos(self, prompt):
        MIN_ERRORS = 1
        MAX_ERRORS = int(len(prompt) / 20)   # max of 5 typos every 100 chars
        num_typos = random.randint(MIN_ERRORS, MAX_ERRORS)
        
        prompt_with_typos = prompt

        for i in range(num_typos):
            strErrer = typo.StrErrer(prompt_with_typos)
            selected_method = random.choice(TYPO_LIST)
            selected_method_to_call = getattr(strErrer, selected_method)
            prompt_with_typos = selected_method_to_call().result

        return prompt_with_typos
    
         