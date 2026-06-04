import json
from dataclasses import dataclass


"""
a) Create a class Employee.
b) Create a class Department that stores department name and employees.
c) Create a function that reads JSON.
d) Create a function that converts JSON data to Employee objects.
e) Create a method that returns the average salary of an employee.
f) Find the employee with the highest average salary.
g) Find which gender has the highest average salary.
h) Create a function that returns a list of departments and their employees.
i) Create a method that returns the average salary of a department.
j) Find the department with the highest average salary.

"""
import json
from dataclasses import dataclass


@dataclass
class Employee:
    first_name: str
    last_name: str
    age: int
    salary: list[int]
    gender: str
    department: str

    def average_salary(self):
        s = 0
        for salary in self.salary:
            s += salary
        return s / len(self.salary)


@dataclass
class Department:
    department_name: str
    employees: list[Employee]

    def average_salary(self):
        s = 0
        for employee in self.employees:
            s += employee.average_salary()
        return s / len(self.employees)


def import_json(path: str) -> list[dict]:
    with open(path) as json_file:
        data = json.load(json_file)
        return data


def convert_to_employees(employees_data: list[dict]) -> list[Employee]:
    employees = []
    for data in employees_data:
        employees.append(Employee(**data))
    return employees


def best_employee(employees: list[Employee]) -> Employee:
    if not employees:
        return None

    best = employees[0]
    for employee in employees:
        if employee.average_salary() > best.average_salary():
            best = employee
    return best


def gender(employees: list[Employee]) -> str:
    if not employees:
        return None

    sm = 0
    sf = 0
    cm = 0
    cf = 0

    for employee in employees:
        if employee.gender == 'male':
            cm += 1
            sm += employee.average_salary()
        else:
            cf += 1
            sf += employee.average_salary()

    avg_m = sm / cm
    avg_f = sf / cf

    if avg_m > avg_f:
        return 'male'
    else:
        return 'female'


def department(employees_data: list[Employee]) -> list[Department]:
    departments = []

    for employee in employees_data:
        find = False

        for department in departments:
            if department.department_name == employee.department:
                department.employees.append(employee)
                find = True
                break

        if not find:
            department = Department(employee.department, [employee])
            departments.append(department)

    return departments