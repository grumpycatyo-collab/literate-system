# models/donut.py
from copy import deepcopy

class Donut:
    def __init__(self):
        self.toppings = []
        self.filling = None
        self.size = None
        self.ingredients = []  # List to store ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        ingredients_str = ", ".join([i.get_name() for i in self.ingredients])
        return f"Donut(size={self.size}, filling={self.filling}, toppings={self.toppings}, ingredients=[{ingredients_str}])"