print("############################ Object Oriented Programming Part 2 ################################")

# ==> Pillar of OPP
#  Inheritance
#  Encapsulation
#  Polymorphism
#  Abstraction



# Class ==> Blueprint / Template / Structure

class Library():
    # constructor
    def __init__(self, name, location):
        # Class Attributes / Class Variables / Parameters
        self.lib_name = name
        self.lib_location = location

# Making an Object
Obj_library = Library("The Library", "Karachi")
# print("library =>", Obj_library)
print("library Name =>", Obj_library.lib_name)
print("library Location =>", Obj_library.lib_location)


# 2nd Class
class Book():
    def __init__(cls, name, authar, availabilty):
        cls.book_name = name
        # cls.book_authar = authar
        cls.book_authar = "nasir"
        cls.book_availabilty = availabilty

    def borrow(cls):
        cls.book_availabilty
        # return cls.book_availabilty

# Instance of class
book1 = Book("The Poetry", "Allama Iqbal", "Yes")
book2 = Book("The Comedy", "Umar Shareef", "Yes")
book3 = Book("The Comedy 2", "Sikandar", "Yes")
print(book1.book_name)
print(book1.book_authar)
print(book1.book_availabilty)


# ====> Real World Library example
class Book_Library():
    # constructor
    def __init__(self, name, authar, availabilty):
        self.books = []
        self.lib_name = name
        self.lib_authar = authar
        self.lib_availabilty = availabilty
        # print(self.books)

    # Class method
    def add_book(self, new_book_name):
        return self.books.append(new_book_name)
    
    def get_book(self):
        return self.books
    
    def remove_book(self, remove_book):
        return self.books.remove(remove_book)

# making object / creating instance for class
my_Library = Book_Library("Comedy", "Umar Shareef", True)

print(my_Library.add_book(book1.book_name))
print(my_Library.add_book(book2.book_name))
print(my_Library.add_book(book3.book_name))
print(my_Library.get_book())

print(my_Library.remove_book(book3.book_name))
print(my_Library.get_book())

# print(my_Library)

    
        