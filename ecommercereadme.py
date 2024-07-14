#2. E-commerce Product Catalog System
#Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

#Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. #Each product type shares some common characteristics but also has unique features. The system should be able to display information about each #product appropriately.

# Task 1: Create Base Product Class

#Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
#Expected Outcome: A Product class that can hold general information about a product and display it.

# Task 2: Implement Subclasses for Specific Products

#(ONLY BOOK SUBCLASS REQUIRED)

#Create subclasses Book, Electronic, and Clothing that inherit from Product.
#Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
#Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

# Task 3: Override Display Method in Subclasses

#Override the method to display product information in each subclass to include specific attributes.
#For example, the Book class should display the author, Electronic should display specs, etc.
#Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

# Task 4: Test Product Catalog Functionality

#Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
#Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method #overriding.

# Code Examples:

#class Product:
    # Constructor and common attributes
    # ...

    #def display_info(self):
        # General method to display product info
        # ...

#class Book(Product):
    #def __init__(self, product_id, name, price, author):
        #super().__init__(product_id, name, price)
        #self.author = author

    #def display_info(self):
        # Overridden method for books
        # ...

# Example usage
#my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
#my_book.display_info()