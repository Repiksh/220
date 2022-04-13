"""
Scott Repik -Repiksh
lab12.py


"""


def find_and_remove(values, search_val):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            values.pop(i)
            values.insert(i, "Scott")
        i += 1
    print(values)






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


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


def main():
    pass

