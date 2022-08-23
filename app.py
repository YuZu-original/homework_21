from app.request import Request, check_request
from app.shop import Shop
from app.store import Store
from app.exceptions import *
from settings import *



def main():
    print(START_TEXT)
    
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
            print("[!] Такого товара нет")
        except NotEnoughItems:
            print("[!] Не хватает товара на складе")
        else:
            try:
                shop.add(request.product, request.amount)
            except NotEnoughSpaceForUniqueItems:
                print("[!] В магазине не хватает места > 5 уникальных товаров")
            except NotEnoughSpace:
                print("[!] В магазине не хватает места > 20 штук")
            else:
                print(COURIER_ACTIONS_TEXT)
                
                print("\nВ склад хранится:\n")
                for title, count in store.get_items().items():
                    print(count, title)
                
                print("\nВ магазин хранится:\n")
                for title, count in shop.get_items().items():
                    print(count, title)


if __name__ == "__main__":
    main()