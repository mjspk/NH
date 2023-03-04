
import csv
import datetime

PATIENT_PATH = 'data/patients.csv'
RECORD_PATH = 'data/records.csv'


class Record:
    def __init__(self, record_id, patient_id, date, time, heart_rate, blood_pressure, temperature, oxygen_saturation, respiratory_rate):
        self.record_id = record_id
        self.patient_id = patient_id
        date = datetime.date(date)
        time = datetime.time(time)
        self.date_time = datetime.datetime.combine(date, time)
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate
        # supplemental oxygen needed later


class Patient:
    def __init__(self, name, age, address, phone_number, patient_id):
        self.name = name
        self.age = age
        self.address = address
        self.patient_id = patient_id
        self.current_record: Record = None


class PatientList:
    def __init__(self):
        self.patients = []
        self.records = []
        self.load_data()

    # just most recent one
    def load_data(self):

        with open(RECORD_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                record = Record(row[0], row[1], row[2], row[3],
                                row[4], row[5], row[6], row[7], row[8])
                self.records.append(record)
                for patient in self.patients:
                    if patient.patient_id == record.patient_id:
                        patient.records.append(record)

        with open(PATIENT_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                patient = Patient(row[0], row[1], row[2], row[3], row[4])
                # need to get 'current record' for patient from get_record
                latest_record = self.get_record(patient.patient_id)
                patient.current_record = latest_record
                # patient append after latest record found
                self.patients.append(patient)

    def get_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

    def get_record(self, patient_id):
        for record in self.records:
            patient_records = []
            if record.patient_id == patient_id:
                patient_records.append(record)
        if not patient_records:
            return None
        return max(patient_records, key=lambda r: r.date_time)

    def add_patient(self, patient):
        self.patients.append(patient)
        with open(RECORD_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([patient.name, patient.age, patient.address,
                            patient.phone_number, patient.patient_id])

    def add_record(self, record):
        self.records.append(record)
        with open(RECORD_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([record.record_id, record.patient_id, record.date, record.time, record.hart_rate,
                            record.blood_pressure, record.temperature, record.oxygen_saturation, record.respiratory_rate])

    def update_patient(self, patient):
        for i in range(len(self.patients)):
            if self.patients[i].patient_id == patient.patient_id:
                self.patients[i] = patient
                break
        with open(PATIENT_PATH, 'w') as file:
            writer = csv.writer(file)
            for patient in self.patients:
                writer.writerow([patient.name, patient.age, patient.address,
                                patient.phone_number, patient.patient_id])

    def update_record(self, record):
        for i in range(len(self.records)):
            if self.records[i].record_id == record.record_id:
                self
