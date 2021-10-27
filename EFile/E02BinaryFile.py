def read_binary_file():
    an_image = open('uk.png', mode='rb')  # ①
    print(an_image.mode)  # ②
    # rb

    print(an_image.name)  # ③
    # 'beauregard.jpg'

    print(an_image.encoding)  # ④
    # Traceback (most recent call last):
    #   File "__ed_file.py", line 8, in <module>
    # print (an_image.encoding) #\u2463
    # AttributeError: '_io.BufferedReader' object has no attribute 'encoding'


def read_bytes():
    # continued from the previous example
    an_image = open('uk.png', mode='rb')
    print(an_image.tell())
    # 0

    data = an_image.read(3)  # ①
    print(data)
    # b'\xff\xd8\xff'

    print(type(data))  # ②
    # <class 'bytes'>

    print(an_image.tell())  # ③
    # 3

    print(an_image.seek(0))
    # 0

    data = an_image.read()
    print(len(data))
    # 3150


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_binary_file()
    read_bytes()
