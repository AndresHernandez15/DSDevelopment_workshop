from datetime import timedelta


class Report:
    """
    Class containing methods to generate various reports related to clinical histories.
    """
    @staticmethod
    def occupancy_rate(total_beds: int, occupied_beds: int) -> float:
        """ Calculate the occupancy rate of hospital beds.

        :param total_beds: The total number of beds in the hospital.
        :type total_beds: int
        :param occupied_beds: The number of beds currently occupied.
        :type occupied_beds: int
        :returns: The occupancy rate as a percentage.
        :rtype: float
        """
        if total_beds <= 0:
            return 0.0
        return (occupied_beds / total_beds) * 100.0

    @staticmethod
    def avg_stay_per_service(histories) -> dict:
        """ Calculate the average length of stay for patients in each medical service.

        :param histories: A list of clinical histories.
        :type histories: list
        :returns: A dictionary mapping medical services to their average length of stay.
        :rtype: dict[str, str]
        """
        avg_stay_per_service = {}
        n_patients = {}

        for history in histories:
            if history.discharge_date and history.service:
                service = history.service
                length_of_stay = history.discharge_date - history.admission_date

                if service in avg_stay_per_service:
                    avg_stay_per_service[service] += length_of_stay
                    n_patients[service] += 1
                else:
                    avg_stay_per_service[service] = length_of_stay
                    n_patients[service] = 1

        for service in avg_stay_per_service:
            avg_stay_per_service[service] = str(timedelta(seconds=avg_stay_per_service[service].total_seconds() / n_patients[service]))

        return avg_stay_per_service

    @staticmethod
    def admissions_and_discharges_per_service(histories) -> tuple:
        """ Count the number of admissions and discharges per medical service.

        :param histories: A list of clinical histories.
        :type histories: list
        :returns: Two dictionaries - one for admissions and one for discharges - mapping medical services to counts.
        :rtype: tuple[dict[str, int], dict[str, int]]
        """
        admissions_per_service = {}
        discharges_per_service = {}

        for clinical_history in histories:
            service = clinical_history.service

            if clinical_history.discharge_date is None:
                admissions_per_service[service] = admissions_per_service.get(service, 0) + 1
            else:
                discharges_per_service[service] = discharges_per_service.get(service, 0) + 1

        return admissions_per_service, discharges_per_service

    @staticmethod
    def patients_with_chronic_diseases(histories) -> set:
        """ Identify patients with chronic diseases.

        :param histories: A list of clinical histories.
        :type histories: list
        :returns: A set containing the names of patients with chronic diseases.
        :rtype: set
        """
        chronic_patients = set()
        for clinical_history in histories:
            if clinical_history.chronic_disease:
                chronic_patients.add(clinical_history.patient.name)
        return chronic_patients

    @staticmethod
    def meds_per_service(histories) -> dict:
        """ Count the number of medicines prescribed per medical service.

        :param histories: A list of clinical histories.
        :type histories: list
        :returns: A dictionary mapping medical services to lists of prescribed medicines.
        :rtype: dict[str, list]
        """
        medicines_per_service = {}
        for clinical_history in histories:
            service = clinical_history.service
            medicines = clinical_history.medicines
            if service:
                if service not in medicines_per_service:
                    medicines_per_service[service] = []
                medicines_per_service[service].extend(medicines)
        return medicines_per_service


if __name__ == '__main__':
    from patient import Patient
    from vital_signs import VitalSigns
    from clinical_history import ClinicalHistory
    from datetime import datetime

    patient = Patient("patient_id", "name", "gender", datetime.strptime("2001-12-05", "%Y-%m-%d"))
    vital_signs = VitalSigns(3, 2, 55, 13)
    admission_date = datetime.strptime("2023-10-15 02:21", "%Y-%m-%d %H:%M")
    clinical_histories = [ClinicalHistory(patient, vital_signs, "General Medicine", admission_date)]

    a = Report.patients_with_chronic_diseases(clinical_histories)

    print(a)
