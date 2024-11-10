from domain.facades import OrderingFacade
from domain.decorators import ExtraToppingsDecorator
from domain.adapters import ExternalOrderSystem, OrderAdapter
from factory.donut_factory import DonutFactory


def display_order_details(order, order_type="Standard"):
    print(f"\n=== {order_type} Order Details ===")
    for i, donut in enumerate(order, 1):
        print(f"Donut {i}: {donut.get_description()}")
        if hasattr(donut, 'get_cost'):
            print(f"Cost: ${donut.get_cost():.2f}")


def main():
    print("=== Donut Manufacturing System ===\n")

    print("1. USING ORDERING FACADE")
    ordering_system = OrderingFacade()

    chocolate_order = ordering_system.place_chocolate_donut_order(2)
    vanilla_order = ordering_system.place_vanilla_donut_order(3)

    display_order_details(chocolate_order, "Chocolate")
    display_order_details(vanilla_order, "Vanilla")

    print(f"\nSystem Status: {ordering_system.get_order_status()}")

    print("\n2. USING DECORATOR PATTERN")

    donut_factory = DonutFactory()
    basic_donut = donut_factory.create_basic_donut()
    print(f"Basic Donut Cost: ${basic_donut.get_cost():.2f}")
    print(f"Basic Donut Description: {basic_donut.get_description()}")


    decorated_donut = ExtraToppingsDecorator(basic_donut, ["nuts"])
    print(f"\nDecorated Donut (with nuts):")
    print(f"Cost: ${decorated_donut.get_cost():.2f}")
    print(f"Description: {decorated_donut.get_description()}")


    super_decorated_donut = ExtraToppingsDecorator(decorated_donut, ["sprinkles", "chocolate chips"])
    print(f"\nSuper Decorated Donut:")
    print(f"Cost: ${super_decorated_donut.get_cost():.2f}")
    print(f"Description: {super_decorated_donut.get_description()}")

    print("\n3. USING ADAPTER PATTERN")

    external_system = ExternalOrderSystem()
    adapter = OrderAdapter(external_system)

    external_orders = [
        external_system.create_external_order(
            ["chocolate donut", "vanilla donut"],
            "CUST123"
        ),
        external_system.create_external_order(
            ["vanilla donut", "vanilla donut", "chocolate donut"],
            "CUST456"
        )
    ]

    print("\nProcessing External Orders:")
    for i, ext_order in enumerate(external_orders, 1):
        internal_order = adapter.convert_to_internal_order(ext_order)
        print(f"\nExternal Order {i}:")
        print(f"Original format: {ext_order}")
        print(f"Converted format: {internal_order}")

    print("\n4. COMBINING PATTERNS")

    special_order = ordering_system.place_chocolate_donut_order(1)
    decorated_special = ExtraToppingsDecorator(special_order[0], ["premium sprinkles", "gold leaf"])

    print("\nSpecial Order Details:")
    print(f"Description: {decorated_special.get_description()}")
    print(f"Total Cost: ${decorated_special.get_cost():.2f}")

    print(f"\nFinal System Status: {ordering_system.get_order_status()}")

    print("\n5. CREATING SPECIAL ORDERS")
    premium_ingredients = {
        "Belgian chocolate": 2.0,
        "Madagascar vanilla": 1.5
    }
    extra_toppings = ["golden sprinkles", "edible flowers"]

    special_order = ordering_system.create_special_order(
        donut_type="chocolate",
        premium_ingredients=premium_ingredients,
        extra_toppings=extra_toppings
    )

    display_order_details(special_order, "Premium Special")

if __name__ == "__main__":
    main()