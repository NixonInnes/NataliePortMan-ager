from .base import try_draw

def join_content_with(chr):
    def get_content(self) -> str:
        return chr.join([try_draw(arg) for arg in self.args])
    return get_content


overwrite_funcs = {
    'join_content_with': join_content_with
}

def overwrite(**kwargs):
    def wrapper(cls):
        for key, value in kwargs.items():
            func, args = value
            setattr(cls, key, overwrite_funcs[func](args))
        return cls
    return wrapper