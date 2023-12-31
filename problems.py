data = [
    {
        "problem_id": "HE4",
        "problem_description": "Write function to calculate mean absolute deviation",
        "prompts": [
            {
                "0-shot": "For a given list of input numbers, write a function to calculate the Mean Absolute Deviation around the mean of the dataset. The function must receive a List of floats as input and return a float."
            },
            {
                "original": "from typing import List\n\n\ndef mean_absolute_deviation(numbers: List[float]) -> float:\n    \"\"\" For a given list of input numbers, calculate Mean Absolute Deviation\n    around the mean of this dataset.\n    Mean Absolute Deviation is the average absolute difference between each\n    element and a centerpoint (mean in this case):\n    MAD = average | x - x_mean |\n    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])\n    1.0\n    \"\"\"\n",
                "entry_point": "mean_absolute_deviation",
                "canonical_solution": "    mean = sum(numbers) / len(numbers)\n    return sum(abs(x - mean) for x in numbers) / len(numbers)\n",
                "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[1.0, 2.0, 3.0, 4.0]",
                "output": "1.0"
            },
            {
                "input": "[-3.2, -1, 0.5, 2.5]",
                "output": "1.8"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[1.0, 2.0, 3.0, 4.0]",
                "output": "2.5"
            },
            {
                "input": "[-3.2, -1, 0.5, 2.5]",
                "output": "-0.3"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[1.0, 2.0, 3.0, 4.0]",
                "output": "1,0"
            },
            {
                "input": "[-3.2, -1, 0.5, 2.5]",
                "output": "1,8"
            }
        ],
        "tests": [
            {
                "inputs": [
                    [1.0, 2.0, 3.0, 4.0]
                ],
                "output": 1.0
            },
            {
                "inputs": [
                    [-3.2, -1, 0.5, 2.5]
                ],
                "output": 1.8
            },
            {
                "inputs": [
                    [1.0, 1.0]
                ],
                "output": 0.0
            },
            {
                "inputs": [
                    [5.0]
                ],
                "output": 0.0
            },
            {
                "inputs": [
                    [1.0, -1.0, 1.0, -1.0]
                ],
                "output": 1.0
            }
        ]
    },
    {
        "problem_id": "HE6",
        "problem_description": "Write function to find the deepest level of nesting of parentheses.",
        "prompts": [
            {
                "0-shot": "For a given string with multiple groups of nested parentheses, write a function to determine the deepest level of nesting of the parentheses. The function must receive a string as input and return an integer."
            },
            {
                "original": "from typing import List\n\n\ndef parse_nested_parens(paren_string: str) -> List[int]:\n    \"\"\" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.\n    For each of the group, output the deepest level of nesting of parentheses.\n    E.g. (()()) has maximum two levels of nesting while ((())) has three.\n\n    >>> parse_nested_parens('(()()) ((())) () ((())()())')\n    [2, 3, 1, 3]\n    \"\"\"\n",
                "entry_point": "parse_nested_parens",
                "canonical_solution": "    def parse_paren_group(s):\n        depth = 0\n        max_depth = 0\n        for c in s:\n            if c == '(':\n                depth += 1\n                max_depth = max(depth, max_depth)\n            else:\n                depth -= 1\n\n        return max_depth\n\n    return [parse_paren_group(x) for x in paren_string.split(' ') if x]\n",
                "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]\n    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]\n    assert candidate('(()(())((())))') == [4]\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "()",
                "output": "1"
            },
            {
                "input": "((())()())",
                "output": "3"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "()",
                "output": "2"
            },
            {
                "input": "((())()())",
                "output": "10"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "()",
                "output": "1"
            },
            {
                "input": "((())()()",
                "output": "3"
            }
        ],
        "tests": [
            {
                "inputs": ["()"],
                "output": 1
            },
            {
                "inputs": ["((())()())"],
                "output": 3
            },
            {
                "inputs": ["(()()())"],
                "output": 2
            },
            {
                "inputs": ["(((()(()))()))"],
                "output": 5
            },
            {
                "inputs": ["(()((())))"],
                "output": 4
            }
        ]
    },
    {
        "problem_id": "HE11",
        "problem_description": "Write function to perform logical XOR",
        "prompts": [
            {
                "0-shot": "For two given strings, consisting only of 0s and 1s, write a function that performs binary XOR on the inputs. The function must receive two strings as inputs and return a string."
            },
            {
                "original": "from typing import List\n\n\ndef string_xor(a: str, b: str) -> str:\n    \"\"\" Input are two strings a and b consisting only of 1s and 0s.\n    Perform binary XOR on these inputs and return result also as a string.\n    >>> string_xor('010', '110')\n    '100'\n    \"\"\"\n",
                "entry_point": "string_xor",
                "canonical_solution": "    def xor(i, j):\n        if i == j:\n            return '0'\n        else:\n            return '1'\n\n    return ''.join(xor(x, y) for x, y in zip(a, b))\n",
                "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('111000', '101010') == '010010'\n    assert candidate('1', '1') == '0'\n    assert candidate('0101', '0000') == '0101'\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": [
                    "010",
                    "110"
                ],
                "output": "100"
            },
            {
                "input": [
                    "1",
                    "0"
                ],
                "output": "1"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["010", "110"],
                "output": "110"
            },
            {
                "input": ["1", "0"],
                "output": "1"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["010", "110"],
                "output": "10"
            },
            {
                "input": ["1", "0"],
                "output": "1"
            }
        ],
        "tests": [
            {
                "inputs": ["010", "110"],
                "output": "100"
            },
            {
                "inputs": ["0", "0"],
                "output": "0"
            },
            {
                "inputs": ["1", "0"],
                "output": "1"
            },
            {
                "inputs": ["0", "1"],
                "output": "1"
            },
            {
                "inputs": ["1", "1"],
                "output": "0"
            },
            {
                "inputs": ["001001", "100100"],
                "output": "101101"
            }
        ]
    },
    {
        "problem_id": "HE18",
        "problem_description": "Write function to count how many substring occurrences in string",
        "prompts": [
            {
                "0-shot": "For two given strings, write a function to count how many times the second string can be found in the first string, incluing overlapping cases. The function must receive two strings as inputs and return an integer."
            },
            {
                "original": "\n\ndef how_many_times(string: str, substring: str) -> int:\n    \"\"\" Find how many times a given substring can be found in the original string. Count overlaping cases.\n    >>> how_many_times('', 'a')\n    0\n    >>> how_many_times('aaa', 'a')\n    3\n    >>> how_many_times('aaaa', 'aa')\n    3\n    \"\"\"\n",
                "entry_point": "how_many_times",
                "canonical_solution": "    times = 0\n\n    for i in range(len(string) - len(substring) + 1):\n        if string[i:i+len(substring)] == substring:\n            times += 1\n\n    return times\n",
                "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('', 'x') == 0\n    assert candidate('xyxyxyx', 'x') == 4\n    assert candidate('cacacacac', 'cac') == 4\n    assert candidate('john doe', 'john') == 1\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": [
                    "",
                    "a"
                ],
                "output": "0"
            },
            {
                "input": [
                    "aaa",
                    "a"
                ],
                "output": "3"
            },
            {
                "input": [
                    "aaa",
                    "aa"
                ],
                "output": "2"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["a", ""],
                "output": "0"
            },
            {
                "input": ["a", "aaa"],
                "output": "3"
            },
            {
                "input": ["aa", "aaa"],
                "output": "2"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["", "a"],
                "output": "0"
            },
            {
                "input": ("aaa", "a"),
                "output": "3"
            },
            {
                "input": ["aaa", "aa"],
                "output": "2"
            }
        ],
        "tests": [
            {
                "inputs": ["", "string"],
                "output": 0
            },
            {
                "inputs": ["aaa", "a"],
                "output": 3
            },
            {
                "inputs": ["aaa", "aa"],
                "output": 2
            },
            {
                "inputs": ["substring", "string"],
                "output": 1
            },
            {
                "inputs": ["A string with spaces", " "],
                "output": 3
            }
        ]
    },
    {
        "problem_id": "HE31",
        "problem_description": "Write function to determine whether number is prime",
        "prompts": [
            {
                "0-shot": "For a given integer, write a function to check if the number is a prime number. The function must receive an integer as input and return a boolean."
            },
            {
                "original": "\n\ndef is_prime(n):\n    \"\"\"Return true if a given number is prime, and false otherwise.\n    >>> is_prime(6)\n    False\n    >>> is_prime(101)\n    True\n    >>> is_prime(11)\n    True\n    >>> is_prime(13441)\n    True\n    >>> is_prime(61)\n    True\n    >>> is_prime(4)\n    False\n    >>> is_prime(1)\n    False\n    \"\"\"\n",
                "entry_point": "is_prime",
                "canonical_solution": "    if n < 2:\n        return False\n    for k in range(2, n - 1):\n        if n % k == 0:\n            return False\n    return True\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate(6) == False\n    assert candidate(101) == True\n    assert candidate(11) == True\n    assert candidate(13441) == True\n    assert candidate(61) == True\n    assert candidate(4) == False\n    assert candidate(1) == False\n    assert candidate(5) == True\n    assert candidate(11) == True\n    assert candidate(17) == True\n    assert candidate(5 * 17) == False\n    assert candidate(11 * 7) == False\n    assert candidate(13441 * 19) == False\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "6",
                "output": "False"
            },
            {
                "input": "11",
                "output": "True"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "1",
                "output": "True"
            },
            {
                "input": "2",
                "output": "True"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "6",
                "output": "0"
            },
            {
                "input": "11",
                "output": "1"
            }
        ],
        "tests": [
            {
                "inputs": [1],
                "output": False
            },
            {
                "inputs": [2],
                "output": True
            },
            {
                "inputs": [5],
                "output": True
            },
            {
                "inputs": [6],
                "output": False
            },
            {
                "inputs": [11],
                "output": True
            },
            {
                "inputs": [23],
                "output": True
            },
            {
                "inputs": [24],
                "output": False
            },
            {
                "inputs": [13441],
                "output": True
            },
            {
                "inputs": [13441 * 2],
                "output": False
            }
        ]
    },
    {
        "problem_id": "HE44",
        "problem_description": "Write function to change base of number",
        "prompts": [
            {
                "0-shot": "For two given numbers, convert the first number from decimal base to the base represented by the second number. The function must receive two integers as inputs and return an string."
            },
            {
                "original": "\n\ndef change_base(x: int, base: int):\n    \"\"\"Change numerical base of input number x to base.\n    return string representation after the conversion.\n    base numbers are less than 10.\n    >>> change_base(8, 3)\n    '22'\n    >>> change_base(8, 2)\n    '1000'\n    >>> change_base(7, 2)\n    '111'\n    \"\"\"\n",
                "entry_point": "change_base",
                "canonical_solution": "    ret = \"\"\n    while x > 0:\n        ret = str(x % base) + ret\n        x //= base\n    return ret\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate(8, 3) == \"22\"\n    assert candidate(9, 3) == \"100\"\n    assert candidate(234, 2) == \"11101010\"\n    assert candidate(16, 2) == \"10000\"\n    assert candidate(8, 2) == \"1000\"\n    assert candidate(7, 2) == \"111\"\n    for x in range(2, 8):\n        assert candidate(x, x + 1) == str(x)\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[8, 3]",
                "output": "22"
            },
            {
                "input": "[8, 2]",
                "output": "1000"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[8, 3]",
                "output": "3"
            },
            {
                "input": "[8, 2]",
                "output": "2"
            }
        ],
        "misformatted_inputs": [
            {
                "input": [8, 3],
                "output": "22"
            },
            {
                "input": [8, 2],
                "output": "1000"
            }
        ],
        "tests": [
            {
                "inputs": [8, 3],
                "output": "22"
            },
            {
                "inputs": [8, 2],
                "output": "1000"
            },
            {
                "inputs": [7, 8],
                "output": "7"
            },
            {
                "inputs": [15325, 10],
                "output": "15325"
            },
            {
                "inputs": [234, 2],
                "output": "11101010"
            }
        ]
    },
    {
        "problem_id": "HE48",
        "problem_description": "Write function to check if a string is a palindrome.",
        "prompts": [
            {
                "0-shot": "For a given string, write a function to check whether the string is a palindrome. The function must receive a string as input and return a boolean."
            },
            {
                "original": "\n\ndef is_palindrome(text: str):\n    \"\"\"\n    Checks if given string is a palindrome\n    >>> is_palindrome('')\n    True\n    >>> is_palindrome('aba')\n    True\n    >>> is_palindrome('aaaaa')\n    True\n    >>> is_palindrome('zbcd')\n    False\n    \"\"\"\n",
                "entry_point": "is_palindrome",
                "canonical_solution": "    for i in range(len(text)):\n        if text[i] != text[len(text) - 1 - i]:\n            return False\n    return True\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate('') == True\n    assert candidate('aba') == True\n    assert candidate('aaaaa') == True\n    assert candidate('zbcd') == False\n    assert candidate('xywyx') == True\n    assert candidate('xywyz') == False\n    assert candidate('xywzx') == False\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "abcba",
                "output": "True"
            },
            {
                "input": "zbcd",
                "output": "False"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "abcba",
                "output": "True"
            },
            {
                "input": "zbcd",
                "output": "True"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "abcba",
                "output": "1"
            },
            {
                "input": "zbcd",
                "output": "0"
            }
        ],
        "tests": [
            {
                "inputs": ["abcba"],
                "output": True
            },
            {
                "inputs": ["zbcd"],
                "output": False
            },
            {
                "inputs": ["aaaaaaa"],
                "output": True
            },
            {
                "inputs": [""],
                "output": True
            },
            {
                "inputs": ["abccba"],
                "output": True
            },
            {
                "inputs": ["Palindrome"],
                "output": False
            },
            {
                "inputs": ["abcba"],
                "output": True
            }
        ]
    },
    {
        "problem_id": "HE51",
        "problem_description": "Write function to remove vowels from string",
        "prompts": [
            {
                "0-shot": "For a given string, write a function to remove the vowels from the string. The function must receive a string as input and return a string."
            },
            {
                "original": "\n\ndef remove_vowels(text):\n    \"\"\"\n    remove_vowels is a function that takes string and returns string without vowels.\n    >>> remove_vowels('')\n    ''\n    >>> remove_vowels(\"abcdef\\nghijklm\")\n    'bcdf\\nghjklm'\n    >>> remove_vowels('abcdef')\n    'bcdf'\n    >>> remove_vowels('aaaaa')\n    ''\n    >>> remove_vowels('aaBAA')\n    'B'\n    >>> remove_vowels('zbcd')\n    'zbcd'\n    \"\"\"\n",
                "entry_point": "remove_vowels",
                "canonical_solution": "    return \"\".join([s for s in text if s.lower() not in [\"a\", \"e\", \"i\", \"o\", \"u\"]])\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate('') == ''\n    assert candidate(\"abcdef\\nghijklm\") == 'bcdf\\nghjklm'\n    assert candidate('fedcba') == 'fdcb'\n    assert candidate('eeeee') == ''\n    assert candidate('acBAA') == 'cB'\n    assert candidate('EcBOO') == 'cB'\n    assert candidate('ybcd') == 'ybcd'\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "abcdef",
                "output": "bcdf"
            },
            {
                "input": "aeiou",
                "output": ""
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "abcdef",
                "output": "bcdf"
            },
            {
                "input": "aeiou",
                "output": ""
            },
            {
                "input": "always",
                "output": "lws"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "abcdef",
                "output": "bcdf"
            },
            {
                "input": "aeiou",
                "output": None
            }
        ],
        "tests": [
            {
                "inputs": ["abcdef"],
                "output": "bcdf"
            },
            {
                "inputs": ["aeiou"],
                "output": ""
            },
            {
                "inputs": ["A string with vowels"],
                "output": " strng wth vwls"
            },
            {
                "inputs": ["aAbBcC"],
                "output": "bBcC"
            },
            {
                "inputs": ["yaml"],
                "output": "yml"
            }
        ]
    },
    {
        "problem_id": "HE55",
        "problem_description": "Write function to return n-th Fibonacci number",
        "prompts": [
            {
                "0-shot": "For a given number n, write a function to determine the n-th Fibonacci number, starting from 1 and 1. The function must receive an integer as input and return an integer."
            },
            {
                "original": "\n\ndef fib(n: int):\n    \"\"\"Return n-th Fibonacci number.\n    >>> fib(10)\n    55\n    >>> fib(1)\n    1\n    >>> fib(8)\n    21\n    \"\"\"\n",
                "entry_point": "fib",
                "canonical_solution": "    if n == 0:\n        return 0\n    if n == 1:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate(10) == 55\n    assert candidate(1) == 1\n    assert candidate(8) == 21\n    assert candidate(11) == 89\n    assert candidate(12) == 144\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "10",
                "output": "55"
            },
            {
                "input": "1",
                "output": "1"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "10",
                "output": "34"
            },
            {
                "input": "1",
                "output": "0"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "10",
                "output": "'55'"
            },
            {
                "input": "1",
                "output": "'1"
            }
        ],
        "tests": [
            {
                "inputs": [1],
                "output": 1
            },
            {
                "inputs": [2],
                "output": 1
            },
            {
                "inputs": [3],
                "output": 2
            },
            {
                "inputs": [10],
                "output": 55
            },
            {
                "inputs": [12],
                "output": 144
            }
        ]
    },
    {
        "problem_id": "HE89",
        "problem_description": "Write function to encrypt string with alphabet rotation",
        "prompts": [
            {
                "0-shot": "For a given string, write a function that encrypts the string using a Caesar cipher with a shift corresponding to a given number. The function must receive a string and a number as inputs and return a string."
            },
            {
                "original": "\ndef encrypt(s):\n    \"\"\"Create a function encrypt that takes a string as an argument and\n    returns a string encrypted with the alphabet being rotated. \n    The alphabet should be rotated in a manner such that the letters \n    shift down by two multiplied to two places.\n    For example:\n    encrypt('hi') returns 'lm'\n    encrypt('asdfghjkl') returns 'ewhjklnop'\n    encrypt('gf') returns 'kj'\n    encrypt('et') returns 'ix'\n    \"\"\"\n",
                "entry_point": "encrypt",
                "canonical_solution": "    d = 'abcdefghijklmnopqrstuvwxyz'\n    out = ''\n    for c in s:\n        if c in d:\n            out += d[(d.index(c)+2*2) % 26]\n        else:\n            out += c\n    return out\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate('hi') == 'lm', \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('asdfghjkl') == 'ewhjklnop', \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('gf') == 'kj', \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('et') == 'ix', \"This prints if this assert fails 1 (good for debugging!)\"\n\n    assert candidate('faewfawefaewg')=='jeiajeaijeiak', \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('hellomyfriend')=='lippsqcjvmirh', \"This prints if this assert fails 2 (good for debugging!)\"\n    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh')=='hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', \"This prints if this assert fails 3 (good for debugging!)\"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert candidate('a')=='e', \"This prints if this assert fails 2 (also good for debugging!)\"\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": [
                    "hi",
                    "2"
                ],
                "output": "jk"
            },
            {
                "input": [
                    "asdfghjkl",
                    "4"
                ],
                "output": "ewhjklnop"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["hi", "2"],
                "output": "fg"
            },
            {
                "input": ["asdfghjkl", "4"],
                "output": "wozbcdfgh"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["hi", "2"],
                "output": "jk"
            },
            {
                "input": ["asdfghjkl", "4"],
                "output": "ewhjklno"
            }
        ],
        "tests": [
            {
                "inputs": ["hi", 2],
                "output": "jk"
            },
            {
                "inputs": ["asdfghjkl", 4],
                "output": "ewhjklnop"
            },
            {
                "inputs": ["Caesar Cipher", 9],
                "output": "Ljnbja Lryqna"
            },
            {
                "inputs": ["Thirteen", 13],
                "output": "Guvegrra"
            },
            {
                "inputs": ["dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh", 4],
                "output": "hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl"
            }
        ]
    },
    {
        "problem_id": "HE111",
        "problem_description": "Write function to count number of occurences of each character in a string",
        "prompts": [
            {
                "0-shot": "For a given string, write a function that counts the number of occurrences of each letter in the string, displaying each letter and its number of occurrences as a key-value pair in a dictionary. The function must receive a string as input and return a dictionary."
            },
            {
                "original": "\ndef histogram(test):\n    \"\"\"Given a string representing a space separated lowercase letters, return a dictionary\n    of the letter with the most repetition and containing the corresponding count.\n    If several letters have the same occurrence, return all of them.\n    \n    Example:\n    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}\n    histogram('a b b a') == {'a': 2, 'b': 2}\n    histogram('a b c a b') == {'a': 2, 'b': 2}\n    histogram('b b b b a') == {'b': 4}\n    histogram('') == {}\n\n    \"\"\"\n",
                "entry_point": "histogram",
                "canonical_solution": "    dict1={}\n    list1=test.split(\" \")\n    t=0\n\n    for i in list1:\n        if(list1.count(i)>t) and i!='':\n            t=list1.count(i)\n    if t>0:\n        for i in list1:\n            if(list1.count(i)==t):\n                \n                dict1[i]=t\n    return dict1\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate('a b b a') == {'a':2,'b': 2}, \"This prints if this assert fails 1 (good for debugging!)\"\n    assert candidate('a b c a b') == {'a': 2, 'b': 2}, \"This prints if this assert fails 2 (good for debugging!)\"\n    assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, \"This prints if this assert fails 3 (good for debugging!)\"\n    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, \"This prints if this assert fails 4 (good for debugging!)\"\n    assert candidate('b b b b a') == {'b': 4}, \"This prints if this assert fails 5 (good for debugging!)\"\n    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}, \"This prints if this assert fails 6 (good for debugging!)\"\n    \n    \n    # Check some edge cases that are easy to work out by hand.\n    assert candidate('') == {}, \"This prints if this assert fails 7 (also good for debugging!)\"\n    assert candidate('a') == {'a': 1}, \"This prints if this assert fails 8 (also good for debugging!)\"\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "abc",
                "output": "{'a': 1, 'b': 1, 'c': 1}"
            },
            {
                "input": "abcbaa",
                "output": "{'a': 3, 'b': 2, 'c': 1}"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "abc",
                "output": "{'a': 1, 'b': 1, 'c': 1}"
            },
            {
                "input": "acbbaa",
                "output": "{'a': 3, 'b': 2, 'c': 1}"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "abc",
                "output": "{'a': 1, 'b': 1, 'c': 1}"
            },
            {
                "input": "abcbaa",
                "output": "{'a': 3, 'b': 2}"
            }
        ],
        "tests": [
            {
                "inputs": ["abc"],
                "output": {'a': 1, 'b': 1, 'c': 1}
            },
            {
                "inputs": ["abcbaa"],
                "output": {'a': 3, 'b': 2, 'c': 1}
            },
            {
                "inputs": ["bbbbba"],
                "output": {'b': 5, 'a': 1}
            },
            {
                "inputs": [''],
                "output": {}
            },
            {
                "inputs": ['a'],
                "output": {'a': 1}
            }
        ]
    },
    {
        "problem_id": "HE124",
        "problem_description": "Write function to validate date",
        "prompts": [
            {
                "0-shot": "For a given date string, write a function that checks whether the date is valid. A date is considered valid if it has a valid month and a valid number of days for its corresponding month, and if it has the format 'mm-dd-yyyy'. The function must receive a string as input and return a boolean."
            },
            {
                "original": "\ndef valid_date(date):\n    \"\"\"You have to write a function which validates a given date string and\n    returns True if the date is valid otherwise False.\n    The date is valid if all of the following rules are satisfied:\n    1. The date string is not empty.\n    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.\n    3. The months should not be less than 1 or higher than 12.\n    4. The date should be in the format: mm-dd-yyyy\n\n    for example: \n    valid_date('03-11-2000') => True\n\n    valid_date('15-01-2012') => False\n\n    valid_date('04-0-2040') => False\n\n    valid_date('06-04-2020') => True\n\n    valid_date('06/04/2020') => False\n    \"\"\"\n",
                "entry_point": "valid_date",
                "canonical_solution": "    try:\n        date = date.strip()\n        month, day, year = date.split('-')\n        month, day, year = int(month), int(day), int(year)\n        if month < 1 or month > 12:\n            return False\n        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:\n            return False\n        if month in [4,6,9,11] and day < 1 or day > 30:\n            return False\n        if month == 2 and day < 1 or day > 29:\n            return False\n    except:\n        return False\n\n    return True\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate('03-11-2000') == True\n\n    assert candidate('15-01-2012') == False\n\n    assert candidate('04-0-2040') == False\n\n    assert candidate('06-04-2020') == True\n\n    assert candidate('01-01-2007') == True\n\n    assert candidate('03-32-2011') == False\n\n    assert candidate('') == False\n\n    assert candidate('04-31-3000') == False\n\n    assert candidate('06-06-2005') == True\n\n    assert candidate('21-31-2000') == False\n\n    assert candidate('04-12-2003') == True\n\n    assert candidate('04122003') == False\n\n    assert candidate('20030412') == False\n\n    assert candidate('2003-04') == False\n\n    assert candidate('2003-04-12') == False\n\n    assert candidate('04-2003') == False\n"
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must determine whether the date is formatted correctly. Then if the format is correct, we must determine whether the date exists, by verifying the number of days in a month and whether the year is a leap year or not. In the example, '03-11-2000' follows the required 'mm-dd-yyyy' format. Additionally, March 11th of the year 2000 is an existing date. Therefore, '03-11-2000' is a valid date.",
        "input_examples": [
            {
                "input": "03-11-2000",
                "output": "True"
            },
            {
                "input": "15-01-2012",
                "output": "False"
            },
            {
                "input": "06/04/1998",
                "output": "False"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "03-11-2000",
                "output": "True"
            },
            {
                "input": "15-01-2012",
                "output": "False"
            },
            {
                "input": "06/04/1998",
                "output": "True"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "3-11-2000",
                "output": "True"
            },
            {
                "input": "15-1-2012",
                "output": "False"
            },
            {
                "input": "06/04/1998",
                "output": "False"
            }
        ],
        "tests": [
            {
                "inputs": ["03-11-2000"],
                "output": True
            },
            {
                "inputs": ["15-01-2012"],
                "output": False
            },
            {
                "inputs": ["06/04/1998"],
                "output": False
            },
            {
                "inputs": ["02-0-2009"],
                "output": False
            },
            {
                "inputs": ["12-31-2000"],
                "output": True
            },
            {
                "inputs": ["02-31-1999"],
                "output": False
            },
            {
                "inputs": ["02.02.1990"],
                "output": False
            },
            {
                "inputs": ["01-01-2023"],
                "output": True
            }
        ]
    },
    {
        "problem_id": "HE127",
        "problem_description": "Write function to determine the intersection between two intervals",
        "prompts": [
            {
                "0-shot": "For two given closed intervals, write a function to determine the intersection between them. The function must receive two tuples of two integers each as input and return a tuple of two integers, if the length of the intersection is larger than 1, or a single integer otherwise."
            },
            {
                "original": "\ndef intersection(interval1, interval2):\n    \"\"\"You are given two intervals,\n    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).\n    The given intervals are closed which means that the interval (start, end)\n    includes both start and end.\n    For each given interval, it is assumed that its start is less or equal its end.\n    Your task is to determine whether the length of intersection of these two \n    intervals is a prime number.\n    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)\n    which its length is 1, which not a prime number.\n    If the length of the intersection is a prime number, return \"YES\",\n    otherwise, return \"NO\".\n    If the two intervals don't intersect, return \"NO\".\n\n\n    [input/output] samples:\n    intersection((1, 2), (2, 3)) ==> \"NO\"\n    intersection((-1, 1), (0, 4)) ==> \"NO\"\n    intersection((-3, -1), (-5, 5)) ==> \"YES\"\n    \"\"\"\n",
                "entry_point": "intersection",
                "canonical_solution": "    def is_prime(num):\n        if num == 1 or num == 0:\n            return False\n        if num == 2:\n            return True\n        for i in range(2, num):\n            if num%i == 0:\n                return False\n        return True\n\n    l = max(interval1[0], interval2[0])\n    r = min(interval1[1], interval2[1])\n    length = r - l\n    if length > 0 and is_prime(length):\n        return \"YES\"\n    return \"NO\"\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate((1, 2), (2, 3)) == \"NO\"\n    assert candidate((-1, 1), (0, 4)) == \"NO\"\n    assert candidate((-3, -1), (-5, 5)) == \"YES\"\n    assert candidate((-2, 2), (-4, 0)) == \"YES\"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert candidate((-11, 2), (-1, -1)) == \"NO\"\n    assert candidate((1, 2), (3, 5)) == \"NO\"\n    assert candidate((1, 2), (1, 2)) == \"NO\"\n    assert candidate((-2, -2), (-3, -2)) == \"NO\"\n\n"
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must compare the start of each interval and find the maximum of the two. Let us call it a1. Then, we must compare the end of each interval and find the minimum of the two. Let us call it a2. Lastly, these values must be compared. If a1 < a2, the intersection is (a1, a2). If a1 = a2, the intersection is a1. If a1 > a2, the intersection does not exist. In the example, a1 = 2, a2 = 3. Given that a1 < a2, the intersection is (2, 3)",
        "input_examples": [
            {
                "input": [
                    "(1, 3)",
                    "(2, 4)"
                ],
                "output": "(2, 3)"
            },
            {
                "input": [
                    "(1, 2)",
                    "(2, 3)"
                ],
                "output": "2"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["(1, 3)", "(2, 4)"],
                "output": "(2, 3)"
            },
            {
                "input": ["(1, 2)", "(2, 3)"],
                "output": "(2, 2)"
            }
        ],
        "misformatted_inputs": [
            {
                "input": [(1, 3), (2, 4)],
                "output": "'(2, 3)'"
            },
            {
                "input": [(1, 2), (2, 3)],
                "output": "'2'"
            }
        ],
        "tests": [
            {
                "inputs": [(1,3), (2,4)],
                "output": (2,3)
            },
            {
                "inputs": [(1,2), (2,3)],
                "output": 2
            },
            {
                "inputs": [(-1,2), (0,2)],
                "output": (0,2)
            },
            {
                "inputs": [(0,5), (2,3)],
                "output": (2,3)
            },
            {
                "inputs": [(-5,-1), (-2,0)],
                "output": (-2,-1)
            }
        ]
    },
    {
        "problem_id": "HE156",
        "problem_description": "Write function to convert to roman numerals",
        "prompts": [
            {
                "0-shot": "For a given integer, write a function to convert the number to uppercase roman numerals. The function must receive an integer as input and return a string."
            },
            {
                "original": "\ndef int_to_mini_roman(number):\n    \"\"\"\n    Given a positive integer, obtain its roman numeral equivalent as a string,\n    and return it in lowercase.\n    Restrictions: 1 <= num <= 1000\n\n    Examples:\n    >>> int_to_mini_roman(19) == 'xix'\n    >>> int_to_mini_roman(152) == 'clii'\n    >>> int_to_mini_roman(426) == 'cdxxvi'\n    \"\"\"\n",
                "entry_point": "int_to_mini_roman",
                "canonical_solution": "    num = [1, 4, 5, 9, 10, 40, 50, 90,  \n           100, 400, 500, 900, 1000] \n    sym = [\"I\", \"IV\", \"V\", \"IX\", \"X\", \"XL\",  \n           \"L\", \"XC\", \"C\", \"CD\", \"D\", \"CM\", \"M\"] \n    i = 12\n    res = ''\n    while number: \n        div = number // num[i] \n        number %= num[i] \n        while div: \n            res += sym[i] \n            div -= 1\n        i -= 1\n    return res.lower()\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate(19) == 'xix'\n    assert candidate(152) == 'clii'\n    assert candidate(251) == 'ccli'\n    assert candidate(426) == 'cdxxvi'\n    assert candidate(500) == 'd'\n    assert candidate(1) == 'i'\n    assert candidate(4) == 'iv'\n    assert candidate(43) == 'xliii'\n    assert candidate(90) == 'xc'\n    assert candidate(94) == 'xciv'\n    assert candidate(532) == 'dxxxii'\n    assert candidate(900) == 'cm'\n    assert candidate(994) == 'cmxciv'\n    assert candidate(1000) == 'm'\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "19",
                "output": "XIX"
            },
            {
                "input": "426",
                "output": "CDXXVI"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "19",
                "output": "xix"
            },
            {
                "input": "426",
                "output": "cdxxvi"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "19",
                "output": "XIX"
            },
            {
                "input": "426",
                "output": "CDXXVII"
            }
        ],
        "tests": [
            {
                "inputs": [19],
                "output": "XIX"
            },
            {
                "inputs": [426],
                "output": "CDXXVI"
            },
            {
                "inputs": [1],
                "output": "I"
            },
            {
                "inputs": [1992],
                "output": "MCMXCII"
            },
            {
                "inputs": [46],
                "output": "XLVI"
            }
        ]
    },
    {
        "problem_id": "HE160",
        "problem_description": "Write function that performs algebraic operation depending on operator",
        "prompts": [
            {
                "0-shot": "Given a list of integers and a list of operations, write a function that builds an algebraic expression by sequentially placing each operation in the list of operations between two integers in the list of integers, and calculates the result of this expression. The function must receive a list of integers and a list of strings and return an integer."
            },
            {
                "original": "\ndef do_algebra(operator, operand):\n    \"\"\"\n    Given two lists operator, and operand. The first list has basic algebra operations, and \n    the second list is a list of integers. Use the two given lists to build the algebric \n    expression and return the evaluation of this expression.\n\n    The basic algebra operations:\n    Addition ( + ) \n    Subtraction ( - ) \n    Multiplication ( * ) \n    Floor division ( // ) \n    Exponentiation ( ** ) \n\n    Example:\n    operator['+', '*', '-']\n    array = [2, 3, 4, 5]\n    result = 2 + 3 * 4 - 5\n    => result = 9\n\n    Note:\n        The length of operator list is equal to the length of operand list minus one.\n        Operand is a list of of non-negative integers.\n        Operator list has at least one operator, and operand list has at least two operands.\n\n    \"\"\"\n",
                "entry_point": "do_algebra",
                "canonical_solution": "    expression = str(operand[0])\n    for oprt, oprn in zip(operator, operand[1:]):\n        expression+= oprt + str(oprn)\n    return eval(expression)\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37\n    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9\n    assert candidate(['//', '*'], [7, 3, 4]) == 8, \"This prints if this assert fails 1 (good for debugging!)\"\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True, \"This prints if this assert fails 2 (also good for debugging!)\"\n\n"
            }
        ],
        "chain_of_thought": "Let's think step by step. First, the list of integers and the list of operands must be joined in order to form an expression. Then, the expression must be evaluated, respecting the priority of operands. In the example, the expression obtained by joining the inputs is 2 + 3 * 4 - 5 = 9.",
        "input_examples": [
            {
                "input": [
                    "[2, 3, 4, 5]",
                    "['+', '*', '-']"
                ],
                "output": "9"
            },
            {
                "input": [
                    "[2, 3, 4, 5]",
                    "['**', '*', '+']"
                ],
                "output": "37"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": [
                    "[2, 3, 4, 5]",
                    "['+', '*', '-']"
                ],
                "output": "15"
            },
            {
                "input": [
                    "[2, 3, 4, 5]",
                    "['**', '*', '+']"
                ],
                "output": "37"
            }
        ],
        "misformatted_inputs": [
            {
                "input": [
                    "(2, 3, 4, 5)",
                    "(+, *, -)"
                ],
                "output": "9"
            },
            {
                "input": [
                    "(2, 3, 4, 5)",
                    "(**, *, +)"
                ],
                "output": "37"
            }
        ],
        "tests": [
            {
                "inputs": [[2, 3, 4, 5], ['+', '*', '-']],
                "output": 9
            },
            {
                "inputs": [[2, 3, 4, 5], ['**', '*', '+']],
                "output": 37
            },
            {
                "inputs": [[1, 0, 5, -2], ['*', '/', '-']],
                "output": 2
            },
            {
                "inputs": [[2, 3, 4, 0], ['*', '*', '**']],
                "output": 6
            },
            {
                "inputs": [[5, 5, 5, 5], ['*', '/', '+']],
                "output": 10
            },
        ]
    },
    {
        "problem_id": "HE162",
        "problem_description": "Write function to convert string to md5 hash",
        "prompts": [
            {
                "0-shot": "For a given string, write a function that converts the string to its md5 hash. The function must receive a string as input and return a string."
            },
            {
                "original": "\ndef string_to_md5(text):\n    \"\"\"\n    Given a string 'text', return its md5 hash equivalent string.\n    If 'text' is an empty string, return None.\n\n    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'\n    \"\"\"\n",
                "entry_point": "string_to_md5",
                "canonical_solution": "    import hashlib\n    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None\n",
                "test": "def check(candidate):\n\n    # Check some simple cases\n    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'\n    assert candidate('') == None\n    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'\n    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'\n\n    # Check some edge cases that are easy to work out by hand.\n    assert True\n\n"
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "Hello world",
                "output": "3e25960a79dbc69b674cd4ec67a72c62"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "Hello world",
                "output": "0027cecd99a68653ef66259ca9572276153dad298fe359eed389bee679d864e6"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "'Hello world'",
                "output": "'3e25960a79dbc69b674cd4ec67a72c62'"
            }
        ],
        "tests": [
            {
                "inputs": ["Hello world"],
                "output": "3e25960a79dbc69b674cd4ec67a72c62"
            },
            {
                "inputs": ["password"],
                "output": "5f4dcc3b5aa765d61d8327deb882cf99"
            },
            {
                "inputs": ["A B C"],
                "output": "0ef78513b0cb8cef12743f5aeb35f888"
            },
            {
                "inputs": ["SuperSecretCredential123!"],
                "output": "c6ebb6c8a0c55764f1e4e1703e8482cb"
            }
        ]
    },
    {
        "problem_id": "MBPP12",
        "problem_description": "Write a function to sort a given matrix in ascending order according to the sum of its rows.",
        "prompts": [
            {
                "0-shot": "For a given matrix, write a function that sorts the matrix in ascending order, according to the sum of its rows. The function must receive an array of arrays as input and return an array of arrays."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[[1, 2, 3], [2, 4, 5], [1, 1, 1]]",
                "output": "[[1, 1, 1], [1, 2, 3], [2, 4, 5]]"
            },
            {
                "input": "[[1, -2, 0, 0], [-2, -3, 1, 1], [3, 4, 1, 4], [1, 0, -1, 0]]",
                "output": "[[-2, -3, 1, 1], [1, -2, 0, 0], [1, 0, -1, 0], [3, 4, 1, 4]]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[[1, 2, 3], [2, 4, 5], [1, 1, 1]]",
                "output": "[[1, 2, 3], [2, 4, 5], [1, 1, 1]]"
            },
            {
                "input": "[[1, -2, 0, 0], [-2, -3, 1, 1], [3, 4, 1, 4], [1, 0, -1, 0]]",
                "output": "[[-2, 0, 1, 0], [-3, 1, -2, 1], [4, 1, 3, 4], [0, -1, 1, 0]]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[[1, 2, 3], [2, 4, 5], [1, 1, 1]]",
                "output": "([1, 1, 1], [1, 2, 3], [2, 4, 5])"
            },
            {
                "input": "[[1, -2, 0, 0], [-2, -3, 1, 1], [3, 4, 1, 4], [1, 0, -1, 0]]",
                "output": "([-2, -3, 1, 1], [1, -2, 0, 0], [1, 0, -1, 0], [3, 4, 1, 4])"
            }
        ],
        "tests": [
            {
                "inputs": [[[1, 2, 3], [2, 4, 5], [1, 1, 1]]],
                "output": [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
            },
            {
                "inputs": [[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]],
                "output": [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
            },
            {
                "inputs": [[[5,8,9],[6,4,3],[2,1,4]]],
                "output": [[2, 1, 4], [6, 4, 3], [5, 8, 9]]
            },
            {
                "inputs": [[[1, -2, 0, 0], [-2, -3, 1, 1], [3, 4, 1, 4], [1, 0, -1, 0]]],
                "output": [[-2, -3, 1, 1], [1, -2, 0, 0], [1, 0, -1, 0], [3, 4, 1, 4]]
            },
            {
                "inputs": [[[-1, -1.2], [-3.2, 0]]],
                "output": [[-3.2, 0], [-1, -1.2]]
            }
        ]
    },
    {
        "problem_id": "MBPP59",
        "problem_description": "Write a function to find the nth octagonal number.",
        "prompts": [
            {
                "0-shot": "For a given integer n, write a function that returns the nth octagonal number. The function must receive an integer as input and return an integer."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "1",
                "output": "1"
            },
            {
                "input": "2",
                "output": "8"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "1",
                "output": "8"
            },
            {
                "input": "2",
                "output": "21"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "1",
                "output": "'1'"
            },
            {
                "input": "2",
                "output": "'8'"
            }
        ],
        "tests": [
            {
                "inputs": [1],
                "output": 1
            },
            {
                "inputs": [2],
                "output": 8
            },
            {
                "inputs": [5],
                "output": 65
            },
            {
                "inputs": [10],
                "output": 280
            },
            {
                "inputs": [15],
                "output": 645
            }
        ]
    },
    {
        "problem_id": "MBPP65",
        "problem_description": "Write a function to flatten a list and sum all of its elements.",
        "prompts": [
            {
                "0-shot": "For a given list, write a function to flatten the list and add all of its elements. The function must receive a list as input and return a number."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must check if there are any nested lists among the elements of the list. If there are any nested lists, we must iterate over the nested list, looking for other nested lists. This process must be repeated until no more nested lists are found. Then, all integers inside all nested lists must be added. In the example, first, we must check the list [3, 4]. Since there are no nested lists inside this list, we can add 3 + 4 = 7 as an intermediate result. Lastly, returning to the original list, since there are no additional lists, the sum of all elements must be 1 + 2 + 7 = 10.",
        "input_examples": [
            {
                "input": "[1, 2, [3, 4]]",
                "output": "10"
            },
            {
                "input": "[[[3], 4]]",
                "output": "7"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[1, 2, [3, 4]]",
                "output": "3"
            },
            {
                "input": "[[[3], 4]]",
                "output": "0"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[1, 2, [3, 4]",
                "output": "10"
            },
            {
                "input": "[[[3 4]]]",
                "output": "7"
            }
        ],
        "tests": [
            {
                "inputs": [[1, 2, [3, 4]]],
                "output": 10
            },
            {
                "inputs": [[[3], 4]],
                "output": 7
            },
            {
                "inputs": [[7, 10, [15,14],[19,41]]],
                "output": 106
            },
            {
                "inputs": [[10, 20, [30,40],[50,60]]],
                "output": 210
            },
            {
                "inputs": [[-2, 5, [0.5], -0.2]],
                "output": 3.3
            }
        ]
    },
    {
        "problem_id": "MBPP72",
        "problem_description": "Write a function to check whether the given number can be represented as the difference of two squares or not.",
        "prompts": [
            {
                "0-shot": "For a given number, write a function to check whether the number can be represented as the difference of two squares. The function must receive an integer as input and return a boolean."
            }
        ],
        "chain_of_thought": "Let's think step by step. An integer can be expressed as the difference between two squares only if it is not of the form 4k + 2. So, the number's remainder modulo 4 must be tested. In the example, 5 modulo 4 = 1, which means it can be represented as the difference between two squares.",
        "input_examples": [
            {
                "input": "5",
                "output": "True"
            },
            {
                "input": "10",
                "output": "False"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "2",
                "output": "True"
            },
            {
                "input": "5",
                "output": "True"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "5.0",
                "output": "True"
            },
            {
                "input": "10.0",
                "output": "False"
            }
        ],
        "tests": [
            {
                "inputs": [5],
                "output": True
            },
            {
                "inputs": [10],
                "output": False
            },
            {
                "inputs": [15],
                "output": True
            },
            {
                "inputs": [20],
                "output": True
            },
            {
                "inputs": [1],
                "output": True
            }
        ]
    },
    {
        "problem_id": "MBPP103",
        "problem_description": "Write a function to find the Eulerian number A(n,k).",
        "prompts": [
            {
                "0-shot": "For two given integers n and k, write a function to find the Eulerian number A(n, k). The function must receive two integers as inputs and return an integer."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["3", "1"],
                "output": "4"
            },
            {
                "input": ["4", "1"],
                "output": "11"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["3", "1"],
                "output": "3"
            },
            {
                "input": ["4", "1"],
                "output": "9"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["3", "1", "0"],
                "output": "4"
            },
            {
                "input": ["4", "1", "0"],
                "output": "11"
            }
        ],
        "tests": [
            {
                "inputs": [3, 1],
                "output": 4
            },
            {
                "inputs": [4, 1],
                "output": 11
            },
            {
                "inputs": [5, 3],
                "output": 26
            },
            {
                "inputs": [6, 1],
                "output": 57
            },
            {
                "inputs": [9, 2],
                "output": 14608
            }
        ]
    },
    # {
    #     "problem_id": "MBPP124",
    #     "problem_description": "Write a function to get the angle of a complex number.",
    #     "prompts": [
    #         {
    #             "0-shot": "For a given complex number, write a function to get the angle (in radians) of the number. The function must receive a complex number as input and return a float, with three precision points."
    #         }
    #     ],
    #     "input_examples": [
    #         {
    #             "input": "1j",
    #             "output": "1.571"
    #         },
    #         {
    #             "input": "2 + 1j",
    #             "output": "0.464"
    #         }
    #     ],
    #     "inaccurate_inputs": [
    #         {
    #             "input": "1j",
    #             "output": "90"
    #         },
    #         {
    #             "input": "1 + 1j",
    #             "output": "45"
    #         }
    #     ],
    #     "misformatted_inputs": [
    #         {
    #             "input": ["0", "1j"],
    #             "output": "1.571"
    #         },
    #         {
    #             "input": ["2", "1j"],
    #             "output": "0.464"
    #         }
    #     ],
    #     "tests": [
    #         {
    #             "inputs": [1j],
    #             "output": 1.571
    #         },
    #         {
    #             "inputs": [2 + 1j],
    #             "output": 0.464
    #         },
    #         {
    #             "inputs": [0 + 2j],
    #             "output": 1.571
    #         },
    #         {
    #             "inputs": [0],
    #             "output": 0
    #         },
    #         {
    #             "inputs": [1 + 1j],
    #             "output": 0.785
    #         }
    #     ]
    # },
    {
        "problem_id": "MBPP129",
        "problem_description": "Write a function to check whether the matrix is a magic square.",
        "prompts": [
            {
                "0-shot": "For a given matrix, write a function to check if the matrix is a magic square. The function must receive a list of lists and return a boolean."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[[2, 7, 6], [9, 5, 1], [4, 3, 8]]",
                "output": "True"
            },
            {
                "input": "[[2, 7, 6], [9, 5, 1], [4, 3, 7]]",
                "output": "False"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[[2, 7, 6], [9, 5, 1], [4, 3, 7]]",
                "output": "True"
            },
            {
                "input": "[[2, 7, 6], [9, 5, 1], [4, 3, 8]]",
                "output": "False"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["[2, 7, 6]", "[9, 5, 1]", "[4, 3, 8]"],
                "output": "True"
            },
            {
                "input": ["[2, 7, 6]", "[9, 5, 1]", "[4, 3, 7]"],
                "output": "False"
            }
        ],
        "tests": [
            {
                "inputs": [[[2, 7, 6], [9, 5, 1], [4, 3, 8]]],
                "output": True
            },
            {
                "inputs": [[[2, 7, 6], [9, 5, 1], [4, 3, 7]]],
                "output": False
            },
            {
                "inputs": [[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]],
                "output": True
            },
            {
                "inputs": [[[4, 9, 2], [3, 5, 7], [8, 1, 6]]],
                "output": True
            },
            {
                "inputs": [[[2, 7, 6], [9, 5, 1], [4, 3, 8]]],
                "output": True
            }
        ]
    },
    {
        "problem_id": "MBPP160",
        "problem_description": "Write a function that finds a solution to ax + by = n.",
        "prompts": [
            {
                "0-shot": "For three given integers a, b and n, write a function that returns integers x and y that satisfy ax + by = n. The function must receive three integers as inputs and return a tuple of integers, if there is a solution, or None otherwise."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["2", "3", "7"],
                "output": "(2, 1)"
            },
            {
                "input": ["4", "2", "7"],
                "output": "None"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["3", "2", "7"],
                "output": "None"
            },
            {
                "input": ["4", "2", "7"],
                "output": "(1, 2)"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["2", "3", "7"],
                "output": "[2, 1]"
            },
            {
                "input": ["4", "2", "7"],
                "output": "[]"
            }
        ],
        "tests": [
            {
                "inputs": [2, 3, 7],
                "output": (2, 1)
            },
            {
                "inputs": [3, 2, 7],
                "output": (1, 2)
            },
            {
                "inputs": [4, 2, 7],
                "output": None
            },
            {
                "inputs": [1, 13, 17],
                "output": (4, 1)
            },
            {
                "inputs": [1, 13, 11],
                "output": (11, 0)
            }
        ]
    },
    {
        "problem_id": "MBPP163",
        "problem_description": "Write a function to calculate the area of a regular polygon.",
        "prompts": [
            {
                "0-shot": "For two given integers l and n, write a function to calculate the area of a regular polygon with l as the length of its sides and n as the number of its sides. The function must receive two integers as inputs and return a number with three precision points."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["20", "4"],
                "output": "400.000"
            },
            {
                "input": ["15", "10"],
                "output": "1731.197"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["4", "20"],
                "output": "400.000"
            },
            {
                "input": ["10", "15"],
                "output": "1731.197"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["20", "4"],
                "output": "400"
            },
            {
                "input": ["15", "10"],
                "output": "1731.197"
            }
        ],
        "tests": [
            {
                "inputs": [20, 4],
                "output": 400.000
            },
            {
                "inputs": [15, 10],
                "output": 1731.197
            },
            {
                "inputs": [7, 9],
                "output": 302.909
            },
            {
                "inputs": [2, 3],
                "output": 1.732
            },
            {
                "inputs": [1, 4],
                "output": 1.000
            }
        ]
    },
    {
        "problem_id": "MBPP311",
        "problem_description": "Write a function to set the left most unset bit.",
        "prompts": [
            {
                "0-shot": "For a given integer, write a function to set its leftmost unset bit. The function must receive an integer as input and return an integer."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must convert the input to a binary number. Then, we must locate the leftmost unset bit (0) in the binary string, and set it (change it to 1). Lastly, we must convert the binary number back to decimal. In the example, 10 (in decimal) is converted to b'1010' (in binary). Then, by setting the leftmost unset bit, we have b'1110'. Lastly, converting it back to decimal base, we have 14.",
        "input_examples": [
            {
                "input": "10",
                "output": "14"
            },
            {
                "input": "12",
                "output": "14"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "10",
                "output": "1"
            },
            {
                "input": "12",
                "output": "4"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "10",
                "output": "1110"
            },
            {
                "input": "12",
                "output": "1110"
            }
        ],
        "tests": [
            {
                "inputs": [10],
                "output": 14
            },
            {
                "inputs": [12],
                "output": 14
            },
            {
                "inputs": [14],
                "output": 15
            },
            {
                "inputs": [15],
                "output": 15
            },
            {
                "inputs": [0],
                "output": 1
            }
        ]
    },
    {
        "problem_id": "MBPP390",
        "problem_description": "Write a function to apply a given format string to all elements in a list.",
        "prompts": [
            {
                "0-shot": "For a given list and a given format string, write a function to apply the format string to all elements in the list. The function must receive a list and a string as inputs and return a list."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["[1, 2, 3, 4]", "temp{0}"],
                "output": "['temp1', 'temp2', 'temp3', 'temp4']"
            },
            {
                "input": ["['a', 'b', 'c', 'd']", "python{0}"],
                "output": "['pythona', 'pythonb', 'pythonc', 'pythond']"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["[1, 2, 3, 4]", "temp{0}"],
                "output": "['temp1234']"
            },
            {
                "input": ["['a', 'b', 'c', 'd']", "python{0}"],
                "output": "['pythonabcd']"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["[1, 2, 3, 4]", "temp{0}"],
                "output": "'temp1', 'temp2', 'temp3', 'temp4'"
            },
            {
                "input": ["['a', 'b', 'c', 'd']", "python{0}"],
                "output": "'pythona', 'pythonb', 'pythonc', 'pythond'"
            }
        ],
        "tests": [
            {
                "inputs": [[1, 2, 3, 4], "temp{0}"],
                "output": ["temp1", "temp2", "temp3", "temp4"]
            },
            {
                "inputs": [['a', 'b', 'c', 'd'], "python{0}"],
                "output": ["pythona", "pythonb", "pythonc", "pythond"]
            },
            {
                "inputs": [[5, 6, 7], "string{0}"],
                "output": ["string5", "string6", "string7"]
            },
            {
                "inputs": [[0, 1, 2], "{0}-day"],
                "output": ["0-day", "1-day", "2-day"]
            },
            {
                "inputs": [['always', 'seldom', 'often', 'never'], "frequency: {0}"],
                "output": ["frequency: always", "frequency: seldom", "frequency: often", "frequency: never"]
            }
        ]
    },
    {
        "problem_id": "MBPP392",
        "problem_description": "Write a function to calculate according to the equation.",
        "prompts": [
            {
                "0-shot": "For a given integer n, write a function to find the maximum sum possible according to the equation: f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). The function must receive an integer as input and return an integer."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, by analyzing the equation, we notice the initial values are f(0) = 0, f(1) = max(f(0) + f(0) + f(0) + f(0), 1) = 1, and so on. Then, we must store these values in memory and recursively determine the value of the equation for different values of n, by successively calculating the floor of the division of n by 2, 3, 4 and 5, and comparing f(n//2) + f(n//3) + f(n//4) + f(n//5) with n, and finally extracting the maximum. In the example, f(2) = max(f(1) + f(0) + f(0) + f(0), 2) = max(1, 2) = 2.",
        "input_examples": [
            {
                "input": "2",
                "output": "2"
            },
            {
                "input": "10",
                "output": "12"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "2",
                "output": "2"
            },
            {
                "input": "10",
                "output": "11"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "2",
                "output": "2.0"
            },
            {
                "input": "10",
                "output": "11.0"
            }
        ],
        "tests": [
            {
                "inputs": [2],
                "output": 2
            },
            {
                "inputs": [10],
                "output": 12
            },
            {
                "inputs": [60],
                "output": 106
            },
            {
                "inputs": [3],
                "output": 3
            },
            {
                "inputs": [6],
                "output": 7
            }
        ]
    },
    {
        "problem_id": "MBPP428",
        "problem_description": "Write a function to sort using shell sort.",
        "prompts": [
            {
                "0-shot": "For a given array, write a function to sort it using shell sort. The function must receive an array as input and return an array."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]",
                "output": "[2, 3, 4, 5, 12, 12, 23, 56, 81, 95]"
            },
            {
                "input": "[24, 22, 39, 34, 87, 73, 68]",
                "output": "[22, 24, 34, 39, 68, 73, 87]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]",
                "output": "[95, 81, 56, 23, 12, 12, 5, 4, 3, 2]"
            },
            {
                "input": "[24, 22, 39, 34, 87, 73, 68]",
                "output": "[87, 73, 68, 39, 34, 24, 22]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]",
                "output": "[2, 3, 4, 5, 12, 23, 56, 81, 95]"
            },
            {
                "input": "[24, 22, 39, 34, 87, 73, 68]",
                "output": "[22, 24, 34, 39, 68, 73, 87]"
            }
        ],
        "tests": [
            {
                "inputs": [[12, 23, 4, 5, 3, 2, 12, 81, 56, 95]],
                "output": [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
            },
            {
                "inputs": [[24, 22, 39, 34, 87, 73, 68]],
                "output": [22, 24, 34, 39, 68, 73, 87]
            },
            {
                "inputs": [[32, 30, 16, 96, 82, 83, 74]],
                "output": [16, 30, 32, 74, 82, 83, 96]
            },
            {
                "inputs": [[11, 10, 9, 0, -1, -2]],
                "output": [-2, -1, 0, 9, 10, 11]
            },
            {
                "inputs": [[-1, 0, 1, 2, 3]],
                "output": [-1, 0, 1, 2, 3]
            }
        ]
    },
    {
        "problem_id": "MBPP577",
        "problem_description": "Write a function to find the last digit of the factorial of a given number.",
        "prompts": [
            {
                "0-shot": "For a given integer, write a function to find the last digit of the factorial of the integer. The function must receive an integer as input and return an integer."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "4",
                "output": "4"
            },
            {
                "input": "21",
                "output": "0"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "4",
                "output": "24"
            },
            {
                "input": "0",
                "output": "1"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "0",
                "output": "True"
            },
            {
                "input": "21",
                "output": "False"
            }
        ],
        "tests": [
            {
                "inputs": [4],
                "output": 4
            },
            {
                "inputs": [0],
                "output": 1
            },
            {
                "inputs": [21],
                "output": 0
            },
            {
                "inputs": [30],
                "output": 0
            },
            {
                "inputs": [3],
                "output": 6
            }
        ]
    },
    {
        "problem_id": "MBPP603",
        "problem_description": "Write a function to get all ludic numbers smaller than or equal to a given integer.",
        "prompts": [
            {
                "0-shot": "For a given integer n, write a function to get all ludic numbers smaller than or equal to n. The function must receive an integer as input and return a list of integers."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we include 1 to the list of ludic numbers. Then, we must write a list of numbers starting from 2. The first number of the list (2) must be popped and included to the list of ludic numbers. Then, every 2nd number must be removed from the list. We then move on to the new first number of the list, 3. This number must be popped and included to the list of ludic numbers. Next, every 3rd number must be removed from the list. This process is then repeated until all ludic numbers smaller than or equal to n are found. In the example, we first include 1 to the list of ludic numbers. Then, we write a list of numbers starting from 2: [2, 3, 4, 5, 6, 7, 8, 9, 10, ...]. We pop 2 from the list, include it to the ludic numbers list and remove every 2nd number: [3, 5, 7, 9, ...]. We then pop 3 from the list, include it to the ludic numbers list, and remove every third number: [5, 7, ...]. Since n = 10, the last two ludic numbers smaller than 10 will be 5 and 7, leaving us with the list of ludic numbers: [1, 2, 3, 5, 7].",
        "input_examples": [
            {
                "input": "10",
                "output": "[1, 2, 3, 5, 7]"
            },
            {
                "input": "25",
                "output": "[1, 2, 3, 5, 7, 11, 13, 17, 23, 25]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "10",
                "output": "[2, 3, 5, 7]"
            },
            {
                "input": "25",
                "output": "[2, 3, 5, 7, 11, 13, 17, 19, 23]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "10",
                "output": "(1, 2, 3, 5, 7)"
            },
            {
                "input": "25",
                "output": "(1, 2, 3, 5, 7, 11, 13, 17, 23, 25)"
            }
        ],
        "tests": [
            {
                "inputs": [10],
                "output": [1, 2, 3, 5, 7]
            },
            {
                "inputs": [25],
                "output": [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
            },
            {
                "inputs": [45],
                "output": [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
            },
            {
                "inputs": [1],
                "output": [1]
            },
            {
                "inputs": [7],
                "output": [1, 2, 3, 5, 7]
            }
        ]
    },
    {
        "problem_id": "MBPP626",
        "problem_description": "Write a function to find the area of the largest triangle that can be inscribed in a semicircle.",
        "prompts": [
            {
                "0-shot": "For a given number r, write a function to find the area of the largest triangle that can be inscribed in a semicircle with radius r. The function must receive a number r and return a number, or None."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "-1",
                "output": "None"
            },
            {
                "input": "2",
                "output": "4"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "0",
                "output": "None"
            },
            {
                "input": "2",
                "output": "4"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "-1",
                "output": "0"
            },
            {
                "input": "2",
                "output": "4.0"
            }
        ],
        "tests": [
            {
                "inputs": [-1],
                "output": None
            },
            {
                "inputs": [1],
                "output": 1
            },
            {
                "inputs": [2],
                "output": 4
            },
            {
                "inputs": [1.5],
                "output": 2.25
            },
            {
                "inputs": [10],
                "output": 100
            }
        ]
    },
    {
        "problem_id": "MBPP721",
        "problem_description": "Write a function to calculate the path of most cost.",
        "prompts": [
            {
                "0-shot": "For a given matrix, where each cell is associated with a cost, write a function to find the average cost of the path with the maximum average over all existing paths. A path is defined as a sequence of cells that starts from the top-left cell, moving only right or down, and ending on the bottom right cell. The average is computed as the total cost divided by the number of cells visited in the path. The function must receive a list of lists as input and return a number."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "[[1, 2, 3], [6, 5, 4], [7, 3, 9]]",
                "output": "5.2"
            },
            {
                "input": "[[2, 3, 4], [7, 6, 5], [8, 4, 10]]",
                "output": "6.2"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[[1, 2, 3], [6, 5, 4], [7, 3, 9]]",
                "output": "26"
            },
            {
                "input": "[[2, 3, 4], [7, 6, 5], [8, 4, 10]]",
                "output": "31"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["[1, 2, 3]", "[6, 5, 4]", "[7, 3, 9]"],
                "output": "5.2"
            },
            {
                "input": ["[2, 3, 4]", "[7, 6, 5]", "[8, 4, 10]"],
                "output": "6.2"
            }
        ],
        "tests": [
            {
                "inputs": [[[1, 2, 3], [6, 5, 4], [7, 3, 9]]],
                "output": 5.2
            },
            {
                "inputs": [[[2, 3, 4], [7, 6, 5], [8, 4, 10]]],
                "output": 6.2
            },
            {
                "inputs": [[[3, 4, 5], [8, 7, 6], [9, 5, 11]]],
                "output": 7.2
            },
            {
                "inputs": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
                "output": 5.8
            }
        ]
    },
    {
        "problem_id": "MBPP765",
        "problem_description": "Write a function to find nth polite number.",
        "prompts": [
            {
                "0-shot": "For a given integer n, write a function to find the nth polite number. The function must receive an integer as input and return an integer."
            }
        ],
        "chain_of_thought": "Let's think step by step. A polite number is a positive integer that can be written as the sum of two or more consecutive integers. As such, all numbers that aren't powers of 2 are polite numbers. In the example, the first 7 polite numbers are: 3, 5, 6, 7, 9, 10, 11. Thus, the 7th polite number is 11.",
        "input_examples": [
            {
                "input": "7",
                "output": "11"
            },
            {
                "input": "4",
                "output": "7"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "1",
                "output": "1"
            },
            {
                "input": "5",
                "output": "7"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "7",
                "output": "[3, 5, 6, 7, 9, 10, 11]"
            },
            {
                "input": "4",
                "output": "[3, 5, 6, 7]"
            }
        ],
        "tests": [
            {
                "inputs": [7],
                "output": 11
            },
            {
                "inputs": [4],
                "output": 7
            },
            {
                "inputs": [1],
                "output": 3
            },
            {
                "inputs": [9],
                "output": 13
            },
            {
                "inputs": [16],
                "output": 21
            }
        ]
    },
    {
        "problem_id": "MBPP783",
        "problem_description": "Write a function to convert rgb to hsv.",
        "prompts": [
            {
                "0-shot": "For a given rgb value, write a function to convert the rgb color to hsv color. The function must receive three integers as inputs and return a tuple with three floats up to one decimal place."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["255", "255", "255"],
                "output": "(0.0, 0.0, 100.0)"
            },
            {
                "input": ["0", "215", "0"],
                "output": "(120.0, 100.0, 84.3)"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["255", "255", "255"],
                "output": "(0.0, 0.0, 0.0)"
            },
            {
                "input": ["0", "215", "0"],
                "output": "(120.0, 100.0, 84)"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[255, 255, 255]",
                "output": "[0.0, 0.0, 100.0]"
            },
            {
                "input": "[0, 215, 0]",
                "output": "[120.0, 100.0, 84.3]"
            }
        ],
        "tests": [
            {
                "inputs": [255, 255, 255],
                "output": (0.0, 0.0, 100.0)
            },
            {
                "inputs": [0, 215, 0],
                "output": (120.0, 100.0, 84.3)
            },
            {
                "inputs": [10, 215, 110],
                "output": (149.3, 95.3, 84.3)
            },
            {
                "inputs": [0, 0, 0],
                "output": (0.0, 0.0, 0.0)
            },
            {
                "inputs": [128, 0, 150],
                "output": (291.2, 100.0, 58.8)
            }
        ]
    },
    {
        "problem_id": "CC1575A",
        "problem_description": "Asc-desc-ending sorting.",
        "prompts": [
            {
                "0-shot": "Ally and Billy were given an assignment to tidy up their bookshelf of n books. Each book is represented by the book title — a string s_i numbered from 1 to n, each with length m. Ally really wants to sort the book lexicographically ascending, while Billy wants to sort it lexicographically descending.\n\nSettling their fight, they decided to combine their idea and sort it asc-desc-endingly, where the odd-indexed characters will be compared ascendingly, and the even-indexed characters will be compared descendingly.\n\nA string a occurs before a string b in asc-desc-ending order if and only if in the first position where a and b differ, the following holds:\n\n  * if it is an odd position, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b; \n  * if it is an even position, the string a has a letter that appears later in the alphabet than the corresponding letter in b. Write a function to perform the aforementioned asc-desc-ending sorting. The function must receive two integers n and m (1 ≤ n ⋅ m ≤ 10^6), as well as a list, with n strings of length m. The function must return a list of integers, corresponding to the indices of the strings, starting at 1, after they are sorted asc-desc-endingly.",
                "simplified": "For a given list of strings, the 'asc-desc-ending' sort is defined as a sorting strategy in which a string 'a' occurs before a string 'b' if and only if in the first position where 'a' and 'b' differ, the following holds: if the position has an odd index, the letter in 'a' must appaear earlier in the alphabet than the corresponding letter in 'b'; if the position has an even index, the letter in 'b' must appear earlier in the alphabet than the corresponding letter in 'a'. Write a function to perform 'asc-desc-ending' sorting. The function must receive two integers n and m, as well as a list, with n strings of length m. The function must return a list of integers, corresponing to the indices of the strings, starting at 1, after they are sorted."
            }
        ],
        "chain_of_thought": "Let's think step by step. Considering indexes start at 1, first the strings must be ordered lexicographically ascending according to their first letter. Then, for strings with the same first letter, we must analyze the second letter of each string, and then order them in descending order. This process of grouping and ordering strings ascendingly for odd indexes and descendingly for even indexes must be repeated until all strings have been ordered. In the example, we are given the list [AA, AB, BB, BA, AZ]. We must first order the strings ascendingly according to their first letter, thus giving us the intermediate list [AA, AB, AZ, BB, BA]. Then, for each group of strings with the same first letter, we must order their second letters descendingly. Given the strings AA, AB and AZ all start with 'A', ordering their second letters descendingly gives us [AZ, AB, AA]. Similarly for the group of strings starting with the letter 'B', we obtain [BB, BA]. Thus, our asc-desc-ending sorted list is [AZ, AB, AA, BB, BA]. Extracting the original indices of each string, we obtain [5, 2, 1, 3, 4].",
        "input_examples": [
            {
                "input": "[5, 2, [AA, AB, BB, BA, AZ]]",
                "output": "[5, 2, 1, 3, 4]"
            },
            {
                "input": "[4, 3, [AAA, AZA, AAZ, AZZ]]",
                "output": "[2, 4, 1, 3]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[5, 2, [AA, AB, BB, BA, AZ]]",
                "output": "[5, 2, 1, 4, 3]"
            },
            {
                "input": "[5, 2, [AA, AB, CB, BA, AZ]]",
                "output": "[5, 2, 1, 3, 4]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[5, 2, AA, AB, BB, BA, AZ]",
                "output": "[5, 2, 1, 3, 4]"
            },
            {
                "input": "[5, 2, AA, AB, CB, BA, AZ]",
                "output": "[5, 2, 1, 4, 3]"
            }
        ],
        "tests": [
            {
                "inputs": [5, 2, ["AA", "AB", "BB", "BA", "AZ"]],
                "output": [5, 2, 1, 3, 4]
            },
            {
                "inputs": [5, 2, ["AA", "AB", "CB", "BA", "AZ"]],
                "output": [5, 2, 1, 4, 3]
            },
            {
                "inputs": [6, 6, ["Abacus", "Orange", "Avians", "Oyster", "Bigger", "Bandie"]],
                "output": [3, 1, 5, 6, 4, 2]
            },
            {
                "inputs": [4, 3, ["AAA", "AZA", "AAZ", "AZZ"]],
                "output": [2, 4, 1, 3]
            },
            {
                "inputs": [5, 2, ["AA", "AB", "BB", "BA", "ZA"]],
                "output": [2, 1, 3, 4, 5]
            }
        ]
    },
    {
        "problem_id": "CC1575H",
        "problem_description": "Holiday Wall Ornaments.",
        "prompts": [
            {
                "0-shot": "The Winter holiday will be here soon. Mr. Chanek wants to decorate his house's wall with ornaments. The wall can be represented as a binary string a of length n. His favorite nephew has another binary string b of length m (m ≤ n).\n\nMr. Chanek's nephew loves the non-negative integer k. His nephew wants exactly k occurrences of b as substrings in a. \n\nHowever, Mr. Chanek does not know the value of k. So, for each k (0 ≤ k ≤ n - m + 1), find the minimum number of elements in a that have to be changed such that there are exactly k occurrences of b in a.\n\nA string s occurs exactly k times in t if there are exactly k different pairs (p,q) such that we can obtain s by deleting p characters from the beginning and q characters from the end of t. Write a function to determine the minimum number of elements needed to be changed for each k. The function must receive two integers n and m, and two binary strings a and b, of lengths n and m. The function must return a list with (n - m + 2) integers, where the (k+1)-th integer denotes the minimal number of elements in a that must be changed so there are exactly k occurrences of b as substrings in a. If no amount of changes is capable of satisfying k occurrences, the (k+1)-th integer must be -1."
            }
        ],
        "chain_of_thought": "Let's think step by step. Given m and n, we can determine k will range from 0 to n - m + 1. For each k, we must change 0s and 1s in the string a in order to have the substring b appear k times, and we wish to find the minimum number of changes in order to accomplish so. In the example, for k = 0, we wish for the substring '101' never to appear. This can be accomplished in one change by replacing the 6th character in our string a, so that it becomes '10010011'. For k = 1, only one change is needed in order for '101' to appear only once, and that can be to change a to '100001011'. For k = 2, no changes are needed, since '101' already appears twice. This process is repeated until k = n - m + 1, which yields the list of changes for each k: [1, 1, 0, 1, 6, -1, -1, -1].",
        "input_examples": [
            {
                "input": ["9", "3", "100101011", "101"],
                "output": "[1, 1, 0, 1, 6, -1, -1, -1]"
            },
            {
                "input": ["9", "3", "101101011", "111"],
                "output": "[0, 2, 1, 3, 2, 2, 4, 3]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["9", "3", "100101011", "101"],
                "output": "[0, 2, 1, 3, 2, 2, 4, 3]"
            },
            {
                "input": ["9", "3", "101101011", "111"],
                "output": "[1, 1, 0, 1, 6, -1, -1, -1]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": ["9", "3", "100101011", "101"],
                "output": "1 1 0 1 6 -1 -1 -1"
            },
            {
                "input": ["9", "3", "101101011", "111"],
                "output": "0 2 1 3 2 2 4 3"
            }
        ],
        "tests": [
            {
                "inputs": [1, 1, "1", "1"],
                "output": [1, 0]
            },
            {
                "inputs": [1, 1, "1", "0"],
                "output": [0, 1]
            },
            {
                "inputs": [9, 3, "100101011", "101"],
                "output": [1, 1, 0, 1, 6, -1, -1, -1]
            },
            {
                "inputs": [9, 3, "101101011", "111"],
                "output": [0, 2, 1, 3, 2, 2, 4, 3]
            },
            {
                "inputs": [9, 3, "100101011", "110"],
                "output": [0, 1, 2, 5, -1, -1, -1, -1]
            }
        ]
    },
    {
        "problem_id": "CC1580B",
        "problem_description": "Mathematics Curriculum.",
        "prompts": [
            {
                "0-shot": "Let c_1, c_2, …, c_n be a permutation of integers 1, 2, …, n. Consider all subsegments of this permutation containing an integer x. Given an integer m, we call the integer x good if there are exactly m different values of maximum on these subsegments. A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array). A sequence a is a subsegment of a sequence b if a can be obtained from b by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. Given four integers n, m, k and p, write a function to count the number of permutations of length n with exactly k good numbers, modulo p. The function must receive four integers n, m, k and p and return an integer."
            }
        ],
        "chain_of_thought": "Let's think step by step. In the example, for n=4, take permutation [1, 3, 2, 4] for instance. For number 1, all subsegments containing it are: [1], [1, 3], [1, 3, 2] and [1, 3, 2, 4], and there are three different maxima: 1, 3 and 4. Similarly, for number 3, there are two different maxima 3 and 4. For number 2, there are three different maxima 2, 3 and 4. And for number 4, there is only one, which is 4 itself. Given m=3 and k=2, which corresponds to a permutation with 2 numbers having three different maxima each, the permutation [1, 3, 2, 4] should be included in our count, given numbers 1 and 2 have three different maxima each. Repeating this analysis for all permutations of numbers 1 to 4, we find that permutations [1, 3, 2, 4], [2, 3, 1, 4], [4, 1, 3, 2] and [4, 2, 3, 1] have 2 good numbers each, which brings us to a total of 4 permutations.",
        "input_examples": [
            {
                "input": ["4", "3", "2", "10007"],
                "output": "4"
            },
            {
                "input": ["6", "4", "1", "769626776"],
                "output": "472"
            },
            {
                "input": ["66", "11", "9", "786747482"],
                "output": "206331312"
            },
            {
                "input": ["99", "30", "18", "650457567"],
                "output": "77365367"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["4", "3", "2", "10007"],
                "output": "4"
            },
            {
                "input": ["6", "4", "1", "769626776"],
                "output": "472"
            },
            {
                "input": ["66", "11", "9", "6747482"],
                "output": "206331312"
            },
            {
                "input": ["99", "30", "18", "457567"],
                "output": "77365367"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "4 3 2 10007",
                "output": "4"
            },
            {
                "input": "6 4 1 769626776",
                "output": "472"
            },
            {
                "input": "66 11 9 786747482",
                "output": "206331312"
            },
            {
                "input": "99 30 18 650457567",
                "output": "77365367"
            }
        ],
        "tests": [
            {
                "inputs": [4, 3, 2, 10007],
                "output": 4
            },
            {
                "inputs": [6, 4, 1, 769626776],
                "output": 472
            },
            {
                "inputs": [66, 11, 9, 786747482],
                "output": 206331312
            },
            {
                "inputs": [99, 30, 18, 650457567],
                "output": 77365367
            },
            {
                "inputs": [9, 4, 1, 765062520],
                "output": 66112
            }
        ]
    },
    {
        "problem_id": "CC1582A",
        "problem_description": "Luntik and Concerts.",
        "prompts": [
            {
                "0-shot": "Luntik has decided to try singing. He has a one-minute songs, b two-minute songs and c three-minute songs. He wants to distribute all songs into two concerts such that every song should be included to exactly one concert. The duration of the concert is the sum of durations of all songs in that concert. Write a function to find the minimal possible difference in minutes between the concerts durations. The function must receive three integers a, b and c, and return an integer."
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": ["1", "1", "1"],
                "output": "0"
            },
            {
                "input": ["2", "1", "3"],
                "output": "1"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["1", "1", "1"],
                "output": "1"
            },
            {
                "input": ["2", "1", "3"],
                "output": "0"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "1 1 1",
                "output": "0"
            },
            {
                "input": "2 1 3",
                "output": "1"
            }
        ],
        "tests": [
            {
                "inputs": [1, 1, 1],
                "output": 0
            },
            {
                "inputs": [2, 1, 3],
                "output": 1
            },
            {
                "inputs": [5, 5, 5],
                "output": 0
            },
            {
                "inputs": [1, 1, 2],
                "output": 1
            },
            {
                "inputs": [3, 8, 5],
                "output": 0
            }
        ]
    },
    {
        "problem_id": "CC1582F2",
        "problem_description": "Korney Korneevich and XOR (hard version).",
        "prompts": [
            {
                "0-shot": "For a given array a of length n, write a function to find all integers x >= 0 such that there exists an increasing subsequence of the array a, in which the bitwise XOR of numbers is equal to x. A sequence s is a subsequence of a sequence b if s can be obtained from b by deletion of several (possibly, zero or all) elements. A sequence s1, s2, ..., sm is called increasing if s1 < s2 < ... < sm. The function must receive a list with n integers a1, a2, ..., an - the elements of the array a. The function must return a list of integers x1, x2, ..., xk, in increasing order - the found x values."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must determine the largest possible bitwise XOR that can be obtained from an increasing subsequence of the array a. Then for each integer x ranging from 0 to this result, we must test whether there is an increasing subsequence of the array a whose bitwise XOR of its elements is equal to x, and, if so, add it to a list to be returned. In the example, for x = 0, it is possible to choose the empty subsequence []. For x = 2, it is possible to choose the subsequence [2]. For x = 4, we can choose the subsequence [4]. Lastly, for x = 6, we can choose subsequence [2, 4], given that 2 ^ 4 = b'10' ^ b'100' = b'110' = 6. Therefore, we end up with the list [0, 2, 4, 6].",
        "input_examples": [
            {
                "input": ["4", "2", "2", "4"],
                "output": "[0, 2, 4, 6]"
            },
            {
                "input": ["1", "0", "1", "7", "12", "5", "3", "2"],
                "output": "[0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["4", "2", "4"],
                "output": "[0, 2, 4, 6]"
            },
            {
                "input": ["0", "1", "7", "12", "5", "3", "2"],
                "output": "[0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "4 2 2 4",
                "output": "[0, 2, 4, 6]"
            },
            {
                "input": "1 0 1 7 12 5 3 2",
                "output": "[0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]"
            }
        ],
        "tests": [
            {
                "inputs": [[4, 2, 2, 4]],
                "output": [0, 2, 4, 6]
            },
            {
                "inputs": [[1, 0, 1, 7, 12, 5, 3, 2]],
                "output": [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13]
            },
            {
                "inputs": [[2, 1, 4, 2, 4]],
                "output": [0, 1, 2, 3, 4, 5, 6, 7]
            },
            {
                "inputs": [[5000]],
                "output": [0, 5000]
            },
            {
                "inputs": [[0]],
                "output": [0]
            }
        ]
    },
    {
        "problem_id": "CC1586F",
        "problem_description": "Defender of Childhood Dreams",
        "prompts": [
            {
                "0-shot": "Consider a directed graph containing n nodes, labeled from 1 to n. There is a directed edge from node a to node b if and only if a < b. A path between nodes a and b is defined as a sequence of edges such that you can start at a, travel along all of these edges in the corresponding direction, and end at b. The length of a path is defined by the number of edges. A rainbow path of length x is defined as a path in the graph such that there exists at least 2 distinct colors among the set of x edges. Considering it is possible to label each edge with a color, write a function to determine the minimum number of colors needed to ensure that all paths of length k or longer are rainbow paths. The function must receive two integers, n and k, as inputs, and return an integer - the minimum number of colors needed."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, given the number of nodes and the path length, we must list all edges, given that an edge from node a to node b exists only if a < b. Then, we must find all valid paths with length k or longer. We must then compare these paths with each other, looking for edges in common, and determine which edges appear more frequently in all paths, in order to paint some of them, in a way that guarantees each path is a rainbow path. In the example, we have the following valid paths of length 3 or longer: (1, 2, 3), (1, 2, 4), (1, 2, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (2, 3, 4, 5), (1, 2, 3, 4, 5). Given these paths, and the edges belonging to them, we can make every path a rainbow path by coloring the edges (1,2), (3,4), (3,5) and (4,5). Thus, we only need 2 different colors in this example.",
        "input_examples": [
            {
                "input": ["5", "3"],
                "output": "2"
            },
            {
                "input": ["5", "2"],
                "output": "3"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["5", "3"],
                "output": "3"
            },
            {
                "input": ["5", "2"],
                "output": "4"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "5 3",
                "output": "2"
            },
            {
                "input": "5 2",
                "output": "4"
            }
        ],
        "tests": [
            {
                "inputs": [5, 3],
                "output": 2
            },
            {
                "inputs": [5, 2],
                "output": 4
            },
            {
                "inputs": [8, 7],
                "output": 2
            },
            {
                "inputs": [3, 2],
                "output": 2
            },
            {
                "inputs": [9, 2],
                "output": 4
            }
        ]
    },
    {
        "problem_id": "CC1600E",
        "problem_description": "Array game",
        "prompts": [
            {
                "0-shot": "Alice and Bob are playing a game. They are given an array A. The array consists of integers. They are building a sequence together. In the beginning, the sequence is empty. In one turn a player can remove a number from the left or right side of the array and append it to the sequence. The rule is that the sequence they are building must be strictly increasing. The winner is the player that makes the last move. Alice is playing first. Given the starting array, under the assumption that they both play optimally, write a function to determine the winner of the game. The function must receive a list of integers A1, A2, ..., AN, corresponding to the array A. The function must return a string corresponding to the name of the winner (either 'Alice' or 'Bob')."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must define the optimal strategy for the game, which, for both players, consists of removing the largest number from the array and appending it to the sequence, as long as it is larger than the last appended value (otherwise the game is already over). Then, we must take turns playing as Alice and as Bob, until the numbers on the left and right side of the array are both smaller than the last value added to sequence, or when the array is empty, at which point no more moves can be made. Then, we determine the winner, which is the last player to have appended a number to the sequence. In the example, there is only one number to remove from the array and append to the sequence. Therefore, given that the first player is Alice, and after her move the array is then empty, the winner is Alice.",
        "input_examples": [
            {
                "input": "[5]",
                "output": "Alice"
            },
            {
                "input": "[5, 4, 5]",
                "output": "Alice"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[5]",
                "output": "Alice"
            },
            {
                "input": "[5, 4, 5]",
                "output": "Bob"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "5",
                "output": "Alice"
            },
            {
                "input": "5 4 5",
                "output": "Alice"
            }
        ],
        "tests": [
            {
                "inputs": [[5]],
                "output": "Alice"
            },
            {
                "inputs": [[5, 4, 5]],
                "output": "Alice"
            },
            {
                "inputs": [[5, 8, 2, 1, 10, 9]],
                "output": "Bob"
            },
            {
                "inputs": [[5, 6, 5]],
                "output": "Bob"
            },
            {
                "inputs": [[5, 4, 2, 1, 10, 9]],
                "output": "Alice"
            }
        ]
    },
    {
        "problem_id": "CC1618C",
        "problem_description": "Paint the Array",
        "prompts": [
            {
                "0-shot": "Consider a given array consisting of positive integers. Upon selecting a positive integer d, all elements of the array which are divisible by d will be painted red, and all other elements will be painted blue. The coloring is called beautiful if there are no pairs of adjacent elements with the same color in the array. Write a function to find the smallest value of d which yields a beautiful coloring, or report that it is impossible. The function must receive a list of integers - the elements of the array - as input, and return a positive integer d, or 0, if there is no value of d that yields a beautiful coloring."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must analyze the divisors of each number of the list. If there are one or more divisors belonging to interspersed elements of the array, then we must return the smallest of these divisors. Otherwise the problem has no solution. In the example, the elements 2 and 4 have 2 as a common divisor, which also isn't a divisor for any other elements of the array. Therefore, the smallest value which returns a beautiful coloring is 2.",
        "input_examples": [
            {
                "input": "[1, 2, 3, 4, 5]",
                "output": "2"
            },
            {
                "input": "[10, 5, 15]",
                "output": "0"
            },
            {
                "input": "[100, 10, 200]",
                "output": "100"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "[1, 2, 3, 4, 5]",
                "output": "4"
            },
            {
                "input": "[10, 5, 15]",
                "output": "0"
            },
            {
                "input": "[100, 10, 200]",
                "output": "0"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "[1, 2, 3, 4, 5]",
                "output": "2"
            },
            {
                "input": "[10, 5, 15]",
                "output": "-1"
            },
            {
                "input": "[100, 10, 200]",
                "output": "100"
            }
        ],
        "tests": [
            {
                "inputs": [[1, 2, 3, 4, 5]],
                "output": 2
            },
            {
                "inputs": [[10, 5, 15]],
                "output": 0
            },
            {
                "inputs": [[100, 10, 200]],
                "output": 4
            },
            {
                "inputs": [[9, 8, 2, 6, 6, 2, 8, 6, 5, 4]],
                "output": 0
            },
            {
                "inputs": [[1, 3]],
                "output": 3
            }
        ]
    },
    {
        "problem_id": "CC1620C",
        "problem_description": "BA-String",
        "prompts": [
            {
                "0-shot": "Given an integer k and a string s, that consists only of characters 'a' and '*', each asterisk should be replaced with several (from 0 to k inclusive) lowercase Latin letters 'b'. Different asterisks can be replaced with different counts of the letter 'b'. The result of the replacement is called a BA-string. A string p is lexicographically smaller than q if and only if one of the following holds: p is a prefix of q, but p != q, or in the first position where p and q differ, the string p has a letter that appears earlier in the alphabet than the corresponding letter in q. Now consider all different BA-strings and write a function to find the x-th lexicographically smallest of them. The function must receive two integers k and x, and a string s. The function must return a string consisting only of 'b's and 'a's, corresponding to the x-th lexicographically smallest BA-string."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must create a list of all possible strings we can obtain by replacing asterisks by 'b's from 0 to k times. Then, we must list these strings in lexicographically ascending order. Then, given x, we can find the x-th smallest BA-string. In the example, the strings we can obtain by replacing '*' with 'b' up to 4 times are: 'a', 'ab', 'abb', 'abbb' and 'abbbb', in lexicographically ascending order. Thus, the third smallest BA-string is 'abb'.",
        "input_examples": [
            {
                "input": ["4", "3", "a*"],
                "output": "abb"
            },
            {
                "input": ["1", "3", "a**a"],
                "output": "abba"
            },
            {
                "input": ["3", "20", "**a***"],
                "output": "babbbbbbbbb"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": ["4", "3", "a*"],
                "output": "abbb"
            },
            {
                "input": ["1", "3", "a**a"],
                "output": "abbba"
            },
            {
                "input": ["3", "20", "**a***"],
                "output": "babbbbbbbbbb"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "4 3 a*",
                "output": "abb"
            },
            {
                "input": "1 3 a**a",
                "output": "abba"
            },
            {
                "input": "3 20 **a***",
                "output": "babbbbbbbbb"
            }
        ],
        "tests": [
            {
                "inputs": [4, 3, "a*"],
                "output": "abb"
            },
            {
                "inputs": [1, 3, "a**a"],
                "output": "abba"
            },
            {
                "inputs": [3, 20, "**a***"],
                "output": "babbbbbbbbbb"
            },
            {
                "inputs": [4, 2, "a**"],
                "output": "ab"
            },
            {
                "inputs": [2, 2, "a**a"],
                "output": "aba"
            }
        ]
    },
    {
        "problem_id": "CC1619B",
        "problem_description": "Squares and Cubes",
        "prompts": [
            {
                "0-shot": "Polycarp likes squares and cubes of positive integers. Here is the beginning of the sequence of numbers he likes: 1, 4, 8, 9, .... For a given number n, write a function to count the number of integers from 1 to n that Polycarp likes. In other words, find the number of such x that x is a square of a positive integer number or a cube of a positive integer number (or both a square and a cube simultaneously). The function must receive an integer n, and return an integer."
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must determine the square root of n. Then, for each number k smaller than or equal to the square root of n, we must add k^2 to the list of numbers Polycarp likes. Additionally, if k^3 is smaller than n, it must also be added to list. Finally, the number of integers from 1 to n that Polycarp likes will be given by the length of the list. In the example, we first calculate the floor of the square root of 10, which is 3. Then, we iterate over k from 1 to 3. For k = 1, we add it to the list. For k = 2, we add both 2^2 = 4 and 2^3 = 8 to the list. Lastly, for k = 3, we add 3^2 = 9 to the list, totalling 4 numbers.",
        "input_examples": [
            {
                "input": "10",
                "output": "4"
            },
            {
                "input": "1",
                "output": "1"
            },
            {
                "input": "25",
                "output": "6"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "10",
                "output": "4"
            },
            {
                "input": "2",
                "output": "1"
            },
            {
                "input": "25",
                "output": "5"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "10",
                "output": "[1, 4, 8, 9]"
            },
            {
                "input": "1",
                "output": "[1]"
            },
            {
                "input": "25",
                "output": "[1, 4, 8, 9, 16, 25]"
            }
        ],
        "tests": [
            {
                "inputs": [10],
                "output": 4
            },
            {
                "inputs": [1],
                "output": 1
            },
            {
                "inputs": [25],
                "output": 6
            },
            {
                "inputs": [1000000000],
                "output": 32591
            },
            {
                "inputs": [999999999],
                "output": 32590
            },
            {
                "inputs": [500000000],
                "output": 23125
            }
        ]
    },
    {
        "problem_id": "YTDL1",
        "problem_description": "Base url util",
        "prompts": [
            {
                "0-shot": 'The following `base_url` function and docstring refer to a utility function to extract the base url given a url, in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```import re\n\ndef base_url(url):\n    """ Returns the base url given a full url\n    """\n    pass```. Complete the function, having it return the base url as a string.',
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "http://foo.de/",
                "output": "http://foo.de/"
            },
            {
                "input": "http://foo.de/bar/",
                "output": "http://foo.de/bar/"
            },
            {
                "input": "http://foo.de/bar",
                "output": "http://foo.de/"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "http://foo.de/",
                "output": "http://foo.de/"
            },
            {
                "input": "http://foo.de/bar/",
                "output": "http://foo.de/bar/"
            },
            {
                "input": "http://foo.de/bar",
                "output": "http://foo.de/bar/"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "http://foo.de/",
                "output": "foo.de"
            },
            {
                "input": "http://foo.de/bar/",
                "output": "foo.de/bar"
            },
            {
                "input": "http://foo.de/bar",
                "output": "foo.de/bar"
            }
        ],
        "tests": [
            {
                "inputs": ["http://foo.de/"],
                "output": "http://foo.de/"
            },
            {
                "inputs": ["http://foo.de/bar"],
                "output": "http://foo.de/"
            },
            {
                "inputs": ["http://foo.de/bar/"],
                "output": "http://foo.de/bar/"
            },
            {
                "inputs": ["http://foo.de/bar/baz"],
                "output": "http://foo.de/bar/"
            },
            {
                "inputs": ["http://foo.de/bar/baz?x=z/x/c"],
                "output": "http://foo.de/bar/"
            }
        ]
    },
    {
        "problem_id": "YTDL2",
        "problem_description": "Determine extension util",
        "prompts": [
            {
                "0-shot": 'The following `determine_ext` function and docstring refer to a utility function to determine the video extension of a given url, in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```KNOWN_EXTENSIONS = (\n    \'mp4\', \'m4a\', \'m4p\', \'m4b\', \'m4r\', \'m4v\', \'aac\',\n    \'flv\', \'f4v\', \'f4a\', \'f4b\',\n    \'webm\', \'ogg\', \'ogv\', \'oga\', \'ogx\', \'spx\', \'opus\',\n    \'mkv\', \'mka\', \'mk3d\',\n    \'avi\', \'divx\',\n    \'mov\',\n    \'asf\', \'wmv\', \'wma\',\n    \'3gp\', \'3g2\',\n    \'mp3\',\n    \'flac\',\n    \'ape\',\n    \'wav\',\n    \'f4f\', \'f4m\', \'m3u8\', \'smil\')\n\ndef determine_ext(url):\n    """ Extract the video extension from a URL, returning \'None\' if no valid extension was found.\n    URLs such as \'http://example.com/foo/bar.mp4/?download\' can also have extensions extracted.\n    """\n    \n    pass```. Complete the function, having it return the video extension as a string.',
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we need to parse the input url and remove the base URL. Then, we need to search the remaining string for one of the extensions in the list of known extensions followed by a dot, such as '.wav', and return it if it exists. In the example, parsing the url results in '/foo/bar.mp4/'. If we then perform a search for an extension followed by '.', we are able to extract the '.mp4' extension.",
        "input_examples": [
            {
                "input": "http://example.com/foo/bar.mp4/?download",
                "output": "mp4"
            },
            {
                "input": "http://example.com/foo/bar/?download",
                "output": "None"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "http://example.com/foo/bar.mp4/?download",
                "output": "mp4"
            },
            {
                "input": "http://example.com/foo/bar/?download",
                "output": "mp3"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "http://example.com/foo/bar.mp4/?download",
                "output": "mp4"
            },
            {
                "input": "http://example.com/foo/bar/?download",
                "output": ""
            }
        ],
        "tests": [
            {
                "inputs": ["http://example.com/foo/bar.mp4/?download"],
                "output": "mp4"
            },
            {
                "inputs": ["http://example.com/foo/bar/?download"],
                "output": None
            },
            {
                "inputs": ["http://example.com/foo/bar.nonext/?download"],
                "output": None
            },
            {
                "inputs": ["http://example.com/foo/bar/mp4?download"],
                "output": None
            },
            {
                "inputs": ["http://example.com/foo/bar.m3u8//?download"],
                "output": "m3u8"
            },
            {
                "inputs": ["foobar"],
                "output": None
            }
        ]
    },
    {
        "problem_id": "YTDL3",
        "problem_description": "Escape RFC 3986 util",
        "prompts": [
            {
                "0-shot": 'The following `escape_rfc3986` function and docstring refer to a utility function to escape non-ASCII characters from a given string, in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```def escape_rfc3986(s):\n    """ Escape non-ASCII characters as suggested by RFC 3986.\n        The characters "!*\'();:@&=+$,/?%#[]" are reserved and aren\'t converted.\n    """\n    pass```. Complete the function, having it return the escaped string.',
            }
        ],
        "chain_of_thought": "",
        "input_examples": [
            {
                "input": "!*\'();:@&=+$,/?%#[]",
                "output": "!*\'();:@&=+$,/?%#[]"
            },
            {
                "input": "foo bar",
                "output": "foo%20bar"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "!*\'();:@&=+$,/?%#[]",
                "output": "%21%2A%5C%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5D"
            },
            {
                "input": "foo bar",
                "output": "foo%20bar"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "!*\'();:@&=+$,/?%#[]",
                "output": "%21%2A%5C%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5"
            },
            {
                "input": "foo bar",
                "output": "foo+bar"
            }
        ],
        "tests": [
            {
                "inputs": ["!*\'();:@&=+$,/?%#[]"],
                "output": "!*\'();:@&=+$,/?%#[]"
            },
            {
                "inputs": ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"],
                "output": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
            },
            {
                "inputs": ["foo bar"],
                "output": "foo%20bar"
            },
            {
                "inputs": ["тест"],
                "output": "%D1%82%D0%B5%D1%81%D1%82"
            },
            {
                "inputs": ["%D1%82%D0%B5%D1%81%D1%82"],
                "output": "%D1%82%D0%B5%D1%81%D1%82"
            },
            {
                "inputs": ["foo%20bar"],
                "output": "foo%20bar"
            }
        ]
    },
    {
        "problem_id": "YTDL4",
        "problem_description": "Fix xml ampersands util",
        "prompts": [
            {
                "0-shot": 'The following `fix_xml_ampersands` function and docstring refer to a utility function to replace all lone "&" characters from a given xml string by "&amp;", in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```def fix_xml_ampersands(xml_str):\n    """Replace all lone \'&\' characters by \'&amp;\' in XML"""\n    pass```. Complete the function, having it return the replaced xml string.',
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must locate all '&' in the string. Then, we must check whether it has already been escaped, by verifying if it is already followed by an 'amp;' substring. If not, we must escape the ampersand, changing it to '&amp;'. In the example, since no ampersands were escaped yet, we must escape all of them, thus resulting in the escaped string: '\"&amp;x=y&amp;z=a'.",
        "input_examples": [
            {
                "input": '"&x=y&z=a',
                "output": '"&amp;x=y&amp;z=a'
            },
            {
                "input": "&amp;",
                "output": "&amp;"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": '"&x=y&z=a',
                "output": '"&amp;x=y&amp;z=a'
            },
            {
                "input": "&amp;",
                "output": "&amp;amp;"
            }
        ],
        "misformatted_inputs": [
            {
                "input": '&x=y&z=a',
                "output": '"&amp;x=y&amp;z=a'
            },
            {
                "input": "&amp",
                "output": "&amp;"
            }
        ],
        "tests": [
            {
                "inputs": ['"&x=y&z=a'],
                "output": '"&amp;x=y&amp;z=a'
            },
            {
                "inputs": ["&amp;"],
                "output": "&amp;"
            },
            {
                "inputs": ['"&amp;x=y&wrong;&z=a'],
                "output": '"&amp;x=y&amp;wrong;&amp;z=a'
            },
            {
                "inputs": ["&amp;&apos;&gt;&lt;&quot;"],
                "output": "&amp;&apos;&gt;&lt;&quot;"
            },
            {
                "inputs": ["&#1234;&#x1abC;"],
                "output": "&#1234;&#x1abC;"
            },
            {
                "inputs": ["&#&#"],
                "output": "&amp;#&amp;#"
            }
        ]
    },
    {
        "problem_id": "YTDL5",
        "problem_description": "Mimetype to extension util",
        "prompts": [
            {
                "0-shot": 'The following `mimetype2ext` function and docstring refer to a utility function to convert a mimetype into its corresponding extension, in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```MIMETYPE_EXTENSION_MAPPING = {\n    \'3gpp\': \'3gp\',\n    \'smptett+xml\': \'tt\',\n    \'ttaf+xml\': \'dfxp\',\n    \'ttml+xml\': \'ttml\',\n    \'x-flv\': \'flv\',\n    \'x-mp4-fragmented\': \'mp4\',\n    \'x-ms-sami\': \'sami\',\n    \'x-ms-wmv\': \'wmv\',\n    \'mpegurl\': \'m3u8\',\n    \'x-mpegurl\': \'m3u8\',\n    \'vnd.apple.mpegurl\': \'m3u8\',\n    \'dash+xml\': \'mpd\',\n    \'f4m+xml\': \'f4m\',\n    \'hds+xml\': \'f4m\',\n    \'vnd.ms-sstr+xml\': \'ism\',\n    \'quicktime\': \'mov\',\n    \'mp2t\': \'ts\',\n    \'x-wav\': \'wav\',\n}\n\ndef mimetype2ext(mt):\n    """ Converts mimetype to extension\n    \n    Specifications:\n        \'audio/mp4\': \'m4a\'\n        \'audio/mpeg\': \'mp3\' (Per RFC 3003, audio/mpeg can be .mp1, .mp2 or .mp3 - which is most popular)\n        Other extensions: refer to mimetype-extension mapping. If no corresponding extension is found,\n        returns the input mt.\n    """\n    \n    pass```. Complete the function, having it return the string corresponding to the mimetype equivalent extension.',
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must check for the special cases, such as 'audio/mp4' and 'audio/mpeg'. If the mimetype does not match a special case, we must extract only the second part of the mimetype. Then, we must try to match this substring with a mimetype in the mimetype-extension mapping. If a match is found, then we must return the mapped extension, otherwise, we must return the stripped mimetype substring. In the example, since 'video/x-flv' is not a special case, we must match the second part of the mimetype, 'x-flv' with its corresponding extension, which, from the mapping, is 'flv'.",
        "input_examples": [
            {
                "input": "video/x-flv",
                "output": "flv"
            },
            {
                "input": "application/x-mpegURL",
                "output": "m3u8"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "video/x-flv",
                "output": "flv"
            },
            {
                "input": "audio/mp4",
                "output": "mp4"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "video/x-flv",
                "output": "x-flv"
            },
            {
                "input": "application/x-mpegURL",
                "output": "x-mpegURL"
            }
        ],
        "tests": [
            {
                "inputs": ["video/x-flv"],
                "output": "flv"
            },
            {
                "inputs": ["application/x-mpegURL"],
                "output": "m3u8"
            },
            {
                "inputs": ["text/vtt"],
                "output": "vtt"
            },
            {
                "inputs": ["text/vtt;charset=utf-8"],
                "output": "vtt"
            },
            {
                "inputs": ["audio/mp4"],
                "output": "m4a"
            },
            {
                "inputs": ["audio/mpeg"],
                "output": "mp3"
            }
        ]
    },
    {
        "problem_id": "YTDL6",
        "problem_description": "Parse iso8601",
        "prompts": [
            {
                "0-shot": 'The following `parse_iso8601` function and docstring refer to a utility function to convert an ISO datetime into a UNIX timestamp, in the context of a project to download videos from video hosting services, such as Youtube. The function is as follows: ```def parse_iso8601(date_str, delimiter=\'T\', timezone=None):\n    """ Return a UNIX timestamp from the given date.\n        Delimiter corresponds to the time delimiter (e.g. 2023-10-19T00:00:00+0000)\n    """\n\n    pass```. Complete the function, having it return a string corresponding to the UNIX timestamp if the datetime is valid, or None otherwise.',
            }
        ],
        "chain_of_thought": "Let's think step by step. First, we must parse the input datetime. This input can have multiple formats, such as '2014-03-23T23:04:26+0100' or '2014-03-23T22:04:26Z', so we must sanitize them first. Then, we must convert the datetime into a UNIX timestamp. Lastly, we must convert the timestamp into a string. In the example, '2014-03-23T23:04:26+0100' corresponds to 1395612266 seconds in a UNIX timestamp, which then is converted to a string: '1395612266'.",
        "input_examples": [
            {
                "input": "2014-03-23T23:04:26+0100",
                "output": "1395612266"
            },
            {
                "input": "2014-03-23T22:04:26Z",
                "output": "1395612266"
            }
        ],
        "inaccurate_inputs": [
            {
                "input": "2014-03-23T23:04:26+0100",
                "output": "1395612265"
            },
            {
                "input": "2014-03-23T22:04:26Z",
                "output": "1395612265"
            }
        ],
        "misformatted_inputs": [
            {
                "input": "2014-03-23T23:04:26+0100",
                "output": "1395612266000"
            },
            {
                "input": "2014-03-23T22:04:26Z",
                "output": "1395612266000"
            }
        ],
        "tests": [
            {
                "inputs": ["2014-03-23T23:04:26+0100"],
                "output": "1395612266"
            },
            {
                "inputs": ["2014-03-23T22:04:26+0000"],
                "output": "1395612266"
            },
            {
                "inputs": ["2014-03-23T22:04:26Z"],
                "output": "1395612266"
            },
            {
                "inputs": ["2014-03-23T22:04:26.1234Z"],
                "output": "1395612266"
            },
            {
                "inputs": ["2015-09-29T08:27:31.727"],
                "output": "1443515251"
            },
            {
                "inputs": ["2015-09-29T08-27-31.727"],
                "output": None
            }
        ]
    }
]