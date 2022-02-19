"""
Scott Repik -Repiksh
hw5.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter a name: (First Last)")
    name.split(" ")
    first, last = name.split(" ")
    print(last, ",", first)


def company_name():
    name = input("Enter a three part domain:")
    out_name = name.split(".")[1]
    print(out_name)


def initials():
    n = eval(input("How many students?"))
    for i in range(n):
        name = input("What is the name of the student")
        name.split(" ")
        first, last = name.split(" ")
        print(first[0] + last[0])


def names():
    name = input("List the names:")
    name_split = name.split(", ")
    name_list = name_split.split(" ")


    start = ""

    for name in name_list:

        start = start + name[0].upper() + " "
    print(start)


def thirds():
    n = eval(input("Enter number of sentences:"))
    sentence_list = []
    for i in range(n):
        sentence = input("Enter the sentence:")
        sentence_list.append(list(sentence))
    print(sentence_list[0::3])


def word_average():
    sentence = input("Enter a sentence:")
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)


def pig_latin():
    sentence = input("Enter a sentence:").lower()
    words = sentence.split()
    for word in words:
        print(word[1:] + word[0] + "ay", end=" ")
    print()


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
