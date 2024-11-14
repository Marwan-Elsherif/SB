from enum import Enum

class ComponentsTypes(Enum):
    INVERTER = "inverter"
    BMS = "battery_module"
    GRID = "Grid"
    HOUSE = "House"
    PVPANEL = "PVPanel"
    SB = "Storage"