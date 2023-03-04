
import csv

PATIENT_PATH = 'data/patients.csv'
RECORD_PATH = 'data/records.csv'

class Record:
    def __init__(self, record_id, patient_id, date_time,hart_rate, blood_pressure, temperature, oxygen_saturation, respiratory_rate, rank=0):
        self.record_id = record_id
        self.patient_id = patient_id
        self.date_time = date_time
        self.hart_rate = hart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate
        self.rank = rank

      




class Patient:
    def __init__(self,patient_id,name,age,address,location,arrival_time,complaint,Ctas,rank=0,current_record=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.address = address
        self.location = location
        self.arrival_time = arrival_time
        self.complaint = complaint
        self.Ctas=Ctas
        self.rank = rank
        self.current_record : Record = current_record







class PatientList:
    def __init__(self):
        self.patients = []
        self.records = []
        self.load_data()

    def get_patients(self):
        return self.patients
    


    def load_data(self):
        with open(RECORD_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 9:
                    continue
                record = Record(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.records.append(record)
        
        self.records.sort(key=lambda x: x.date_time, reverse=True)
                

        with open(PATIENT_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 9:
                    continue
                patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], self.get_record(row[0]))
                self.patients.append(patient)
        

    def get_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

    def get_record(self, patient_id):
        for record in self.records:
            if record.patient_id == patient_id:
                return record

    def add_patient(self, patient):
        self.patients.append(patient)
        with open(PATIENT_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([patient.patient_id,patient.name, patient.age, patient.address,patient.location,patient.arrival_time,patient.complaint, patient.Ctas, patient.rank])

    def add_record(self, record):
        self.records.append(record)
        with open(RECORD_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([record.record_id, record.patient_id, record.date_time, record.hart_rate, record.blood_pressure, record.temperature, record.oxygen_saturation, record.respiratory_rate, record.rank])

    def update_patient(self, patient):
        for i in range(len(self.patients)):
            if self.patients[i].patient_id == patient.patient_id:
                self.patients[i] = patient
                break
        with open(PATIENT_PATH, 'w') as file:
            writer = csv.writer(file)
            for patient in self.patients:
                writer.writerow([patient.patient_id,patient.name, patient.age, patient.address,patient.location,patient.arrival_time,patient.complaint,patient.Ctas, patient.rank])

    