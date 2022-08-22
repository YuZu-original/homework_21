def safe_list_get (l: list, idx: int, default=None):
    try:
        return l[idx]
    except IndexError:
        return default