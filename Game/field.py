class TetrisField:
    def __init__(self):
        self.grid = [[(0, 0, 0) for x in range(10)] for x in range(17)]
        self.deleted_lines = []

    def upgrade_array_condition(self, shape):
        for i in shape.coordinates:
            copy_color = shape.color
            self.grid[i[0]][i[1]] = copy_color
        return

    def check_filled_lines(self):
        for i in range(len(self.grid)):
            if not (0, 0, 0) in self.grid[i]:
                self.deleted_lines.append(i)
        if len(self.deleted_lines) != 0:
            return True
        else:
            return False

    def check_empty_cells(self, coordinates):
        for i in coordinates:
            if 0 <= i[0] <= 16 and 0 <= i[1] <= 9:
                if self.grid[i[0]][i[1]] != (0, 0, 0):
                    return False
            else:
                return False
        return True

