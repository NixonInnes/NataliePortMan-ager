
class Extend:
    def __init__(self, filename):
        self.filename = filename

    def draw(self):
        return r'{% extends "' + self.filename + r'" %}'


class Import:
    def __init__(self, filename, import_as):
        self.filename = filename
        self.import_as = import_as

    def draw(self):
        return  r'{% import "' + self.filename + '" as '\
                  + self.import_as + r' %}'





class Something:
    defaults = {}
    _combined_keys = []

    def __init__(self, *args, **kwargs):
        self.args = args
        self._kwargs = kwargs
        self.kwargs = self._combine_kwargs(self.defaults, kwargs)

    def _skip_key(self, key):
        return key.startswith('_')

    def _combine_kwargs(self, kwargs1, kwargs2):
        kwargs = {k:v for k,v in kwargs1.items() if not self._skip_key(key)}
        for key, value in kwargs2.items():
            if self._skip_key(key):
                continue
            if key in self._combined_keys and key in kwargs:
                kwargs[key] = kwargs[key] + value
            else:
                kwargs[key] = value
        return kwargs

    def __call__(self, *args, **kwargs):
        return self.__class__(
            *args if args else *self.args,
            **{**self.kwargs, **kwargs}
        )

    def __repr__(self) -> str:
        s = self.__class__.__qualname__ + '('
        if self.args:
            s += ', '.join([arg.__repr__() for arg in self.args])
        if self._kwargs:
            if self.args:
                s += ', '
            s += ', '.join([f'{k}={v.__repr__()}' for k,v in self._kwargs.items()])
        s += ')'
        return s