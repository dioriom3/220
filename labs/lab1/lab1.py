"""
Name: Michael DIorio
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    shots_made = eval(input("Enter the number of shots made: "))
    total_shots = eval(input("Enter the total number of shots: "))
    shot_percentage = (shots_made / total_shots) * 100
    print("Shooting percentage: ", shot_percentage, "%")


def coffee():
    coffee_cost = 10.50
    shipping_cost = 0.86
    fixed_cost = 1.50
    pounds_purchased = eval(input("Enter the number of pounds of coffee purchased: "))
    total_cost = fixed_cost + pounds_purchased * (coffee_cost + shipping_cost)
    print("Total cost: ", total_cost)


def kilometers_to_miles():
    kilometers_traveled = eval(input("Enter the number of kilometers traveled"))
    miles_traveled = kilometers_traveled / 1.61
    print("Miles traveled: ", miles_traveled)
