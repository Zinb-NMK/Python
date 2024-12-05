class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,odr2 ):
        return self.price > odr2.price
odr1 = Order("Watch", 1000)
odr2 = Order("Glass", 500)

print(odr1 > odr2)