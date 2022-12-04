import json
import os
import sys
from typing import Optional


def join_path(path: str or tuple or list) -> str:
    """
    Join the path passed in the list or tuple.

    :param str or tuple or list path: path to the object
    :return str: the joined path
    """
    if isinstance(path, str):
        return path
    return os.path.join(*path)


def touch(path: str or tuple or list, file: bool = False) -> bool:
    """
    Create an object (file or directory) if it doesn't exist.

    :param str or tuple or list path: path to the object
    :param bool file: is it a file?
    :return bool: True if the object was created
    """
    path = join_path(path)
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


def write_json(path: str or tuple or list, obj: list or dict, indent: Optional[int] = None) -> None:
    """
    Write Python list or dictionary to a JSON file.

    :param str or tuple or list path: path to the JSON file
    :param list or dict obj: the Python list or dictionary
    :param Optional[int] indent: the indent level
    """
    path = join_path(path)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=indent)


def read_lines(path: str or tuple or list, skip_empty_rows: bool = False) -> list:
    """
    Read a file and return a list of lines.

    :param str or tuple or list path: path to the file
    :param bool skip_empty_rows: if True it doesn't include empty rows to the list
    :return list: the list of lines
    """
    path = join_path(path)
    with open(path) as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]
    if skip_empty_rows and '' in lines:
        lines.remove('')

    return lines


def read_json(path: str or tuple or list) -> list or dict:
    """
    Read a JSON file and return a Python list or dictionary.

    :param str or tuple or list path: path to the JSON file
    :return list or dict: the Python list or dictionary
    """
    path = join_path(path)
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
