#!/usr/bin/python3
import unittest
from models import place
from models.base_model import BaseModel
Place = place.Place

class Testamenity(unittest.TestCase):
    def test_docstring(self):
        """ Test doc strings """
        # assertIsNotNone(x): check that x is not None
        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(place.__init__.__doc__)
        self.assertIsNotNone(place.__str__.__doc__)
    
    def test_is_sub(self):
        """Test that Place is subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_name_attr(self):
        """Test that Place has attribute name and  its empty str"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_id_attr(self):
        """Test that Place has attribute city_id and  its empty str"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test that Place has attribute user_id and  its empty str"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_description_attr(self):
        """Test that Place has description name and  its empty str"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
    
    def test_number_room_attr(self):
        """Test Place has attr number_rooms and its an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(type(place.number_room, int))
        self.assertIsEqual(place.number_rooms, 0)

    def test_number_bath(self):
        """Test Place has attr number_bath and its an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(type(place.number_bathrooms, int))
        self.assertIsEqual(place.number_rooms, 0)

    def test_max_guest(self):
        """Test Place has attr max_guest and its an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(type(place.max_guest, int))
        self.assertIsEqual(place.max_guets, 0)

    def test_price_by_night(self):
        """Test Place has attr price_by_night and its an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(type(place.price_by_night, int))
        self.assertIsEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude_attr and its an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(type(place.latitude, float))
        self.assertIsEqual(place.latitude, 0.0)

if __name__ == "__main__":
    unittest.main()