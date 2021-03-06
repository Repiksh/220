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


def won(secret_word, guessed):
    if secret_word == guessed:
        return True
    else:
        return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    trials = 6
    guess_list = []
    striped = secret_word.strip()
    while not won(striped, make_hidden_secret(striped, guess_list)):
        guess = input(f"Guesses Left {trials}, Enter Next Guess:")
        if not already_guessed(guess, guess_list):
            guess_list.append(guess)
            if letter_in_secret_word(guess, striped):
                print(make_hidden_secret(striped, guess_list))
            else:
                print("Letter not in word.")
                trials -= 1
                print(make_hidden_secret(striped, guess_list))
        else:
            print("Already Guessed")
        if trials == 0:
            print("The word was:", striped)
            break
    if trials == 0 and not won(striped, make_hidden_secret(striped, guess_list)):
        print("You lose")
    else:
        print("You Win")


if __name__ == '__main__':
    play_command_line(get_random_word(get_words("words.txt")))
    # play_command_line(secret_word)
    # play_graphics(secret_word)
