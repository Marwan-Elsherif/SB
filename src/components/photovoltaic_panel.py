

class PVPanel:
    """
    Represents a photovoltaic (PV) panel that produces energy from the sun radiation.
    """
    
    def __init__(self, voltage: int = 100, current: int = 10, power: int = None) -> None:
        """
        Initializes the PVPanel instance with given voltage, current and power values.
        If power value is missing, it can be calculated from provided current & voltage
        
        Args:
            voltage (int): Voltage in Volts.
            current (int): Current in Amps. 
            power (int): Power in Watts. Defaults to None.
        """
        self._voltage = voltage
        self._current = current
        if power:
            self._power = power
        else:
            self._calculate_power()

    @property
    def power(self) -> int:
        """Returns the power produced by the PV panel in Watts."""
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        """Sets the power produced by the PV panel, in Watts, and recalculates current or voltage if needed."""
        if value < 0:
            raise ValueError("Power must be a positive value.")
        self._power = value

    @property
    def voltage(self) -> int:
        """Returns the voltage produced by the PV panel in Volts."""
        return self._voltage

    @voltage.setter
    def voltage(self, value: int) -> None:
        """Sets the voltage produced by the PV panel in Volts."""
        if value < 0:
            raise ValueError("Voltage must be a positive value.")
        self._voltage = value

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

    def _calculate_power(self) -> None:
        """Calculates power based on voltage and current."""
        if self._voltage is not None and self._current is not None:
            self._power = self._voltage * self._current

         