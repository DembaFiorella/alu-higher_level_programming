#!/usr/bin/python3
"""Unittests for max_integer([..list..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with the max value at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test a list with the max value in the middle."""
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling the function without an argument."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Test a list of negative and positive numbers."""
        self.assertEqual(max_integer([-3, 0, 5, -8]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Test a list of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, -3]), 2.5)

    def test_equal_elements(self):
        """Test a list where all the elements are equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_repeated_max(self):
        """Test a list where the max value appears twice."""
        self.assertEqual(max_integer([5, 1, 5, 2]), 5)

    def test_big_numbers(self):
        """Test a list with very large numbers."""
        self.assertEqual(max_integer([10 ** 20, 5, 10 ** 10]), 10 ** 20)

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_int_and_string(self):
        """Test a list mixing an integer and a string."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none(self):
        """Test None instead of a list."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_instead_of_list(self):
        """Test an integer instead of a list."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == "__main__":
    unittest.main()
