# методы tuple, list, dict, set

def list_methods(arr: list):
    print("\n" + "===" * 50)
    arr.append(24)
    print(f'append: {arr}')

    print("\n" + "===" * 50)
    arr.extend([1, 2, 3])
    print(f'extend: {arr}')

    print("\n" + "===" * 50)
    arr.insert(0, 256)  # Встаявляет на позицию 0 число 256
    print(f'insert: {arr}')

    print("\n" + "===" * 50)
    arr.remove(256)  # Удаляет из списка первый элемент со значением  256
    print(f'remove: {arr}')

    print("\n" + "===" * 50)
    arr.pop(1)  # Возвращает последний или i элемент, удаляя его из последовательности
    print(f'pop: {arr}')

    print("\n" + "===" * 50)
    arr.clear()  # Очищает список
    print(f'clear: {arr}')

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"Список до сортировки: {arr}")

    arr.sort()

    print(f"Список после сортировки: {arr}")

    print("\n" + "===" * 50)
    arr.reverse()
    print(f'reverse: {arr}')

    del arr[0]  # Удаляет из списка i-ый элемент(или несколько, если задан индекс j)
    print(f"del arr[i[:j]] {arr}")

    arr_1 = ["a", "b"]

    arr_2 = ["c", "d", "e"]

    for elem, number in zip(arr_1, arr_2):
        print(elem, number)

    return


def tuple_methods(tup: tuple):
    # нельзя изменить кортеж напрямую, но можно изменять то, что лежит внутри
    tup[0].append(567)
    print(tup)

    t = (23, 12)

    # Конкатенация
    print(t + tup)
    pass


def dict_methods(d: dict):
    val = d["ManCity"]
    print(f"Значение словаря по ключу: {val}")

    val_1 = d.get("ManCity")
    print(f"Значение словаря по ключу: {val_1}")

    d["ManCity"] = 23
    print(f"Измененное значение: {d['ManCity']}")

    print(f"все пары ключ значение: {d.items()}")

    print(f"Весь набор ключей для нашего словаря: {d.keys()}")

    print(f"Весь набор значений для нашего словаря: {d.values()}")

    del d["Inter"]

    print(f"Удаление пары по ключу del d[Inter]. Словарь сейчас {d.items()}")

    d.clear()

    print(f"состояние после очистки {d.items()}")
    pass


def set_methods(s: set, f: frozenset):
    s.add('adddddd')
    s.remove('first')  # если элемента нет, то ошибка
    s.discard('second')  # удаляет если присутствует
    print(f"pop метод: {s.pop()}")
    s.clear()

    s.add("set")

    a = set("k")

    uni = s.union(a)
    print(uni)

    set_1 = set()
    set_1.add('first')
    set_1.add('second')
    set_1.add('third')

    set_2 = set()
    set_2.add('one')
    set_2.add('two')
    set_2.add('third')

    set_3 = set_1.intersection(set_2)  # пересечение
    print(set_3)

    set_4 = set_1.difference(set_2)
    print(f"разность: {set_4}")

    check = set_1.isdisjoint(set_2)  # если есть общие элементы, то false
    print(check)

    check = set_1.issubset(set_2)  # по сути сравнение множеств, если все элементы set_1 есть в set_2
    print(check)

    check = set_1.issuperset(set_2)  # наоброт к issubset, тут set_2 в set_1

    set_1.add("df")
    print(set_1 > set_2)

    set_1.update(set_2)  # добавление элементов одного множества в другое
    print(set_1)
    pass


arr = ["23", "34", "34"]
tup = ([1, 2, 3], ["homiak", "karkusha"])

# dict - словари, отображающие множество неизменяемых ключей на соответствующие значения
d = {"ManCity": 1,
     "RealM": 2,
     "Inter": 3}  # создание словаря так или через dict()

# set - это неупорядоченная коллекция уникальных элементов.
# set - изменяемое множество
# frozenset - неизменяемое множество
s = {'first', 'second'}
f = frozenset(['three', 'four', 'five'])

# list_methods(arr)
# tuple_methods(tup)
# dict_methods(d)
# set_methods(s,f)

str1 = "dslkfhjlis"

ar = [1, 2, 3, 4, 5]

ar = ar[1:3:2]

print(ar)
