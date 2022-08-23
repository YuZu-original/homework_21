from app.utils import safe_list_get

class Request:
    def __init__(self, req: str) -> None:
        req_list = req.split()
        
        self.from_ = safe_list_get(req_list, 4)
        self.to = safe_list_get(req_list, 6)
        amount: str|None = safe_list_get(req_list, 1)
        self.amount = int(amount) if amount is not None and amount.isdigit() else None
        self.product = safe_list_get(req_list, 2)



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