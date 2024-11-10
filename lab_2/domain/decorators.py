from abc import ABC, abstractmethod
from models.donut import Donut

class DonutDecorator(ABC):
    def __init__(self, donut: Donut):
        self._donut = donut

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class ExtraToppingsDecorator(DonutDecorator):
    def __init__(self, donut: Donut, extra_toppings):
        super().__init__(donut)
        self.extra_toppings = extra_toppings

    def get_cost(self):
        return self._donut.get_cost() + (len(self.extra_toppings) * 0.5)

    def get_description(self):
        return f"{self._donut.get_description()} with extra {', '.join(self.extra_toppings)}"


class PremiumIngredientDecorator(DonutDecorator):
    def __init__(self, donut: Donut, premium_ingredient: str, cost_increase: float):
        super().__init__(donut)
        self.premium_ingredient = premium_ingredient
        self.cost_increase = cost_increase

    def get_cost(self):
        return self._donut.get_cost() + self.cost_increase

    def get_description(self):
        return f"{self._donut.get_description()} with premium {self.premium_ingredient}"