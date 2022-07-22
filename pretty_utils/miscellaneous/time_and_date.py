import time
from datetime import datetime, timezone, timedelta
from typing import Optional


def strtime_to_unix(strtime: str, utc_offset: int = 0, format: str = '%d.%m.%Y %H:%M') -> int:
    """
    Convert string time to unix.

    :param strtime: a string time
    :param utc_offset: hour offset from UTC (0)
    :param format: format for string time parsing (%d.%m.%Y %H:%M)
    :return: the unix time
    """
    return int(datetime.strptime(strtime, format).replace(
        tzinfo=timezone(timedelta(seconds=utc_offset * 60 * 60))).timestamp())


def unix_to_strtime(unix_time: int or float or str = time.time(), utc_offset: Optional[int] = None,
                          format: str = '%d.%m.%Y %H:%M'):
    """
    Convert unix to string time. In particular return the current time.

    :param unix_time: a unix time (current)
    :param utc_offset: hour offset from UTC (None)
    :param format: format for string time output (%d.%m.%Y %H:%M)
    :return: the string time
    """
    if isinstance(unix_time, str):
        unix_time = int(unix_time)

    if utc_offset is None:
        strtime = datetime.utcfromtimestamp(unix_time)
    else:
        strtime = datetime.utcfromtimestamp(unix_time).replace(tzinfo=timezone(timedelta(seconds=utc_offset * 60 * 60)))

    return strtime.strftime(format)
