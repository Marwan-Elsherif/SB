import pytest
from src.constants.constants import GlobalConstants
from src.constants.components_types import ComponentsTypes


def test_production_greater_than_consumption(dut):
    # Set up PV production to be greater than house consumption
    dut.set(ComponentsTypes.PVPANEL.value + GlobalConstants.STR_SEPARATOR + "power", 2000)  # Example PV production in Watts
    dut.set(ComponentsTypes.HOUSE.value + GlobalConstants.STR_SEPARATOR + "power_in", 500)      # Example house consumption in Watts
    dut.set(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + "power_out", dut.grid.power_out)
    dut.set(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command', dut.sb._power_command)

    # Run the energy management algorithm
    dut.sb.controller.manage_energy()

    # Verify that the storage system charges and excess power goes to the grid
    assert dut.get(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command') > 0, "Storage should charge with surplus PV power"
    assert dut.get(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + 'power_in') >= 0, "Excess power should be sent to the grid"


def test_production_equal_to_consumption(dut):
    # Set up PV production to be equal to house consumption
    dut.set(ComponentsTypes.PVPANEL.value + GlobalConstants.STR_SEPARATOR + "power", 500)  # Example PV production in Watts
    dut.set(ComponentsTypes.HOUSE.value + GlobalConstants.STR_SEPARATOR + "power_in", 500)      # Example house consumption in Watts
    dut.set(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + "power_out", dut.grid.power_out)
    dut.set(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command', dut.sb._power_command)

    # Run the energy management algorithm
    dut.sb.controller.manage_energy()

    # Verify that neither charging nor discharging occurs, and no power flows to/from the grid
    assert dut.get(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command') == 0, "Storage should neither charge nor discharge"
    assert dut.get(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + 'power_in') == 0 and dut.get(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + 'power_out') == 0, "No power should be sent to or drawn from the grid"


def test_production_less_than_consumption(dut):
    # Set up PV production to be less than house consumption
    dut.set(ComponentsTypes.PVPANEL.value + GlobalConstants.STR_SEPARATOR + "power", 300)
    dut.set(ComponentsTypes.HOUSE.value + GlobalConstants.STR_SEPARATOR + "power_in", 500)
    dut.set(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + "power_out", dut.grid.power_out)
    dut.set(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command', dut.sb._power_command)

    # Run the energy management algorithm
    dut.sb.controller.manage_energy()

    # Verify that the storage system discharges and the grid supplies additional power if needed
    assert dut.get(ComponentsTypes.SB.value + GlobalConstants.STR_SEPARATOR + 'power_command') <= 0, "Storage should discharge to meet household demand"
    assert dut.get(ComponentsTypes.GRID.value + GlobalConstants.STR_SEPARATOR + 'power_out') > 0, "Additional power should come from the grid if storage is insufficient"
