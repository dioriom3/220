"""
Name: Michael Diorio
lab9.py
"""
from graphics import GraphWin, Circle, Point, Text
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])


def writeSumOfSquares():
    infile_name = input("Enter name of input file: ")
    infile = open(infile_name, "r")
    outfile = open("outfile.txt", "w+")
    acc = 0
    for line in infile:
        num_list = line.split()
        toNumbers(num_list)
        squareEach(num_list)
        acc = sumList(num_list)
        outfile.write("Sum of squares = " + str(acc) + '\n')


def starter():
    weight = float(eval(input("Enter the weight of a player: ")))
    num_wins = int(eval(input("Enter the number of wins the player has: ")))
    if 150 <= weight < 160 and num_wins >= 5:
        print("The player should start on the team.")
    elif weight > 199 or num_wins > 20:
        print("The player should start on the team.")
    else:
        print("The player should not start on the team.")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + "is a leap year")
        return True
    else:
        print(str(year) + " is not a leap year")
        return False


def circleOverlap():
    win = GraphWin("CircleOverlap", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)

    if distance <= (radius1 + radius2):
        inst_pt = Point(400 / 2, 400 - 10)
        instructions = Text(inst_pt, "The circles overlap.")
        instructions.draw(win)
    else:
        inst_pt = Point(400 / 2, 400 - 10)
        instructions = Text(inst_pt, "The circles do not overlap.")
        instructions.draw(win)

    win.getMouse()
    win.close()


def main():
    # starter()
    # leapYear(2000)
    # writeSumOfSquares()
    # circleOverlap()


    pass


main()
