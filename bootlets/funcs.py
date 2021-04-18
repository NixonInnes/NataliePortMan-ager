from typing import Any


def try_draw(obj: Any) -> str:
    if hasattr(obj, "draw"):
        return obj.draw()
    return str(obj)
    # try:
    #    return obj.draw()
    # except (AttributeError, TypeError):
    #    print(f'Unable to draw object of type {obj.__class__.__name__}')
    #    pass
    # return str(obj)


def list_to_str(obj) -> str:
    if isinstance(obj, str):
        return obj
    if isinstance(obj, (list, tuple)):
        return " ".join(obj)
    return str(obj)
