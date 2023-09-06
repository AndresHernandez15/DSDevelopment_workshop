from datetime import datetime


class Patient:
    """
    Class used to represent a Patient information
    """
    def __init__(self, patient_id: str = "", name: str = "", gender: str = "",
                 birth_date: datetime = datetime(1900, 1, 1)):
        """ Patient Constructor Object.

        :param patient_id: The id of the patient.
        :type patient_id: str
        :param name: The name of the patient.
        :type name: str
        :param gender: The gender of the patient.
        :type gender: str
        :param birth_date: The birthdate of the patient.
        :type birth_date: datetime
        :returns: A patient object.
        :rtype: object
        """
        self._id = patient_id
        self._name = name
        self._gender = gender
        self._birth_date = birth_date

    @property
    def id(self) -> str:
        """ Get the unique identifier for the patient.

        :returns: The patient's unique identifier.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, patient_id: str):
        """ Set the unique identifier for the patient.

        :param patient_id: The new unique identifier for the patient.
        :type patient_id: str
        """
        self._id = patient_id

    @property
    def name(self) -> str:
        """ Get the name of the patient.

        :returns: The name of the patient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ Set the name of the patient.

        :param name: The new name for the patient.
        :type name: str
        """
        self._name = name

    @property
    def gender(self) -> str:
        """ Get the gender of the patient.

        :returns: The gender of the patient.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """ Set the gender of the patient.

        :param gender: The new gender for the patient.
        :type gender: str
        """
        self._gender = gender

    @property
    def birth_date(self) -> datetime:
        """ Get the date of birth of the patient.

        :returns: The date of birth of the patient.
        :rtype: datetime
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: datetime):
        """ Set the date of birth of the patient.

        :param birth_date: The new date of birth for the patient.
        :type birth_date: datetime
        """
        self._birth_date = birth_date

    def __str__(self):
        """ Returns str of patient
        :returns: string patient
        :rtype: str
        """
        return (f"ID: {self._id}\nName: {self._name}\nGender: {self._gender}\n"
                f"Birth Date: {self._birth_date.strftime('%Y-%m-%d')}")


if __name__ == '__main__':
    patient = Patient("1234", "Andres", "F", datetime.strptime("2004-05-15", "%Y-%m-%d"))
    print(patient.__str__())
