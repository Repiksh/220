"""
Name: Scott Repik - Repiksh
hw3.py

Problem: Create Functions that Use loops to solve problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    tot_grade = 0
    avg_grade = 0
    num_grade = eval(input("How many grades will be entered?"))
    for _ in range(num_grade):
        grade = eval(input("Enter Grade:"))
        tot_grade = tot_grade + grade
        avg_grade = tot_grade / num_grade
    print("The Average Grade Is:", avg_grade)


def tip_jar():
    tot_tip = 0
    for _ in range(5):
        tip = eval(input("How much would you like to tip?"))
        tot_tip = tot_tip + tip
    print("The total tips = $", tot_tip)


def newton():
    numb = eval(input("What Number Do You Want To Square Root?"))
    approx = eval(input("How many times should the approximation be improved?"))
    approx_root = numb
    for _ in range(approx):
        approx_root = .5 * (approx_root + numb/approx_root)
    print(approx_root)


def sequence():
    list1 = []
    list_terms = eval(input("How many terms in the list?"))
    for _ in range(list_terms):
        pass


def pi():
    terms = eval(input("How many terms in the series?"))
    p = 1
    m = 2
    for _ in range(terms):
        pt = m/(m-1)
        nt = m/(m+1)
        p = p * pt * nt
        m = m + 2
    print(p * 2.5)


if __name__ == '__main__':
    pass
