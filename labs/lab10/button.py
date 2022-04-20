"""
Scott Repik -Repiksh
lab10.py


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

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

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def color_button(self, color):
        self.shape.setFill(color)
