#!/usr/bin/python3
import unittest
import pep8
from models.base_model import BaseModel
"""
Test cases for the console ArBnB
"""


class Test_BaseModel(unittest.TestCase):
    """
    TestBaseModel - test the base model
    """

    def setUp(self):
        """ Setup the class """
        self.objects = BaseModel()

    def test_instance(self):
        """ test_instance - verify if instance exist """
        self.assertIsInstance(self.objects, BaseModel)

    def test_docString_class(self):
        """ test_docString_class - verifi if the doc is string """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_id_str(self):
        """ test_id_str - verifi if the id are str """
        self.assertEqual(type(self.objects.id), str)

    def test_pep8_data(self):
        """ test_pep8_data - test the pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")


if __name__ == '__main__':
    unittest.main()
