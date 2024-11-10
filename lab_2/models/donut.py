from copy import deepcopy

class Donut:
    def __init__(self):
        self.toppings = []
        self.filling = None
        self.size = None
        self.ingredients = []
        self.base_cost = 2.0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def clone(self):
        return deepcopy(self)

    def get_cost(self):
        return self.base_cost

    def get_description(self):
        return f"{self.size} donut with {self.filling} filling"

    def __str__(self):
        ingredients_str = ", ".join([i.get_name() for i in self.ingredients])
        return f"Donut(size={self.size}, filling={self.filling}, toppings={self.toppings}, ingredients=[{ingredients_str}])"