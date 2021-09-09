"""
Name: Michael Diorio
lab.py
"""
import math


def sum_of_threes():
    acc = 0
    bound = eval(input("Enter an upper bound: "))
    for i in range(0, bound + 1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter length of side 1: "))
    b = eval(input("Enter length of side 2: "))
    c = eval(input("Enter length of side 3: "))
    s = (a + b + c) / 2
    A = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(A)

    print("The area of the triangle is: ", area)


def sumSquares():
    acc = 0
    lower_bound = eval(input("Enter a lower bound: "))
    upper_bound = eval(input("Enter an upper bound: "))
    for i in range(lower_bound, upper_bound + 1):
        acc = acc + (i ** 2)

    print(acc)


def power():
    acc = 1
    base = eval(input("Enter a base: "))
    exp = eval(input("Enter an exponent: "))
    for i in range(exp):
        acc = acc * base

    print(base, " ^ ", exp, " = ", acc)
