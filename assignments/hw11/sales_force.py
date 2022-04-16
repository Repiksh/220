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
        self.sales_p = SalesPerson(self.sales_person[0], self.sales_person[1])

    def add_data(self, file_name):
        text = open(file_name, "r").readlines()
        for i in text:
            self.sales_person.append(i.replace("\n", "").split(","))

    def quota_report(self, quota):
        new_list = []

        for i in self.sales_person:
            new_list.append(self.sales_p.get_id() + self.sales_p.get_name() + self.sales_p.total_sales() + self.sales_p.met_quota(quota))
        return new_list

    def top_seller(self):
        pass





