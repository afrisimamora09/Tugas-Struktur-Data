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

    def display(self):
        for row in self.data:
            print(" ".join(str(cell) for cell in row))
        print()
