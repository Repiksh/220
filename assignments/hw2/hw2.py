"""
Name: Scott Repik -Repiksh
hw2.py

Problem: These programs solve different arithmetic problems based on what a use inputs.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper = eval(input("What is the upper limit?"))
    sum_three = sum([i for i in range(upper+1) if i % 3 == 0])
    print("The sum of numbers divisible by three in range is:", sum_three)


def multiplication_table():
    for i in range(1, 11):
        for q in range(1, 11):
            print(i*q, end="\t")
        print()


def triangle_area():
    a = eval(input("Input the side lengths in a:"))
    b = eval(input("Input the side lengths in b:"))
    c = eval(input("Input the side lengths in c:"))
    s = (a+b+c)/2
    area_tri = math.sqrt((s*(s - a))*(s - b)*(s - c))
    print("The area of the triangle is:", area_tri)


def sum_squares():
    lower = eval(input("What are the lower bounds?"))
    upper = eval((input("What are the upper bounds?")))
    sum_int = 0
    for i in range(lower, upper+1):
        sum_int = sum_int + (i * i)
    print(sum_int)


def power():
    num = eval(input("What is the base?"))
    expo = eval(input("What is the exponent?"))
    result = 1
    for _ in range(expo):
        result = result * num
    print(result)

if __name__ == '__main__':
    pass
