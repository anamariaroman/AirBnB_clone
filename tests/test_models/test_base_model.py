#!/usr/bin/python3
""" Module unittest for BaseModel """
import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
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

