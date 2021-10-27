# String: search, replace, changing the Letter case
# type conversions: int(), ord(), float(), str(), bool()

def method_of_string():
    # search
    random_string = "This is a string"
    print(random_string.find("is"))  # First instance of 'is' occurs at index 2
    print(random_string.find("is", 9, 13))  # No instance of 'is' in this range
    # replace
    a_string = "Welcome to Educative!"
    new_string = a_string.replace("Welcome to", "Greetings from")
    print(a_string)
    print(new_string)
    # changing
    print("UpperCase".upper())
    print("LowerCase".lower())


def method_type_conversion():
    # int
    print(int("12") * 10)  # String to integer
    print(int(20.5))  # Float to integer
    print(int(False))  # Bool to integer
    # print (int("Hello")) # This wouldn't work!
    # ord()
    print(ord('a'))
    print(ord('0'))
    # float
    print(float(24))
    print(float('24.5'))
    print(float(True))
    # str
    print(str(12) + '.345')
    print(str(False))
    print(str(12.345) + ' is a string')
    # bool()
    print(bool(10))
    print(bool(0.0))
    print(bool("Hello"))
    print(bool(""))


if __name__ == '__main__':
    method_of_string()
    method_type_conversion()