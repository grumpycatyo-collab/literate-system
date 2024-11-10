from factory.donut_factory import DonutFactory
from domain.decorators import ExtraToppingsDecorator, PremiumIngredientDecorator
from domain.manufacturing_system import ManufacturingSystem

class OrderingFacade:
    def __init__(self):
        self.donut_factory = DonutFactory()
        self.manufacturing_system = ManufacturingSystem()

    def place_chocolate_donut_order(self, quantity):
        order = []
        for _ in range(quantity):
            donut = self.donut_factory.create_chocolate_donut()
            order.append(donut)
        self.manufacturing_system.add_order(order)
        return order

    def place_vanilla_donut_order(self, quantity):
        order = []
        for _ in range(quantity):
            donut = self.donut_factory.create_vanilla_donut()
            order.append(donut)
        self.manufacturing_system.add_order(order)
        return order

    def get_order_status(self):
        active = len(self.manufacturing_system.get_active_orders())
        completed = len(self.manufacturing_system.get_completed_orders())
        return f"Active orders: {active}, Completed orders: {completed}"

    def create_special_order(self, donut_type, premium_ingredients=None, extra_toppings=None):
        if donut_type == "chocolate":
            donut = self.donut_factory.create_chocolate_donut()
        else:
            donut = self.donut_factory.create_vanilla_donut()

        if premium_ingredients:
            for ingredient, cost in premium_ingredients.items():
                donut = PremiumIngredientDecorator(donut, ingredient, cost)

        if extra_toppings:
            donut = ExtraToppingsDecorator(donut, extra_toppings)

        order = [donut]
        self.manufacturing_system.add_order(order)
        return order