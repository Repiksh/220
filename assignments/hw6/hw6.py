"""
Name: Scott Repik- Repiksh
hw6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def cash_converter():
    int_entry = eval(input("Enter an int"))
    text = "The Dollar Amount is {dollar:.2f}"
    print(text.format(dollar=int_entry))


def encode():
    text = input("Enter Text")
    key = eval(input("Enter Key Number"))
    text_encode = []
    for i in range(len(text)):
        new_text = ord(text[i]) + key
        text_encode.append(chr(new_text))

    print("".join(text_encode))


def sphere_area(radius):
    equation = 4 * math.pi * (radius ** 2)
    return equation


def sphere_volume(radius):
    equation = (4 / 3) * math.pi * (radius ** 3)
    return equation


def sum_n(number):
    total = 0
    for i in range(1, number + 1):
        total = i + total
    return total


def sum_n_cubes(number):
    total = 0
    for i in range(1, number + 1):
        total = (i ** 3) + total
    return total


def encode_better():
    encode_text = input("Enter Text")
    key = input("Enter Key")
    encode_text_upper = encode_text.upper()
    key_upper = key.upper()

    enc_text_list = []
    for i in range(len(encode_text)):
        new_text = (ord(encode_text_upper[i]) + ord(key_upper[i % len(key_upper)])) % 26
        new_text = new_text + ord("A")
        enc_text_list.append(chr(new_text))
    print("".join(enc_text_list))


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
