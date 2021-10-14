"""
Name: Michael Diorio
Partner: <your partner's name goes here – first and last>
lab7.py
"""
import math


def cash_conversion():
    x = eval(input("Enter a number: "))
    print("${:.2f}".format(x))


def encode():
    s = input("Enter a message to be encoded: ")
    x = eval(input("Enter a key value: "))
    acc = " "
    for c in s:
        i = ord(c)
        i = i + x
        c = chr(i)
        acc = acc + c
    print(acc)


def sphere_area(radius):
    s_area = 4 * math.pi * (radius ** 2)
    return s_area


def sphere_volume(radius):
    vol = (4 / 3) * math.pi * (radius ** 3)
    return vol


def sum_n(n):
    acc = 0
    for i in range(n+1):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n+1):
        acc = acc + (i ** 3)
    return acc


def encode_better():
    s = input("Enter a message to be encoded: ")
    k = input("Enter a cipher key message: ")
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        x = c + key
        x = chr(x)
        acc += x
    print(acc)


def main():
    # cash_conversion()
    # encode()
    # print(round(sphere_area(5), 4))
    # print(round(sphere_volume(5), 4))
    # print(round(sum_n(6), 3))
    # print(sum_n_cubes(4))
    # encode_better()
    pass


main()
