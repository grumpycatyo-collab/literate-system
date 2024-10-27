from models.ingredients import Flour, Sugar, Chocolate, Vanilla

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