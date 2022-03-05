"""
Name:Scott Repik -Repiksh
hw7.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def number_words(in_file_name, out_file_name):
    pass


def hourly_wages(in_file_name, out_file_name):
    wages = open(in_file_name, "r")
    out = open(out_file_name, "w")
    wages_list = wages.readlines()
    for i in wages_list:
        wage_split = i.split(" ")
        first = wage_split[0].split()
        last = wage_split[1].split()
        payment = wage_split[2].split()
        payment_list = [float(val) for val in payment]
        print(payment_list)
        hours = wage_split[3].split()
        hours_list = [float(val) for val in hours]
        bonus = [1.65]
        int_wage = [a * b for a, b in zip(hours_list, payment_list)]
        bonus_wage = [c * d for c, d in zip(bonus, hours_list)]
        total = bonus_wage[0] + int_wage[0]
        out.write(repr(first) + repr(last) + "total payment is " + repr(total) + "\n")
    wages.close()
    out.close()


def calc_check_sum(isbn):
    isbn_list = []
    isbn_list.append(isbn)
    for i in isbn_list:
        isbn_replace = i.replace("-", " ")
        isbn_split = isbn_replace.split(" ")
        if len(isbn_split) > 10
            print("The isbn length is greater than 10")
        else



def send_message(file_name, friend_name):
    file = open(file_name, "r")
    file_list = file.readlines()
    name = friend_name
    new_file = open(name + ".txt", "w")
    for i in file_list:
        new_file.write(repr(file_list) + "\n")
    file.close()
    new_file.close()


def encode(text, key):

    text_encode = []
    for i in range(len(text)):
        new_text = ord(text[i]) + key
        text_encode.append(chr(new_text))
    return text_encode


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    file_list = file.readlines()
    new_file = open(friend_name + ".txt", "w")
    text = encode(file_list, key)
    new_file.write(repr(text))


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
