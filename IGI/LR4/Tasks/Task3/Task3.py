from Tasks.Task3.ExpCalculator import ExpSeriesCalculator
from Services.InputService import InputService
from Tasks.Task import Task


class Task3(Task):
    @staticmethod
    def solve():
        calculator = ExpSeriesCalculator()
        x = InputService.input_float("Введите аргумент x:")
        eps = InputService.input_float("Введите экспоненту:")

        answ, n, true_answ = calculator.compute(x, eps)
        print("X: ", x)
        print("Количество операций", n)
        print("Ответ по Тейлору: ", answ)
        print("Ответ по математической функции: ", true_answ)
        print("Погрешность: ", eps)

        print(f'Медиана: {calculator.median()}')
        print(f'Мода: {calculator.mode()}')
        print(f'Дисперсия: {calculator.variance()}')
        print(f'Оптимальный подсчёт площади: {calculator.std_deviation()}')

        calculator.plot(-2, 2, 0.1, 'Task3plot.png')
