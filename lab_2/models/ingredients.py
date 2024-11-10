from abc import ABC, abstractmethod

class Ingredient(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Flour(Ingredient):
    def get_name(self):
        return "Flour"

class Sugar(Ingredient):
    def get_name(self):
        return "Sugar"

class Chocolate(Ingredient):
    def get_name(self):
        return "Chocolate"

class Vanilla(Ingredient):
    def get_name(self):
        return "Vanilla"