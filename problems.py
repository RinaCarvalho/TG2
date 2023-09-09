data = [
    {
        "problem_id": "HE4",
        "problem_description": "Write function to calculate mean absolute deviation",
        "prompts": [
            {
                "0-shot": "For a given list of input numbers, write a function to calculate the Mean Absolute Deviation around the mean of the dataset. The function must receive a List of floats as the input and return a float as the output."
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
                "0-shot": "Write a function to determine the intersection between two given closed intervals. The function must receive two tuples of two integers each as input and return a tuple of two integers, if the length of the intersection is larger than 1, or a single integer otherwise."
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
                "0-shot": "Write a function to convert a given number to uppercase roman numerals. The function must receive an integer as input and return a string."
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
                "0-shot": "Write a function that converts a given string to its md5 hash. The function must receive a string as input and return a string."
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