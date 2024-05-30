import math
from prettytable import PrettyTable
from typing import Tuple

def get_user_input() -> Tuple[float, float]:
    x = float(input("Enter the value of x: "))
    epsilon = float(input("Enter the desired accuracy (epsilon): "))
    return x, epsilon

def calculate_exponential_series(x: float, epsilon: float) -> list:
    series_data = []
    result = 0
    n = 0

    while abs(math.exp(x) - result) > epsilon:
        if n <= 500:
            term = (x ** n) / math.factorial(n)
            result += term
            series_data.append([x, n, result, math.exp(x), epsilon])
            n += 1
        else:
            break

    return series_data

def display_result_table(series_data: list):
    table = PrettyTable(["x", "n", "F(x)", "Math F(x)", "eps"])
    for row in series_data:
        table.add_row(row)
    print(table)

def main():
    x, epsilon = get_user_input()
    series_data = calculate_exponential_series(x, epsilon)
    display_result_table(series_data)

if __name__ == "__main__":
    main()