
import csv

PATIENT_PATH = 'data/patients.csv'
RECORD_PATH = 'data/records.csv'

class Record:
    def __init__(self, record_id, patient_id, date, time,hart_rate, blood_pressure, temperature, oxygen_saturation, respiratory_rate):
        self.record_id = record_id
        self.patient_id = patient_id
        self.date = date
        self.time = time
        self.hart_rate = hart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate

      




class Patient:
    def __init__(self,name,age,address,phone_number,patient_id):
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.patient_id = patient_id
        self.records = []
        



class PatientList:
    def __init__(self):
        self.patients = []
        self.records = []
        self.load_data()

    def load_data(self):
        with open(PATIENT_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                patient = Patient(row[0], row[1], row[2], row[3], row[4])
                self.patients.append(patient)
        with open(RECORD_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                record = Record(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.records.append(record)
                for patient in self.patients:
                    if patient.patient_id == record.patient_id:
                        patient.records.append(record)

    def get_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

    def get_record(self, record_id):
        for record in self.records:
            if record.record_id == record_id:
                return record

    def add_patient(self, patient):
        self.patients.append(patient)
        with open(RECORD_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([patient.name, patient.age, patient.address, patient.phone_number, patient.patient_id])

    def add_record(self, record):
        self.records.append(record)
        with open(RECORD_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([record.record_id, record.patient_id, record.date, record.time, record.hart_rate, record.blood_pressure, record.temperature, record.oxygen_saturation, record.respiratory_rate])

    def update_patient(self, patient):
        for i in range(len(self.patients)):
            if self.patients[i].patient_id == patient.patient_id:
                self.patients[i] = patient
                break
        with open(PATIENT_PATH, 'w') as file:
            writer = csv.writer(file)
            for patient in self.patients:
                writer.writerow([patient.name, patient.age, patient.address, patient.phone_number, patient.patient_id])

    def update_record(self, record):
        for i in range(len(self.records)):
            if self.records[i].record_id == record.record_id:
                self