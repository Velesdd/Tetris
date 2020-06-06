import random
from copy import deepcopy
from Game.field import TetrisField


class Shape:
    S_SHAPE_TEMPLATE = [[[0, 4], [0, 5], [1, 3], [1, 4]],
                        [[0, 4], [1, 4], [1, 5], [2, 5]]]
    Z_SHAPE_TEMPLATE = [[[0, 3], [0, 4], [1, 4], [1, 5]],
                        [[0, 4], [1, 3], [1, 4], [2, 3]]]
    I_SHAPE_TEMPLATE = [[[0, 4], [1, 4], [2, 4], [3, 4]],
                        [[0, 3], [0, 4], [0, 5], [0, 6]]]
    O_SHAPE_TEMPLATE = [[[0, 3], [0, 4], [1, 3], [1, 4]]]
    J_SHAPE_TEMPLATE = [[[0, 4], [1, 4], [2, 3], [2, 4]],
                        [[0, 3], [1, 3], [1, 4], [1, 5]],
                        [[0, 3], [0, 4], [1, 3], [2, 3]],
                        [[0, 3], [0, 4], [0, 5], [1, 5]]]
    L_SHAPE_TEMPLATE = [[[0, 4], [1, 4], [2, 3], [2, 4]],
                        [[0, 3], [1, 3], [1, 4], [1, 5]],
                        [[0, 3], [0, 4], [1, 3], [2, 3]],
                        [[0, 3], [0, 4], [0, 5], [1, 5]]]
    T_SHAPE_TEMPLATE = [[[0, 4], [1, 3], [1, 4], [1, 5]],
                        [[0, 4], [1, 4], [1, 5], [2, 4]],
                        [[0, 3], [0, 4], [0, 5], [1, 4]],
                        [[0, 5], [1, 4], [1, 5], [2, 5]]]
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    VIOLET = (148, 0, 211)
    TURGUOISE = (64, 224, 208)
    PINK = (255, 20, 147)
    YELLOW = (255, 255, 0)
    SHAPES = [S_SHAPE_TEMPLATE, Z_SHAPE_TEMPLATE, I_SHAPE_TEMPLATE, O_SHAPE_TEMPLATE,
              J_SHAPE_TEMPLATE, L_SHAPE_TEMPLATE, T_SHAPE_TEMPLATE]
    COLORS = [RED, GREEN, BLUE, VIOLET, TURGUOISE, PINK, YELLOW]

    def __init__(self):
        self.number_type_shape = 0
        self.type_shape = random.randrange(0, len(self.SHAPES))
        self.coordinates = deepcopy(self.SHAPES[self.type_shape][0])
        self.color = deepcopy(self.COLORS[random.randrange(0, len(self.COLORS))])

    def check_and_move_down(self, step, field: TetrisField):
        for i in self.coordinates:
            if i[0] > 15:
                return False
            elif field.grid[i[0] + 1][i[1]] != (0, 0, 0):
                    return False
            elif i[0] < 15:
                if field.grid[i[0]+2][i[1]] != (0, 0, 0):
                    step = 1
                elif field.grid[i[0] + step][i[1]] != (0, 0, 0) and i[0] < 14:
                        step = 2
        for i in self.coordinates:
            i[0] += step
        return True

    def check_the_right_position(self, field: TetrisField):
        for i in self.coordinates:
            if i[1] > 8:
                return False
            elif field.grid[i[0]][i[1]+1] != (0, 0, 0):
                return False
        for i in self.coordinates:
            i[1] += 1
        return True

    def check_the_left_position(self, field: TetrisField):
        for i in self.coordinates:
            if i[1] < 1:
                return False
            elif field.grid[i[0]][i[1] - 1] != (0, 0, 0):
                return False
        for i in self.coordinates:
            i[1] -= 1
        return True

    def change_shape(self, field: TetrisField):
        new_number_type_shape = 0
        if len(self.SHAPES[self.type_shape])-1 > self.number_type_shape:
            new_number_type_shape = self.number_type_shape + 1
        new_position = self.get_different_between_coordinates(deepcopy(self.SHAPES[self.type_shape][new_number_type_shape]))
        if field.check_empty_cells(new_position):
            self.coordinates = deepcopy(new_position)
            self.number_type_shape = deepcopy(new_number_type_shape)

    def get_different_between_coordinates(self, new_coordinates):
        different_between_coordinates = [[], [], [], []]
        for i in range(len(self.coordinates)):
            different_between_coordinates[i] += [
                self.coordinates[i][0] - self.SHAPES[self.type_shape][self.number_type_shape][i][0],
                self.coordinates[i][1] - self.SHAPES[self.type_shape][self.number_type_shape][i][1]]
        for i in range(len(new_coordinates)):
            new_coordinates[i][0] += different_between_coordinates[i][0]
            new_coordinates[i][1] += different_between_coordinates[i][1]
        return new_coordinates
