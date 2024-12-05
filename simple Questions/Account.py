class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "Was Debited")

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "Was credited")

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(560)
acc1.credit(23000)
acc1.debit(5400)
