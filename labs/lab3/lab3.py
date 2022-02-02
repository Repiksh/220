"""Scott Repik - Repiksh
lab3.py
A user inputs data relating to traffic, in which this code uses the data to
determine the average number of cars on any given road as well as total number of cars
on all roads

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    tot_num_roads = eval(input("How many roads were surveyed"))
    tot_car_all = 0
    avg_car_all = 0

    for i in range(tot_num_roads):
        tot_car_day = 0
        avg_car_day = 0
        print("How many days was road", i+1, "surveyed")
        days = eval(input())
        for q in range(days):
            print("How many cars traveled on day", q+1, "?")
            day_car = eval(input())
            tot_car_all = tot_car_all+day_car
            tot_car_day = tot_car_day + day_car
            avg_car_day = round(tot_car_day / days, 2)
        print("The average cars on road", i+1, "is:", avg_car_day)
        print("the total cars on road", i+1, "is", tot_car_day)
    avg_car_all = round(tot_car_all / tot_num_roads, 2)
    print("The total number of cars is:", tot_car_all)
    print("The average number of cars per road is:", avg_car_all)
