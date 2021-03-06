#!/usr/bin/python3
""" Module unittest for BaseModel """
import unittest
import datetime
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_dunder_str(self):
        """ Test that the str method has the correct output"""
        instance = BaseModel()
        string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_to_dict(self):
        """ Test conversion of object attributes to dictionary for json"""
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 89
        base_dict = base.to_dict()
        attributes = ["id", "created_at", "updated_at",
                      "name", "my_number", "__class__"]
        self.assertCountEqual(base_dict.keys(), attributes)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["name"], "Holberton")
        self.assertEqual(base_dict["my_number"], 89)

    def test_attributes(self):
        """Test attributes id, created_at and updated_at"""
        my_base = BaseModel()
        my_base2 = BaseModel()
        self.assertTrue(hasattr(my_base, "id"), "'id' attribute not found")
        self.assertTrue(hasattr(my_base, "created_at"),
                        "'created_at' attribute not found")
        self.assertTrue(hasattr(my_base, "updated_at"),
                        "'updated_at' attribute not found")
        self.assertNotEqual(my_base.id, my_base2.id,
                            "BaseModels instances has the same 'id'")

    def test_datetime(self):
        """ Test if instances are created with different times"""
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertNotEqual(base_1.created_at, base_2.updated_at)

    def test_save(self):
        """ Test Base MOdel save method """
        my_model = BaseModel()
        updated = my_model.updated_at
        my_model.save()
        self.assertFalse(updated == my_model.updated_at)

    def test_pep8(self):
        """Test that models/base.py conforms to PEP8."""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(["models/base_model.py"])
        # unit testing to check the equality of two values
        # assertEqual(firstValue, secondValue, message)
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors and warnings found.")
