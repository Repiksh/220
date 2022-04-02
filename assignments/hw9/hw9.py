"""
Scott Repik -Repiksh
hw9.py

I certify that this assignment is entirely my own work.
"""
from random import *


def get_words(file_name):
    text = open(file_name, "r")
    return text.readlines()


def get_random_word(words):
    x = randint(0, len(words))
    return words[x]


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    new_list = []
    new_string = ""
    for i in secret_word:
        if i.lower() in guesses:
            new_list.append(i)
        else:
            new_list.append("_")
    return new_string.join(new_list)


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    make_hidden_secret(secret_word, ["a", "e", "i", "o", "u"])



if __name__ == '__main__':
    play_command_line(get_random_word(get_words("words.txt")))
    # play_command_line(secret_word)
    # play_graphics(secret_word)
