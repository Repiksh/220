"""
Scott Repik -Repiksh
lab10.py

A

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.secret = False
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        rect_1 = self.shape.getP1()
        rect_2 = self.shape.getP2()
        rect_1_x = rect_1.getX()
        rect_1_y = rect_1.getY()
        rect_2_x = rect_2.getX()
        rect_2_y = rect_2.getY()
        if rect_2_x >= point.getX() >= rect_1_x and rect_2_y >= point.getY() >= rect_1_y:
            return True
        else:
            return False

    def open(self, label):
        self.shape.setFill(label)

    def close(self, label):
        self.shape.setFill(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        elif not self.secret:
            return False

    def set_secret(self, secret):
        self.secret = secret
