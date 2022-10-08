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

book1 = Book("Harry Potter", 12, "J. K. Rowling", 120)
book2 = Book("Sherlock Homes", 18, "Arthur Conan Doyle", 220)

print(f"Original price of book1 is {book1.price}")

book1.set_discount(0.2)
book1_final_price = book1.price - book1.__discount * book1.price
print(f"Final price of book1 is {book1_final_price}")
