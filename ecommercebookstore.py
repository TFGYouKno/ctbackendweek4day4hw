class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


# Example usage
books = [
Book("123", "Shantaram", 29.99, "Gregory David Roberts"),
Book("124", "The River We Remember", 19.99, "William Kent Krueger"),
Book("125", "Cirque du Freak", 24.99, "Darren Shan"),
Book("126", "The Last Thing He Told Me", 29.99, "Laura Dave"),
Book("127", "The Silent Patient", 29.99, "Alex Michaelides"),
Book("128", "The Nightingale", 29.99, "Kristin Hannah"),
Book("129", "The Four Winds", 29.99, "Kristin Hannah"),
Book("130", "Gone With the Wind", 29.99, "Margaret Mitchell")
]
for book in books:
    book.display_info()









