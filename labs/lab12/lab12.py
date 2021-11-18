"""
Name: Michael Diorio
lab12.py
"""
from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Michael"
    except:
        pass


def read_data(filename):
    infile = open(filename, "r")
    data = infile.readlines()
    data = data[0].split()
    i = 0
    while i < len(data):
        data[i] = int[i]
        i += 1
    return data


def search(lst, value):
    i = 0
    while i < len(lst):
        if lst[i] == value:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("Enter a number between 1 and 10"))
    while x < 1 or x > 10:
        x = eval(input("Number not in range, try again"))
    return x


def num_digits():
    x = eval(input("Enter a positive integer: "))
    while x >= 1:
        digits = 0
        while digits > 0:
            digits += 1
            x //= 10
        print("The number of digits is: " + str(digits))
        x = eval(input("Enter another positive integer: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("Guess a number from 1 to 100"))
    while guess != num and guesses < 7:
        guesses += 1
        if guess > num and guesses < 7:
            print("The number entered was too high.")
            guess = eval(input("Guess again."))
        elif guess < num and guesses < 7:
            print("The number entered was too low.")
            guess = eval(input("Guess again."))
        guesses += 1
        if guess != num and guesses < 7:
            guess = eval(input("Guess a number 1-100"))
    if guess == num:
        print("You guessed the number correctly in " + str(guesses) + " guesses.")
    else:
        print("The correct number was " + str(num) + " !")



def main():
    # find_and_remove_first([1, 2, 3, 4, 5, 6], 4)
    # read_data("dataSorted.txt")
    # print(search(4, data))
    # good_input()
    # num_digits()
    # hi_lo_game()
    pass


main()
