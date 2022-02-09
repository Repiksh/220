"""
Scott Repik - Repiksh
lab4.py
This lab draws a heart along with text in a window. The text also notifies the user how to close the window.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *
import time


def greeting_card():
    height = 400
    width = 400
    c_radius = height / 10
    c_width = width / 2
    c_height = height / 4
    arrow_width = 20
    arrow_height = height / 1.5
    win = GraphWin("The Heart", height, width)
    circle_1 = Circle(Point(c_width - c_radius / 2, c_height), c_radius)
    circle_2 = Circle(Point(c_width + c_radius / 2, c_height), c_radius)
    circle_1.setFill("red")
    circle_2.setFill("red")
    circle_1.setOutline("red")
    circle_2.setOutline("red")
    circle_1.draw(win)
    circle_2.draw(win)
    triangle_mid = Point(c_width, c_height + (c_radius + (c_radius * 1.5)))
    triangle_left = Point(c_width - (c_radius * 1.3), c_height + c_radius / 2)
    triangle_right = Point(c_width + (c_radius * 1.3), c_height + c_radius / 2)
    triangle_full = Polygon(triangle_left, triangle_mid, triangle_right)
    triangle_full.setOutline("red")
    triangle_full.setFill("red")
    triangle_full.draw(win)
    arrow_left = Point(arrow_width - 20, arrow_height + 50)
    arrow_right = Point(arrow_width + 30, arrow_height)
    arrow_full = Line(arrow_left, arrow_right)
    arrow_full.setArrow("last")
    arrow_full.draw(win)
    for _ in range(16):
        arrow_full.move(10, -10)
        time.sleep(.1)
    message_start = Text(Point((width / 2), (height - (height / 4))), "Happy Valentine’s Day!")
    message_start.draw(win)
    message_close = Text(Point((width / 2), (height - (height / 5))), "Click Anywhere to Close")
    message_close.draw(win)
    win.getMouse()
    win.close()


greeting_card()
