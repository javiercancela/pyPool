from physics.table import Table
from physics.rack import Rack


def test_count_table_balls():
    table = Table()
    assert len(table.get_balls()) == 16


def test_rack_positions():
    rack = Rack(Table.FOOT_SPOT)
    assert len(rack.get_positions()) == 15
