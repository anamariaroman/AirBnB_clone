#!/usr/bin/python3
"""Tests for pep8"""
import unittest
import pep8
from models.base_model import BaseModel

class Test_pep8(unittest.TestCase):
    """ test class BaseModel """

    def test_pep8(self):
        """Test that models/base.py conforms to PEP8."""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(["models/base_model.py"])
        # unit testing to check the equality of two values
        # assertEqual(firstValue, secondValue, message)
        self.assertEqual(result.total_errors, 0, 
                        "Found code style errors and warnings found.")
