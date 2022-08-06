import json
import os


def touch(path: str, file: bool = False) -> bool:
    """
    Create an object (file or directory) if it doesn't exists.

    :param str path: path to the object
    :param bool file: is it a file?
    :return bool: True if the object was created
    """
    if file:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
            return True
        return False

    if not os.path.isdir(path):
        os.mkdir(path)
        return True
    return False


def read_lines(path: str) -> list:
    """
    Read a file and return a list of lines.

    :param str path: path to the file
    :return list: the list of lines
    """
    with open(path) as f:
        lines = f.readlines()
    return lines


def read_json(path: str) -> list or dict:
    """
    Read a JSON file and return a Python list or dictionary.

    :param str path: path to the JSON file
    :return list or dict: the Python list or dictionary
    """
    return json.load(open(path))
