from repository.IngredientRepository import IngredientRepository


class IngredientStorage:
    def __init__(self):
        ingredients = IngredientRepository().get_ingredients()
        self.storage = {}
        for i in ingredients:
            self.storage[i.id] = i

    def to_update(self):
        ingredients = []
        for id, ing in self.storage.items():
            ingredients.append((ing.count, ing.id))
        return ingredients
