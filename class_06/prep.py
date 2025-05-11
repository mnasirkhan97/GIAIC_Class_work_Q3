# my_tupe = ("apple", "banana", "cherry")
# print(my_tupe[0])
# my_tupe[1] = 'orange'
# print(my_tupe)


my_list = [10, 20, 30, 40, 50, 60, 70]
sliced_list = my_list[2:5]

# print(sliced_list)



# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing a value using the key
# value = my_dict["age"]

# Printing the value
# print(value)


# Accessing a value using the key
my_dict["age"] = 40
# print(my_dict)



numbers = [1, 2, 3, 4, 5]

# Using for loop to print each number
# for number in numbers:
    # print(number)




# Dictionary of students and their scores
scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}

# Using for loop to print each student's name and score
# for student, score in scores.items():
#     print(f"{student} scored {score}")


# def greet(name, age):
    # print(f"Hello {name}, you are {age} years old.")

# Calling the function with incorrect number of arguments
# greet("Alice")


# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# # Calling the function with keyword arguments
# greet(age=25, name="Alice")


my_string = r'Hello, World!'
# print(my_string)



# print("Hello,\b World!") #\b backspace
# print("Hello,\tWorld!")  #\t tab
# print("Hello, \"World!\"")
# print("Hello,\ World!")


print(r"\u0041 = ", "\u0041")
print(r"\u0042 = ", "\u0042")
print(r"\u0043 = ", "\u0043")


# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)



# Find factors of a number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")
     