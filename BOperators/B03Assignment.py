def print_hi(name):
    print(f'Hi, {name}')


def assignment():
    year = 2021
    print(year)
    year = 2022
    print(year)
    year = year + 1  # Using the existing value to create a new one
    print(year)

    first = 20
    second = first
    first = 35  # Updating 'first'
    print(first, second)  # 'second' remains unchanged

    num = 10
    print(num)
    num += 5
    print(num)
    num -= 5
    print(num)
    num *= 2
    print(num)
    num /= 2
    print(num)
    num **= 2
    print(num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    assignment()
