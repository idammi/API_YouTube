from pathlib import Path


def get_list_from_file(filename):
    """ generator list from file by path """

    with open(Path(__file__).parent / filename, encoding="utf8", errors='ignore') as file:
        list_from_file = [line.strip() for line in file.readlines()]

    return list_from_file


def add_info_to_file(filename, info_as_list):
    """
    add information type str to file
    info_as_list - this foo information which need to write in the file
    """

    with open(Path(__file__).parent / filename, 'a', encoding="utf8", errors='ignore') as file:
        file.write('\n'.join(str(info_as_str) for info_as_str in info_as_list))