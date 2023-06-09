"""
Question:
Write a Python program that iterates the integers from 1 to 50. For multiples of
three print "Fizz" instead of the number and for multiples of five print "Buzz". For
numbers that are multiples of three and five, print "FizzBuzz"

Instructions:
Please provide the code, any workings and the expected output
"""

import numbers
from itertools import zip_longest
from typing import Generator, Iterable, Optional

DEFAULT_DRAW_PADDING = 16
DEFAULT_FIZBUZZ = {
    3: "Fizz",
    5: "Buzz"
}


def get_value(target: int, modulos: dict[int, str]) -> str | int:
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
            f"Attribute is not a number. Supplied value: "
            f"<{target = } : {type(target) = }>")

    if any(map(lambda x: x == 0, modulos)):
        raise ValueError(
            f"Dividers can not be zero. Supplied value: <{modulos = }>")

    result = ''.join(value for key, value in modulos.items() if target % key == 0)
    return result if result else target


def gen_fizzbuzz(limit: int, start: int = 1, modulos: Optional[(dict[int, str])] = None) -> \
Generator[
    tuple[int, int | str], None, None]:
    """generate the sequence of values according to the FizzBuzz puzzle rules
        Will iterate from start value to limit value, inclusive.
        :param limit: upper limit, inclusive to iterate through
        :param start: lower limit, default = 1
        :param modulos: a dictionary of key-value pairs which define the FizzBuzz
                divisors and corresponding st values
    """
    if modulos is None:
        modulos = DEFAULT_FIZBUZZ

    yield from ((value, get_value(value, modulos))
                for value in range(start, limit + 1))


def draw(output: Iterable[tuple[int, int | str]], page_size: int = 1,
         padding=DEFAULT_DRAW_PADDING) -> str:
    # Convert output to printable values
    printable = (f"{value} => {fizzbuzz}" for value, fizzbuzz in output)
    # Chunk the output in lines, with each line containing no more than <page_size> elements
    chunked = (filter(None, line) for line in zip_longest(*[iter(printable)] * page_size))
    # return formatted string for output
    return "\n".join("".join(map(lambda x: x.ljust(padding), line)) for line in chunked)
