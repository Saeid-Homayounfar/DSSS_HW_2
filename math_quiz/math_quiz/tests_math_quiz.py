import unittest
from random import randint
from math_quiz import generate_random_integer
from math_quiz import generate_operator
from math_quiz import generate_problem

class TestGenerateRandomInteger(unittest.TestCase):
    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

if __name__ == '__main__':
    unittest.main()

class TestGenerateOperator(unittest.TestCase):
    def test_generate_operator(self):
        operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_operator()
            self.assertIn(operator, operators)

if __name__ == '__main__':
    unittest.main()

class TestGenerateProblem(unittest.TestCase):
    def test_generate_problem(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
        ]

        for n1, n2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(n1, n2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == '__main__':
    unittest.main()