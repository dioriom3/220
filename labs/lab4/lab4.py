"""
Name: Michael Diorio
lab4.py
"""
import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(width / 2, height - 30)
    instructions = Text(inst_pt, "Click to add corners of rectangle")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    r = Rectangle(p1, p2)
    r.draw(win)

    length = abs(p2.getX() - p1.getX())
    width = abs(p2.getX() - p1.getX())
    area = length * width
    perimeter = (2 * length) + (2 * width)

    instructions.undraw()
    instructions.setText("Area: " + str(area) + ", Perimeter: " + str(perimeter) + ". Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()

    pass


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add center of circle & point on circumference")
    instructions.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    dist = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    rad = round(math.sqrt(dist), 4)

    c = Circle(p1, rad)
    c.draw(win)

    instructions.undraw()
    instructions.setText("Radius is " + str(rad) + ". Click to close.")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    terms = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(0, terms):
        num = 4 * ((-1) ** i)
        den = 1 + (2 * i)
        fraction = num / den
        acc = acc + fraction
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
