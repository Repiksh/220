"""
Scott Repik
sales_person.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sales(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(0, len(self.sales)):
            total += self.sales[i]

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() == quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.total_sales() == other:
            return 0
        elif self.total_sales() < other:
            return -1
        elif self.total_sales() > other:
            return 1

    def __str__(self):
        return self.employee_id + "-" + self.name + ":" + self.sales
