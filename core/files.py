import os
import sys


def resource_path(relative_path):
    """
    Get absolute path to resource

    :param relative_path: The relative path to the resource
    :return: The absolute path to the resource
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
