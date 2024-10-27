# Laboratory Work 1: Creational Design Patterns

## Student Information
- **Name:** Plămădeală Maxim
- **Group:** FAF-222

## Overview
This laboratory work focuses on implementing creational design patterns in a Python project. The implemented patterns are:
1. Singleton Pattern
2. Factory Method Pattern
3. Prototype Pattern
4. Abstract Factory Pattern

## Project Description
The project implements a donut manufacturing system that manages the creation of different types of donuts, their ingredients, and order processing. It demonstrates how various creational patterns can be used to create a flexible and maintainable manufacturing system.

## Design Patterns Implementation

### 1. Singleton Pattern

#### Implemented Class:
- `ManufacturingSystem`: Ensures a single instance of the manufacturing system exists

#### Demonstration:
```python
class ManufacturingSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ManufacturingSystem, cls).__new__(cls)
            cls._instance.active_orders = []
            cls._instance.completed_orders = []
        return cls._instance
```

### 2. Factory Method Pattern

#### Implemented Classes:
- `DonutFactory`: Creates different types of donuts
- `IngredientFactory`: Creates different types of ingredients

#### Demonstration:
```python
class DonutFactory:
    def create_chocolate_donut(self) -> Donut:
        donut = self.create_basic_donut()
        donut.filling = "chocolate"
        donut.toppings = ["chocolate sprinkles"]
        donut.add_ingredient(IngredientFactory.create_ingredient("chocolate"))
        return donut
```

### 3. Prototype Pattern

#### Implemented in:
- `Donut` class with clone functionality

#### Demonstration:
```python
class Donut:
    def clone(self):
        return deepcopy(self)
```

### 4. Abstract Factory Pattern

#### Implemented Classes:
- `IngredientFactory`: Creates families of related ingredients
- Various ingredient classes (Flour, Sugar, Chocolate, Vanilla)

#### Demonstration:
```python
class IngredientFactory:
    @staticmethod
    def create_ingredient(ingredient_type: str):
        ingredients = {
            "flour": Flour(),
            "sugar": Sugar(),
            "chocolate": Chocolate(),
            "vanilla": Vanilla()
        }
        return ingredients.get(ingredient_type.lower())
```

## Project Structure
```
lab_1/
├── main.py
├── models/
│   ├── donut.py
│   └── ingredients.py
├── factory/
│   ├── donut_factory.py
│   └── ingredient_factory.py
└── domain/
    └── manufacturing_system.py
```

## How to Run
1. Navigate to the project directory
2. Execute: `python3 main.py`

## Output Example
```
Singleton check: True

Active orders:
Donut(size=medium, filling=chocolate, toppings=['chocolate sprinkles'], ingredients=[Flour, Sugar, Chocolate])
Donut(size=medium, filling=vanilla, toppings=['sugar powder'], ingredients=[Flour, Sugar, Vanilla])
Donut(size=medium, filling=chocolate, toppings=['chocolate sprinkles', 'gold leaf'], ingredients=[Flour, Sugar, Chocolate, Chocolate])
Donut(size=large, filling=None, toppings=['custom topping'], ingredients=[Flour, Sugar, Chocolate])

Completed orders:
[List of completed orders...]
```

## Conclusions
This laboratory work successfully demonstrates the implementation and practical application of various creational design patterns. Each pattern serves a specific purpose:
- **Singleton** ensures system-wide consistency in order management
- **Factory Method** provides flexible donut creation
- **Prototype** enables efficient donut customization
- **Abstract Factory** manages ingredient creation systematically

The combination of these patterns results in a flexible, maintainable, and extensible donut manufacturing system. The implementation showcases how creational patterns can be used together to create a robust object creation framework.
