id = 0 #Recipe's ID
name = 'Recipe name' #Recipe's name
photo = 'Recipe photo' #Recipe's photo
ingredients = ['eggs', 'salt', 'herbs', 'spices'] #Recipe's ingredients
time = '15 minutes' #Recipe's time
difficulty = 'piece of cake' #Recipe's difficulty

class Recipe:
    def __init__(self, recipe_id, recipe_name, recipe_photo, recipe_ingredients, recipe_time, recipe_difficulty):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.recipe_photo = recipe_photo
        self.recipe_ingredients = recipe_ingredients
        self.recipe_time = recipe_time
        self.recipe_difficulty = recipe_difficulty
    def recipe_identify(self):
        print(f"RecipeId: {self.recipe_id}, RecipeName: {self.recipe_name}, RecipePhoto: {self.recipe_photo}, RecipeIngredients: {self.recipe_ingredients}, RecipeTime: {self.recipe_time}, RecipeDifficulty: {self.recipe_difficulty}")

recipe = Recipe(id, name, photo, ingredients, time, difficulty)
recipe.recipe_identify()