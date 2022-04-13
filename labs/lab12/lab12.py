"""
Scott Repik -Repiksh
lab12.py


"""

from random import *


def find_and_remove(values, search_val):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            values.pop(i)
            values.insert(i, "Scott")
        i += 1


def read_data(file_name):
    text = open(file_name, "r")
    list_file = []
    lines = text.readline()

    while lines:
        i = 0
        no_new = lines.strip("\n")
        lines_strip = no_new.split(" ")
        while i < len(lines_strip):
            is_int = int(lines_strip[i])
            i += 1
            list_file.append(is_int)
        lines = text.readline()
    text.close()

    return list_file


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def good_input():
    new_input = eval(input("Enter a number:"))
    while not 10 >= new_input >= 1:
        if new_input < 1:
            new_input = eval(input("Number is too low, enter between 1-10"))
        elif new_input > 10:
            new_input = eval(input("Number is too high, enter between 1-10"))
    return new_input


def num_digits():

    new_input = eval(input("Enter a number:"))
    while new_input > 0:
        num_div = 0
        while new_input > 0:
            new_input //= 10
            num_div += 1

        new_input = eval(input("Enter a number"))


def hi_lo_game():
    num_guess = 7
    secret = randint(1, 100)
    while num_guess > 0:
        guess = eval(input("Enter a guess:"))
        if guess == secret:
            print("Correct! You took {} guess(es).".format(8 - num_guess))
            num_guess = 0
        elif guess > secret:
            print("That is too high!")
            num_guess -= 1
        elif guess < secret:
            print("That is too low!")
            num_guess -= 1
    print("The number was: {}".format(secret))




def main():
    pass

