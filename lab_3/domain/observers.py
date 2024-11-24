from abc import ABC, abstractmethod

class OrderObserver(ABC):
    @abstractmethod
    def update(self, status, order_details):
        pass

class KitchenDisplayObserver(OrderObserver):
    def update(self, status, order_details):
        print(f"\nKITCHEN DISPLAY UPDATE:")
        print(f"Status: {status}")
        if "type" in order_details:
            print(f"Order Type: {order_details['type']}")
            if order_details['type'] == "special":
                print(f"Special Instructions:")
                if order_details.get('premium_ingredients'):
                    print(f"- Premium Ingredients: {order_details['premium_ingredients']}")
                if order_details.get('extra_toppings'):
                    print(f"- Extra Toppings: {order_details['extra_toppings']}")

class OrderManagementObserver(OrderObserver):
    def update(self, status, order_details):
        print(f"\nORDER MANAGEMENT UPDATE:")
        print(f"Status: {status}")
        if "active_orders" in order_details:
            print(f"Active Orders: {order_details['active_orders']}")
            print(f"Completed Orders: {order_details['completed_orders']}")

class NotificationObserver(OrderObserver):
    def update(self, status, order_details):
        print(f"\nNOTIFICATION SYSTEM:")
        print(f"New Status: {status}")
        if "quantity" in order_details:
            print(f"Order placed for {order_details['quantity']} {order_details['type']} donuts")