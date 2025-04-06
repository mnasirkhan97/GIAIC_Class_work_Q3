print("Class ====> 04")

# ==> Functions
# Positional Argumengts
def Login(email, password):
    user_obj = {
        "email": email,
        "password": password
    }
    print('Noraml functiom', user_obj)
Login("nasir@gmail.com", "nasir123")

# keyword Argumengts
def Login_keyword_arguments(*, email, password, dob):
    user_obj = {
        "email": email,
        "password": password,
        "dob": dob
    }
    print("Functions with keyword Argumengts", user_obj)
Login_keyword_arguments(email="nasir@gmail.com", password="nasir123", dob="20-Sep")
# change position of values
Login_keyword_arguments(email="nasir@gmail.com", dob="20-Sep", password="nasir123")

#==> Double Asteriskes(*) f0r unlimited parameters
def Binance(**kwargs):
    print(kwargs)

Binance(bitcoin=1234, eth=99)

# ==> Exercise
print("Class Exercise")
def wallet(**kuch_bhi):
    print(kuch_bhi)
wallet(USD=100, PKR = 5000, EURO = 50)

# ===> for mcqs visist panaversity github > advance python > colab
# ==> for datatype checking use Just in type (mypy)
# pip install mypy
# pip install pytest
# string casting