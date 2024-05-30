import inputCheck as ic
from gen import gen


def Task5():
    arr = []
    while True:
        print('Введите 1 для самостоятельного ввода и 2 для генерации')
        choice = ic.intCheck()
        if choice == 1:
            # arr = list(map(float, input("Введите элементы списка через пробел: ").split()))
            arr = ic.listFloatCheck()
            break
        elif choice == 2:
            print('Введите длину желаемого массива')
            arrlen = ic.intCheck()
            # arr = [i ** 2 / 100 for i in range(0, 10)]
            arr = list(gen(arrlen))
            break
        else:
            print('Попробуйте ещё раз')
            continue

    print(*arr)

    zeros = countZeros(arr)

    sumOfAbs = sumAfterMinAbs(arr)

    print(f"Кол-во элементов списка равных нулю {zeros}")

    print(f"Сумма элементов списка после минимального по модулю элемента {sumOfAbs}")


def countZeros(arr: list):
    """Function to count the number of list elements equal to 0."""
    count = 0

    for i in range(len(arr)):
        if arr[i] == 0.0:
            count += 1
        else:
            continue

    return count


def sumAfterMinAbs(arr: list):
    minIndex = arr.index(min(arr, key=abs))

    sumAfterMin = sum(arr[minIndex + 1:])

    return sumAfterMin
