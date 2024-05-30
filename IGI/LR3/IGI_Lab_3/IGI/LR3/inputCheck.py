from typing import Callable, List


def input_checker(prompt: str, validator: Callable[[str], float]) -> float:
    while True:
        try:
            user_input = input(prompt)
            return validator(user_input)
        except ValueError as e:
            print(f"Error: {e}")


def int_validator(value: str) -> int:
    return int(value)


def float_validator(value: str) -> float:
    return float(value)


def float_list_validator(value: str) -> List[float]:
    return [float(x) for x in value.split()]


def main():
    int_value = input_checker("Enter an integer: ", int_validator)
    print(f"You entered: {int_value}")

    float_value = input_checker("Enter a float: ", float_validator)
    print(f"You entered: {float_value}")

    float_list = input_checker("Enter a list of floats separated by spaces: ", float_list_validator)
    print(f"You entered: {float_list}")


if __name__ == "__main__":
    main()
