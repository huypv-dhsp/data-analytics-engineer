class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = 0.0

    def print_discount(self):
        print(self.__discount)

    def set_discount(self, value):
        self.__discount = value

    def get_final_price(self):
        final_price = self.price - self.__discount * self.price
        return final_price


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages
        self.tax = 0.1

    def get_final_price(self):
        final_price = self.price +  self.__discount * self.price + self.tax * self.price
        return final_price


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.4)
academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')
academic1.set_discount(0.5)
print(novel1.get_final_price())
