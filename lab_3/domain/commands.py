# domain/commands.py
from abc import ABC, abstractmethod

class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class PlaceDonutOrderCommand(OrderCommand):
    def __init__(self, ordering_facade, donut_type, quantity):
        self.ordering_facade = ordering_facade
        self.donut_type = donut_type
        self.quantity = quantity
        self.last_order = None

    def execute(self):
        if self.donut_type == "chocolate":
            self.last_order = self.ordering_facade.place_chocolate_donut_order(self.quantity)
        elif self.donut_type == "vanilla":
            self.last_order = self.ordering_facade.place_vanilla_donut_order(self.quantity)
        return self.last_order

    def undo(self):
        if self.last_order:
            self.ordering_facade.manufacturing_system.remove_order(self.last_order)
            self.last_order = None

class CreateSpecialOrderCommand(OrderCommand):
    def __init__(self, ordering_facade, donut_type, premium_ingredients=None, extra_toppings=None):
        self.ordering_facade = ordering_facade
        self.donut_type = donut_type
        self.premium_ingredients = premium_ingredients
        self.extra_toppings = extra_toppings
        self.last_order = None

    def execute(self):
        self.last_order = self.ordering_facade.create_special_order(
            self.donut_type,
            self.premium_ingredients,
            self.extra_toppings
        )
        return self.last_order

    def undo(self):
        if self.last_order:
            self.ordering_facade.manufacturing_system.remove_order(self.last_order)
            self.last_order = None

class OrderInvoker:
    def __init__(self):
        self.command_history = []

    def execute_command(self, command):
        self.command_history.append(command)
        return command.execute()

    def undo_last_command(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()