num = 20


def multiply_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside function:", num)
    return n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    multiply_by_10()
