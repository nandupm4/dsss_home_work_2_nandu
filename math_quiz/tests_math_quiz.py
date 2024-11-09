import unittest
from math_quiz import generate_random_integer, generate_random_operator, generate_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the valid operators: '+', '-', or '*'
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators)

    def test_function_C(self):
            # Test that the generated problem and answer are correct
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 5, '-', '10 - 5', 5),
                (3, 4, '*', '3 * 4', 12),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)  # Check if problem matches expected
                self.assertEqual(answer, expected_answer)  # Check if answer matches expected


if __name__ == "__main__":
    unittest.main()
