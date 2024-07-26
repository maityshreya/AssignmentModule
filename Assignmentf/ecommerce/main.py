from ecommerce.product_management.products import Product, add_product, remove_product, get_product
from ecommerce.order_processing.orders import Order, create_order, cancel_order, get_order

def main1():
    # Product Management
    product_list = []
    p1 = Product(product_id=1, name="Laptop", price=1000, stock=50)
    p2 = Product(product_id=2, name="Smartphone", price=500, stock=200)
    
    add_product(product_list, p1)
    add_product(product_list, p2)
    
    print("Product List:")
    for product in product_list:
        print(product)
    
    # Order Processing
    order_list = []
    order1 = Order(order_id=101, customer_name="John Doe")
    order1.add_item(p1, 2)
    order1.add_item(p2, 3)
    
    create_order(order_list, order1)
    
    print("\nOrder List:")
    for order in order_list:
        print(order)
    
    # Update Stock
    p1.update_stock(-2)
    p2.update_stock(-3)
    
    print("\nUpdated Product List:")
    for product in product_list:
        print(product)

if __name__ == "__main__":
    main1()
  