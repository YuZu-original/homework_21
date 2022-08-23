from typing import Any

def safe_list_get (l: list, idx: int, default=None) -> Any:
    """
    like dict.get() function.
    Return value by index or default
    """
    try:
        return l[idx]
    except IndexError:
        return default