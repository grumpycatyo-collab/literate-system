# Laboratory Work 2: Structural Design Patterns (self-made)
**Name**: Plămădeală Maxim
**Group**: FAF-222

---
## Overview
This laboratory work extends the donut manufacturing system by implementing behavioral design patterns. The implemented patterns are:
* Observer Pattern
* Command Pattern
These patterns enhance the system's communication and operation handling capabilities.

## Project Description
The project adds new functionalities to the donut manufacturing system, including:
* Real-time order status notifications
* Command-based order processing
* Order history tracking
* Undo capabilities for orders

---
## Design Patterns Implementation
### 1. Observer Pattern
**Purpose**:
Implements a notification system that keeps different parts of the system updated about order status changes.
In my case, the notification system is attached to the Ordering Facade, so on each order there will be a notification
triggered by the observers.

Implementation:
```python
# Abstract representation for every observer
class OrderObserver(ABC):
    @abstractmethod
    def update(self, status, order_details):
        pass

# Observer Example
class KitchenDisplayObserver(OrderObserver):
    def update(self, status, order_details):
        print(f"\nKITCHEN DISPLAY UPDATE:") # Can do anything, chose to print to show that it works
        print(f"Status: {status}")
        if "type" in order_details:
            print(f"Order Type: {order_details['type']}")

# Modifications to the Ordering Facade to be able to attach observers to it
class OrderingFacade:
    def __init__(self):
        self.observers = []
        self.order_status = "Ready"

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self, order_details):
        for observer in self.observers:
            observer.update(self.order_status, order_details)
```

### 2. Command Pattern
Purpose:
Encapsulates order requests as objects, enabling order history tracking and undo operations. 
In my case, it encapsulates the `ordering_facade._place_chocolate_donut_order(self.quantity)` and makes it simpler. It also
offers the possibility to track or undo the order using `self.last_order` and `undo(self)` parts.

Implementation:
```python
class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class PlaceDonutOrderCommand(OrderCommand):
    # Initialization based on the Ordering Facade
    def __init__(self, ordering_facade, donut_type, quantity):
        self.ordering_facade = ordering_facade
        self.donut_type = donut_type
        self.quantity = quantity
        self.last_order = None

    # Execute command (abstractisation for the `place_chocolate_donut_order`)
    def execute(self):
        if self.donut_type == "chocolate":
            self.last_order = self.ordering_facade.place_chocolate_donut_order(self.quantity)
        return self.last_order

    # Undo command (abstractisation for the `remove_order(self.last_order)`    
    def undo(self):
        if self.last_order:
            self.ordering_facade.manufacturing_system.remove_order(self.last_order)
```

---
## Project Structure
```
lab_3/
├── main.py
├── domain/
│   ├── commands.py
│   ├── observers.py
│   ├── facades.py
│   └── manufacturing_system.py
└── models/
    └── donut.py
```
P.S: Same as previous but with `observers.py` and `commands.py` added.

---
## Usage Example
```python
def main():
    # Create the ordering system
    ordering_system = OrderingFacade()

    # Create and attach observers
    kitchen_display = KitchenDisplayObserver()
    order_management = OrderManagementObserver()
    notification_system = NotificationObserver()

    ordering_system.attach(kitchen_display)
    ordering_system.attach(order_management)
    ordering_system.attach(notification_system)

    # Create command invoker (designed to execute the created commands)
    order_invoker = OrderInvoker()

    # Create and execute commands
    chocolate_order = PlaceDonutOrderCommand(ordering_system, "chocolate", 2)
    order_invoker.execute_command(chocolate_order)

    # Demonstrate undo functionality
    order_invoker.undo_last_command()
```
To launch the actual code, use `python3 lab_3/main.py`.

---
## Output Example
```bash
=== Donut Manufacturing System ===

KITCHEN DISPLAY UPDATE:
Status: New Chocolate Donut Order
Order Type: chocolate
Quantity: 2

ORDER MANAGEMENT UPDATE:
Status: New Order
Active Orders: 1
Completed Orders: 0

Undoing last order...
Order removed from system

Final System Status: Active orders: 0, Completed orders: 0
```

---
## Conclusions
The implementation of behavioral design patterns has significantly enhanced the donut manufacturing system:
The **Observer Pattern** enables *real-time notifications* across different system components.
The **Command Pattern** provides a robust way to manage orders, supporting features like *undo operations* and *order history tracking*.
The implementation demonstrates how behavioral patterns can effectively manage complex interactions between system components while maintaining clean and maintainable code.
