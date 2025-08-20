#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from main import get_integer_input, ask_question


class TestMultiplicationTrainer(unittest.TestCase):
    """Test cases for multiplication trainer functions."""

    @patch('builtins.input')
    def test_get_integer_input_valid(self, mock_input):
        """Test valid integer input."""
        mock_input.return_value = "5"
        result = get_integer_input("Enter number: ")
        self.assertEqual(result, 5)

    @patch('builtins.input')
    def test_get_integer_input_quit(self, mock_input):
        """Test quit command input."""
        mock_input.return_value = "q"
        result = get_integer_input("Enter number: ")
        self.assertIsNone(result)

    @patch('builtins.input')
    def test_get_integer_input_invalid_then_valid(self, mock_input):
        """Test invalid input followed by valid input."""
        mock_input.side_effect = ["abc", "5"]
        result = get_integer_input("Enter number: ")
        self.assertEqual(result, 5)

    @patch('builtins.input')
    def test_get_integer_input_with_range(self, mock_input):
        """Test input validation with min constraints."""
        mock_input.side_effect = ["0", "5"]  # First too low, second valid
        result = get_integer_input("Enter number: ", min_val=1)
        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 2)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('time.sleep')
    def test_ask_question_correct_answer(self, mock_sleep, mock_input, mock_randint):
        """Test asking a question with correct answer."""
        mock_randint.side_effect = [3, 4]  # Will generate 3 × 4
        mock_input.return_value = "12"  # Correct answer

        continue_playing, is_correct = ask_question(1, 5, 1, 5)

        self.assertTrue(continue_playing)
        self.assertTrue(is_correct)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('time.sleep')
    def test_ask_question_wrong_answer(self, mock_sleep, mock_input, mock_randint):
        """Test asking a question with wrong answer."""
        mock_randint.side_effect = [3, 4]  # Will generate 3 × 4
        mock_input.return_value = "10"  # Wrong answer

        continue_playing, is_correct = ask_question(1, 5, 1, 5)

        self.assertTrue(continue_playing)
        self.assertFalse(is_correct)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('time.sleep')
    def test_ask_question_quit(self, mock_sleep, mock_input, mock_randint):
        """Test quitting during a question."""
        mock_randint.side_effect = [3, 4]
        mock_input.return_value = "q"

        continue_playing, is_correct = ask_question(1, 5, 1, 5)

        self.assertFalse(continue_playing)
        self.assertFalse(is_correct)


def run_manual_test():
    """Manual test function to demonstrate all the features."""
    print("Manual Test Demo")
    print("-" * 20)
    print("Features demonstrated:")
    print("1. Input validation")
    print("2. Error handling")
    print("3. Session tracking")
    print("4. Clean interface")
    print("\nRun: python main.py")


if __name__ == "__main__":
    print("Running tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    print()
    run_manual_test()
