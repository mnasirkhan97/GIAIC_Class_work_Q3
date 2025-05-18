print("######################## Encapsulation #########################################")


class Library():
    def __init__(self, name, location):
        self.lib_name = name
        self.lib_location = location
        # Private 
        self.__expences = {
            "salary" : 10000,
            "bill": 5000
        }

    #  Getter Method
    def get_expenses(self):
        return self.__expences
    
    # Setter Method 01
    def update_expenses(self):
        self.__expences = {
            "salary" : 20000,
            "bill": 10000,
            "furniture": 5000
        }
        return self.__expences
    
    # # Setter Method 02
    # def update_expenses(self, update_exp):
    #     self.__expences = update_exp
    #     return self.__expences

# Making an Object
Obj_library = Library("The Library", "Karachi")
print("library Name =>", Obj_library.lib_name)
print("library Location =>", Obj_library.lib_location)
print("library Expences =>", Obj_library.get_expenses())
print("library Updated Expences =>", Obj_library.update_expenses())
# print("library Updated Expences =>", Obj_library.update_expenses(update_exp={}))
 


    
        
