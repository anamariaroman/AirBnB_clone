#!/usr/bin/python3
import unittest
from models import amenity
from models.base_model import BaseModel
Amenity = amenity.Amenity

class Testamenity(unittest.TestCase):
    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(amenity.__init__.__doc__)
        self.assertIsNotNone(amenity.__str__.__doc__)
    
    def test_is_sub(self):
        """Test that Amenity is subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name and  its empty str"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()