"""
Scott Repik -Repiksh
lab11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import *


def three_door_game():
    width = 600
    height = 400
    won_point = 0
    loss_point = 0
    win = GraphWin("Three Door", width, height)

    door_2_rect = Rectangle(Point(width/2 - 40, height / 3.5), Point(width/2 + 40, height - 10))
    door_2 = Door(door_2_rect, "Door 2")
    door_1_rect = Rectangle(Point(width/4 - 40, height / 3.5), Point(width/4 + 40, height - 10))
    door_1 = Door(door_1_rect, "Door 1")
    door_3_rect = Rectangle(Point(width * .75 - 40, height / 3.5), Point(width * .75 + 40, height - 10))
    door_3 = Door(door_3_rect, "Door 3")

    door_1.draw(win)
    door_1.color_door("brown")
    door_2.draw(win)
    door_2.color_door("brown")
    door_3.draw(win)
    door_3.color_door("brown")

    point_win_rect = Rectangle(Point(0, 0), Point(30, 20))
    point_win = Button(point_win_rect, won_point)
    point_win.draw(win)
    point_loss_rect = Rectangle(Point(30, 0), Point(60, 20))
    point_loss = Button(point_loss_rect, loss_point)
    point_loss.draw(win)

    loss_point_text = Text(Point(50, 30), "Loss")
    won_point_text = Text(Point(15, 30), "Won")
    loss_point_text.draw(win)
    won_point_text.draw(win)
    start_text = Text(Point(width / 2, height / 6), "Click on the door you think is the secret")
    start_text.draw(win)

    exit_rect = Rectangle(Point(width - 50, 0), Point(width - 1, 40))
    exit_button = Button(exit_rect, "Exit")
    exit_button.draw(win)

    secret_door = randint(1, 3)
    print(secret_door)
    user_click = win.getMouse()
    loss_text = "That is not the secret! Click to Try Again"
    won_text = "That is the secret! Click to Try Again"
    won_drawn = Text(Point(width / 2, height / 4), won_text)
    loss_drawn = Text(Point(width / 2, height / 4), loss_text)
    while not exit_button.is_clicked(user_click):
        if secret_door == 1:
            door_1.set_secret(True)
        elif secret_door == 2:
            door_2.set_secret(True)
        else:
            door_3.set_secret(True)
        if door_1.is_clicked(user_click):
            if door_1.is_secret():
                door_1.color_door("green")
                won_point += 1
                won_drawn.draw(win)
            elif not door_1.is_secret():
                door_1.color_door("red")
                loss_point += 1
                loss_drawn.draw(win)
        elif door_2.is_clicked(user_click):
            if door_2.is_secret():
                door_2.color_door("green")
                won_point += 1
                won_drawn.draw(win)
            elif not door_2.is_secret():
                door_2.color_door("red")
                loss_point += 1
                loss_drawn.draw(win)
        elif door_3.is_clicked(user_click):
            if door_3.is_secret():
                door_3.color_door("green")
                won_point += 1
                won_drawn.draw(win)
            elif not door_3.is_secret():
                door_3.color_door("red")
                loss_point += 1
                loss_drawn.draw(win)
        if door_1.is_secret():
            door_1.color_door("green")
        if door_2.is_secret():
            door_2.color_door("green")
        if door_3.is_secret():
            door_3.color_door("green")
        point_win.set_label(won_point)
        point_loss.set_label(loss_point)
        win.getMouse()
        loss_drawn.undraw()
        won_drawn.undraw()
        secret_door = randint(1, 3)
        door_1.color_door("brown")
        door_2.color_door("brown")
        door_3.color_door("brown")
        door_1.set_secret(False)
        door_2.set_secret(False)
        door_3.set_secret(False)
        user_click = win.getMouse()

    win.close()
