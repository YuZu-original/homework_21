from app.request import Request
from app.shop import Shop
from app.storage import Storage
from app.store import Store
from app.exceptions import *

def check_request(request: Request):
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


def main():
    print("- Чтобы отправить курьера нужно вводить подобные сообщения:")
    print("\t- [Забрать/Доставить] [_Кол-во_] [_Товар_] из [_Откуда_] в [_Куда_]")
    print("\t- 'Забрать 3 яблоки из склад в магазин' (не обращайте внимание на неверные окончания)")
    print("- Полезные команды:")
    print("\t- 'exit'/'выход' - чтобы выйти")
    print("(Press Enter to Start)")
    
    input()
    
    store = Store()
    store.add("огурцы", 4)
    store.add("йогурт", 1)
    store.add("колбаса", 8)
    
    shop = Shop()
    shop.add("колбаса", 3)
    shop.add("телевизоры", 1)
    shop.add("огурцы", 5)
    
    
    
    while True:
        user_input = input(">>> ").lower().strip()
        
        if user_input in ['exit', 'выход']:
            print("выход")
            quit()
        
        request = Request(user_input)
        
        error = check_request(request)
        if error is not None:
            print(error)
            continue
        
        try:
            store.remove(request.product, request.amount)
        except NotFoundItem:
            print("Такого товара нет")
        except NotEnoughItems:
            print("Не хватает товара на складе")
        else:
            try:
                shop.add(request.product, request.amount)
            except NotEnoughSpaceForUniqueItems:
                print("В магазине не хватает места > 5 уникальных товаров")
            except NotEnoughSpace:
                print("В магазине не хватает места > 20 штук")
            else:
                print("Нужное количество есть на складе\n" +\
                    f"Курьер забрал {request.amount} {request.product} со {request.from_}\n" +\
                    f"Курьер везет {request.amount} {request.product} со {request.from_} в {request.to}\n" +\
                    f"Курьер доставил {request.amount} {request.product} в {request.to}")
                
                print("\nВ склад хранится:\n")
                for title, count in store.get_items().items():
                    print(count, title)
                
                print("\nВ магазин хранится:\n")
                for title, count in shop.get_items().items():
                    print(count, title)


if __name__ == "__main__":
    main()