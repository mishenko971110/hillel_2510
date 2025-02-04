# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, 
# Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати 
# додатковий атрибут department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати 
# всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який 
# вказує на кількість розробників у команді, якою керує керівник.
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

import unittest

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def check_attributes(lead_employee):
    print(f"Name: {lead_employee.name}")
    print(f"Salary: {lead_employee.salary}")
    print(f"Department: {lead_employee.department}")
    print(f"Programming Language: {lead_employee.programming_language}")
    print(f"Team Size: {lead_employee.team_size}")
    

try:
    lead_employee = TeamLead('Oliwia', 50000, 'Dev', 'python', 7)
    check_attributes(lead_employee)
    print('All required arguments are in object.')
except TypeError as e:
    print('Required argument is missed.')
