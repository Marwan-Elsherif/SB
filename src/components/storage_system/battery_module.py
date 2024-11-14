class BMS:
    """
    Represents each of the battery packs that can be connected into a sonnenBatterie storage system.
    """
    
    def __init__(self, temperature: int = 60, voltage: int = 50, max_power: int = 2500) -> None:
        """
        Initializes the BatteryModule instance with temperature, voltage, and max power.
        
        Args:
            temperature (int): Module temperature in Celsius degrees.
            voltage (int): Module voltage in Volts.
            max_power (int): Maximum power that the module can charge or discharge in Watts.
        """
        self._temperature = temperature
        self._voltage = voltage
        self._max_power = max_power

    @property
    def temperature(self) -> int:
        """Gets the temperature of the battery module in Celsius degrees."""
        return self._temperature

    @temperature.setter
    def temperature(self, value: int) -> None:
        """Sets the temperature of the battery module in Celsius degrees, must be within a realistic range."""
        if value < -40 or value > 100:  # Assuming an operational range for safety
            raise ValueError("Temperature must be between -40 and 100 Celsius degrees.")
        self._temperature = value

    @property
    def voltage(self) -> int:
        """Gets the voltage of the battery module in Volts."""
        return self._voltage

    @voltage.setter
    def voltage(self, value: int) -> None:
        """Sets the voltage of the battery module in Volts, must be a positive integer."""
        if value < 0:
            raise ValueError("Voltage must be a positive value.")
        self._voltage = value

    @property
    def max_power(self) -> int:
        """Gets the maximum power the battery module can charge or discharge in Watts."""
        return self._max_power

    @max_power.setter
    def max_power(self, value: int) -> None:
        """Sets the maximum power of the battery module in Watts, must be a positive integer."""
        if value < 0:
            raise ValueError("Max power must be a positive value.")
        self._max_power = value
