from typing import Callable


def get_integer_input() -> int:
    """Prompts the user for an integer input and returns it."""
    while True:
        user_input = input("Enter an integer (enter a number > 100 to exit): ")
        if user_input.isdigit() and int(user_input) > 100:
            return int(user_input)
        elif user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter an integer.")


def sum_integers(get_input: Callable[[], int]) -> None:
    """Sums the integers entered by the user until a number greater than 100 is entered."""
    total = 0
    while True:
        num = get_input()
        if num > 100:
            break
        total += num
    print(f"The sum of the entered numbers is: {total}")


def main() -> None:
    """Main function that runs the integer summation task."""
    sum_integers(get_integer_input)


if __name__ == "__main__":
    main()
