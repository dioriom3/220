"""
Name: Michael Diorio
lab6.py
"""


def name_reverse():
    s = input("Enter a first name then last name: ")
    s = s.split()
    print(s[1] + ", " + s[0])


def company_name():
    x = input("Enter a three-part internet domain name: ")
    x = x.split(".")
    print(x[1])


def initials():
    name = eval(input("How many names would you like to input? : "))
    for i in range(0, name):
        first_name = input("Enter a first name: ")
        last_name = input("Enter the last name: ")
        print("The initials are: ", first_name[0] + last_name[0])


def names():
    y = input("Enter a list of names separated by a comma: ")
    y = y.split(", ")
    for i in y:
        parts = i.split()
        print("The initials of the names are: ", parts[0][0] + parts[1][0])


def thirds():
    n = eval(input("How many sentences would you like to input? : "))
    for i in range(n):
        s = input("Enter a sentence: ")
        print(s[2:-1:3])


def word_average():
    x = input("Enter a sentence: ")
    acc = 0
    x = x.split()
    for word in x:
        acc = acc + len(word)
    print(acc / len(x))


def pig_latin():
    x = input("Enter a sentence: ")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay")


def main():
    name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()


main()
