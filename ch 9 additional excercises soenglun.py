class CellPhone:
    def __init__(self, man, model, price):
        self.manufact = man
        self.model = model
        self.retail_price = price

    def set_manufact(self, man):
        self.manufact = man

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, price):
        self.retail_price = price

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price

man = input('Enter the manufacturer: ')
model = input('Enter the model number: ')
price = float(input('Enter the retail price: '))
phone = CellPhone(man, model, price)
print('Here is the data that you have entered')
print('Manufacturer: ' + phone.get_manufact())
print('Model Number: ' + phone.get_model())
print('Retail Price: $' + '%.2f' % phone.get_retail_price())

class Employee:
    def employee_name(self, name)
        self.name = name

    def id_number(self, number)
        self.number = number

    def employee_dept(self, dept)
        self.dept = dept

    def job_title(self, title)
        self.title = title

name = input('Enter first and last name: ')
number = input('Enter employee ID Number: ')
dept = input('Enter employee department: ')
title = input('Enter employee job title: ')
