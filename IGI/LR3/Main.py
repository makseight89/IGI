import math
from Task1 import Task1
from Task2 import Task2
from Task3 import Task3
from Task4 import Task4
from Task5 import Task5

while True:
    print("Выберите номер задания(1 - 5) или 0 для выхода: ")
    choice = int(input())

    if choice == 0: break

    switch = {1: Task1,
              2: Task2,
              3: Task3,
              4: Task4,
              5: Task5}

    if choice in switch:
        switch[choice]()

        print("\n" + "=" * 100)
    else:
        print("Неправильный выбор")
        continue