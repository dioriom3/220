"""
Name: Michael Diorio
File Name: greeting.py

Problem: To display a heart & arrow/greeting card using graphics package commands.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
import time
from graphics import GraphWin, Circle, Polygon, Point, Text, Line


def main():
    width = 450
    height = 450
    win = GraphWin("Greeting Card", width, height)

    circle1 = Circle(Point(175, 175), 61)
    circle1.setOutline("pink")
    circle1.setFill("pink")
    circle1.draw(win)

    circle2 = Circle(Point(285, 175), 61)
    circle2.setOutline("pink")
    circle2.setFill("pink")
    circle2.draw(win)

    triangle1 = Polygon(Point(120, 202), Point(340, 202), Point(225, 355))
    triangle1.setOutline("pink")
    triangle1.setFill("pink")
    triangle1.draw(win)

    inst_pt = Point(width / 2, height - 40)
    instructions = Text(inst_pt, "Happy Valentine's Day!")
    instructions.setOutline("red")
    instructions.draw(win)

    arrow = Line(Point(0, 400), Point(225, 255))
    arrow.setArrow("last")
    arrow.setOutline("purple")
    arrow.draw(win)

    for _ in range(0, 28):
        arrow.move(5, -4)
        time.sleep(0.1)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to close.")
    instructions.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
