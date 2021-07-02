#!/usr/bin/python3
""" Model Unittest """
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import json
import pep8


class TestFileStorage(unittest.TestCase):
    """Unittest for file_storage.py"""
    storage = FileStorage()
    path = storage._FileStorage__file_path

    def test_storage_isinstance(self):
        """Tests if storage is an instance of FileStorage"""
        self.assertIsInstance(TestFileStorage.storage, FileStorage)

    def test_pep8(self):
        """Test that models/base.py conforms to PEP8."""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(["models/base_model.py"])
        # unit testing to check the equality of two values
        # assertEqual(firstValue, secondValue, message)
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors and warnings found.")

    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
