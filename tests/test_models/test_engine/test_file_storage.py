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

    def test_FileStorage_instantiation_no_args(self):
        """Checks correct storage instantiation."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Checks inappropiate args type """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Checks if file path is a string"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Chechks if instance is a private dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

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

class TestFileStorage_methods(unittest.TestCase):
    """Check correct implementation of all() method."""
    def test_dict(self):
        """Checks for correct type of dict."""
        dictionary = FileStorage().all()
        self.assertEqual(type(dictionary), dict)

    def test_error(self):
        """Checks if error raises."""
        with self.assertRaises(TypeError):
            dictionary = FileStorage().all(None)
    
class TestFileStorage_new_save(unittest.TestCase):
    """Checks correct implementation of new(), save() and reload()
    method."""

    def test_Base_new(self):
        """Checks object type BaseModel newly created in __objects"""
        obj_dict = FileStorage().all()
        bm1 = BaseModel()
        FileStorage().new(bm1)
        key = "BaseModel." + bm1.id
        self.assertIn(key, obj_dict.keys())
