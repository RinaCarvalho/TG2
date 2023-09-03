from enum import Enum

TYPO_LIST = [
    'char_swap',
    'missing_char',
    'extra_char',
    'nearby_char',
    'skipped_space',
    'random_space',
    'repeated_char',
    'unichar',
]

class Technique(Enum):
    ZERO_SHOT = 0
    FEW_SHOT = 1
    CHAIN_OF_THOUGHT = 2

class Variation(Enum):
    NONE = 0
    TYPO = 1
    FORMATTING = 2
    FORMULATION = 3

