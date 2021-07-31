class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split('\n')

    def row(self, index):
        return [*map(lambda num_str: int(num_str), self.matrix[index-1].split(' '))]

    def column(self, index):
        return [*map(lambda num_str: int(num_str.split(' ')[index-1]), self.matrix)]
