def list_to_str(obj) -> str:
    if isinstance(obj, str):
        return obj
    if isinstance(obj, (list, tuple)):
        return ' '.join(obj)
    return str(obj)