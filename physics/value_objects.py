from dataclasses import dataclass
import math


class ValueObject:
    pass


@dataclass(frozen=True)
class Position(ValueObject):
    """
    _x: cartesion coordinate in millimeters
    _y: cartesion coordinate in millimeters
    """
    _x: float
    _y: float

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_new_position(self, velocity, time):
        """
        Creates a new Position VO based on velocity and time lapsed
        :param velocity: Velocity used to calculate new position
        :param time: Time lapsed
        :return: A new updated position that reflects the movement of the ball
        """
        delta_x, delta_y = velocity.get_speed_components()
        return Position(self._x + delta_x * time, self._y + delta_y * time)

    def get_distance(self, position):
        """
        Calculates the distance from this position to another
        :param position: the other position
        :return: distance in mm
        """
        x2 = math.pow(self._x - position.get_x(), 2)
        y2 = math.pow(self._y - position.get_y(), 2)
        return math.sqrt(x2 + y2)


@dataclass(frozen=True)
class Velocity(ValueObject):
    """
    Velocity in polar coordinates
    _speed: in millimeters per millisecond, or m/s
    _direction: in radians
    """
    _speed: float
    _direction: float

    def get_speed_components(self):
        """
        We calculate cartesian coordinates for the velocity vector
        :return: list with both the x and y speed components
        """
        return self._speed * math.cos(self._direction), self._speed * math.sin(self._direction)
