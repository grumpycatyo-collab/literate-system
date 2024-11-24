from domain.facades import OrderingFacade

from domain.commands import OrderInvoker, PlaceDonutOrderCommand, CreateSpecialOrderCommand
from domain.observers import KitchenDisplayObserver, OrderManagementObserver, NotificationObserver

def main():
    ordering_system = OrderingFacade()

    kitchen_display = KitchenDisplayObserver()
    order_management = OrderManagementObserver()
    notification_system = NotificationObserver()

    ordering_system.attach(kitchen_display)
    ordering_system.attach(order_management)
    ordering_system.attach(notification_system)

    order_invoker = OrderInvoker()

    chocolate_order = PlaceDonutOrderCommand(ordering_system, "chocolate", 2)
    vanilla_order = PlaceDonutOrderCommand(ordering_system, "vanilla", 3)

    print("\nPlacing orders using Command pattern:")
    order_invoker.execute_command(chocolate_order)
    order_invoker.execute_command(vanilla_order)

    premium_ingredients = {
        "Belgian chocolate": 2.0,
        "Madagascar vanilla": 1.5
    }
    extra_toppings = ["golden sprinkles", "edible flowers"]

    special_order = CreateSpecialOrderCommand(
        ordering_system,
        "chocolate",
        premium_ingredients,
        extra_toppings
    )
    order_invoker.execute_command(special_order)

    print("\nUndoing last order:")
    order_invoker.undo_last_command()

    print(f"\nFinal System Status: {ordering_system.get_order_status()}")

if __name__ == "__main__":
    main()