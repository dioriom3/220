"""
Name: Michael Diorio
File Name: interest.py

Problem: To design a program that will give the Root-Mean-Square Average, the Harmonic Mean,
and Geometric Mean determined by user input.

1. The program will take user input to determine the number of values being calculated and the
values themselves to be used in calculation. Using a definite loop, the code will output the
respective means/averages.

2. The inputs will be the number of values being averaged and the values being averaged. The outputs
will be the three calculated means/averages.

3. The program must take in input from the user, use that data to calculate the desired result
through a definite loop, and then output the results.

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
import math


def main():
    acc = 0
    acc1 = 0
    acc2 = 1
    terms = eval(input("Enter the values to be entered: "))
    for i in range(1, terms + 1):
        value = eval(input("Enter value " + str(i) + ":"))
        acc = acc + (value * value)

        den = 1 / value
        acc1 = acc1 + den

        acc2 = acc2 * value

    acc = acc / terms
    rms = math.sqrt(acc)

    harmonic = terms / acc1

    geo = acc2 ** (1 / terms)

    print(round(rms, 3))
    print(round(harmonic, 3))
    print(round(geo, 3))
