
def print_integers():
    print(10)  # A positive integer
    print(-3000)  # A negative integer

    num = 123456789  # Assigning an integer to a variable
    print(num)
    num = -16000  # Assigning a new integer
    print(num)


def print_floating():
    print(1.00000000005)  # A positive float
    print(-85.6701)  # A negative float

    flt_pt = 1.23456789
    print(flt_pt)


def print_complex_number():
    print(complex(10, 20))  # Represents the complex number (10 + 20j)
    print(complex(2.5, -18.2))  # Represents the complex number (2.5 - 18.2j)

    complex_1 = complex(0, 2)
    complex_2 = complex(2, 0)
    print(complex_1)
    print(complex_2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_integers()
    print_floating()
    print_complex_number()
