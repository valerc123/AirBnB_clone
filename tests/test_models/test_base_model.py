#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import pep8

"""
TestBaseModel - Unittest for base_model
"""


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.objects = BaseModel()

    def test_instance(self):
        """Test if the instance is BaseModel"""
        self.assertIsInstance(self.objects, BaseModel)

    def test_docString_class(self):
        """
        Test docstring in class
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_id_str(self):
        """Test if the id is a string """
        self.assertEqual(type(self.objects.id), str)

    def test_pep8_conformance_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_add_attribute(self):
        """
        Test to add the name and my_number attributes to the class
        """
        self.objects.name = "Holberton"
        self.objects.my_number = 89
       # self.assertIsTrue(hasattr(self.objects, 'id')
        self.assertTrue(isinstance(self.objects, BaseModel))

    def test_to_dict(self):
        """ Tests that the function retrieves a dictionary """
        ret_dict = self.objects.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_save(self):
        """ updates the public instance attribute updated_at"""
        var = self.objects.updated_at
        self.objects.save()
        self.assertNotEqual(var, self.objects.updated_at)

if __name__ == '__main__':
    unittest.main()

