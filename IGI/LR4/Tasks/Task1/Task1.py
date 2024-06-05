from Tasks.Task1.FractionalGenerator import FractionalGenerator
from Tasks.Task1.Serializer import Serializer
from Tasks.Task import Task


class Task1(Task):
    @staticmethod
    def __contains_duplicates(numbers):
        return len(numbers) != len(set(numbers))

    @staticmethod
    def __find_maximum(numbers):
        return max(numbers)

    @staticmethod
    def solve():
        def get_numbers_from_user():
            return list(FractionalGenerator.get_from_console(10))

        def generate_random_numbers():
            return list(FractionalGenerator.generate_random(10))

        actions = {
            '1': get_numbers_from_user,
            '2': generate_random_numbers
        }

        while True:
            choice = input("Выберите способ:\n1. Ввод десяти чисел\n2. Генерация десяти произвольных чисел\n")
            if choice in actions:
                numbers = actions[choice]()
                break
            else:
                print("Неправильная операция, попробуйте снова.")

        Serializer.serialize_csv("Task1.csv", numbers)
        Serializer.serialize_pickle("Task1.pickle", numbers)

        print("Entered numbers:")
        for num in numbers:
            print(num)

        if Task1.__contains_duplicates(numbers):
            print("Элементы дублируют друг друга.")
        else:
            print("Элемент не дублируют друг друга.")

        max_value = Task1.__find_maximum(numbers)
        print(f"The maximum value is: {max_value}")

        sorted_numbers = sorted(numbers)
        print("Отсортированный список:")
        for num in sorted_numbers:
            print(num)