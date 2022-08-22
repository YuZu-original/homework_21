from app.storage import Storage
from app.exceptions import *

class Shop(Storage):
    def __init__(self) -> None:
        self._items: dict[str, int] = dict()
        self._capacity: int = 20
    
    @property
    def items(self):
        return self._items
    
    @property
    def capacity(self):
        return self._capacity
    
    def add(self, title: str, count: int) -> None:
        if self.get_unique_items_count() == 5:
            assert NotEnoughSpaceForUniqueItems("В магазине не хватает места > 5 уникальных товаров")
        if count > self.get_free_space():
            assert NotEnoughSpace("В магазине не хватает места > 20 штук")
        self.items[title] = self.items.get(title, 0) + count
    
    def remove(self, title, count) -> None:
        current_count = self.items.get(title)
        if current_count is None:
            raise NotFoundItem("Такого товара нет")
        if current_count - count < 0:
            raise NotEnoughItems("Не хватает товара в магазине")
        self.items[title] = current_count - count
    
    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())
    
    def get_items(self) -> dict[str, int]:
        return self.items
    
    def get_unique_items_count(self) -> int:
        return len(self.items)
