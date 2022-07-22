def split_list(s_list: list, n: int = 100, parts: bool = False) -> list:
    """
    Split a list to several lists.

    :param s_list: a list to split
    :param n: split the list into parts of n elements (100)
    :param parts: split the list into n parts (False)
    :return: the split list
    """
    import math

    if parts:
        n = math.ceil(len(s_list) / n)

    if len(s_list) > n:
        lists = []
        for i in range(0, len(s_list), n):
            lists.append(s_list[i:i + n])
    else:
        lists = [s_list]

    return lists


def replace_to_null(r_list: list) -> list:
    """
    Replace all None in a list with 0.

    :param r_list: a list to replace
    :return: the processed list
    """
    for i in range(len(r_list)):
        if r_list[i] is None:
            r_list[i] = 0
    return r_list
