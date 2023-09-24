
dule that contains class Base"""
import json
import csv
import os.path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON string"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves objects to a JSON file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs:
            list_dic = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to a list of dictionaries"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates and returns an instance with attributes"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file"""
        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = [cls.create(**dic) for dic in list_cls]

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves objects to a CSV file"""
        filename = "{}.csv".format(cls.__name__)
        list_keys = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']

        matrix = []

        if list_objs:
            for obj in list_objs:
                matrix.append([getattr(obj, key) for key in list_keys])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances from a CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        list_keys = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = [cls.create(**dic) for dic in matrix]

        return list_ins
