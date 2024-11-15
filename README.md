# SB Test Automation Framework

## Introduction

The **sonnenBatterie (SB)** is a market-leading battery storage system in Europe, designed to optimize energy usage in households. It integrates three main components:
- **Inverter**: Controls power flow to/from batteries.
- **Battery Modules**: Store and discharge energy.
- **Controller**: Manages energy logic and executes commands.

The SB system supports three setups:
1. **Basic**: 1 inverter, up to 2 battery modules, 1 controller.
2. **Standard**: 1 inverter, up to 3 battery modules, 1 controller.
3. **Pro**: 1 inverter, up to 5 battery modules, 1 controller.

The SB operates by managing energy between photovoltaic (PV) panels, the grid, and household consumption:
- **Surplus Production**: Charges the storage system first, and sends remaining power to the grid.
- **Energy Deficit**: Supplies power from the storage system, with the grid as a backup.

This framework aims to test the energy management algorithm using pytest, ensuring accurate simulation of the SB system's behavior under different setups.

## Goals

1. **Test Automation**:
   - Implement a pytest test case to validate the SB energy algorithm across all setups (Basic, Standard, Pro).
   - Use a DUT fixture with `set` and `get` methods to mock readings and ensure state restoration after each test.

2. **Additional Features**:
   - Implement a Python generator for the Fibonacci sequence --> `fibonacci.py`
   - Evaluate the benefits of pytest fixtures over setup/teardown methods. --> `pytest_fixtures.md`
   - Explore the integration of Machine Learning in hardware-dependent test frameworks. --> `ml_hw.md`


## Setup and Execution

**Clone the Repository**

    git clone https://github.com/Marwan-Elsherif/SB.git
    cd SB
**Install Requirements**

    pip install -r requirements.txt
  **Run Tests** 

    pytest tests\test_dut.py
**View Reports**

 - HTML reports are automatically generated in the `reports/` directory.
 - It is in the format of `report_<time_stamp>.html`
