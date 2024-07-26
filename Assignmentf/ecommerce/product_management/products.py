class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, stock={self.stock})"

def add_product(product_list, product):
    product_list.append(product)

def remove_product(product_list, product_id):
    product_list[:] = [product for product in product_list if product.product_id != product_id]

def get_product(product_list, product_id):
    for product in product_list:
        if product.product_id == product_id:
            return product
    return None

