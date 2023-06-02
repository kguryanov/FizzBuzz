"""
Question:
Write a Python program that iterates the integers from 1 to 50. For multiples of
three print "Fizz" instead of the number and for multiples of five print "Buzz". For
numbers that are multiples of three and five, print "FizzBuzz"

Instructions:
Please provide the code, any workings and the expected output
"""

from typing import Generator, Iterable
import numbers

DEFAULT_FIZBUZZ = {
    3: "Fizz",
    5: "Buzz"
}


def get_fizzbuzz(target: int, modulos: dict[int: str]) -> str | int:
    """Atomic function, which returns either original value,
        or accumulated str depending on the divisibility of the value with key
        :param target: target integer to test
        :param modulos: a dictionary of modulos and corresponding str values
        :return: target or accumulated string if target value is divisible by at
                 least one of them keys in modules dict.
        :rtype: str or int
        """
    if not isinstance(target, numbers.Number):
        raise TypeError(
            f"Attribute is not a number. Supplied value: <{target = } : {type(target) = }>")
    result = ''.join(value for key, value in modulos.items() if target % key == 0)
    return result if result else target


def fizzbuzz(limit: int, start: int = 1, modulos: dict[int, str] = None) -> Generator:
    """generate the sequence of values according to the FizzBuzz puzzle rules
        Will iterate from start value to limit value, inclusive.
        :param limit: upper limit, inclusive to iterate through
        :param start: lower limit, default = 1
        :param modulos: a dictionary of key-value pairs which define the FizzBuzz
                divisors and corresponding st values
    """
    if modulos is None:
        modulos = DEFAULT_FIZBUZZ

    if start > limit:
        raise ValueError("Argument start is larger that the range limit.")

    yield from (get_fizzbuzz(value, modulos) for value in range(start, limit + 1))


def print_fizzbuzz(fizzes_n_buzzes: Iterable, sep=" ") -> None:
    print(*fizzes_n_buzzes, sep=sep)


