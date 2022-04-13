"""
Scott Repik -Repiksh
hw10.py

I certify that this assignment is entirely my own work.
"""
from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size/ 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        self.head.draw(self.window)
        self.left_eye.draw(self.window)
        self.right_eye.draw(self.window)


    def shock(self):
        pass

    def wink(self):
        self.head.draw(self.window)
        self.mouth.draw(self.window)
        self.right_eye.draw(self.window)
        left_eye = Line()