"""
Scott Repik -Repiksh
hw10.py

I certify that this assignment is entirely my own work.
"""
import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        area = 4 * math.pi * self.radius**2
        return area

    def volume(self):
        volume_value = (4 / 3) * math.pi * self.radius**3
        return volume_value



