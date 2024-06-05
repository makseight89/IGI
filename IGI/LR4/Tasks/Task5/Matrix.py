import numpy as np
from Tasks.MyMixin import MyMixin


class Matrix(MyMixin):
    def __init__(self, matrix: np.array):
        self._matrix = matrix

    @property
    def data(self):
        return self._matrix

    @data.setter
    def data(self, value):
        self._matrix = value

    def rebuild_matrix(self):
        rows, columns = self._matrix.shape
        for i in range(rows):
            max_in_row = self._matrix[i][i]
            max_pos = i
            for j in range(columns):
                if max_in_row < self._matrix[i][j]:
                    max_in_row = self._matrix[i][j]
                    max_pos = j
            self._matrix[i][i], self._matrix[i][max_pos] = self._matrix[i][max_pos], self._matrix[i][i]

    def get_main_diagonal(self):
        diagonal = np.diag(self._matrix)
        return diagonal

    def get_median_numpy(self):
        diagonal = self.get_main_diagonal()
        return np.median(diagonal)

    def get_median(self):
        diagonal = self.get_main_diagonal()
        diagonal.sort()
        size = len(diagonal)
        if size % 2 == 0:
            return (diagonal[size // 2] + diagonal[size // 2 - 1]) / 2
        else:
            return diagonal[size // 2]

    def __str__(self):
        return str(self._matrix)