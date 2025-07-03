from abc import ABC, abstractmethod

class Searchable(ABC):
    @abstractmethod
    def search(self, name):
        pass