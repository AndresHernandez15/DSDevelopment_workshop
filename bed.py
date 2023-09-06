class Bed:
    """
    Class used to represent a hospital bed.
    """

    def __init__(self, number: int):
        """ Bed constructor object.

        :param number: The number of the bed.
        :type number: int
        """
        self._number = number
        self._service = None
        self._occupied = False
        self._clinical_history = None

    def admit_patient(self, clinical_history, service: str):
        """ Admit a patient to the bed.

        :param clinical_history: The clinical history object of the patient.
        :type clinical_history: ClinicalHistory
        :param service: The medical service to which the patient is admitted.
        :type service: str
        :raises BedOccupiedError: If the bed is already occupied.
        """
        if not self._occupied:
            self._occupied = True
            self._clinical_history = clinical_history
            self._service = service
        else:
            raise BedOccupiedError(f"The bed {self._number} is already occupied")

    def release_patient(self):
        """ Release the patient from the bed.

        :raises BedEmptyError: If the bed is already empty.
        """
        if self._occupied:
            self._occupied = False
            self._clinical_history = None
        else:
            raise BedEmptyError(f"The bed {self._number} is already empty")

    @property
    def number(self) -> int:
        """ Get the bed number.

        :returns: The bed number.
        :rtype: int
        """
        return self._number

    @property
    def service(self) -> str:
        """ Get the medical service associated with the bed.

        :returns: The name of the medical service.
        :rtype: str
        """
        return self._service

    @property
    def occupied(self) -> bool:
        """ Check if the bed is occupied by a patient.

        :returns: True if the bed is occupied, False otherwise.
        :rtype: bool
        """
        return self._occupied

    @property
    def clinical_history(self):
        """ Get the clinical history of the patient in the bed.

        :returns: The clinical history object.
        :rtype: ClinicalHistory
        """
        return self._clinical_history

    def __str__(self):
        """ Returns a string representation of the bed.

        :returns: String representation of the bed.
        :rtype: str
        """
        status = "Occupied" if self._occupied else "Vacant"
        return f"Bed {self._number} - Medical Service: {self._service} - Status: {status}"


class BedOccupiedError(Exception):
    """Exception raised when trying to admit a patient to an occupied bed."""
    pass


class BedEmptyError(Exception):
    """Exception raised when trying to release a patient from an empty bed."""
    pass


if __name__ == "__main__":
    from patient import Patient
    from vital_signs import VitalSigns
    from clinical_history import ClinicalHistory
    from datetime import datetime

    patient = Patient("1234", "Andres", "F", datetime.strptime("2004-05-15", "%Y-%m-%d"))
    vital_signs = VitalSigns(120, 37, 80, 80)
    admission_date = datetime.strptime("2023-10-15 02:40", "%Y-%m-%d %H:%M")
    ClinicalHistoryTest = ClinicalHistory(patient, vital_signs, "General Medicine", admission_date)
    bed = Bed(0)

    bed.admit_patient(ClinicalHistoryTest, "General Medicine")

    print(bed.__str__())

    bed.release_patient()

    print(bed.__str__())
