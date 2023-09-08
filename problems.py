data = [
    {
        "problem_id": "HE4",
        "problem_description": "Calculate mean absolute deviation",
        "prompts": [
            {
                "0-shot": "For a given list of input numbers, write a function to calculate the Mean Absolute Deviation around the mean of the dataset. The function must receive a List of floats as the input and a return a float as the output."
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
]