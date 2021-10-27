triple = lambda num: num * 3  # Assigning the lambda to a variable
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
my_func = lambda num: "High" if num > 50 else "Low" # if-else pair is necessary
# my_func = lambda num


if __name__ == '__main__':
    print(triple(10))  # Calling the lambda and giving it a parameter
    print(concat_strings("World", "Wide", "Web"))
    print(my_func(60))