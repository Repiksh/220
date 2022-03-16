"""
Scott Repik - Repiksh
lab8.py

Creating a game using multiple functions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *


def get_random(move_amount):
    right = move_amount
    left = move_amount * -1
    return randint(left, right)


def did_collide(ball, ball_2):
    ball_1_center = ball.getCenter()
    ball_2_center = ball_2.getCenter()
    ball_1_radius = ball.getRadius()
    ball_2_radius = ball_2.getRadius()
    rad_diff = ball_2_radius + ball_1_radius
    ball_1_x = ball_1_center.getX()
    ball_1_y = ball_1_center.getY()
    ball_2_x = ball_2_center.getX()
    ball_2_y = ball_2_center.getY()
    distance = (((ball_2_x - ball_1_x) ** 2) + ((ball_2_y - ball_1_y) ** 2)) ** (1/2)
    if distance - rad_diff > rad_diff:
        return True
    else:
        return False


def hit_vertical(ball, win):
    ball_center = ball.getCenter()
    ball_y = ball_center.getY()
    ball_rad = ball.getRadius()
    win_max = win.getHeight()
    win_min = 0
    if (ball_y > win_max - ball_rad) or (ball_y < win_min + ball_rad):
        return True
    else:
        return False


def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    ball_x = ball_center.getX()
    ball_rad = ball.getRadius()
    win_max = win.getWidth()
    win_min = 0
    if (ball_x > win_max - ball_rad) or (ball_x < win_min + ball_rad):
        return True
    else:
        return False


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return color_rgb(r, g, b)


def bumper():
    height = 400
    width = 400
    circle_win = GraphWin("Circles", height, width)
    radius = 40
    ball_1 = Circle(Point(randint(radius, width - radius), randint(radius, height - radius)), radius)
    ball_1.setFill(get_random_color())
    ball_1.draw(circle_win)
    ball_2 = Circle(Point(randint(radius, width - radius), randint(radius, height - radius)), radius)
    ball_2.setFill(get_random_color())
    ball_2.draw(circle_win)
    did_collide(ball_1, ball_2)

    circle_win.getMouse()
    circle_win.close()
