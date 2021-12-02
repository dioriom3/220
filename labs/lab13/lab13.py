"""
Name: Michael Diorio
lab13.py
"""
from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    mid = len(values) // 2
    while values[mid] != search_val and len(values) != 1:
        if values[mid] < search_val:
            values = values[mid:]
        else:
            values = values[:mid]
        mid = len(values) // 2
    if search_val == values[mid]:
        return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]
    return values


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = d[(areas[i])]
    return rectangles


def star_find(filename):
    infile = open(filename, 'r')
    signals = infile.read().split()
    stars_found = []
    acc = 0
    for i in range(len(signals)):
        if 4000 <= int(signals[i]) <= 5000:
            stars_found.append(signals[i])
        if len(stars_found) >= 5:
            break
        acc = acc + 1
    print(len(stars_found), "pulses were found.")
    if len(stars_found) >= 5:
        print("The following signal strengths were found: ", stars_found)
        print(acc - 1, " signals were searched before the fifth was detected.")
    else:
        print("The neutron star was not found.")


def main():
    print(is_in_binary(3, [1, 2, 3, 4, 5]))
    print()
    print(selection_sort([1, 92, 4, 5, 2, 18, 5]))
    print()
    print(rect_sort([Rectangle(Point(0, 0), Point(20, 5)), Rectangle(Point(0, 0), Point(30, 5)),
               Rectangle(Point(0, 0), Point(10, 5))]))
    print()
    star_find("signals.txt")
    pass


main()
