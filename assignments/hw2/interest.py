"""
Name: Michael Diorio
File Name: interest.py

Problem: To compute and output the monthly interest charge on a credit card account

Certification of Authenticity: I certify that this assignment is entirely my own work.
"""


def main():
    apr = eval(input("Enter the annual interest rate: "))
    days_in_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_bal = eval(input("Enter the previous (net) balance: "))
    payment = eval(input("Enter the amount of the payment: "))
    day_of_payment = eval(input("Enter the day of the billing cycle the payment was made: "))

    step1 = net_bal * days_in_cycle
    step2 = payment * (days_in_cycle - day_of_payment)
    step3 = step1 - step2
    avg_daily_bal = step3 / days_in_cycle
    monthly_interest_rate = (apr / 12) * (1/100)
    month_interest_charge = avg_daily_bal * monthly_interest_rate

    print(round(month_interest_charge, 2))
