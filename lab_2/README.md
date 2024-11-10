# Laboratory Work 2: Structural Design Patterns
**Name**: Plămădeală Maxim

**Group**: FAF-222

---
## Overview
This laboratory work extends the previous donut manufacturing system by implementing structural design patterns. The implemented patterns are:

Decorator Pattern
Facade Pattern
Adapter Pattern

Project Description
The project enhances the donut manufacturing system by adding new functionalities such as dynamic pricing, simplified ordering interface, and external system integration. These improvements demonstrate how structural patterns can enhance system flexibility and maintainability.

---
## Design Patterns Implementation
### 1. Decorator Pattern
Purpose:
Allows dynamic addition of extra features and costs to donuts without altering their basic structure.
Implementation:

```python
# domain/decorators.py
class DonutDecorator(ABC):
    def __init__(self, donut: Donut):
        self._donut = donut

    @abstractmethod
    def get_cost(self):
        pass

class ExtraToppingsDecorator(DonutDecorator):
    def get_cost(self):
        return self._donut.get_cost() + (len(self.extra_toppings) * 0.5)

    def get_description(self):
        return f"{self._donut.get_description()} with extra {', '.join(self.extra_toppings)}"
```

### 2. Facade Pattern
Purpose:
Provides a simplified interface for the complex donut manufacturing system.
Implementation:
```python
# domain/facades.py
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
```
### 3. Adapter Pattern
Purpose:
Enables integration with external ordering systems by converting their format to our system's format.
Implementation:
```python
# domain/adapters.py
class OrderAdapter:
    def __init__(self, external_system: ExternalOrderSystem):
        self.external_system = external_system

    def convert_to_internal_order(self, external_order):
        return {
            "items": external_order["order_items"],
            "customer_id": external_order["customer"],
            "status": "active"
        }
```
---
## Project Structure

```commandline
lab_2/
├── main.py
├── models/
│   ├── donut.py
│   └── ingredients.py
├── factory/
│   ├── donut_factory.py
│   └── ingredient_factory.py
└── domain/
    ├── decorators.py
    ├── facades.py
    ├── adapters.py
    └── manufacturing_system.py
```
---
## Usage Example
NOTE: Usage example is different from the actual `main.py`. Same for **Output Example**

To run the project do:
```python
python3 lab_2/main.py
```

Here how the `main.py` should look like:

```python
def main():
    # Using Facade
    ordering_system = OrderingFacade()
    chocolate_order = ordering_system.place_chocolate_donut_order(2)
    
    # Using Decorator
    decorated_donut = ExtraToppingsDecorator(
        chocolate_order[0], 
        ["nuts", "sprinkles"]
    )
    print(f"Decorated donut: {decorated_donut.get_description()}")
    print(f"Total cost: ${decorated_donut.get_cost()}")
    
    # Using Adapter
    external_system = ExternalOrderSystem()
    adapter = OrderAdapter(external_system)
    external_order = external_system.create_external_order(
        ["chocolate donut"], 
        "CUST123"
    )
    internal_order = adapter.convert_to_internal_order(external_order)
```
---
## Output Example
```bash
=== Donut Manufacturing System ===

1. USING ORDERING FACADE
Chocolate Order Details:
Donut 1: medium donut with chocolate filling
Cost: $2.00
Donut 2: medium donut with chocolate filling
Cost: $2.00

2. USING DECORATOR PATTERN
Basic Donut Cost: $2.00
Decorated Donut (with nuts):
Cost: $2.50
Description: medium donut with chocolate filling with extra nuts

3. USING ADAPTER PATTERN
Processing External Orders:
External Order 1:
Original format: {'order_items': ['chocolate donut'], 'customer': 'CUST123', 'status': 'pending'}
Converted format: {'items': ['chocolate donut'], 'customer_id': 'CUST123', 'status': 'active'}
```
---
### Conclusions
The implementation of structural design patterns has significantly improved the donut manufacturing system:

- The **Decorator Pattern** provides a flexible way to add new features and modify costs without changing the core donut classes.
- The **Facade Pattern** simplifies the system's usage by providing a clean, high-level interface for common operations.
- The **Adapter Pattern** enables seamless integration with external systems by converting between different data formats.

These patterns work together to create a more flexible and maintainable system while keeping the code organized and easy to understand.
The implementation demonstrates how structural patterns can be effectively used to enhance system architecture while maintaining clean and maintainable code.