"""
Name: Michael Diorio
lab3.py
"""


def average():
    number_of_grades = eval(input("Enter the number of hw grades: "))
    acc = 0
    for i in range(1, number_of_grades + 1):
        grade = eval(input("Enter your grade on HW " + str(i) + ":"))
        acc = (acc + grade)
    acc = acc / number_of_grades
    print(acc)


def tip_jar():
    acc2 = 0
    for i in range(1, 6):
        donation = eval(input("Enter the amount of your donation: "))
        acc2 = acc2 + donation
    print("Total: ", round(acc2, 2))


def newton():
    x = eval(input("Enter a value for 'x': "))
    refine = eval(input("Enter the number of times to refine the approx: "))
    approx = (x / 2)
    for x in range(refine):
        approx = (approx + (x / approx)) / 2
    print(x, ", ", approx)


def sequence():
    terms = eval(input("Enter the number of terms in the series: "))
    for i in range(1, terms + 1):
        y = 1 + ((i//2) * 2)
        print(y, end=" ")


def pi():
    acc = 1
    terms = eval(input("Enter the number of terms in the series: "))
    for n in range(0, terms):
        num = 2 + (n // 2) * 2
        den = 1 + ((n + 1) // 2) * 2
        fraction = num / den
        acc = acc * fraction
    print(2 * acc)



