class patients():
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history):
        # Initialize the attributes of the patient object.
        # 'patient_name' stores the name of the patient.
        self.patient_name = patient_name
        # 'age' stores the age of the patient.
        self.age = age
        # 'date_of_latest_admission' stores the date of the patient's latest admission.
        self.date_of_latest_admission = date_of_latest_admission
        #'medical_history' stores the medical history information of the patient.
        self.medical_history = medical_history

    def get_patients_information(self):
        # Print the information of the patient in a formatted way.
        print(f"Patient Name: {self.patient_name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}")


# Create an instance of the 'patients' class with specific patient details.
patient_1 = patients("Wang Liwei", 18, "2025-04-01", "Has a history of hypertension")
# Call the method to display the patient's information.
patient_1.get_patients_information()