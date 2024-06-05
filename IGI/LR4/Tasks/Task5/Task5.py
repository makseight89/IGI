from Tasks.Task5.Matrix import Matrix
from Services.InputService import InputService
import numpy as np
from Tasks.Task import Task


class Task5(Task):
    @staticmethod
    def solve():
        print("Введите n, m - размерность матрицы:")
        while True:
            try:
                n = InputService.input_int()
                m = InputService.input_int()
                matrix = Matrix(np.random.randint(100, size=(n, m)))
                break
            except ValueError:
                print("Некорректный размер, попробуйте снова")

        print(f"Ваша матрица:\n{matrix}\n")

        matrix.rebuild_matrix()
        print(f"Перестроенная матрица:\n{matrix}\n")

        print(f"Главная диагональ матрицы: {matrix.get_main_diagonal()}\n")
        print("Медиана главных элементов матрицы:")
        print(f"Numpy: {matrix.get_median_numpy()}")
        print(f"Моя функция: {matrix.get_median()}")
        print(matrix.get_type())
