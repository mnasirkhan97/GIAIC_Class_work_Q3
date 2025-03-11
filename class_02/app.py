# ====> TUPLES
gisic_rules = ("Assignments", "Attendence")
# print(gisic_rules)
# print(type(gisic_rules))

# print(gisic_rules[0])  
# => output : Assignments
# print(gisic_rules[1]) 
 # => output : Attendence


# ==> Exercise: Make a tuple and store your ID card info (3 values)

giaic_info = (269865, "Muhammad Nasir Khan", "Quarter_03", "sunday_evening", "Governor House Karachi", "Sir Ali jawad")
# print(giaic_info[0])
# print(giaic_info[1])
# print(giaic_info[2])
# print(giaic_info[3])
# print(giaic_info[4])
# print(giaic_info[5])

# print(f"My Name is {giaic_info[1]}")

# ==> can we add another value in exiting tuple
# giaic_info[6] = "email@test.com"  
# ==> No (TypeError: 'tuple' object does not support item assignment)

# ==> Methods in Tuples (1. count 2. index)
# print(giaic_info.count("Quarter_03")) 
# ==>  count ye btaye ga k ye value ktni bar ai hai is tuple me yani count btaye ga
# print(giaic_info.index("Quarter_03")) 
# ==> index ye btaye ga k ye value kis index pe mojood hai


# ====> LISTS
fruits = ["apple", "orange", "mango", 123, True]
# print(fruits)
# print(fruits[2])

# fruits[3] = "banana" 
# print(fruits)

# fruits[5] = 345 
# print(fruits)
# ==> Error : IndexError: list assignment index out of range


# ===>  Dictionary || Objects

order_food = {
    "order_id": 123,
    "items": ['Biryani', 'Raita'],
    "status": 'pending'
}

# print(order_food)
# print(order_food.items) 
# ==> Error
# print(order_food["order_id"])
# ==> Working

# print(order_food["items"])
# print(order_food["items"][0])
# print(order_food["items"][1])
# print(type(order_food["items"]))

# ==> Update status value pending to Delivered
# order_food["status"] = 'Pending'
order_food['status'] = 'Delivered'
# print(order_food) 


# ==> Exercise:  Make an Object name a key (Your name)

my_name = {
    "nasir": {
        "Subject": "Nextjs", 
        "score": 81
        }
}

print(my_name["nasir"]["score"])
