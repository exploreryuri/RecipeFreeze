class Recipe:
    def __init__(self, recipe_id: int, recipe_name: str, recipe_ingredients: list[int], recipe_time: int, recipe_difficulty: str, recipe_photo: str = None):
        self.recipe_id,self.recipe_name,self.recipe_ingredients,self.recipe_time,self.recipe_difficulty,self.recipe_photo = recipe_id,recipe_name,recipe_ingredients,recipe_time,recipe_difficulty,recipe_photo