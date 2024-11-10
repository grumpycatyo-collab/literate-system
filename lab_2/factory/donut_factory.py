from models.donut import Donut
from factory.ingredient_factory import IngredientFactory

class DonutFactory:
    def __init__(self):
        self._basic_donut = None

    def create_basic_donut(self) -> Donut:
        donut = Donut()
        donut.size = "medium"
        donut.add_ingredient(IngredientFactory.create_ingredient("flour"))
        donut.add_ingredient(IngredientFactory.create_ingredient("sugar"))
        return donut

    def create_chocolate_donut(self) -> Donut:
        donut = self.create_basic_donut()
        donut.filling = "chocolate"
        donut.toppings = ["chocolate sprinkles"]
        donut.add_ingredient(IngredientFactory.create_ingredient("chocolate"))
        return donut

    def create_vanilla_donut(self) -> Donut:
        donut = self.create_basic_donut()
        donut.filling = "vanilla"
        donut.toppings = ["sugar powder"]
        donut.add_ingredient(IngredientFactory.create_ingredient("vanilla"))
        return donut