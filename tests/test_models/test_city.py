#!/usr/bin/python3
import unittest
from models import city
from models.base_model import BaseModel
City = city.City

class TestCity(unittest.TestCase):
    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(city.__doc__)
        self.assertIsNotNone(city.__init__.__doc__)
        self.assertIsNotNone(city.__str__.__doc__)
    
    def test_is_sub(self):
        """Test that Amenity is subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name and  its empty str"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()