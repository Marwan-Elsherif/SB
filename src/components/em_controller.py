class EMController:
    """
    Handles the energy logic and issues commands to each device in the system.
    """

    def __init__(self, pv_panel, grid, house, storage) -> None:
        self._pv_panel = pv_panel
        self._grid = grid
        self._house = house
        self._storage = storage

    def manage_energy(self) -> None:
        """Manages energy flow based on PV production and household consumption."""
        if self._pv_panel.power > self._house.power_in:
            surplus = self._pv_panel.power - self._house.power_in
            self._storage.charge(surplus)
            self._grid._power_in += surplus - self._storage._power_command
        else:
            # If house consumption exceeds PV production
            deficit = self._house.power_in - self._pv_panel.power
            # Check if storage can cover the deficit
            if abs(self._storage._power_command) >= deficit:
                # Storage can fully cover the deficit
                self._storage.discharge(-deficit)
            else:
                # Storage can partially cover the deficit
                available_from_storage = abs(self._storage._power_command)
                self._storage.discharge(-available_from_storage)
                # Get the remaining deficit from the grid
                remaining_deficit = deficit - available_from_storage
                self._grid._power_out += remaining_deficit