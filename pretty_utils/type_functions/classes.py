class AutoRepr:
    """Contains a __repr__ function that automatically builds the output of a class using all its variables."""

    def __repr__(self):
        values = ('{}={!r}'.format(key, value) for key, value in vars(self).items())
        return '{}({})'.format(self.__class__.__name__, ', '.join(values))
