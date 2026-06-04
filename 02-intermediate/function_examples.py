"""
Companion examples for the functions lesson.

Run this file from a terminal with:  python function_examples.py
It asks for three numbers and keeps only the positive ones.
"""


def check_number(number):
    """Return True if number is positive, otherwise print why and return False."""
    if number > 0:
        print(f"{number} is positive, adding to the list")
        return True
    elif number == 0:
        print("You entered zero, not adding it")
        return False
    else:
        print(f"{number} is negative, not adding it")
        return False


def collect_positive_numbers(how_many):
    """Ask the user for numbers until `how_many` positive ones are collected."""
    numbers = []
    while len(numbers) < how_many:
        value = int(input("Enter a number: "))
        if check_number(value):
            numbers.append(value)
    return numbers


if __name__ == "__main__":
    result = collect_positive_numbers(3)
    print("Your list:", result)
