# ---------------------------------------------------<<1>>------------------------------------------------
# Person Class:

# Create a Person class with attributes such as name, age, and address.
# Add a method to calculate the birth year based on the current year.

# solution
# from datetime import datetime as dt
# class Person:
#     def __init__(self, name, age, adress):
#         self.name = name
#         self.age = age
#         self.adress = adress

#     def birth_year(self):
#         print(f"So {self.name} had born in {dt.now().year - self.age}")

# Naiem = Person("MD Naiem", 17, "Kendua")
# Naiem.birth_year()

# Completed

# ---------------------------------------------------<<2>>------------------------------------------------

# Book Class:

# Create a Book class with attributes like title, author, and publication year.
# Include a method to display information about the book.

# solution
# from datetime import datetime as dt

# class Book:
#     def __init__(self, tittle, author, publication_year):
#         self.tittle = tittle
#         self.author = author
#         self.publication_year = publication_year
        
#     def book_info(self):
#         print(f"The book tittle is {self.tittle}")
#         print(f"The book author is {self.author}")
#         print(f"The book had published in {self.publication_year}")
#         print(f"The book age is {dt.now().year - self.publication_year}")

# DSABook = Book("My DSA Book", "MD Naiem Hosen", 2012)
# DSABook.book_info()

# Completed

# ---------------------------------------------------<<3>>------------------------------------------------

# Bank Account Class:

# Create a BankAccount class with attributes for account number, account holder name, and balance.
# Add methods for deposit, withdrawal, and displaying the account information.

# solution
# class Bank_account:
#     def __init__(self, account_number, account_holder_name, balance):
#         self.account_number = account_number
#         self.account_holder_name = account_holder_name
#         self.balance = balance

#     def deposit(self, ammount):
#         self.balance += ammount
    
#     def withdraw(self, ammount):

#         if ammount > self.balance:
#             print(f"You don't have {ammount} in your account.")
#         else:
#             self.balance -= ammount
    
#     def account_info(self):
#         print(f"So {self.account_holder_name}, your account info are, account number {self.account_number} and current balance is {self.balance}")

# my_account = Bank_account(545451, "MD Naiem Hosen", 500)
# my_account.deposit(1000)
# my_account.withdraw(300)
# my_account.account_info()

# Completed

# ---------------------------------------------------<<4>>------------------------------------------------

# Rectangle Class:

# Implement a Rectangle class with attributes for length and width.
# Include methods to calculate the area and perimeter of the rectangle.

# Solution
# class Rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
    
#     def area(self):
#         print(f"Ractangle area is {self.lenght * self.width}")
    
#     def peramiters(self):
#         print(f"Ractangle peramiters are {2 * (self.lenght + self.width)}")

# my_ractangle = Rectangle(5, 7)
# my_ractangle.area()
# my_ractangle.peramiters()

# Completed

# ---------------------------------------------------<<5>>------------------------------------------------

# Student Class:

# Develop a Student class with attributes for name, age, and grades.
# Add a method to calculate the average grade.

# ---------------------------------------------------<<6>>------------------------------------------------

# Library Catalog Class:

# Create a LibraryCatalog class to manage a collection of books.
# Include methods to add a book, remove a book, and display the available books.

# ---------------------------------------------------<<7>>------------------------------------------------

# Employee Class:

# Design an Employee class with attributes for name, position, and salary.
# Implement a method to give a salary raise.

# ---------------------------------------------------<<8>>------------------------------------------------

# Product Inventory Class:

# Build a ProductInventory class to keep track of products in stock.
# Include methods for adding products, removing products, and displaying the current inventory.

# ---------------------------------------------------<<9>>------------------------------------------------

# Shape Hierarchy:

# Create a hierarchy of shape classes (e.g., Circle, Square, Triangle) with a common base class (Shape).
# Include methods to calculate area and perimeter for each shape.

# ---------------------------------------------------<<10>>------------------------------------------------
  
# Vehicle Class:

# Develop a Vehicle class with attributes for make, model, and year.
# Add a method to check if the vehicle is a classic (e.g., more than 25 years old).