from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass
    
class Person(Animal):
    
    def eat(self, food):