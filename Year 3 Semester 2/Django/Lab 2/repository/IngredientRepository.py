from model.Ingredient import Ingredient


class IngredientRepository:

    def get_ingredients(self):
        ingredients = []
        for ingredient in Ingredient.select().order_by(Ingredient.name.asc()):
            ingredients.append(self.__extract_ingredient(ingredient))
        return ingredients

    def __extract_ingredient(self, ingredient: Ingredient) -> Ingredient:
        return Ingredient(
            name=ingredient.name,
            price=ingredient.price,
            count=ingredient.count,
            id=ingredient.id,
        )
