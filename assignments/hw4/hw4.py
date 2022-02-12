"""
Name: Scott Repik - Repiksh
hw4.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        # clone the last pos of shape and redraw the clone
        clone = shape.clone()
        clone.draw(win)
        shape.move(change_x, change_y)
    new_instructions = Text(Point(width / 2, height - 20), "Click to Exit")
    new_instructions.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    height = 400
    width = 400
    win = GraphWin("Rectangle", width, height)

    for i in range(1):
        rect_point = win.getMouse()
        rect_point_2 = win.getMouse()
        rect = Rectangle(rect_point, rect_point_2)
        point_1_x = rect_point.getX()
        point_1_y = rect_point.getY()
        point_2_x = rect_point_2.getX()
        point_2_y = rect_point_2.getY()
        rect_width = abs(point_1_x - point_2_x)
        rect_height = abs(point_1_y - point_2_y)
        rect_perimeter = 2 * (rect_height + rect_width)
        rect_area = rect_height * rect_width
        text_area = Text(Point(width / 2, height - 20), rect_area)
        text_area_string = Text(Point(width / 4, height - 20), "Area:")
        text_area_string.draw(win)
        text_area.draw(win)
        text_perimeter_string = Text(Point(width / 4, height - 35), "Perimeter:")
        text_perimeter_string.draw(win)
        text_perimeter = Text(Point(width / 2, height - 35), rect_perimeter)
        text_perimeter.draw(win)
        rect.setFill("green")
        rect.setOutline("green")
        rect.draw(win)
    instructions = Text(Point(width / 2, height / 2), "Click to Close")
    instructions.draw(win)
    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)
    for _ in range(1):
        center_point = win.getMouse()
        radius_point = win.getMouse()
        c_x = center_point.getX()
        c_y = center_point.getY()
        r_x = radius_point.getX()
        r_y = radius_point.getY()
        real_radius = ((r_x - c_x) ** 2 + (r_y - c_y) ** 2) ** (1 / 2)

        the_circle = Circle(center_point, real_radius)
        the_circle.setFill("blue")
        the_circle.draw(win)
        radius_text = Text(Point(width / 2, height - 20), real_radius)
        radius_text_2 = Text(Point(width / 2, height - 40), "Radius")
        radius_text.draw(win)
        radius_text_2.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("How many terms?"))
    total = 0
    for i in range(n):
        total = total + (4 * (-1) ** i) / (2 * i + 1)
        # Because the sign alternates between "+" and "-" the -1 ** i is needed
    print(total)
    error = abs(math.pi - total)
    print(error)


if __name__ == '__main__':
    pass
