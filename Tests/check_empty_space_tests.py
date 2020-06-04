from unittest import TestCase

from Game import field
from Game.shape import Shape
from Game.tetris import TetrisGameLogic


class EmptySpaceTestCase(TestCase):
    def setUp(self):
        self.field = field.TetrisField()
        for i in range(len(self.field.grid[5])):
            self.field.grid[5][i] = (255, 255, 255)
        self.shape = Shape()

    def test_check_filled_lines(self):
        self.assertTrue(self.field.check_filled_lines())

    def test_check_empty_cells_1(self):
        self.assertTrue(self.field.check_empty_cells(self.shape.coordinates))

    def test_check_empty_cells_2(self):
        for i in range(len(self.shape.coordinates)):
            self.shape.coordinates[i][0] += 5
        self.assertFalse(self.field.check_empty_cells(self.shape.coordinates))


class DeleteLinesTestCase(TestCase):
    def setUp(self):
        self.tetris = TetrisGameLogic()
        for i in range(len(self.tetris.field.grid[5])):
            self.tetris.field.grid[5][i] = (255, 255, 255)

    def test_delete_filled_lines(self):
        self.assertTrue(self.tetris.delete_filled_lines())
