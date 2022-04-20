"""
Scott Repik -Repiksh
lab13.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(file_name):
    text = open(file_name, "r").readline()
    trades_split = text.split(" ")
    int_list = [int(i) for i in trades_split]
    for trades in range(len(int_list)):
        if int_list[trades] > 830:
            print("Warning at", trades + 1, "sec")
        elif int_list[trades] == 500:
            print("Alert at", trades + 1, "sec")
