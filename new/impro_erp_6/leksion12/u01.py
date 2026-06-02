""" u1 """
import json
from dataclasses import dataclass

"""
Në një json ruhen të dhënat e studentëve të një universiteti.
a) Ndërtoni një klasë e cila do të ruaj të dhënat e këtyre
    studentëve
b) Ndërtoni një klasë e cila do të ruaj emrin e shtetit dhe
    një listë me studentët e tij
c) Ndërtoni një funksion i cili kthen të dhënat e këtij json.
d) Ndërtoni një funksion i cili kthen një listë me
    studentë nga json i dhënë
e) Ndërtoni një metodë për studentët që kthen
    mesataren e tij
f) Gjeni studentin më të mirë
g) Gjeni kush prej gjinive ka mesatare më të lartë
h) Ndërtoni një funksion i cili kthën një listë
    me shtete dhe studentët e secilit shtet
i) Ndërtoni një metodë e cila kthen mesataren e shtetit
j) Ndërtoni një funksion i cili kthen shtetin
    me mesatare më të lartë
"""


@dataclass
class Student:
    first_name: str
    last_name: str
    age: int
    score: list[int]
    gender: str
    country: str

    def avg(self):
        s = 0
        for score in self.score:
            s += score
        return s / len(self.score)


@dataclass
class Country:
    name: str
    students: list[Student]

    def avg(self):
        s = 0
        for student in self.students:
            s += student.avg()
        return s / len(self.students)


def import_json(path: str) -> list[dict]:
    with open(path) as file:
        return json.load(file)


def convert_to_students(students_data: list[dict]) -> list[Student]:
    students = []
    for student in students_data:
        students.append(Student(**student))
    return students


def find_best_student(students: list[Student]) -> Student:
    if not students:
        return None

    best_student = students[0]
    for student in students:
        if student.avg() > best_student.avg():
            best_student = student
    return best_student


def find_best_gender(students: list[Student]) -> Student:
    if not students:
        return None
    s_m = 0
    count_m = 0
    s_f = 0
    count_f = 0
    for student in students:
        if student.gender == 'male':
            s_m += student.avg()
            count_m += 1
        else:
            s_f += student.avg()
            count_f += 1

    avg_m = s_m / count_m
    avg_f = s_f / count_f
    # return 'male' if avg_m > avg_f else 'female'
    if avg_m > avg_f:
        return 'male'
    else:
        return 'female'


def create_countries_list(students_data: list[Student]) -> list[Country]:
    countries = []
    for student in students_data:
        find = False
        for country in countries:
            if country.name == student.country:
                country.students.append(student)
                find = True
                break
        if not find:
            country = Country(student.country, [student])
            countries.append(country)
    return countries


def find_best_country(countries: list[Country]) -> Country:
    if not countries:
        return None
    best_country = countries[0]
    for country in countries:
        if country.avg() > best_country.avg():
            best_country = country
    return best_country


students_data = import_json('data/student.json')
students_list = convert_to_students(students_data)
countires_list = create_countries_list(students_list)
print(find_best_student(students_list))
print(find_best_gender(students_list))
print(find_best_country(countires_list).name)
