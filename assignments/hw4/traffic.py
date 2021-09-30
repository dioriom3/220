"""
Name: Michael Diorio
File Name: traffic.py
Problem: To take input from the user using nested loops to determine the number
of roads surveyed, for how many days, and how many cars per day in order to obtain
a calculation of the average cars traveled per road.
"""


def main():
    roads = eval(input("How many roads were surveyed: "))
    acc = 0
    acc_total = 0
    for i in range(1, roads + 1):
        days = eval(input("How many days was road " + str(i) + " surveyed? :"))
        for j in range(1, days + 1):
            cars = eval(input("How many cars traveled on day " + str(j) + "? :"))
            acc = acc + cars
            acc_total = acc_total + cars
        print("Road " + str(i) + " average vehicles per day: ", round((acc / days), 2))
        acc = 0
    print("Total number of vehicles traveled on all roads: ", acc_total)
    print("Average number of vehicles per road: ", round((acc_total / roads), 2))
