class Product:

    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"You Saved: {self.you_save}")
        print(f"Rating: {self.rating}")

    def get_deal_price(self):
        return self.deal_price


class Electronic(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months


class Grocery(Product):
    pass



class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.item_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address


    def add_item(self, product, quantity):
        self.item_in_cart.append((product, quantity))


    def display_order_details(self):
        for product, quantity in self.item_in_cart:
            product.display_product_details()
            print(f"Quantity: {quantity}")

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.item_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print(f"Total Bill: {total_bill}")


milk = Grocery('milk', 40, 25, 3.5)
tv = Electronic('tv', 45000, 40000, 4.9)
order = Order("parul", "Vadodara")
order.add_item(milk, 2)
order.add_item(tv, 1)
order.display_order_details()
order.display_total_bill()