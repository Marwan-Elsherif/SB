import pytest

from src.constants.system_setup import SystemSetup
from src.constants.constants import GlobalConstants
from src.constants.components_types import ComponentsTypes

from src.components.storage_system.storage import Storage
from src.components.photovoltaic_panel import PVPanel
from src.components.house import House
from src.components.grid import Grid
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not hasattr(config.option, 'htmlpath') or not config.option.htmlpath:
        config.option.htmlpath = f"reports/report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"

# Customize the report title and content
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "SonnenBattrie Under Test"


@pytest.fixture(params=[SystemSetup.BASIC, SystemSetup.STANDARD, SystemSetup.PRO])
def dut(request):
    class DUT:
        def __init__(self, setup):
            self.setup = setup
            self.initial_state = {}
            self.pv_panel = PVPanel()
            self.grid = Grid()
            self.house = House()
            self.sb = Storage(self.pv_panel, self.grid, self.house, request.param)
            self.components_map = {
                ComponentsTypes.GRID.value: self.grid,
                ComponentsTypes.HOUSE.value: self.house,
                ComponentsTypes.PVPANEL.value: self.pv_panel,
                ComponentsTypes.SB.value: self.sb
            }

        def set(self, key: str, value) -> bool:
            """
            Sets a value for an attribute in any of the DUT components and saves the initial state
            if it's the first time setting this key.
            """
            # Parse the key to determine which component and attribute to set
            component_type, attr = key.split(GlobalConstants.STR_SEPARATOR)
            component = self.components_map.get(component_type, None)

            if component is None:
                raise AttributeError(f"{component_type} is not a valid DUT component")
            
            self.initial_state[key] = value
            setattr(component, attr, value)
            return True

        def get(self, key: str):
            """
            Gets the value of an attribute in any of the DUT components.
            """
            component_type, attr = key.split(GlobalConstants.STR_SEPARATOR)
            component = self.components_map.get(component_type, None)

            if component is None:
                raise AttributeError(f"{component_type} is not a valid DUT component")

            return getattr(component, attr, None)
            
        def reset(self):
            """
            Restores the initial state of the DUT components.
            """
            self.initial_state = {}
            self.sb.reset()

    dut = DUT(request.param)
    yield dut
    dut.reset()
    