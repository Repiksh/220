"""
Scott Repik -Repiksh
lab10.py

A

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
from button import *
from door import *


def main():
    height = 400
    width = 300
    button_window = GraphWin("Buttons", width, height)
    exit_rectangle = Rectangle(Point(width / 4, height / 10), Point(width - width/4, height / 4))
    door_rect = Rectangle(Point(width / 4, height / 3.5), Point(width - width/4, height - 10))
    xit = Button(exit_rectangle, "Exit")
    door = Door(door_rect, "Open")
    xit.draw(button_window)
    xit.color_button("white")
    door.draw(button_window)
    door.color_door("red")
    user_click = button_window.getMouse()
    while not xit.is_clicked(user_click):
        if door.is_clicked(user_click):
            if door.get_label() == "Open":
                door.set_label("Close")
                door.color_door("yellow")
            elif door.get_label() == "Close":
                door.set_label("Open")
                door.color_door("red")
        user_click = button_window.getMouse()
    button_window.close()
