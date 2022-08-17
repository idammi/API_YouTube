import sys
from pathlib import Path


def file_exists(path_to_file):
    """Check file exists by path"""
    path = Path(path_to_file)

    if not path.is_file():
        raise Exception(f"not found file by {path}")

    return path_to_file


def check_path(filename):
    """
    This func need for absolut path in the executable file
    https://stackoverflow.com/questions/22472124/what-is-sys-meipass-in-python
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        bundle_dir = Path(sys._MEIPASS)
    else:
        bundle_dir = Path(__file__).parent

    return file_exists(Path.cwd() / bundle_dir / filename)


def get_list_from_file(filename):
    """ generator list from file by path """

    with open(check_path(filename), encoding="utf8", errors='ignore') as file:
        list_from_file = [line.strip() for line in file.readlines() if line is not "\n"]

    return list_from_file


def add_info_to_file(filename, info_as_list):
    """
    add information type str to file
    info_as_list - this foo information which need to write in the file
    """

    with open(check_path(filename), "r+", encoding="utf8", errors="ignore") as file:

        if not file.readlines()[-1] == "\n":
            file.write("\n")
        file.write("\n".join(str(info_as_str) for info_as_str in info_as_list))
