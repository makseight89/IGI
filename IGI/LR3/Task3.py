from typing import List


def Task3():
    """Function for searching words with first lowercase consonant letter"""
    print("Enter a string: ")
    input_str = input()
    lowercase_consonant_words = count_lowercase_consonant_words(input_str)
    print(f"The number of words starting with a lowercase consonant is {lowercase_consonant_words}")


def count_lowercase_consonant_words(input_str: str) -> int:
    """Count the number of words in the input string that start with a lowercase consonant"""
    words = input_str.split()
    return sum(1 for word in words if is_lowercase_consonant(word))


def is_lowercase_consonant(word: str) -> bool:
    """Check if a word starts with a lowercase consonant"""
    if not word:
        return False
    return word[0].islower() and is_consonant(word[0])


def is_consonant(char: str) -> bool:
    """Check if a character is a consonant"""
    vowels = "aeiou"
    return char.lower() not in vowels
