#!/usr/bin/python3
"""
Unittest for HBNBCommand class
"""
import pep8
import unittest
from unittest import mock

class TestConsole(unittest.TestCase):
 """Test cases for the console"""

    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_EOF(self):
        self.with_mock(cmd="EOF", expected="")

    def test_quit(self):
        self.with_mock(cmd="quit", expected="")

    def test_empty(self):
        self.with_mock(cmd="\n", expected="")

    def test_create_l(self):
        self.with_mock(cmd="create", expected="** class name missing **")
        self.with_mock(cmd="create MyModel", expected="** class doesn't exist **")
        self.with_mock(cmd="create MyModel", expected="** class doesn't exist **")

    def test_show(self):
        self.with_mock(cmd="show", expected="** class name missing **")
        self.with_mock(cmd="show MyModel", expected="** class doesn't exist **")
        self.with_mock(cmd="show BaseModel", expected="** instance id missing **")

    def test_destroy_l(self):
        self.with_mock(cmd="destroy", expected="** class name missing **")
        self.with_mock(cmd="destroy MyModel", expected="** class doesn't exist **")
        self.with_mock(cmd="destroy BaseModel", expected="** instance id missing **")
        self.with_mock(cmd="destroy BaseModel 121212", expected="** no instance found **")

    def test_all_l(self):
        self.with_mock(cmd="all MyModel", expected="** class doesn't exist **")

    def test_update_l(self):                                                                                                                                                                                                                                                              self.with_mock(cmd="update", expected="** class name missing **")
        self.with_mock(cmd="update MyModel",                                                                                                                                                                                                                                                                                                                                                                    expected="** class doesn't exist **")
        self.with_mock(cmd="update BaseModel", expected="** instance id missing **")
        self.with_mock(cmd="update BaseModel 121212", expected="** no instance found **")
