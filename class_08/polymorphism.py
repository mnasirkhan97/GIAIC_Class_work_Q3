print("######################## Polymorphism #########################################")

# ===> Parent - Super - Base Class
class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def get_info(self):
        return f"Name: {self.name}"
       

# ===> Child - Sub - Derived Class
class Member(Person):
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id
    def get_info(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Member ID": self.member_id
        }
    

# ==> Instance / Object for member
member_instance = Member('Nasir', 'nasir@gmail', 1234)
print("Member Name :", member_instance.name)
print("Member email :",member_instance.email)
print("Member member_id :",member_instance.member_id)
print("Member Info :", member_instance.get_info())

# ===> Child - Sub - Derived Class
class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def get_info(self):
        return [
            self.name, 
            self.email
        ]


# ==> Instance Object
librarian_instance = Librarian('Ali', 'ali@gmail.com', 50000)
print("Librarian Name :", librarian_instance.name)
print("Librarian Email :",librarian_instance.email)
print("Librarian salary :",librarian_instance.salary)
print("Function :",librarian_instance.get_info())

