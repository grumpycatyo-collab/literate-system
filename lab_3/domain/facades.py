from factory.donut_factory import DonutFactory
from domain.decorators import ExtraToppingsDecorator, PremiumIngredientDecorator
from domain.manufacturing_system import ManufacturingSystem


class OrderingFacade:
    def __init__(self):
        self.donut_factory = DonutFactory()
        self.manufacturing_system = ManufacturingSystem()
        self.observers = []
        self.order_status = "Ready"

    def attach(self, observer):
        """Add an observer to the notification list"""
        self.observers.append(observer)

    def detach(self, observer):
        """Remove an observer from the notification list"""
        self.observers.remove(observer)

    def notify_observers(self, order_details):
        """Notify all observers about order status changes"""
        for observer in self.observers:
            observer.update(self.order_status, order_details)

    def place_chocolate_donut_order(self, quantity):
        order = []
        for _ in range(quantity):
            donut = self.donut_factory.create_chocolate_donut()
            order.append(donut)
        self.manufacturing_system.add_order(order)

        self.order_status = "New Chocolate Donut Order"
        self.notify_observers({
            "type": "chocolate",
            "quantity": quantity,
            "order": order
        })
        return order

    def place_vanilla_donut_order(self, quantity):
        order = []
        for _ in range(quantity):
            donut = self.donut_factory.create_vanilla_donut()
            order.append(donut)
        self.manufacturing_system.add_order(order)

        self.order_status = "New Vanilla Donut Order"
        self.notify_observers({
            "type": "vanilla",
            "quantity": quantity,
            "order": order
        })
        return order

    def get_order_status(self):
        active = len(self.manufacturing_system.get_active_orders())
        completed = len(self.manufacturing_system.get_completed_orders())
        status = f"Active orders: {active}, Completed orders: {completed}"

        self.order_status = "Status Check"
        self.notify_observers({
            "active_orders": active,
            "completed_orders": completed
        })
        return status

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

        self.order_status = "New Special Order"
        self.notify_observers({
            "type": "special",
            "donut_type": donut_type,
            "premium_ingredients": premium_ingredients,
            "extra_toppings": extra_toppings,
            "order": order
        })
        return order