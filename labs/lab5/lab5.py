"""
Scott Repik -Repiksh
lab5.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
from math import *


def triangle():
    height = 400
    width = 400
    win = GraphWin("Triangle", width, height)
    for _ in range(1):
        point_1 = win.getMouse()
        point_2 = win.getMouse()
        point_3 = win.getMouse()
        triangle_1 = Polygon(point_1, point_2, point_3)
        triangle_1.draw(win)
        a_x = point_1.getX()
        a_y = point_1.getY()
        b_x = point_2.getX()
        b_y = point_2.getY()
        c_x = point_3.getX()
        c_y = point_3.getY()
        side_a_x = abs(b_x - a_x)
        side_a_y = abs(b_y - a_y)
        side_b_x = abs(c_x - b_x)
        side_b_y = abs(c_y - b_y)
        side_c_x = abs(c_x - a_x)
        side_c_y = abs(c_y - a_y)
        side_a = sqrt((side_a_x ** 2 + side_a_y ** 2))
        side_b = sqrt((side_b_x ** 2 + side_b_y ** 2))
        side_c = sqrt((side_c_x ** 2 + side_c_y ** 2))
        s = (side_a + side_b + side_c) / 2
        area_tri = round(((s * (s - side_a) * (s - side_b) * (s - side_c)) ** (1 / 2)))
        per = round(s * 2)
        per_text = Text(Point(width / 2, height / 1.3), per)
        per_text.draw(win)
        per_text_2 = Text(Point(width / 1.5, height / 1.3), "Perimeter")
        per_text_2.draw(win)
        area_disp = Text(Point(width / 2, height / 1.5), area_tri)
        area_disp.draw(win)
        area_disp_2 = Text(Point(width / 1.5, height / 1.5), "Area")
        area_disp_2.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    # Create code to allow a user to color a shape by entering rgb amounts

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()
    red_entry = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 3)
    red_entry.draw(win)
    win.getMouse()
    red_e = red_entry.getText()
    red = int(red_e)

    green_entry = Entry(Point(win_width / 2 + 10, win_height / 2 + 70), 3)
    green_entry.draw(win)
    win.getMouse()
    green_e = green_entry.getText()
    green = int(green_e)

    blue_entry = Entry(Point(win_width / 2 + 10, win_height / 2 + 100), 3)
    blue_entry.draw(win)
    win.getMouse()
    blue_e = blue_entry.getText()
    blue = int(blue_e)

    shape.setFill(color_rgb(red, green, blue))
    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string_input = input("Input String")
    print(string_input[0])
    print(string_input[-1])
    print(string_input[1:5],)
    print(string_input[0], string_input[-1])
    for _ in range(10):
        print(string_input[0:3])
    for i in range(len(string_input)):
        print(string_input[i])
    print(len(string_input))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 3
    print(x)
    x = values[2:5]
    print(x)
    order = [2, 3, 0]
    x = [values[i] for i in order]
    print(x)
    new_float = eval(values[5])
    order = [2, 0, new_float]
    x = [values[i] for i in order]
    print(x)
    x = values[0] + values[2] + new_float
    print(x)
    print(len(values))


def another_series():
    new_list = [2, 4, 6, 2, 4, 6, 2, 4, 6, 2, 4, 6]
    n = eval(input("How many times?"))
    acc_val = 0
    for i in range(n):
        acc_val = acc_val + new_list[n]
    print(acc_val)


def target():
    width = 400
    height = 400
    c_r = width / 2
    win = GraphWin("Target", width, height)
    r = 40
    circle_1 = Circle(Point(width / 2, height / 2), c_r)
    circle_1.setFill("red")
    circle_1.draw(win)
    circle_2 = Circle(Point(width / 2, height / 2), c_r - r)
    circle_2.setFill("blue")
    circle_2.draw(win)
    circle_3 = Circle(Point(width / 2, height / 2), c_r - (r * 2))
    circle_3.setFill("black")
    circle_3.draw(win)
    circle_4 = Circle(Point(width / 2, height / 2), c_r - (r * 3))
    circle_4.setFill("yellow")
    circle_4.draw(win)
    circle_5 = Circle(Point(width / 2, height / 2), c_r - (r * 4))
    circle_5.setFill("white")
    circle_5.draw(win)
    win.getMouse()
    win.close()
