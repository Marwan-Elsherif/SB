class Inverter:
    """
    Represents a device inside the sonnenBattery in charge of controlling the power flow to the batteries.
    """
    
    def __init__(self, battery_voltage: int = 100, battery_current: int = 10, grid_voltage: int = 220, 
                 grid_frequency: int = 50, working_power: int = 1000, max_power: int = 2500) -> None:
        """
        Initializes the Inverter instance with battery voltage, current, grid voltage, frequency, working power, and max power.
        
        Args:
            battery_voltage (int): Battery voltage in Volts.
            battery_current (int): Battery current in Amps.
            grid_voltage (int): Grid voltage in Volts.
            grid_frequency (int): Grid frequency in Hertz.
            working_power (int): Current working power in Watts.
            max_power (int): Maximum power the inverter can handle in Watts.
        """
        self._battery_voltage = battery_voltage
        self._battery_current = battery_current
        self._grid_voltage = grid_voltage
        self._grid_frequency = grid_frequency
        self._working_power = working_power
        self._max_power = max_power

    @property
    def battery_voltage(self) -> int:
        """Gets the battery voltage in Volts."""
        return self._battery_voltage

    @battery_voltage.setter
    def battery_voltage(self, value: int) -> None:
        """Sets the battery voltage in Volts, must be a positive integer."""
        if value < 0:
            raise ValueError("Battery voltage must be a positive value.")
        self._battery_voltage = value

    @property
    def battery_current(self) -> int:
        """Gets the battery current in Amps."""
        return self._battery_current

    @battery_current.setter
    def battery_current(self, value: int) -> None:
        """Sets the battery current in Amps, must be a positive integer."""
        if value < 0:
            raise ValueError("Battery current must be a positive value.")
        self._battery_current = value

    @property
    def grid_voltage(self) -> int:
        """Gets the grid voltage sensed by the inverter in Volts."""
        return self._grid_voltage

    @grid_voltage.setter
    def grid_voltage(self, value: int) -> None:
        """Sets the grid voltage in Volts, must be a positive integer."""
        if value < 0:
            raise ValueError("Grid voltage must be a positive value.")
        self._grid_voltage = value

    @property
    def grid_frequency(self) -> int:
        """Gets the grid frequency sensed by the inverter in Hertz."""
        return self._grid_frequency

    @grid_frequency.setter
    def grid_frequency(self, value: int) -> None:
        """Sets the grid frequency in Hertz, must be a positive integer."""
        if value < 0:
            raise ValueError("Grid frequency must be a positive value.")
        self._grid_frequency = value

    @property
    def working_power(self) -> int:
        """Gets the current power being transferred to/from the battery in Watts."""
        return self._working_power

    @working_power.setter
    def working_power(self, value: int) -> None:
        """Sets the working power in Watts, can be positive (charging) or negative (discharging)."""
        if abs(value) > self._max_power:
            raise ValueError("Working power cannot exceed maximum power limit.")
        self._working_power = value

    @property
    def max_power(self) -> int:
        """Gets the maximum power the inverter can handle in Watts."""
        return self._max_power

    @max_power.setter
    def max_power(self, value: int) -> None:
        """Sets the maximum power the inverter can handle in Watts, must be a positive integer."""
        if value < 0:
            raise ValueError("Max power must be a positive value.")
        self._max_power = value
