class Generators:
    from random import randint
    from pretty_utils.miscellaneous.generators import nickname, password

    print('\n--- Generators ---')
    print(nickname(), nickname(capital=True), nickname(randint(10, 15)), nickname(randint(7, 11), True))
    print(password(), password(use_specials=True), password(randint(12, 16), use_specials=True))


class Selenium_:
    pass


class Time:
    import os
    from pretty_utils.miscellaneous.time_and_date import strtime_to_unix, unix_to_strtime

    os.environ['TZ'] = 'UTC'
    strtime = '27.06.2022 12:35'

    print('\n--- Time ---')
    print(strtime_to_unix(strtime, 0))  # 12:35 UTC -> 1656333300
    print(strtime_to_unix(strtime, -4))  # 16:35 UTC -> 1656347700
    print(strtime_to_unix(strtime, 3))  # 09:35 UTC -> 1656322500

    print(unix_to_strtime(1656333300, 0))  # 1656333300 -> 12:35 UTC
    print(unix_to_strtime(1656347700, -4))  # 1656347700 -> 16:35 UTC
    print(unix_to_strtime(1656322500, 3))  # 1656322500 -> 09:35 UTC


class Bools:
    from pretty_utils.type_functions.bools import randbool

    print('\n--- Bools ---')
    for _ in range(10):
        print(randbool())


class Floats:
    from pretty_utils.type_functions.floats import randfloat, float_range

    print('\n--- Floats ---')
    start = randfloat(0.1, 0.5, 1)
    stop = randfloat(0.6, 1, 1)
    print(start, stop, float_range(start, stop, 0.1))
    start = randfloat(0.1, 0.5, 2)
    stop = randfloat(0.6, 1, 2)
    print(start, stop, float_range(start, stop, 0.02))


class Lists:
    from pretty_utils.type_functions.lists import split_list, replace_to_null

    print('\n--- Lists ---')
    s_list = [1, None, 3, None, 5, None, 7, None]
    print(split_list(s_list, 4))
    print(split_list(s_list, 4, True))
    print(replace_to_null(s_list))


class Strings:
    from pretty_utils.type_functions.strings import text_between, del_ws, format_number

    print('\n--- Strings ---')
    text = 'ONE TWO THREE'
    print(text_between(text, 'ONE '))
    print(text_between(text, 'ONE ', ' THREE'))
    print(text_between(text, end=' THREE'))
    print(del_ws(text))
    print(format_number(123456))
    print(format_number(123456.7890))

if __name__ == '__main__':
    Generators()
    Time()
    Bools()
    Floats()
    Lists()
    Strings()
