from abc import ABC, abstractmethod

class Storage(ABC):
    @property
    @abstractmethod
    def items(self):
        pass
    
    @property
    @abstractmethod
    def capacity(self):
        pass
    
    @abstractmethod
    def add(self, title, count):
        """add items"""
        pass
    
    @abstractmethod
    def remove(self, title, count):
        """remove items"""
        pass
    
    @abstractmethod
    def get_free_space(self):
        """get free space"""
        pass
    
    @abstractmethod
    def get_items(self):
        """get all items"""
        pass
    
    @abstractmethod
    def get_unique_items_count(self):
        """get unique items count"""
        pass
