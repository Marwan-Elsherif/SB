

class House():
    """
    Represents a measurement point of all house connected load.
    """
    def __init__(self, voltage: int = 220, current: int = 60, frequency: int = 50, power_in: int = None) -> None:
        self._voltage = voltage
        self._current = current
        self._frequency = frequency
        self._power_in = power_in

    @property
    def voltage(self) -> int:
        """Returns the voltage produced by the PV panel in Volts."""
        return self._voltage

    @voltage.setter
    def voltage(self, value: int) -> None:
        """Sets the voltage produced by the PV panel, in Volts, and recalculates power or current if needed."""
        if value < 0:
            raise ValueError("Voltage must be a positive value.")
        self._voltage = value

    @property
    def frequency(self) -> int:
        """Returns the frequency produced by the PV panel in Hertz."""
        return self._frequency

    @frequency.setter
    def frequency(self, value: int) -> None:
        """Sets the frequency of the grid in Hertz."""
        if value < 0:
            raise ValueError("Frequency must be a positive value.")
        self._frequency = value

    @property
    def current(self) -> int:
        """Returns the current produced by the PV panel in Amps."""
        return self._current

    @current.setter
    def current(self, value: int) -> None:
        """Sets the current produced by the PV panel in Amps."""
        if value < 0:
            raise ValueError("Current must be a positive value.")
        self._current = value

    @property
    def power_in(self) -> int:
        """Returns the Power in Watts coming to house"""
        return self._power_in

    @power_in.setter
    def power_in(self, value: int) -> None:
        """Sets the Power coming to house"""
        if value < 0:
            raise ValueError("Power must be a positive value.")
        self._power_in = value
