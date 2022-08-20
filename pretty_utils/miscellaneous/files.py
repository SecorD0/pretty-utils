import json
import os
import sys


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


def read_lines(path: str, skip_empty_rows: bool = False) -> list:
    """
    Read a file and return a list of lines.

    :param str path: path to the file
    :return list: the list of lines
    """
    with open(path) as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    if skip_empty_rows:
        lines.remove('')
    return lines


def read_json(path: str) -> list or dict:
    """
    Read a JSON file and return a Python list or dictionary.

    :param str path: path to the JSON file
    :return list or dict: the Python list or dictionary
    """
    return json.load(open(path))


def resource_path(relative_path: str) -> str:
    """
    Get absolute path to resource, works for dev and for PyInstaller.

    :param str relative_path: a relative path to the resource
    :return str: an absolute path to the resource
    """
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)
