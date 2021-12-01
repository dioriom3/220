"""
Name: Michael Diorio
File Name: sales_person.py
Problem: Encapsulates data for a sales person.
Certification of Authenticity: I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """Encapsulates data for a sales person."""

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        for line in infile:
            data = line.split(",")
            ident_num = data[0]
            employ_name = data[1]
            sales = data[2].split()
            sale_person = SalesPerson(ident_num, employ_name)

            for sale in sales:
                sale_person.enter_sale(sale)
            self.sales_people.append(sale_person)

    def quota_report(self, quota):
        employee_data = []
        for sales_person in self.sales_people:  # take from list
            employ_list = [sales_person.get_id(), sales_person.get_name(),
                           sales_person.total_sales(), sales_person.met_quota(quota)]
            employee_data.append(employ_list)
        return employee_data

    def top_seller(self):
        highest_sales_amount = []
        high_seller = 0
        for person in self.sales_people:
            if high_seller < person.total_sales():
                high_seller = person.total_sales()
                highest_sales_amount.append(person)
        for person in self.sales_people:
            if high_seller == person.total_sales():
                highest_sales_amount.append(person)
        return highest_sales_amount

    def individual_sales(self, employee_id):
        for sale_person in self.sales_people:
            if sale_person.get_id() == employee_id:
                return sale_person
            else:
                return None
