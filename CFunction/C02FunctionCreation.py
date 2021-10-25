def my_print_function():  # No parameters
    print("This")
    print("is")
    print("A")
    print("function")
# Function ended


def minimum(first, second):
    if first < second:
        print(first)
    else:
        print(second)


def return_statement(first, second):
    if first < second:
        return first
    return second


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Calling the function in the program multiple times
    my_print_function()
    my_print_function()
    # calling a function with two parameters
    num1 = 10
    num2 = 20
    minimum(num1, num2)
    # calling a function with two parameter
    result = return_statement(num1, num2)  # Storing the value returned by the function
    print(result)
