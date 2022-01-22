"""
Name: Scott Repik
hw1.py

Problem: There are a number of conversion problems, such as converting kilometers to miles, that need to have
user input in order for the function to execute arithmetic and produce the correct result, depending on what is
inputted

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area =", area)


def calc_volume():
    height = eval(input("Enter the height:"))
    width = eval(input("Enter the width:"))
    length = eval(input("Enter the length:"))
    volume = length*width*height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter the total shots:"))
    made = eval(input("Enter how many shots were made:"))
    percent = made/total * 100
    print(percent, "%")


def coffee():
    pound = 10.5
    shipping = .86
    amount = eval(input("How many pounds of coffee would you like?"))
    price = (amount*pound)+1.5+(amount*shipping)
    print("Your total is:", price)


def kilometers_to_miles():
    kilometer = .62
    distance = eval(input("How many kilometers did you travel?"))
    miles = round(distance*kilometer, 2)
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
