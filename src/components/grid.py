
class Grid:
    """
    Represents the main connection from the house to the utility provider grid.
    """
    
    def __init__(self, voltage: int = 220, frequency: int = 50, power_in: int = 0, power_out: int = 0) -> None:
        """
        Initializes the Grid instance with given voltage, frequency and power values.
        
        Args:
            voltage (int): Voltage in Volts.
            current (int): Current in Amps. 
            power_in (int): Power in Watts coming from house to grid.
            power_out(int): Power in Watts feeded from grid to house. 
        """
        self._voltage = voltage
        self._frequency = frequency
        self._power_in = power_in
        self._power_out = power_out

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
    def power_in(self) -> int:
        """Returns the Power in Watts coming from house to grid"""
        return self._power_in

    @power_in.setter
    def power_in(self, value: int) -> None:
        """Sets the Power coming from house to grid"""
        if value < 0:
            raise ValueError("Power must be a positive value.")
        self._power_in = value

    @property
    def power_out(self) -> int:
        """Returns the Power in Watts feeded from grid to house"""
        return self._power_out

    @power_out.setter
    def power_out(self, value: int) -> None:
        """Sets the Power feeded from grid to house"""
        if value < 0:
            raise ValueError("Power must be a positive value.")
        self._power_out = value
