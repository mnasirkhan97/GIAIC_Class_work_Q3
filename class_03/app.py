# ==> Conditions
# weather = input("What is the weather..?").lower()
# print( weather)

# if weather == 'sunny':
#     print("Stay hydraded")

# elif weather == "rainy":
#     print("Bring Umberalla")

# else:
#     print("Normal weather")


# ===> Exercsie: 
    # Calculator 
    # 1. Num 1 , Num 2 , Operator
    # 2. Addition, Division
"""
num_01 = int(input("Enter first value : "))
num_02 = int(input("Enter second value : "))
operator = input("Enter Operator : ")

if operator == "+":
    print(num_01 + num_02)
elif operator == "-":
    print(num_01 / num_02)
elif operator == "-":
    print(num_01 / num_02)
elif operator == "*":
    print(num_01 * num_02)
else:
    print(num_01 // num_02)

"""


# ==> in & not in
# food_items = ['Biryani', 'Nihari', 'Kunnah']
# if "Biryani" in food_items:
#     print("Roza lg rha hai")

food_items = ['Biryani', 'Nihari', 'Kunnah']
# if "Green Tea" not in food_items:
#     print("Shukar hai")

# ==> AND & OR
#  AND
# if ("Biryani" in food_items and "Nihari" in food_items):
#     print("Colestrol")
# else:
#     print("Balance Diet")


# if ("Biryani" in food_items and "Nihari" in food_items and "Chocolate" in food_items):
#     print("Colestrol")
# else:
#     print("Balance Diet")

# OR
# if ("Biryani" in food_items or "Nihari" in food_items or "Chocolate" in food_items):
#     print("Colestrol")
# else:
#     print("Balance Diet")


#  ===> Functions
print("Functions")

# def greet():
#     print("Hello from functions")
# greet()

# user = input("Enter your name ? ")
# user_email = input("Enter your email ? ")
# def greething(name, email):
#     print(f"User name is {name} & user email is {email}")
#     # print("Hello", name)
# greething(user, user_email)

# ==> Email is optional
# user = input("Enter your name ? ")
# def greething(name, email = None):
#     print(f"User name is {name} & user email is {email}")
# greething(user)


#  ==> Default parameters
# def marriage(choice = "Ammi ki choice"):
#     print(choice)

# marriage()

def marriage(choice = "Ammi ki choice"):
    print(choice)
marriage()
marriage("Apni choice")

