from unittest import TestCase

from Game.shape import Shape
from Game.field import TetrisField


class ShapeTestCase(TestCase):
    def setUp(self):
        self.shape = Shape()
        self.field = TetrisField()

    def test_change_shape(self):
        expected_coordinates = self.shape.SHAPES[self.shape.type_shape][self.shape.number_type_shape+1]
        self.shape.change_shape(self.field)
        actual_coordinates = self.shape.coordinates
        self.assertEqual(expected_coordinates, actual_coordinates)
