from Tasks.Task5.Matrix import Matrix
from Services.InputService import InputService
import numpy as np
from Tasks.Task import Task


class Task5(Task):
    @staticmethod
    def solve():
        print("������� n, m - ����������� �������:")
        while True:
            try:
                n = InputService.input_int()
                m = InputService.input_int()
                matrix = Matrix(np.random.randint(100, size=(n, m)))
                break
            except ValueError:
                print("������������ ������, ���������� �����")

        print(f"���� �������:\n{matrix}\n")

        matrix.rebuild_matrix()
        print(f"������������� �������:\n{matrix}\n")

        print(f"������� ��������� �������: {matrix.get_main_diagonal()}\n")
        print("������� ������� ��������� �������:")
        print(f"Numpy: {matrix.get_median_numpy()}")
        print(f"��� �������: {matrix.get_median()}")
        print(matrix.get_type())
