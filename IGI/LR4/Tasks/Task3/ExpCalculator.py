import numpy as np
import matplotlib.pyplot as plt
import math
from Tasks.MyMixin import MyMixin


class ExpSeriesCalculator(MyMixin):
    def __init__(self):
        self._terms = np.array([])

    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, new_terms):
        self._terms = new_terms

    def compute(self, x, tolerance):
        actual_value = math.exp(x)
        approximation = 1.0
        term_number = 1
        factorial = 1
        terms_list = []
        while abs(approximation - actual_value) > tolerance:
            term = (x ** term_number) / factorial
            approximation += term
            terms_list.append(term)
            term_number += 1
            factorial *= term_number
            if term_number > 500:
                print("Exceeded maximum iteration count (500)")
                break

        self.terms = np.array(terms_list)
        return approximation, term_number - 1, actual_value

    def visualize(self, start, end, increment, output_file=None):
        x_values = np.arange(start, end, increment)

        exact_y_values = np.exp(x_values)
        taylor_y_values = [self.compute(x, 0.01)[0] for x in x_values]

        plt.plot(x_values, exact_y_values, label='math.exp', color='green')
        plt.plot(x_values, taylor_y_values, label='Taylor series', color='red')
        plt.xlabel('x')
        plt.ylabel('e^x')
        plt.legend()

        if output_file:
            try:
                plt.savefig(output_file)
            except ValueError:
                print("Invalid file path")

        plt.show()

    def mean(self):
        return np.mean(self._terms)

    def median(self):
        return np.median(self._terms)

    def mode(self):
        values, counts = np.unique(self._terms, return_counts=True)
        mode_index = np.argmax(counts)
        return values[mode_index]

    def variance(self):
        return np.var(self._terms)

    def std_deviation(self):
        return np.std(self._terms)


if __name__ == "__main__":
    exp_calculator = ExpSeriesCalculator()
    x_value = 2
    tolerance = 0.0001
    approx, terms, true_val = exp_calculator.compute(x_value, tolerance)
    print(f"Approximated e^{x_value} = {approx}, using {terms} terms, true value is {true_val}")
    exp_calculator.visualize(-2, 2, 0.1, "exp_plot.png")
    print(f"Главное: {exp_calculator.mean()}")
    print(f"Медиана: {exp_calculator.median()}")
    print(f"Мода: {exp_calculator.mode()}")
    print(f"Вариация: {exp_calculator.variance()}")
    print(f"Стандартное вычисление: {exp_calculator.std_deviation()}")
