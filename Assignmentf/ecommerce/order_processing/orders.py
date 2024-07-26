class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product_id):
        self.items[:] = [(product, qty) for product, qty in self.items if product.product_id != product_id]

    def get_total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        item_details = ", ".join([f"{product.name} x{quantity}" for product, quantity in self.items])
        return f"Order(id={self.order_id}, customer={self.customer_name}, items=[{item_details}])"

def create_order(order_list, order):
    order_list.append(order)

def cancel_order(order_list, order_id):
    order_list[:] = [order for order in order_list if order.order_id != order_id]

def get_order(order_list, order_id):
    for order in order_list:
        if order.order_id == order_id:
            return order
    return None