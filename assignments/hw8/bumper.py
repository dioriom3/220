"""
Name: Michael Diorio
File Name: bumper.py
Problem: To create a graphics window with two circles that act like bumper cars.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""

import math
import time
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb, Text


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def get_random(move_amount):
    why_is_x_not_a_proper_variable_name = randint(-move_amount, move_amount)
    return why_is_x_not_a_proper_variable_name


def main():
    win = GraphWin("Bumper", 450, 450)
    bumper1 = Circle(Point(100, 100), 30)
    bumper2 = Circle(Point(300, 300), 30)
    bumper1.draw(win)
    bumper2.draw(win)
    bumper1.setFill(get_random_color())
    bumper2.setFill(get_random_color())

    bumper1_x = get_random(10)
    bumper1_y = get_random(10)
    bumper2_x = get_random(10)
    bumper2_y = get_random(10)

    inst_pt = Point(win.getWidth() / 2, win.getHeight() - 10)
    instructions = Text(inst_pt, "Type q to quit. :)")
    instructions.draw(win)

    while True:
        key = win.checkKey()
        if key == "q":
            break

        bumper1.move(bumper1_x, bumper1_y)
        bumper2.move(bumper2_x, bumper2_y)

        if hit_horizontal(bumper1, win):
            bumper1_y = -1 * bumper1_y
        elif hit_vertical(bumper1, win):
            bumper1_x = -1 * bumper1_x
        elif hit_horizontal(bumper2, win):
            bumper2_y = -1 * bumper2_y
        elif hit_vertical(bumper2, win):
            bumper2_x = -1 * bumper2_x
        elif did_collide(bumper1, bumper2):
            bumper1_x = -1 * bumper1_x
            bumper2_x = -1 * bumper2_x
            bumper1_y = -1 * bumper1_y
            bumper2_y = -1 * bumper2_y

        time.sleep(0.005)

    win.close()


def hit_vertical(circle, win):
    center = circle.getCenter()
    radius = circle.getRadius()
    center_x_coord = center.getX()
    win_width = win.getWidth()

    return bool(center_x_coord - radius <= 0 or center_x_coord + radius >= win_width)


def hit_horizontal(circle, win):
    center = circle.getCenter()
    radius = circle.getRadius()
    center_y_coord = center.getY()
    win_height = win.getHeight()

    return bool(center_y_coord - radius <= 0 or center_y_coord + radius >= win_height)


def did_collide(bumper1, bumper2):
    x_1 = bumper1.getCenter().getX()
    x_2 = bumper2.getCenter().getX()
    y_1 = bumper1.getCenter().getY()
    y_2 = bumper2.getCenter().getY()
    d_temp = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
    distance = math.sqrt(d_temp)
    radius1 = bumper1.getRadius()
    radius2 = bumper2.getRadius()
    radius_total = radius1 + radius2

    return bool(radius_total >= distance)


if __name__ == '__main__':
    main()
