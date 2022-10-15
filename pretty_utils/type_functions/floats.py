from decimal import Decimal


def randfloat(from_: int or float, to_: int or float, step: int or float = 0.1) -> float:
    """
    Return a random float from the range.

    :param int or float from_: the minimum value
    :param int or float to_: the maximum value
    :param int or float step: the step size (0.1)
    :return float: the random float
    """

    from random import randint

    from_ = Decimal(str(from_))
    to_ = Decimal(str(to_))
    step = Decimal(str(step))
    rand_int = Decimal(str(randint(0, int((to_ - from_) / step))))
    return float(rand_int * step + from_)


def float_range(from_: int or float, to_: int or float, step: int or float = 0.1) -> list:
    """
    Return a float range.

    :param int or float from_: a range start value
    :param int or float to_: the range stop value, not included
    :param int or float step: a step size (0.1)
    :return float: the range list
    """

    from_ = Decimal(str(from_))
    to_ = Decimal(str(to_))
    step = Decimal(str(step))
    range_list = []

    if from_ < to_:
        while from_ < to_:
            range_list.append(float(from_))
            from_ += step

    else:
        while from_ > to_:
            range_list.append(float(from_))
            from_ += step

    return range_list
