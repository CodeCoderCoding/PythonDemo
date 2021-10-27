def read_file():
    a_file = open('./chinese.txt', encoding='utf-8')
    a_string = a_file.read()  # ①
    # 'Dive Into Python 是为有经验的程序员编写的一本 Python 书。\n'

    print(a_string)  # ②
    # ''

    with open('chinese.txt', encoding='utf-8') as a1_file:
        a1_file.seek(17)
        a1_character = a1_file.read(1)
        print(a1_character)


def read_data_one_line_at_a_time():
    line_number = 0
    with open('favorite-people.txt', encoding='utf-8') as a_file:  # ①
        for a_line in a_file:  # ②
            line_number += 1
            print('{:>4} {}'.format(line_number, a_line.rstrip()))


def write_to_file():
    with open('test.log', mode='w', encoding='utf-8') as a_file:  # ①
        a_file.write('test succeeded')  # ②

    with open('test.log', encoding='utf-8') as a_file:
        print(a_file.read())
        # test succeeded

    with open('test.log', mode='a', encoding='utf-8') as a_file:  # ③
        a_file.write('and again')

    with open('test.log', encoding='utf-8') as a_file:
        print(a_file.read())
        # test succeeded and again


if __name__ == '__main__':
    read_file()
    read_data_one_line_at_a_time()
    write_to_file()


