class Product:
    def __init__(self, product_id: int, name: str, photo: str = None):
        self.id = product_id  # ID продукта
        self.name = name
        self.photo = photo

class User:
    def __init__(self, user_id: int, email: str, password: str):
        self.id = user_id  # ID пользователя
        self.email = email
        self.password = password  # Пароль без шифрования (для учебного примера)
        self.products = []  # Список ID продуктов (один-ко-многим)
    
    def add_product(self, product_id: int):
        """Добавляет ID продукта в список пользователя"""
        if product_id not in self.products:
            self.products.append(product_id)

class Recipe:
    def __init__(self, recipe_id: int, name: str, ingredients: list[int], time: int, difficulty: str, photo: str = None):
        self.id = recipe_id  # ID рецепта
        self.name = name
        self.ingredients = ingredients  # Список ID продуктов (многие-ко-многим)
        self.time = time  # Время приготовления в минутах
        self.difficulty = difficulty
        self.photo = photo
