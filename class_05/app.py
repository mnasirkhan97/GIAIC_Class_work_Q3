print("Class ====> 05")

# datatypes
name:str = "Nasir"
phone: int = 5464986533
age:float = 25.5
color: list = ['red', 'blue']
color_2 :list[str] = ['red', 'blue', 65]
# python dynamic typed (pip install mypy)
# print(color_2)

# ==> SET syntsx
# fruits_names = {"apple", "banana", "cherry", "orange"}
# fruits_names = {"apple", "banana", "cherry", "orange", 99}
fruits_names: set = {"apple", "banana", "cherry", "orange", 99.9}
# fruits_names: str = {"apple", "banana", "cherry", "orange", 99.9}
# print(fruits_names) 
# print(fruits_names[0]) # TypeError: 'set' object is not subscriptable


# ===> UNION
electronic_cus : set = {'ali', 'ahmad', 'hamza'}
garments_cus : set = {'sami', 'nabeel', 'ahmad'}
marge = electronic_cus.union(garments_cus)
# print("Union Example => ", marge)

# ===> Example of Union
laugh_react : set = {'haider', 'Amir', "Babar"}
heart_react : set = {'Rizwan', 'Junaid', "Babar"}
# comp = laugh_react.union(heart_react)
comp = laugh_react | heart_react # pipe operator
# print(comp)

# ==> Intercetion
electronic_cust = {'ali', 'ahmad', 'hamza'}
garments_cust = {'sami', 'nabeel', 'ahmad'}
unique = electronic_cust.intersection(garments_cust)
# print("Example of intercection => ", unique)    

# ==> Example 
summer_fruits = {"apple", "banana", "mango"}
winter_fruits = {"banana", "kiwi", "orange"}
common = summer_fruits.intersection(winter_fruits)
# print("Example of intercection => ", common)

# exercise
ali_frnds: set = {"ahmad", "hussain", "khalid"}
haseeb_frnds: set = {"Umar", "khalid", "Shahid"}
# mutual_frnds = ali_frnds.intersection(haseeb_frnds)
mutual_frnds = ali_frnds & haseeb_frnds
# print(mutual_frnds)


# ===> Class exercise: create a SET named fruits contining "apple", "banana", "cherry". Add "Orange" to the fruits set, removed "banana" from the set, check if "apple" is in the set, clear all items from the set.

# fruits: set = {"apple", "banana", "cherry"}
# print("step 01 => ", fruits)
# fruits.add("orange")
# print("step 02 => add orange ", fruits)
# fruits.remove("banana")
# print("step 03 => remove banana ", fruits)
# fruits.remove("cherry")
# print("step 04 => remove cherry ",fruits)
# fruits.remove("apple")
# print("step 05 => remove apple ",fruits)
# fruits.remove("orange")
# print("step 06 => remove orange ",fruits)


# ====> ERROR Handling
# try:
#     a = {"Apple"}
#     a.add("Banana")
#     # a.append("Banana")
#     print(a)
# except: 
#     print("Error aa giya")
# else:
#     print("Error nh aya")
# finally:
#     print("Ye toh hoga")


# ==> Exmple 
# try:
#     req = request.get("https://jsonplaceholder.typicode.com")
#     print(req.json())
# except Exception as e: 
#     print(e)
#     print("Error aa giya")
# else:
#     print("Error nh aya")
    


# ====> Loop
# for loop
cart = [
    {"product": "Shoes", "Price": 2000},
    {"product": "Tshirt", "Price": 2000},
    {"product": "Hat", "Price": 500},
    {"product": "Socks", "Price": 100}
]

# for items in cart:
#     print("items => ", items)


# total = 0
# for items in cart:
#     total += items["Price"]
# print("total => ", total)


# while loop
total = 0
while True:
    item = input("Please Enter price: ")
    if item == "done":
        break
    if item.isnumeric():
        total += int(item)
print("total bill => ", total)