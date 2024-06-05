from Tasks.Task1.RationalNum import RationalNum
from Services.InputService import InputService
import random


class FractionalGenerator:
    @staticmethod
    def get_from_console(n: int):
        count = 0
        while count < n:
            try:
                numerator = InputService.input_int("Enter numerator: ")
                denominator = InputService.input_int("Enter denominator: ")
                rn = RationalNum(numerator, denominator)
                print(f"Введённое число: {rn}")
                yield rn
                count += 1
            except ValueError:
                print("Неправильный ввод, попробуйте снова")

    @staticmethod
    def generate_random(n: int):
        for _ in range(n):
            numerator = random.randint(-100, 100)
            denominator = random.choice([i for i in range(-100, 101) if i != 0])
            yield RationalNum(numerator, denominator)
