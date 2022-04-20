"""
Scott Repik -Repiksh
algorithms.py


"""

from graphics import *


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def read_data(file_name):
    text = open(file_name, "r")
    list_file = []
    lines = text.readline()

    while lines:
        i = 0
        no_new = lines.strip("\n")
        lines_strip = no_new.split(" ")
        while i < len(lines_strip):
            is_int = int(lines_strip[i])
            i += 1
            list_file.append(is_int)
        lines = text.readline()
    text.close()

    return list_file


def selection_sort(values):
    for i in range(len(values)):
        first_index = i
        for q in range(i + 1, len(values)):
            if calc_area(values[first_index]) >= calc_area(values[q]):
                first_index = q
        values[i], values[first_index] = values[first_index], values[i]



def calc_area(rect):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    p_1_x = point_1.getX()
    p_1_y = point_1.getY()
    p_2_x = point_2.getX()
    p_2_y = point_2.getY()
    width = abs(p_2_x - p_1_x)
    length = abs(p_2_y - p_1_y)
    area = width * length
    return area


def rect_sort(rectangles):
    selection_sort(rectangles)


def main():
    list_rect = [Rectangle(Point(0, 0), Point(10, 10)), Rectangle(Point(15, 15), Point(20, 20)),
                 Rectangle(Point(5, 0), Point(20, 30))]
    rect_sort(list_rect)
    print(list_rect)
