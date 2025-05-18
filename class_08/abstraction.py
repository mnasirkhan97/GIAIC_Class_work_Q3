print("######################################### Abstraction #########################################")

from abc import ABC, abstractmethod 
# ABC => Abstract Base CLass 

class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def calculate_fine(self):
        pass

# ===> Child - Sub - Derived Class
class Member(Person):
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id
    
    def calculate_fine(self, days):
        return days * 2

# ==> Instance / Object for member
member_instance = Member('Nasir', 'nasir@gmail.com', 1234)
print("Member Name :", member_instance.name)
print("Member email :",member_instance.email)
print("Member member_id :",member_instance.member_id)
print("Fine on Member :",member_instance.calculate_fine(10))

# ===> Child - Sub - Derived Class
class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def calculate_fine(self, days):
        return self.salary - days

# ==> Instance Object
librarian_instance = Librarian('Ali', 'ali@gmail.com', 50000)
print("Librarian Name :", librarian_instance.name)
print("Librarian Email :",librarian_instance.email)
print("Librarian salary :",librarian_instance.salary)
print("Fine on Librarian  :",librarian_instance.calculate_fine(5))

