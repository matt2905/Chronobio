from json import load as json_load
from pathlib import Path
import pytest
from player.json_class.state_json import StateJSON
from player.player_logic.state import State
from player.player_logic.my_type import Location, Vegetable


@pytest.fixture
def load_my_json() -> State:
    jsonfile = Path('./tests/day3.json')
    with open(jsonfile) as file:
        data = json_load(file)

    state: State = State("Vincent")
    stateJSON: StateJSON = StateJSON(**data)
    state._my_farm.add_field()
    state._my_farm.add_field()
    state._my_farm.add_field()
    state._my_farm.add_employee()
    state._my_farm.add_employee()
    state.data = stateJSON
    return state


def test_state_read_data(load_my_json):
    state: State = load_my_json
    assert state._day == 3


def test_field_read_data(load_my_json):
    state: State = load_my_json
    my_field = state._my_farm.get_field_by_location(Location.FIELD3)
    if my_field is not None:
        assert my_field.content == Vegetable.PATATE


def test_employee_read_data(load_my_json):
    state: State = load_my_json
    my_employee = state._my_farm.get_employee_by_id(1)
    assert my_employee.location == Location.FIELD3


def test_can_sell():
    state: State = State("test")

    state._my_farm.add_field()
    state._my_farm.add_field()
    state._my_farm.fields[1].content = Vegetable.PATATE
    state._my_farm.fields[1]._is_sellable = True
    state.sell()
    assert state._is_busy == 3


def test_cannot_sell():
    state: State = State("test")

    state._my_farm.add_field()
    state.sell()
    assert state._is_busy == 0
