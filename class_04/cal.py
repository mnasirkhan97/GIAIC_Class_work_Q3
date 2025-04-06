def add(x:int, y:int) -> int:
    return x + y

if __name__ == "__main__":
    # This block will only run if this file is executed directly
    # It won't run if this file is imported as a module in another file
    result = add (2, 6)
    print(result)

# result = add (2, 6)
# print(result)
# print(__name__, "cal.py file")