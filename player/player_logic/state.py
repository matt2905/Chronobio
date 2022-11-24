from dataclasses import dataclass
from typing import Any, Dict, Optional
from .farm import Farm


@dataclass
class State:
    _my_farm: Farm
    _username: str
    _day: int = 0
    _is_busy: int = 0

    @property
    def is_busy(self) -> int:
        return self._is_busy

    @is_busy.setter
    def is_busy(self, busy: int) -> None:
        self._is_busy = busy
        if self._is_busy < 0:
            self._is_busy = 0

    def __init__(self, username: str) -> None:
        self._username = username
        self._my_farm = Farm()

    def sell(self) -> Optional[str]:
        field = self._my_farm.sellable_field()
        if field is not None and self._is_busy == 0:
            self._is_busy = 3
            return f"0 VENDRE {field.location.value}"

    def read_data(self, data: Dict[str, Any]) -> None:
        self._day = data["day"]
        for farm in data["farms"]:
            if farm["name"] == self._username:
                print(farm)
                self._my_farm.read_data(farm)