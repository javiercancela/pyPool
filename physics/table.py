from physics.ball import Ball
from physics.value_objects import Position


class Table:
    SIZE_X = 2540
    SIZE_Y = 1270
    FOOT_SPOT = Position((SIZE_X * 3) / 2, SIZE_Y / 2)

    def __init__(self):
        temp_list = []
        for i in range(0, 16):
            temp_list.append(Ball(i, Position(0, 0)))

        self._balls = tuple(temp_list)

    def get_balls(self):
        return self._balls
