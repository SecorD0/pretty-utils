import asyncio
import multiprocessing
import threading


class AutoRepr:
    """Contains a __repr__ function that automatically builds the output of a class using all its variables."""

    def __repr__(self) -> str:
        values = ('{}={!r}'.format(key, value) for key, value in vars(self).items())
        return '{}({})'.format(self.__class__.__name__, ', '.join(values))


class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonWithLock:
    _instances = {}
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__new__(cls, *args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonThreading(SingletonWithLock):
    pass


class SingletonMultiprocessing(SingletonWithLock):
    _lock = multiprocessing.Lock()


class SingletonAsyncio(SingletonWithLock):
    _lock = asyncio.Lock()
