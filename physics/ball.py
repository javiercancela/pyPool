from physics.value_objects import Position, Velocity


class Ball:
    """
    Represents a pool ball, with official size and mass
    """
    DIAMETER_IN_MM = 57
    MASS_IN_GR = 160

    def __init__(self, number: int, position: Position):
        self._number = number
        self._position = position
        self._velocity = Velocity(0, 0)

    def set_velocity(self, velocity):
        self._velocity = velocity

    def update(self, time_in_ms):
        """
        Position is recalculated based on the current vecolity and time lapsed
        :param time_in_ms: Time lapsed in milliseconds
        :return:
        """
        self._position = self._position.get_new_position(self._velocity, time_in_ms)

    def get_position(self):
        return self._position

    def get_distance_from_ball(self, ball: "Ball"):
        """
        Get the distance to another ball, counting from the closest points for each ball
        :param ball: the other ball
        :return: distance in millimeters
        """
        return self.get_position().get_distance(ball.get_position()) - Ball.DIAMETER_IN_MM

    def get_collision(self, ball: "Ball"):
        """
        To detect collisions with another ball, we just calculate the distance between balls
        :param ball: the other ball
        :return: True if the balls collided, False otherwise
        """
        return self.get_distance_from_ball(ball) <= 0
