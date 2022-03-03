"""
Scott Repik - Repiksh
lab7.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# , out_file_name


def weighted_average(in_file_name, out_file_name):
    out = open(out_file_name, "w")
    grades = open(in_file_name, "r")
    grades_list = grades.readlines()
    num_students = 0

    for i in grades_list:
        names_grades = i.split(":")
        names_grades_list = names_grades[0].split()
        print(names_grades_list)
        weights_total = 100
        grades_weights = names_grades[1].split()
        grades_weights_list = list(map(int, grades_weights))
        list_weights = grades_weights_list[::2]
        list_grades = grades_weights_list[1::2]
        weight_sum = sum(list_weights)
        avg = 0
        if weight_sum > weights_total:
            out.write(repr(names_grades_list) + "Error: the weights are above 100" + "\n")
        elif weight_sum < weights_total:
            out.write(repr(names_grades_list) + "Error: the weights are below 100" + "\n")
        else:
            for q in range(len(list_weights)):
                avg = avg + (list_weights[q] * list_grades[q])
            full_avg = avg / 100
            out.write(repr(names_grades_list) + "average grade is:" + repr(full_avg) + "\n")

    grades.close()
    out.close()


def main():
    weighted_average("grades", "avg")


if __name__ == "__main__":
    main()

