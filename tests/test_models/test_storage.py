#!/usr/bin/python3
"""
FileStorage - To prube the class user
"""
import pep8
import unittest
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")
