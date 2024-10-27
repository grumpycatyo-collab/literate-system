from factory.donut_factory import DonutFactory
from factory.ingredient_factory import IngredientFactory
from domain.manufacturing_system import ManufacturingSystem
from models.donut import Donut

def main():
    # Using Singleton pattern
    manufacturing_system = ManufacturingSystem()
    manufacturing_system2 = ManufacturingSystem()
    print("Singleton check:", manufacturing_system is manufacturing_system2)

    # Create ingredients
    flour = IngredientFactory.create_ingredient("flour")
    sugar = IngredientFactory.create_ingredient("sugar")
    chocolate = IngredientFactory.create_ingredient("chocolate")

    # Using Factory pattern
    donut_factory = DonutFactory()
    chocolate_donut = donut_factory.create_chocolate_donut()
    vanilla_donut = donut_factory.create_vanilla_donut()

    # Using Prototype pattern
    special_chocolate_donut = chocolate_donut.clone()
    special_chocolate_donut.toppings.append("gold leaf")
    special_chocolate_donut.add_ingredient(chocolate)

    custom_donut = Donut()
    custom_donut.size = "large"
    custom_donut.add_ingredient(flour)
    custom_donut.add_ingredient(sugar)
    custom_donut.add_ingredient(chocolate)
    custom_donut.toppings = ["custom topping"]

    manufacturing_system.add_order(chocolate_donut)
    manufacturing_system.add_order(vanilla_donut)
    manufacturing_system.add_order(special_chocolate_donut)
    manufacturing_system.add_order(custom_donut)

    print("\nActive orders:")
    for order in manufacturing_system.get_active_orders():
        print(order)

    manufacturing_system.complete_order(chocolate_donut)
    manufacturing_system.complete_order(vanilla_donut)

    print("\nCompleted orders:")
    for order in manufacturing_system.get_completed_orders():
        print(order)

    print("\nRemaining active orders:")
    for order in manufacturing_system.get_active_orders():
        print(order)

if __name__ == "__main__":
    main()