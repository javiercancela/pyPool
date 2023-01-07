from physics.ball import Ball
from physics.value_objects import Position, Velocity
import math


def test_no_movement():
    ball = Ball(1, Position(0, 0))
    ball.set_velocity(Velocity(0, 0))
    ball.update(1000)
    assert ball.get_position() == Position(0, 0)


def test_movement():
    ball = Ball(1, Position(300, 400))
    ball.set_velocity(Velocity(5, math.atan(3 / 4)))
    ball.update(1000)
    new_x_pos = 4 * 1000 + 300
    new_y_pos = 3 * 1000 + 400
    assert ball.get_position() == Position(new_x_pos, new_y_pos)


def test_distance():
    ball1 = Ball(1, Position(0, 0))
    ball2 = Ball(2, Position(150, 0))
    assert ball1.get_distance_from_ball(ball2) == 93

    ball1 = Ball(1, Position(0, 0))
    ball2 = Ball(2, Position(0, 150))
    assert ball1.get_distance_from_ball(ball2) == 93

    ball1 = Ball(1, Position(0, 0))
    ball2 = Ball(2, Position(100, 200))
    assert ball1.get_distance_from_ball(ball2) == math.sqrt(50000) - Ball.DIAMETER_IN_MM

