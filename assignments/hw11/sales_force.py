"""
Scott Repik -Repiksh
sales_force.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_person = []

    def add_data(self, file_name):
        text = open(file_name, "r").readlines()
        for i in text:
            self.sales_person.append(i.replace("\n", "").split(","))
        return self.sales_person

    def quota_report(self, quota):
        new_list = []

        return new_list

    def top_seller(self):
        new_list = []





