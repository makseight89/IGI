from Tasks.Task3.ExpCalculator import ExpSeriesCalculator
from Services.InputService import InputService
from Tasks.Task import Task


class Task3(Task):
    @staticmethod
    def solve():
        calculator = ExpSeriesCalculator()
        x = InputService.input_float("������� �������� x:")
        eps = InputService.input_float("������� ����������:")

        answ, n, true_answ = calculator.compute(x, eps)
        print("X: ", x)
        print("���������� ��������", n)
        print("����� �� �������: ", answ)
        print("����� �� �������������� �������: ", true_answ)
        print("�����������: ", eps)

        print(f'�������: {calculator.median()}')
        print(f'����: {calculator.mode()}')
        print(f'���������: {calculator.variance()}')
        print(f'����������� ������� �������: {calculator.std_deviation()}')

        calculator.plot(-2, 2, 0.1, 'Task3plot.png')
