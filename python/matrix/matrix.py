class Matrix:
    def __init__(self, matrix_string):
        try:
            self.matrix = [
                [*map(lambda num: int(num), nums)]
                for nums in [num_str.split(' ') for num_str in matrix_string.split('\n')]
            ]
        except ValueError:
            print('UH OH. . .Ensure your input is a string representing a matrix of numbers with embedded newlines, if any.')

    def row(self, index):
        return self.matrix[index-1].copy()

    def column(self, index):
        return [row[index-1] for row in self.matrix]
