class Product():
    def __init__(self, name, price, d_price, rating):
        self.name =name
        self.price = price
        self.d_price = d_price
        self.rating = rating
        self.your_save = price-d_price

    def display_details(self):
        print("product: {}".format(self.name))
        print("price: {}".format(self.price))
        print("d_price: {}".format(self.d_price))
        print("rating: {}".format(self.rating))


class ElectricItem(Product):
    def set_Warrent(self, warrent):
        self.warrent = warrent

    def det_warrent(self):
        return self.warrent

    def display_electric_product(self):
        self.display_details()
        print("Warrent {} month".format(self.warrent))

p = ("TV", 13456, 12000, 3.6)
e = ElectricItem("TV", 13456, 12000, 3.6)
e.set_Warrent(24)
e.display_electric_product()
