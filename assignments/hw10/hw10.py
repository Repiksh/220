"""
Scott Repik -Repiksh
hw10.py

I certify that this assignment is entirely my own work.
"""
from face import *



def fibonacci(n):
    fib_list = [1, 1]
    if n <= 0:
        return None
    elif n <= len(fib_list):
        return fib_list[n-1]
    else:
        new_list = fibonacci(n - 1) + fibonacci(n - 2)
        fib_list.append(new_list)
        return new_list


def double_investment(principle, rate):
    one_year = 0
    count = 0
    while one_year <= principle * 2:
        one_year = one_year + (principle * (1 + rate))
        count += 1
    return count


def syracuse(n):
    list_syr = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            list_syr.append(int(n))
        else:
            n = 3 * n + 1
            list_syr.append(n)
    return list_syr


def goldbach(n):
    pass
