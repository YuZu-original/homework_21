from app.request import Request

def safe_list_get (l: list, idx: int, default=None):
    try:
        return l[idx]
    except IndexError:
        return default


def check_request(request: Request):
    """for main func"""
    if request.product is None:
        return "[?] Вы не ввели название товара"
    if request.amount is None:
        return "[?] Кол-во товара должно быть целым числом"
    if request.from_ is None:
        return "[?] Вы не указали откуда брать товар"
    if request.from_ != "склад":
        return f"[?] Забирать товар можно только из 'склад', а не из '{request.from_}'"
    if request.to is None:
        return "[?] Вы не указали куда везти товар"
    if request.to != "магазин":
        return f"[?] Вы должны привозить товар только в 'магазин', а не в '{request.to}'"