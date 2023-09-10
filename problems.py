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
        "input_examples": [
            {
                "input": "[1.0, 2.0, 3.0, 4.0]",
                "output": "1.0"
            },
            {
                "input": "[-3.2, -1, 0.5, 2.5]",
                "output": "1.8"
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
        "input_examples": [
            {
                "input": "()",
                "output": "1"
            },
            {
                "input": "((())()())",
                "output": "3"
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
        "input_examples": [
            {
                "input": "6",
                "output": "False"
            },
            {
                "input": "11",
                "output": "True"
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
        "input_examples": [
            {
                "input": [
                    "8",
                    "3"
                ],
                "output": "22"
            },
            {
                "input": [
                    "8",
                    "2"
                ],
                "output": "1000"
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
        "input_examples": [
            {
                "input": "abcba",
                "output": "True"
            },
            {
                "input": "zbcd",
                "output": "False"
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
        "input_examples": [
            {
                "input": "abcdef",
                "output": "bcdf"
            },
            {
                "input": "aeiou",
                "output": ""
            }
        ]
    },
    {
        "problem_id": "HE55",
        "problem_description": "Write function to return n-th Fibonacci number",
        "prompts": [
            {
                "0-shot": "For a given number n, write a function to determine the n-th Fibonacci number. The function must receive an integer as input and return an integer."
            },
            {
                "original": "\n\ndef fib(n: int):\n    \"\"\"Return n-th Fibonacci number.\n    >>> fib(10)\n    55\n    >>> fib(1)\n    1\n    >>> fib(8)\n    21\n    \"\"\"\n",
                "entry_point": "fib",
                "canonical_solution": "    if n == 0:\n        return 0\n    if n == 1:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n",
                "test": "\n\nMETADATA = {}\n\n\ndef check(candidate):\n    assert candidate(10) == 55\n    assert candidate(1) == 1\n    assert candidate(8) == 21\n    assert candidate(11) == 89\n    assert candidate(12) == 144\n\n"
            }
        ],
        "input_examples": [
            {
                "input": "10",
                "output": "55"
            },
            {
                "input": "1",
                "output": "1"
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
        "input_examples": [
            {
                "input": "abc",
                "output": "{'a': 1, 'b': 1, 'c': 1}"
            },
            {
                "input": "abcbaa",
                "output": "{'a': 3, 'b': 2, 'c': 1}"
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
        "input_examples": [
            {
                "input": "19",
                "output": "XIX"
            },
            {
                "input": "426",
                "output": "CDXXVI"
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
        "input_examples": [
            {
                "input": "Hello world",
                "output": "3e25960a79dbc69b674cd4ec67a72c62"
            }
        ]
    }
]