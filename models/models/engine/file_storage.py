#!/usr/bin/python3
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
import json
"""
FileStorage - save file and get the data, save the data in
format JSON and create new object to save a json
"""


class FileStorage:
    """ FileStorage """
    def __init__(self):
        """
        __init__ init the constructor
        """
        self.__file_path = "file.json"
        # Create a EMPTY object other way
        # to create a empty dict is = {}
        self.__objects = dict()

    def all(self):
        """
        all - return the dict of the object
        """
        return self.__objects

    def new(self, obj):
        """
        new - set a __object attribute
        """
        # Enter to object ["id"] and put in id_c
        id_c = obj.id
        # Enter to object ["__class__"] and put in nameClass
        # type[obj].__name__
        nameClass = type(obj).__name__
        # Create a new variable and construct the data
        key = str(nameClass) + "." + str(id_c)
        # Set the dict of __objects
        self.__objects[key] = obj

    def save(self):
        """
        save - save the file in __file_path
        """
        # Create new dict to add data
        # It is necessary since the obj is not
        # seralized for JSON
        new_dict = dict()
        for key, value in self.__objects.items():
            obj_dict = value.to_dict()
            new_dict[key] = obj_dict
        new_json = json.dumps(new_dict)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(new_json)

    def reload(self):
        """
        reload - reload the data to json
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                # Read the JSON and create variable
                data = json.loads(f.read())
                # Reload any data of the file and put in __objects
                for key, value in data.items():
                    classes = value['__class__']
                    # Save values in __objects and access to base
                    self.__objects[key] = globals()[classes](**value)

        except Exception:
            # Pass if error
            pass
