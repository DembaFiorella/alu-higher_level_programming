#!/usr/bin/python3
"""Module base: defines the Base class."""
import json


class Base:
    """Base class that manages the id attribute of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The id of the new Base. If None, an id is
                assigned automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of objects to a file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                list_objs = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**obj) for obj in list_objs]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                else:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                if cls.__name__ == 'Rectangle':
                    return [cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])) for row in reader]
                else:
                    return [cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])) for row in reader]
        except FileNotFoundError:
            return []
import csv
