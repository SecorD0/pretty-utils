def randfloat(from_: float, to_: float, decimal_places: int = None) -> float:
    """
    Return a random float from the range.

    :param from_: the minimum value
    :param to_: the maximum value
    :param decimal_places: round to N decimal places (don't round)
    :return: the random float
    """
    from random import uniform

    if decimal_places:
        return round(uniform(from_, to_), decimal_places)
    return uniform(from_, to_)


def float_range(from_: int or float, to_: int or float, step: int or float) -> list:
    """
    Return a float range.

    :param from_: a range start value (included)
    :param to_: the range stop value (not included)
    :param step: a step size
    :return: the range list
    """
    import decimal
    from numpy import arange

    decimal_places = decimal.Decimal(str(step)).as_tuple().exponent * -1

    return [round(x, decimal_places) for x in arange(from_, to_, step)]
