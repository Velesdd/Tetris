from copy import deepcopy
from Game.shape import Shape
from Game.field import TetrisField


class TetrisGameLogic:

    def __init__(self, ):
        self.current_shape = Shape()
        self.next_shape = Shape()
        self.field = TetrisField()
        self.score = 0
        self.level = 1

    def check_full_space(self):
        if self.field.check_empty_cells(self.next_shape.coordinates):
            for i in self.current_shape.coordinates:
                if i in self.next_shape.coordinates:
                    return False
            return True
        return False

    def turn_shape(self):
        self.current_shape.change_shape(self.field)

    def find_where_fall(self):
        copy_coordinates = deepcopy(self.current_shape.coordinates)
        while True:
            for i in copy_coordinates:
                if i[0]+1 > 16:
                    return copy_coordinates
                if self.field.grid[i[0]+1][i[1]] != (0, 0, 0):
                    return copy_coordinates
            for i in copy_coordinates:
                i[0] += 1

    def upgrade_array_condition(self):
        for i in self.current_shape.coordinates:
            copy_color = self.current_shape.color
            self.field.grid[i[0]][i[1]] = copy_color
        return

    def delete_filled_lines(self):
        if self.field.check_filled_lines():
            for i in self.field.deleted_lines:
                del self.field.grid[i]
                self.field.grid.insert(0, [(0, 0, 0) for x in range(10)])
                self.score += 100
            self.field.deleted_lines.clear()
            return True
        else:
            return False

    def next_level(self):
        self.current_shape = self.next_shape
        self.next_shape = Shape()
        self.field = TetrisField()
        self.level += 1
        return

    def move(self, step):
        if not self.current_shape.check_and_move_down(step, self.field):
            if not self.check_full_space():
                self.upgrade_array_condition()
                return False
            else:
                self.upgrade_array_condition()
                self.current_shape = self.next_shape
                self.next_shape = Shape()
        return True
