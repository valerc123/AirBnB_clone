#!/usr/bin/python3
"""
TestUser - To prube the class user
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import pep8


class TestUser(unittest.TestCase):

    def setUp(self):
        self.obj = User()

    def test_is_instance(self):
        """test instance of user"""
        self.assertIsInstance(self.obj, User)

    def test_user_inherits_basemodel(self):
        """Testing if user inherits from basemodel"""
        self.assertIsInstance(self.obj, BaseModel)

    def test_docstring(self):
        """Testing docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Test attributes of the user class"""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_types(self):
        """Test type of user class attributes"""
        self.assertIs(type(self.obj.id), str)
        self.assertIs(type(self.obj.created_at), datetime)
        self.assertIs(type(self.obj.updated_at), datetime)
        self.assertIs(type(self.obj.email), str)
        self.assertIs(type(self.obj.password), str)
        self.assertIs(type(self.obj.first_name), str)
        self.assertIs(type(self.obj.last_name), str)
