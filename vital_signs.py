class VitalSigns:
    """
    Class used to represent the vital signs of a patient
    """
    def __init__(self, blood_pressure: float = 0.0, temperature: float = 0.0, oxygen_saturation: float = 0.0,
                 breathing_rate: float = 0.0):
        """ VitalSigns constructor object.

        :param blood_pressure: blood pressure in mmHg.
        :type blood_pressure: float
        :param temperature: temperature in Celsius.
        :type temperature: float
        :param oxygen_saturation: oxygen saturation.
        :type oxygen_saturation: float
        :param breathing_rate: breathing rate.
        :type breathing_rate: float
        :returns: VitalSigns object.
        :rtype: object
        """
        self._blood_pressure = blood_pressure
        self._temperature = temperature
        self._oxygen_saturation = oxygen_saturation
        self._breathing_rate = breathing_rate

    @property
    def blood_pressure(self) -> float:
        """ Returns the blood pressure in mmHg.
        :returns: blood pressure in mmHg
        :rtype: float
        """
        return self._blood_pressure

    @blood_pressure.setter
    def blood_pressure(self, blood_pressure: float):
        """ Set the blood pressure in mmHg.
        :param blood_pressure: blood pressure in mmHg
        :type blood_pressure: float
        """
        if blood_pressure >= 0:
            self._blood_pressure = blood_pressure

    @property
    def temperature(self) -> float:
        """ Returns the temperature in Celsius.
        :returns: temperature in Celsius
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: float):
        """ Set the temperature in Celsius.
        :param temperature: temperature in Celsius
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def oxygen_saturation(self) -> float:
        """ Returns the oxygen saturation.
        :returns: oxygen saturation
        :rtype: float
        """
        return self._oxygen_saturation

    @oxygen_saturation.setter
    def oxygen_saturation(self, oxygen_saturation: float):
        """ Set the oxygen saturation.
        :param oxygen_saturation: oxygen saturation
        :type oxygen_saturation: float
        """
        if 0 <= oxygen_saturation <= 100:
            self._oxygen_saturation = oxygen_saturation

    @property
    def breathing_rate(self) -> float:
        """ Returns the breathing rate.
        :returns: breathing rate
        :rtype: float
        """
        return self._breathing_rate

    @breathing_rate.setter
    def breathing_rate(self, breathing_rate: float):
        """ Set the breathing rate.
        :param breathing_rate: breathing rate
        :type breathing_rate: float
        """
        if breathing_rate >= 0:
            self._breathing_rate = breathing_rate

    def __str__(self):
        """ Returns str of vital signs
        :returns: string vital signs
        :rtype: str
        """
        return (f"Blood Pressure: {self._blood_pressure} mmHg\n"
                f"Temperature: {self._temperature} °C\n"
                f"Oxygen Saturation: {self._oxygen_saturation}%\n"
                f"Breathing Rate: {self._breathing_rate} bpm")


if __name__ == "__main__":
    vital_signs = VitalSigns(120, 37, 80, 80)
    print(vital_signs.__str__())
