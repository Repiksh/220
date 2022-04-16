"""
Scott Repik -Repiksh
sales_force.py


"""


class SalesForce:
    def __init__(self):
        self.sales_person = []

    def add_data(self, file_name):
        text = open(file_name, "r").readlines()
        for i in text:
            self.sales_person.append(i.replace("\n", "").split(","))

    def quota_report(self, quota):
        new_list = []





