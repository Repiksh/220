"""
Scott Repik -Repiksh
lab2.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def means():
    num_val = eval(input("Enter the number of values:"))
    acc_val_root = 0
    acc_val_har = 0
    acc_val_geo = 1
    for i in range(num_val):
        value = eval(input("Enter value:"))
        # print(acc_val_root)
        acc_val_root = acc_val_root + (value ** 2)
        # print(acc_val_root)
        acc_val_har = acc_val_har + (1/value)
        acc_val_geo = acc_val_geo * value

    root_mean = round(math.sqrt(acc_val_root / num_val), 3)
    print("The root mean is:", root_mean)
    har_mean = round(num_val / acc_val_har, 3)
    print("The Harmonic Mean is:", har_mean)
    geo_mean = round(acc_val_geo ** (1/num_val), 3)
    print("The Geometric Mean is:", geo_mean)
