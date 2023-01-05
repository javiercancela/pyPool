from physics.ball import Ball
from physics.value_objects import Position, Velocity
import math


def test_collisions():
    ball1 = Ball(Position(0, 0))
    ball1.set_velocity(Velocity(1, math.pi / 2))
    ball2 = Ball(Position(0, 100))
    while not ball1.collides(ball2):
        ball1.update(1)
        ball2.update(1)

    assert ball1.get_position().get_distance(Position(0, 43)) < 0.0000001


ball1 = Ball(Position(0, 0))
ball1.set_velocity(Velocity(1, 0))
ball2 = Ball(Position(100, 25))
while not ball1.collides(ball2):
    ball1.update(1)
    ball2.update(1)

assert ball1.get_position().get_distance(Position(49, 0)) < 0.0000001
