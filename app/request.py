from app.utils import safe_list_get

class Request:
    def __init__(self, req: str) -> None:
        req_list = req.split()
        
        self.from_ = safe_list_get(req_list, 4)
        self.to = safe_list_get(req_list, 6)
        amount: str|None = safe_list_get(req_list, 1)
        self.amount = int(amount) if amount is not None and amount.isdigit() else None
        self.product = safe_list_get(req_list, 2)
    