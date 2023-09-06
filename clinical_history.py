from datetime import datetime


class ClinicalHistory:
    """
    Class used to represent a patient's clinical history.
    """

    def __init__(self, patient_obj: object, vital_signs_obj: object, service: str = "",
                 admission: datetime = datetime(1900, 1, 1, 00, 00),
                 discharge_date: datetime = None, chronic_disease: bool = False):
        """ ClinicalHistory constructor object

        :param patient_obj: An object with the patient's information.
        :type patient_obj: object.
        :param vital_signs_obj: An object with the vital signs of the patient.
        :type vital_signs_obj: object
        :param service: The name of the medical service.
        :type service: str
        :param admission: The date of patient admission.
        :type admission: datetime
        :param discharge_date: The date of patient discharge (optional).
        :type discharge_date: datetime
        :param chronic_disease: A boolean indicating whether the patient has any chronic disease or not.
        :type chronic_disease: bool
        :returns: A ClinicalHistory object.
        :rtype: object
        """
        self._patient = patient_obj
        self._vital_signs = vital_signs_obj
        self._service = service
        self._admission_date = admission
        self._discharge_date = discharge_date
        self._chronic_disease = chronic_disease
        self._evolution_notes = []
        self._diagnostic_images = []
        self._exam_results = []
        self._medicines = []

    def add_evolution_note(self, note: str):
        """ Add an evolution note to the clinical history.

        :param note: The evolution note to add.
        :type note: str
        """
        self._evolution_notes.append(note)

    def add_diagnostic_image(self, image: str):
        """ Add a diagnostic image to the clinical history.

        :param image: The diagnostic image to add.
        :type image: str
        """
        self._diagnostic_images.append(image)

    def add_exam_results(self, results: str):
        """ Add exam results to the clinical history.

        :param results: The exam results to add.
        :type results: str
        """
        self._exam_results.append(results)

    def add_medicine(self, medicine: str):
        """ Add a medicine to the clinical history.

        :param medicine: The medicine to add.
        :type medicine: str
        """
        self._medicines.append(medicine)

    @property
    def medicines(self) -> list:
        """ Get the list of medicines in the clinical history.

        :returns: The list of medicines.
        :rtype: list[str]
        """
        return self._medicines

    @property
    def patient(self):
        """ Get the patient information associated with the clinical history.

        :returns: The patient object.
        :rtype: Patient
        """
        return self._patient

    @property
    def vital_signs(self):
        """ Get the vital signs of the patient in the clinical history.

        :returns: The vital signs object.
        :rtype: VitalSigns
        """
        return self._vital_signs

    @property
    def service(self) -> str:
        """ Get the name of the medical service in the clinical history.

        :returns: The name of the medical service.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service: str):
        """ Set the name of the medical service in the clinical history.

        :param service: The new name of the medical service.
        :type service: str
        """
        self._service = service

    @property
    def admission_date(self) -> datetime:
        """ Get the date of patient admission in the clinical history.

        :returns: The date of patient admission.
        :rtype: datetime
        """
        return self._admission_date

    @admission_date.setter
    def admission_date(self, admission: datetime):
        """ Set the date of patient admission in the clinical history.

        :param admission: The new date of patient admission.
        :type admission: datetime
        :raises ValueError: If the input is not a valid datetime.
        """
        if isinstance(admission, datetime):
            self._admission_date = admission
        else:
            raise ValueError("Invalid admission date")

    @property
    def discharge_date(self) -> datetime:
        """ Get the date of patient discharge in the clinical history.

        :returns: The date of patient discharge.
        :rtype: datetime
        """
        return self._discharge_date

    @discharge_date.setter
    def discharge_date(self, discharge_date: datetime):
        """ Set the date of patient discharge in the clinical history.

        :param discharge_date: The new date of patient discharge.
        :type discharge_date: datetime
        :raises ValueError: If the input is not a valid datetime.
        """
        if isinstance(discharge_date, datetime):
            self._discharge_date = discharge_date
        else:
            raise ValueError("Invalid discharge date")

    @property
    def chronic_disease(self) -> bool:
        """ Get whether the patient has a chronic disease in the clinical history.

        :returns: True if the patient has a chronic disease, False otherwise.
        :rtype: bool
        """
        return self._chronic_disease

    @chronic_disease.setter
    def chronic_disease(self, disease: bool):
        """ Set whether the patient has a chronic disease in the clinical history.

        :param disease: True if the patient has a chronic disease, False otherwise.
        :type disease: bool
        """
        self._chronic_disease = disease

    def __str__(self) -> str:
        """ Returns str of patient
        :returns: string patient
        :rtype: str
        """
        history_str = f"Admission Date: {self._admission_date.strftime('%Y-%m-%d %H:%M')}\n"
        if self._discharge_date:
            history_str += f"Discharge Date: {self._discharge_date.strftime('%Y-%m-%d %H:%M')}\n"
        history_str += f"{str(self._patient)}\n{str(self._vital_signs)}\n"
        history_str += "Evolution Notes:\n"
        history_str += "\n".join(f"- {note}" for note in self._evolution_notes) + "\n"
        history_str += "Diagnostic Images:\n"
        history_str += "\n".join(f"- {img}" for img in self._diagnostic_images) + "\n"
        history_str += "Exam Results:\n"
        history_str += "\n".join(f"- {result}" for result in self._exam_results) + "\n"
        history_str += "Medications:\n"
        history_str += "\n".join(f"- {med}" for med in self._medicines) + "\n"
        return history_str


if __name__ == "__main__":
    from patient import Patient
    from vital_signs import VitalSigns
    patient = Patient("1234", "Andres", "F", datetime.strptime("2004-05-15", "%Y-%m-%d"))
    vital_signs = VitalSigns(120, 37, 80, 80)
    admission_date = datetime.strptime("2023-10-15 02:40", "%Y-%m-%d %H:%M")
    ClinicalHistoryTest = ClinicalHistory(patient, vital_signs, "General Medicine", admission_date)

    print(ClinicalHistoryTest.__str__())

    ClinicalHistoryTest.add_medicine("Paracetamol 500mg")
    ClinicalHistoryTest.add_diagnostic_image("Radiography.png")
    ClinicalHistoryTest.add_evolution_note("The patient is getting better")
    ClinicalHistoryTest.add_exam_results("Hemoglobin.pdf")
    ClinicalHistoryTest.add_medicine("Lisinopril")

    print(ClinicalHistoryTest.__str__())
