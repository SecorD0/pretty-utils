from typing import Optional


def text_between(text: str, begin: str = '', end: str = '') -> Optional[str]:
    """
    Extract a text between strings.

    :param text: a source text
    :param begin: a string from the end of which to start the extraction
    :param end: a string at the beginning of which the extraction should end
    :return: the extracted text or None
    """
    try:
        if begin:
            start = text.index(begin) + len(begin)
        else:
            start = 0
    except:
        start = 0

    try:
        if end:
            end = text.index(end, start)
        else:
            end = len(text)
    except:
        end = len(text)
    return text[start:end]


def del_ws(text: str) -> str:
    """
    Delete whitespaces.

    :param text: a source text
    :return: the text without whitespaces
    """
    return text.replace(" ", "")


def format_number(number: int or str) -> str:
    """
    Return formated number like 3 392 233.9420.

    :param number: a number for formating
    :return: the text without whitespaces
    """
    return '{0:,}'.format(number).replace(',', ' ')
