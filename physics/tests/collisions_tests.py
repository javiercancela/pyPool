from physics.ball import Ball
from physics.value_objects import Position, Velocity
import math


def test_collisions():
    ball1 = Ball(1, Position(0, 0))
    ball1.set_velocity(Velocity(1, math.pi / 2))
    ball2 = Ball(2, Position(0, 100))
    while not ball1.get_collision(ball2):
        ball1.update(1)
        ball2.update(1)

    assert ball1.get_position().get_distance(Position(0, 43)) < 0.0000001

    ball1 = Ball(1, Position(0, 0))
    ball1.set_velocity(Velocity(1, 0))
    ball2 = Ball(2, Position(100, 25))
    while not ball1.get_collision(ball2):
        ball1.update(1)
        ball2.update(1)

    assert ball1.get_position().get_distance(Position(49, 0)) < 0.0000001


def test_collision_coordinates_system():
    ball1 = Ball(1, Position(0, 0))
    ball1.set_velocity(Velocity(1, 0))
    ball2 = Ball(2, Position(100, 25))
    collision = ball1.get_collision(ball2)
    while collision is None:
        ball1.update(1)
        ball2.update(1)
        collision = ball1.get_collision(ball2)
