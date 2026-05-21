"""
Create a Python class called Student.

The class should have the following attributes:
name, age, student_id, and grades.

The grades attribute should be a list of numbers.

Your class must include:

1. An __init__() method that initializes the student’s name, age, student ID, and grades.
2. A method called add_grade() that adds a new grade to the grades list.
3. A method called average_grade() that returns the average of the student’s grades.
4. A method called passed() that returns True if the student’s average grade is 50 or higher, and False otherwise.
5. A special method __str__() that prints the student’s information in a clear format.

Example output:

Student: Enea, ID: 101, Average Grade: 82.5

"""

class Student:
    def __init__(self, name, age, student_id, grades):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def passed(self):
        if self.average_grade() > 50:
            return True
        else:
            return False

    def __str__(self):
        return f"Student : {self.name}, ID: {self.student_id}, Average Grade: {self.average_grade()}"


s1 = Student("Enea", 21, 201, [100, 90, 65])
s1.add_grade(85)
print(s1)
print(s1.average_grade())
print(s1.passed())