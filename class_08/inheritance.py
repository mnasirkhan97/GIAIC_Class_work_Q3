print("######################## Inheritance #########################################")

# ===> Parent - Super - Base Class
class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.age = age

# ===> Child - Sub - Derived Class
class Librarian(Person):
    def __init__(self, name, email, salary):
        # ==> Super keyword
        super().__init__(name, email)
        self.salary = salary

# ==> Instance Object
librarian_instance = Librarian('Ali', 'ali@gmail.com.com', 50000)
print("Librarian Name :", librarian_instance.name)
print("Librarian Email :",librarian_instance.email)
print("Librarian salary :",librarian_instance.salary)

class Member(Person):
    def __init__(self, name, email, member_id):
    # def __init__(self, name):
        super().__init__(name, email)
        self.member_id = member_id
        # super().__init__(name)

# ==> Instance / Object for member
member_instance = Member('Nasir', 'nasir@gmail', 1234)
# member_instance = Member('Ali')
print("Member Name :", member_instance.name)
print("Member email :",member_instance.email)
print("Member member_id :",member_instance.member_id)