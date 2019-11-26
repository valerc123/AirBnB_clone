#!/usr/bin/python3
"""
Cretae instance for storage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
