from src.constants.system_setup import SystemSetup
from src.constants.components_types import ComponentsTypes
from src.components.em_controller import EMController
from src.components.storage_system.inverter import Inverter
from src.components.storage_system.battery_module import BMS


class Storage():
    def __init__(self, pv_panel, grid, house, system_setup=SystemSetup.BASIC) -> None:
        self._pv_panel = pv_panel
        self._grid = grid
        self._house = house
        self._power_command = 0
        self.plan = system_setup.value['plan']
        self.max_batteries = system_setup.value['max_batteries']
        self._inverter = Inverter()
        self.controller = EMController(pv_panel, grid, house, self)
        self._batteries = [BMS() for _ in range(self.max_batteries)]
    
    @property
    def power_command(self) -> int:
        """Returns the power produced by the PV panel in Watts."""
        return self._power_command

    @power_command.setter
    def power_command(self, value: int) -> None:
        """Sets the power produced by the PV panel, in Watts, and recalculates current or voltage if needed."""
        if value < 0:
            raise ValueError("Power must be a positive value.")
        self._power_command = value


    def charge(self, power: int) -> None:
        """Command the system to charge the batteries."""
        if power > 0:
            self._power_command = min(power, self._inverter.max_power)
            for module in self._batteries:
                if self._power_command > module.max_power:
                    raise ValueError("Power command exceeds module capacity.")

    def discharge(self, power: int) -> None:
        """Command the system to discharge the batteries."""
        if power < 0:
            self._power_command = max(power, -self._inverter.max_power)
            for module in self._batteries:
                if abs(self._power_command) > module.max_power:
                    raise ValueError("Power command exceeds module capacity.")
                
    def get_component_value(self, component_name: str, attribute: str) -> int:
        """
        Retrieves the value of a specific attribute from a specified component in the storage system.
        
        Args:
            component_name (str): Name of the component ('inverter' or 'battery_module_<index>').
            attribute (str): The attribute to retrieve from the specified component.
        
        Returns:
            int: The value of the requested attribute.
        
        Raises:
            AttributeError: If the specified component or attribute does not exist.
        """
        if component_name == ComponentsTypes.INVERTER:
            return getattr(self._inverter, attribute)
        
        elif component_name.startswith(ComponentsTypes.BMS):
            # Extract the index from the component name
            index = int(component_name.split('_')[-1])
            if index < 0 or index >= len(self._batteries):
                raise ValueError("Battery module index out of range.")
            return getattr(self._batteries[index], attribute)
        
        else:
            raise ValueError("Component not found. Valid components are 'inverter' and 'battery_module_<index>'.")
        
    def manage_energy(self) -> None:
        self.controller.manage_energy()

    def reset(self):
        self._inverter = Inverter()
        self.controller = EMController(self._pv_panel, self._grid, self._house, self)
        self._batteries = [BMS() for _ in range(self.max_batteries)]





