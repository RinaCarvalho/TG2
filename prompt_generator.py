import typo

class PromptGenerator:
    def __init__(self, prompt, problem, technique = 0, variation = 0):
        self.prompt = prompt
        self.problem = problem
        self.technique = technique
        self.variation = variation
    

    def generate_prompt_series(self):
        # problem here refers to the codename I have given the problem or sth
        return f"{self.problem}_t{self.technique}_v{self.variation}"
    
    def generate_modified_prompt(self):
        if self.variation == 1:
            self.prompt = self._generate_typo(self.prompt)

        return self.prompt

    def _generate_typo(prompt):
        return typo.StrErrer(prompt)
         