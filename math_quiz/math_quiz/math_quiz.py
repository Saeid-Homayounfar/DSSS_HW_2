import unittest
import random

def generate_random_integer(min_val, max_val):
    """
    Generate a random integer.
    """
    return random.randint(min_val, max_val)

class TestGenerateRandomInteger(unittest.TestCase):
    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

def generate_operator():
    """
    Generate a random operator.
    """
    return random.choice(['+', '-', '*'])

class TestGenerateOperator(unittest.TestCase):
    def test_generate_operator(self):
        operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_operator()
            self.assertIn(operator, operators)

if __name__ == '__main__':
    unittest.main()

def generate_problem(n1, n2, operator):
    """
    Generate a math problem.
    """
    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer

class TestGenerateProblem(unittest.TestCase):
    def test_generate_problem(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases here
        ]

        for n1, n2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(n1, n2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == '__main__':
    unittest.main()