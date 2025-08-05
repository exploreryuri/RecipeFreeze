class User:
    def __init__(self, user_id: int, user_email: str, user_password: str):
        self.user_id, self.user_email, self.user_password, self.user_products = user_id, user_email, user_password,[]
        def user_product_list(self, product_id: int):
            if product_id not in self.products:
                self.products.append(product_id)