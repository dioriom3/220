"""
Name: Michael Diorio
Problem: To process numeric data from a text file, calculate weighted averages and write
them to another text file.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")

    num_students = 0
    acc = 0

    for line in infile:
        part = line.split(": ")
        name = part[0]
        f_and_l_name = name.split(" ")
        grades = part[1]
        values = grades.split(" ")

        phrase = name + "'s average: "

        score = 0
        overall_weight = 0

        for i in range(0, len(values), 2):
            weight = int(values[i])
            overall_weight = overall_weight + weight

        if overall_weight > 100:
            outfile.write(phrase + "Error: The weights are more than 100." + "\n")
        elif overall_weight < 100:
            outfile.write(phrase + "Error: The weights are less than 100." + "\n")
        else:
            for j in range(0, len(values), 2):
                grades = float(values[j + 1])
                weights = float(values[j])
                score = score + (weights * grades)
            overall_score = score / 100
            acc = acc + overall_score
            num_students = num_students + 1
            overall_score = round((score / 100), 1)
            outfile.write(phrase + str(overall_score) + "\n")

    class_avg = round((acc / num_students), 1)
    outfile.write("Class average: " + str(class_avg))


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
