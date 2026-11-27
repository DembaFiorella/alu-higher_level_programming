#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_docstrings(self):
        """Test that the module and the class are documented."""
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_is_instance(self):
        """Test that Base() creates an instance of Base."""
        self.assertIsInstance(Base(), Base)

    def test_first_automatic_id(self):
        """Test that the first automatic id is 1."""
        self.assertEqual(Base().id, 1)

    def test_automatic_id_plus_one(self):
        """Test that each automatic id is the previous one plus 1."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_given_id_saved(self):
        """Test that Base(89) saves the id passed."""
        self.assertEqual(Base(89).id, 89)

    def test_given_id_keyword(self):
        """Test passing the id as a keyword argument."""
        self.assertEqual(Base(id=5).id, 5)

    def test_given_id_does_not_increment(self):
        """Test that a given id does not change the counter."""
        Base(12)
        self.assertEqual(Base().id, 1)

    def test_mixed_ids(self):
        """Test automatic and given ids together."""
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual([b1.id, b2.id, b3.id], [1, 89, 2])

    def test_id_none(self):
        """Test that an explicit None gives an automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_id_zero(self):
        """Test that 0 is kept as the id."""
        self.assertEqual(Base(0).id, 0)

    def test_id_negative(self):
        """Test that a negative id is kept."""
        self.assertEqual(Base(-5).id, -5)

    def test_id_is_public(self):
        """Test that the id attribute can be reassigned."""
        b = Base()
        b.id = 10
        self.assertEqual(b.id, 10)

    def test_nb_objects_is_private(self):
        """Test that __nb_objects is not a public attribute."""
        self.assertFalse(hasattr(Base, "__nb_objects"))

    def test_nb_objects_value(self):
        """Test the value of the private counter."""
        Base()
        Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_two_arguments(self):
        """Test that two arguments raise a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
