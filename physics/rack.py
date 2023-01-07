import math

from physics.ball import Ball
from physics.value_objects import Position


class Rack:
    X_INCREMENT = Ball.DIAMETER_IN_MM * math.cos(math.pi / 6)
    Y_INCREMENT = Ball.DIAMETER_IN_MM * math.sin(math.pi / 6)
    APEX_POSITION = 0
    CENTER_POSITION = 4
    TOP_CORNER_POSITION = 10
    BOTTOM_CORNER_POSITION = 14

    def __init__(self, foot_spot: Position):
        positions = []
        for x in range(0, 5):
            for y in range(x, -(x+1), -2):
                pos_x = foot_spot.get_x() + x * Rack.X_INCREMENT
                pos_y = foot_spot.get_y() + y * Rack.Y_INCREMENT
                positions.append(Position(pos_x, pos_y))
        self._positions = tuple(positions)

    def get_positions(self):
        return self._positions
