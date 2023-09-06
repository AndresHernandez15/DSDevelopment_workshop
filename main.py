from datetime import datetime
from patient import Patient
from vital_signs import VitalSigns
from bed import Bed
from clinical_history import ClinicalHistory
from report import Report

""" List of available medical services """
medical_services_available = ("Internal Medicine", "General Surgery", "Pediatrics", "Cardiology", "Neurology",
                              "Psychiatry", "Radiology", "Rehabilitation")

""" List to create 300 beds """
beds = [Bed(n) for n in range(1, 301)]

print("\n\t\tHospital San Vicente´s System")

while True:
    print("\n\tMain Menu")
    print("1. Admit Patient")
    print("2. Add To Clinical History")
    print("3. Discharge Patient")
    print("4. Generate Report")
    print("5. Exit")

    op = input("Enter The Option: ")

    if op == "1":
        print("\nEnter The Patient Information")
        patient_id = input("ID: ")
        name = input("Name: ")
        gender = input("Gender (M/F): ")
        birth_date = input("Birth Date (YYYY-MM-DD): ")

        print("\nEnter the Patient Vital Signs")
        blood_pressure = float(input("Blood Pressure (mmHg): "))
        temperature = float(input("Temperature (°C): "))
        o2_saturation = float(input("Oxygen saturation (%): "))
        respiratory_rate = float(input("Respiratory rate (bpm): "))

        admission_date_str = input("Admission date (YYYY-MM-DD HH:mm): ")

        patient = Patient(patient_id, name, gender, datetime.strptime(birth_date, "%Y-%m-%d"))
        vital_signs = VitalSigns(blood_pressure, temperature, o2_saturation, respiratory_rate)
        admission_date = datetime.strptime(admission_date_str, "%Y-%m-%d %H:%M")

        """ Validate medical service """
        while True:
            service = input("Medic Service: ")
            if service not in medical_services_available:
                print("Non existent service, services available: ", medical_services_available)
                continue
            else:
                break

        clinical_history = ClinicalHistory(patient, vital_signs, service, admission_date)

        """ Find an available bed to admit the patient """
        available_bed = None
        for bed in beds:
            if not bed.occupied:
                available_bed = bed
                break

        if available_bed:
            available_bed.admit_patient(clinical_history, service)
            print(f"Patient {patient.name} admitted in bed {available_bed.number}")
        else:
            print("No bed available")

    elif op == "2":
        n_bed = int(input("Number of bed of patient to actualize: "))
        bed = beds[n_bed - 1]

        if bed.occupied:
            while True:
                print("\n\tClinical History Menu")
                print("1. Add Chronic Disease")
                print("2. Add Evolution Note")
                print("3. Attach Diagnostic Image")
                print("4. Add Exam Results")
                print("5. Add Medicines")
                print("6. Done")

                sub_op = input("Enter The Option: ")

                if sub_op == "1":
                    while True:
                        chronic_disease = input("Does the patient has a chronic disease? (Y/N): ")
                        if chronic_disease == "Y":
                            bed.clinical_history.chronic_disease = True
                            break
                        elif chronic_disease == "N":
                            bed.clinical_history.chronic_disease = False
                            break
                        else:
                            print("\nPlease enter Y or N")

                elif sub_op == "2":
                    note = input("Write the evolution note: ")
                    bed.clinical_history.add_evolution_note(note)

                elif sub_op == "3":
                    img = input("Paste the image route: ")
                    bed.clinical_history.add_diagnostic_image(img)

                elif sub_op == "4":
                    result = input("Enter the exam result: ")
                    bed.clinical_history.add_exam_results(result)

                elif sub_op == "5":
                    meds = input("Enter Prescription: ")
                    bed.clinical_history.add_medicine(meds)

                elif sub_op == "6":
                    print("Saving...")
                    break

                else:
                    print("Invalid option, please select numbers from 1 - 6")

        else:
            print(f"The bed {bed.number} is not occupied")

    elif op == "3":
        n_bed = int(input("Number of bed of patient to discharge: "))
        bed = beds[n_bed - 1]

        if bed.occupied:
            discharge_date_str = input("Discharge date (YYYY-MM-DD HH:mm): ")
            discharge_date = datetime.strptime(discharge_date_str, '%Y-%m-%d %H:%M')

            bed.clinical_history.discharge_date = discharge_date

            bed.release_patient()
            print(f"Patient Discharged from Bed {bed.number}")

        else:
            print(f"The bed {bed.number} is not occupied")

    elif op == "4":
        clinical_histories = [bed.clinical_history for bed in beds if bed.occupied]

        if not clinical_histories:
            print("No occupied beds to generate a report.")
        else:
            total_beds = len(beds)
            occupied_beds = sum(1 for bed in beds if bed.occupied)
            occupied_beds_per_service = {}

            for bed in beds:
                if bed.occupied:
                    service = bed.service
                    if service in occupied_beds_per_service:
                        occupied_beds_per_service[service] += 1
                    else:
                        occupied_beds_per_service[service] = 1

            admissions, discharges = Report.admissions_and_discharges_per_service(clinical_histories)
            occupation_rate = Report.occupancy_rate(total_beds, occupied_beds)
            average_stay = Report.avg_stay_per_service(clinical_histories)
            chronic_patients = Report.patients_with_chronic_diseases(clinical_histories)
            medicines = Report.meds_per_service(clinical_histories)

            print("\nAdmissions Per Service: ", admissions)
            print("Discharges Per Service: ", discharges)
            print(f"Hospital Occupancy Rate: {occupation_rate} %")
            print("Average Length Of Stay By Service: ", average_stay)
            print("Patients With Chronic Diseases: ", chronic_patients)
            print("Prescription Of Medications By Service: ", medicines)

    elif op == "5":
        confirm_exit = input("Are you sure you want to exit? (Y/N): ")
        if confirm_exit.upper() == "Y":
            print("\n\n\t\tHave a great day :)\n\n")
            break

    else:
        print("Invalid option, please select numbers from 1 - 5")
