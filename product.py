id = 0  # ID of the product
quantity = 5  # Quantity of the product
photo = 'photo of the product'  # Photo of the product
name = 'Bread'  # Name of the product

class Products:
    def __init__(self, product_id, product_quantity, product_photo, product_name):
        self.product_id = product_id
        self.product_quantity = product_quantity
        self.product_photo = product_photo
        self.product_name = product_name
    
    def products_identify(self):
        print(f"ProductId: {self.product_id}, ProductQuantity: {self.product_quantity}, ProductPhoto: {self.product_photo}, ProductName: {self.product_name}")

products = Products(id, quantity, photo, name)
products.products_identify()