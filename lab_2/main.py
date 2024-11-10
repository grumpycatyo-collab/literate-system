from domain.facades import OrderingFacade
from domain.decorators import ExtraToppingsDecorator
from domain.adapters import ExternalOrderSystem, OrderAdapter


def main():
    # Using the Facade
    ordering_system = OrderingFacade()

    # Place orders through the facade
    chocolate_order = ordering_system.place_chocolate_donut_order(2)
    vanilla_order = ordering_system.place_vanilla_donut_order(1)

    # Using the Decorator
    decorated_donut = ExtraToppingsDecorator(chocolate_order[0], ["nuts", "sprinkles"])
    print(f"Decorated donut: {decorated_donut.get_description()}")
    print(f"Total cost: ${decorated_donut.get_cost()}")

    # Using the Adapter
    external_system = ExternalOrderSystem()
    adapter = OrderAdapter(external_system)

    external_order = external_system.create_external_order(["chocolate donut", "vanilla donut"], "CUST123")
    internal_order = adapter.convert_to_internal_order(external_order)

    print(f"Order status: {ordering_system.get_order_status()}")


if __name__ == "__main__":
    main()