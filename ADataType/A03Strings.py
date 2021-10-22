
def print_strings():
    print("Harry Potter!")  # Double quotation marks

    got = 'Game of Thrones...'  # Single quotation marks
    print(got)
    print("$")  # Single character

    empty = ""
    print(empty)  # Just prints an empty line


def length_of_a_string():
    random_string = "I am Batman"  # 11 characters
    print(len(random_string))


def accessing_character():
    batman = "Bruce Wayne"

    first = batman[0]  # Accessing the first character
    print(first)

    space = batman[5]  # Accessing the empty space in the string
    print(space)

    last = batman[len(batman) - 1]
    print(last)
    # The following will produce an error since the index is out of bounds
    # err = batman[len(batman)]


def reverse_indexing():
    batman = "Bruce Wayne"
    print(batman[-1])  # Corresponds to batman[10]
    print(batman[-5])  # Corresponds to batman[6]


def string_slicing():
    # string slicing
    my_string = "This is MY string!"
    print(my_string[0:4])  # From the start till before the 4th index
    print(my_string[1:7])
    print(my_string[8:len(my_string)])  # From the 8th index till the end
    # slicing with a step
    my_string = "This is MY string!"
    print(my_string[0:7])  # A step of 1
    print(my_string[0:7:2])  # A step of 2
    print(my_string[0:7:5])  # A step of 5
    # reverse slicing
    my_string = "This is MY string!"
    print(my_string[13:2:-1])  # Take 1 step back each time
    print(my_string[17:0:-2])  # Take 2 steps back. The opposite of what happens in the slide above
    # partial slicing
    my_string = "This is MY string!"
    print(my_string[:8])  # All the characters before 'M'
    print(my_string[8:])  # All the characters starting from 'M'
    print(my_string[:])  # The whole string
    print(my_string[::-1])  # The whole string in reverse (step is -1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_strings()
    reverse_indexing()
