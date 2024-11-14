from src.components.storage_system.storage import Storage
from src.components.photovoltaic_panel import PVPanel
from src.components.house import House
from src.components.grid import Grid

from src.constants.components_types import ComponentsTypes


def main():
    pv_panel = PVPanel(100, 10)
    grid = Grid(220, 50, 1000, 1000)
    house = House()
    sb = Storage(pv_panel, grid, house)
    print(sb.get_component_value(ComponentsTypes.INVERTER, "battery_voltage"))


if __name__ == "__main__":
    main()
