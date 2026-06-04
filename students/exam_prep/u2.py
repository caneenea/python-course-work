"""
a) Create a class Patient.
b) Create a class Hospital that stores hospital name and patients.
c) Create a function that reads JSON.
d) Create a function that converts JSON data to Patient objects.
e) Create a method that returns the average treatment score of a patient.
f) Find the patient with the highest average treatment score.
g) Find which gender has the highest average treatment score.
h) Create a function that returns a list of hospitals and their patients.
i) Create a method that returns the average treatment score of a hospital.
j) Find the hospital with the highest average treatment score.

"""

import json
from dataclasses import dataclass

@dataclass
class Patient:
    first_name: str
    last_name: str
    age: int
    treatments: list[int]
    gender: str
    hospital: str

    def avg(self):
        return sum(self.treatments) / len(self.treatments)

@dataclass
class Hospital:
    hospital_name: str
    patients: list[Patient]


def import_json(path: str) -> list[dict]:
    with open(path) as f:
        data = json.load(f)
        return data

def convert_json(patients_data: list[dict]) -> list[Patient]:
    patients = []
    for patient in patients_data:
        patients.append(Patient(**patient))
    return patients

def best_patient(patients: list[Patient]) -> Patient:
    best = patients[0]
    for patient in patients:
        if patient.avg() > best.avg():
            best = patient
    return best

def best_gender(patients: list[Patient]) -> Patient:
    sum_male = 0
    sum_female = 0
    count_male = 0
    count_female = 0
    for patient in patients:
        if patient.gender == 'male':
            count_male += 1
            sum_male += patient.avg()
        else:
            count_female += 1
            sum_female += patient.avg()

    avg_male = sum_male / count_male
    avg_female = sum_female / count_female

    if avg_male > avg_female:
        return 'male'
    else:
        return 'female'

def hospitals_list(patients_data: list[Patient]) -> list[Hospital]:
    hospitals = []
    for patient in patients_data:
        find = False
        for hospital in hospitals:
            if hospital.name == patient.hospital:
                hospital.patients.append(hospital)
                find = True
                break

        if not find:
            hospital = Hospital(patient.hospital, [patient])
            hospitals.append(hospital)

    return hospitals





