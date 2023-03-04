import random
import uuid
import users
from datetime import datetime
import time


class Simulator:
    def calculate_rank(self, patient, curr_record):
        # NEWS Dictionaries
        resp_dict = {
            range(0, 8): 3,
            range(9, 11): 1,
            range(12, 20): 0,
            range(21, 24): 2,
            range(25, 100): 3,
        }

        bp_dict = {
            range(0, 90): 3,
            range(91, 100): 2,
            range(101, 110): 1,
            range(111, 219): 0,
            range(220, 300): 3,
        }
        hr_dict = {
            range(0, 40): 3,
            range(41, 50): 1,
            range(51, 90): 0,
            range(91, 110): 1,
            range(111, 130): 2,
            range(131, 300): 3,
        }
        supplimental_dict = {"yes": 1, "no": 0}

        # News Rank Function
        def get_oxy(oxy):
            if oxy <= 91:
                return 3
            elif oxy >= 91.1 and oxy <= 93:
                return 2
            elif oxy >= 93.1 and oxy <= 95:
                return 1
            else:
                return 0

        def get_temp(temp):
            if temp <= 35:
                return 3
            elif temp >= 35.1 and temp <= 36:
                return 1
            elif temp >= 36.1 and temp <= 38:
                return 0
            elif temp >= 38.1 and temp <= 39:
                return 1
            else:
                return 2

        # Calculate News Score
        news_score = 0

        for key in resp_dict:
            if curr_record.respiratory_rate in key:
                print("Resp", resp_dict[key])
                news_score += resp_dict[key]

        for key in bp_dict:
            if curr_record.blood_pressure in key:
                print("BP", bp_dict[key])
                news_score += bp_dict[key]

        for key in hr_dict:
            if curr_record.hart_rate in key:
                print("HR", hr_dict[key])
                news_score += hr_dict[key]

        # for key in supplimental_dict:
        #     if curr_record.supplimental_oxygen in key:
        #         print(supplimental_dict[key])
        #         news_score += supplimental_dict[key]

        news_score += get_temp(curr_record.temperature)
        news_score += get_oxy(curr_record.oxygen_saturation)

        # Calculate Rank
        rank = patient.ctas + news_score

        return rank

    def generate_new_record(self, patient, curr_record):
        new_resp = curr_record.respiratory_rate + (
            curr_record.respiratory_rate * random.uniform(-0.1, 0.1)
        )
        new_oxy = curr_record.oxygen_saturation + (
            curr_record.oxygen_saturation * random.uniform(-0.1, 0.1)
        )
        new_temp = curr_record.temperature + (
            curr_record.temperature * random.uniform(-0.1, 0.1)
        )
        new_bp = curr_record.blood_pressure + (
            curr_record.blood_pressure * random.uniform(-0.1, 0.1)
        )
        new_hr = curr_record.hart_rate + (
            curr_record.hart_rate * random.uniform(-0.1, 0.1)
        )

        return users.Record(
            str(uuid.uuid4()),
            patient.patient_id,
            datetime.now(),
            new_hr,
            new_bp,
            new_temp,
            new_oxy,
            new_resp,
        )

    def simulate(self):
        while True:
            # We need patients and thier records here
            patient_list = users.PatientList()
            for patient in patient_list.patients:
                if patient.records:
                    curr_patient_record = patient.records[-1]
                    if len(patient.records) > 1:
                        # Generate new record
                        new_record = self.generate_new_record(
                            patient, curr_patient_record
                        )
                        # Calculate rank
                        patient.rank = self.calculate_rank(patient, new_record)
                        # Add Record
                        patient_list.add_record(new_record)
                        # Update Patient
                        patient_list.update_patient(patient)
                    else:
                        # Calculate rank
                        patient.rank = self.calculate_rank(patient, new_record)
                        # Update Patient
                        patient_list.update_patient(patient)
            time.sleep(10)
