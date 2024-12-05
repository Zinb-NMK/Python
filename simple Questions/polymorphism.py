class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_num(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
num1 = Complex(1, 3)
num1.show_num()

num2 = Complex(7, 8)
num2.show_num()
num3=num1 - num2
num3.show_num()
