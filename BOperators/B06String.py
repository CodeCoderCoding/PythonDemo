def comparison():
    print('a' < 'b')  # 'a' has a smaller Unicode value

    house = "Gryffindor"
    house_copy = "Gryffindor"

    print(house == house_copy)

    new_house = "Slytherin"

    print(house == new_house)

    print(new_house <= house)

    print(new_house >= house)


def concatenation():
    first_half = "Bat"
    second_half = "man"

    full_name = first_half + second_half
    print(full_name)
    print("ha" * 3)


def search():
    random_string = "This is a random string"

    print('of' in random_string)  # Check whether 'of' exists in randomString
    print('random' in random_string)  # 'random' exists!


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    comparison()
    concatenation()
    search()
