"""
Scott Repik - Repiksh
lab1.py
This code solves the problem of the interest owed after a month. The code uses user inputted data to calculate
the amount of interest owed based on what the user inputs
All code used in this program was coded by Scott Repik, and was not copied from any website or from any other
student.
"""


def monthly_interest():
    annual_rate = eval(input("What is percent annual interest rate of your account?"))
    monthly_rate = annual_rate / 12
    total_days = eval(input("How many days were in this month?"))
    last_month = eval(input("What was the previous net balance this month?"))
    payment_made = eval(input("What was the amount paid on the previous net balance?"))
    payment_date = eval(input("What day was the payment made this month?"))
    days_remaining = total_days - payment_date
    net_day = total_days * last_month
    received_day = days_remaining * payment_made
    sub_bal = net_day - received_day
    avg_bal = sub_bal / total_days
    dec_rate = monthly_rate / 100
    monthly_charge = dec_rate * avg_bal
    print("$", monthly_charge)


monthly_interest()
