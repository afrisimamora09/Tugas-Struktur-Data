import time
import os

class Array2D:
    def __init__(self, rows, cols, default=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

class GameOfLife:
    def __init__(self, rows, cols):
        self.grid = Array2D(rows, cols, 0)

    def set_cell(self, row, col, value):
        self.grid.set(row, col, value)

    def count_neighbors(self, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.grid.get_rows() and 0 <= c < self.grid.get_cols():
                count += self.grid.get(r, c)
        return count

    def next_generation(self):
        new_grid = Array2D(self.grid.get_rows(), self.grid.get_cols(), 0)

        for i in range(self.grid.get_rows()):
            for j in range(self.grid.get_cols()):
                alive = self.grid.get(i, j)
                neighbors = self.count_neighbors(i, j)

                if alive == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid.set(i, j, 0)
                    else:
                        new_grid.set(i, j, 1)
                else:
                    if neighbors == 3:
                        new_grid.set(i, j, 1)

        self.grid = new_grid

    def display(self):
        for i in range(self.grid.get_rows()):
            for j in range(self.grid.get_cols()):
                print("■" if self.grid.get(i, j) == 1 else ".", end=" ")
            print()
        print()

if __name__ == "__main__":
    game = GameOfLife(10, 10)

    # Pola awal: GLIDER
    game.set_cell(1, 2, 1)
    game.set_cell(2, 3, 1)
    game.set_cell(3, 1, 1)
    game.set_cell(3, 2, 1)
    game.set_cell(3, 3, 1)

    for _ in range(20):
        os.system("cls" if os.name == "nt" else "clear")
        game.display()
        game.next_generation()
        time.sleep(0.5)
