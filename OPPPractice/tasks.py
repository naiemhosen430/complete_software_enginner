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

# solution
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def avarage_grade(self):
#         if len(self.grades) == 0:
#             print(f"{self.name}, you don't have marks")
#         else:
#             total_marks = 0
#             for mark in self.grades:
#                 total_marks += mark
#             print(f'So {self.name}, your avarage mark is {total_marks / len(self.grades)}')

# Naiem = Student("MD Naiem Hosen", 17, [20,50,30]) 
# Naiem.avarage_grade()

# Comoleted

# ---------------------------------------------------<<6>>------------------------------------------------

# Library Catalog Class:

# Create a LibraryCatalog class to manage a collection of books.
# Include methods to add a book, remove a book, and display the available books.

# solution
# class Books_librery:
#     def __init__(self):
#         self.librery = []

#     def add_book(self, book):
#         if book in self.librery:
#             print(f"The {book} book is already axist!!")
#         else:
#             self.librery.append(book)
#             print(f"Book has added!")

#     def remove_book(self, book):
#         if not book in self.librery:
#             print(f"No book axist calls {book}!!")
#         else:
#             self.librery.remove(book)
#             print(f"Book has removed!")
    
#     def display_book(self):
#         if len(self.librery) == 0:
#             print("There is no book in this librery!!")
#         else:
#             print(f"Books are {self.librery}")

# new_books_librery = Books_librery()
# new_books_librery.add_book("DSA Basic")
# new_books_librery.add_book("DSA Mestary")
# new_books_librery.remove_book("DSA Basic")
# new_books_librery.display_book()

# Completed

# ---------------------------------------------------<<7>>------------------------------------------------

# Employee Class:

# Design an Employee class with attributes for name, position, and salary.
# Implement a method to give a salary raise.

# Solution
# class Employee:
#     def __init__(self, name, position, selary):
#         self.name = name
#         self.position = position
#         self.selary = selary
    
#     def rise_selary(self, ammount):
#         if self.selary > ammount:
#             self.selary = ammount
#             print(f"Hello MR {self.position} {self.name}! Bad news 😢. Your selary has downed to {self.selary}")
#         else:
#             self.selary = ammount
#             print(f"Hello MR {self.position} {self.name}! Greate news 💕. You selary has rised to {self.selary}")

# new_employee = Employee("MD Naiem Hosen", "Software Engineer", 20000)
# new_employee.rise_selary(300)

# Completed

# ---------------------------------------------------<<8>>------------------------------------------------

# Product Inventory Class:

# Build a Product Inventory class to keep track of products in stock.
# Include methods for adding products, removing products, and displaying the current inventory.

# ---------------------------------------------------<<9>>------------------------------------------------

# Shape Hierarchy:

# Create a hierarchy of shape classes (e.g., Circle, Square, Triangle) with a common base class (Shape).
# Include methods to calculate area and perimeter for each shape.

# ---------------------------------------------------<<10>>------------------------------------------------
  
# Vehicle Class:

# Develop a Vehicle class with attributes for make, model, and year.
# Add a method to check if the vehicle is a classic (e.g., more than 25 years old).