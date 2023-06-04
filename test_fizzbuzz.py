import pytest as pytest

from fizzbuzz import DEFAULT_FIZBUZZ, get_fizzbuzz, fizzbuzz, draw, DEFAULT_DRAW_PADDING

EXPECTED_10 = (10, list(enumerate([1, 2, "Fizz", 4, "Buzz", "Fizz",
                                   7, 8, "Fizz", "Buzz"],
                                  start=1)))
EXPECTED_15 = (15, list(enumerate([1, 2, "Fizz", 4, "Buzz",
                                   "Fizz", 7, 8,
                                   "Fizz", "Buzz", 11,
                                   "Fizz", 13, 14, "FizzBuzz"],
                                  start=1)))

EXPECTED_50 = (50, list(enumerate([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8,
                                   "Fizz", "Buzz", 11, "Fizz", 13, 14,
                                   "FizzBuzz", 16, 17, "Fizz", 19, "Buzz",
                                   "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz",
                                   28, 29, "FizzBuzz", 31, 32, "Fizz", 34,
                                   "Buzz", "Fizz", 37, 38, "Fizz", "Buzz",
                                   41, "Fizz", 43, 44, "FizzBuzz", 46, 47,
                                   "Fizz", 49, "Buzz"], start=1)))

EXPECTED_START_1_1 = (1, 1, [(1, 1)])
EXPECTED_START_1_10 = (1, 10,
                       list(enumerate([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8,
                                       "Fizz", "Buzz"],
                                      start=1)))
EXPECTED_START_5_10 = (5, 10,
                       list(enumerate(["Buzz", "Fizz", 7, 8, "Fizz", "Buzz"], start=5)))
EXPECTED_START_40_50 = (40, 50,
                        list(enumerate(["Buzz", 41, "Fizz", 43, 44,
                                        "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"],
                                       start=40)))
DEFAULT_MODULOS_0_15 = (0, 15,
                        DEFAULT_FIZBUZZ,
                        list(enumerate(["FizzBuzz", 1, 2, "Fizz", 4, "Buzz", "Fizz",
                                        7, 8, "Fizz", "Buzz", 11, "Fizz", 13,
                                        14, "FizzBuzz"])))

TWO_THREE_FIVE_MODULOS_0_15 = (0, 15,
                               {2: "Double", 3: "Triple", 5: "Quintuple"},
                               list(enumerate(["DoubleTripleQuintuple", 1, "Double",
                                               "Triple", "Double", "Quintuple",
                                               "DoubleTriple", 7, "Double", "Triple",
                                               "DoubleQuintuple", 11, "DoubleTriple",
                                               13, "Double", "TripleQuintuple"])))

EXPECTED_DRAW_10_1 = list(
    map(lambda x: x.ljust(DEFAULT_DRAW_PADDING), ['1 => 1', '2 => 2', '3 => Fizz',
                                                  '4 => 4', '5 => Buzz', '6 => Fizz',
                                                  '7 => 7', '8 => 8', '9 => Fizz',
                                                  '10 => Buzz']))

EXPECTED_DRAW_10_5 = [
    "".join(map(lambda x: x.ljust(DEFAULT_DRAW_PADDING), ['1 => 1', '2 => 2', '3 => Fizz',
                                                          '4 => 4', '5 => Buzz'])),
    "".join(map(lambda x: x.ljust(DEFAULT_DRAW_PADDING), ['6 => Fizz',
                                                          '7 => 7', '8 => 8', '9 => Fizz',
                                                          '10 => Buzz']))]


def get_test_modulos():
    yield from (DEFAULT_MODULOS_0_15, TWO_THREE_FIVE_MODULOS_0_15)


@pytest.fixture()
def default_modulo():
    return DEFAULT_FIZBUZZ


@pytest.fixture()
def zero_modulo():
    return {0: "Dummy"}


@pytest.mark.parametrize("test_input, expected", {0: "FizzBuzz",
                                                  1: 1,
                                                  3: "Fizz",
                                                  5: "Buzz",
                                                  15: "FizzBuzz",
                                                  0b101111: 47,
                                                  0x48: "Fizz",
                                                  0o226: "FizzBuzz",
                                                  14.0: 14.0,
                                                  30: "FizzBuzz",
                                                  50: "Buzz"}.items())
def test_fizzbuzz_default_modulos(test_input, expected, default_modulo):
    assert get_fizzbuzz(test_input, default_modulo) == expected


@pytest.mark.parametrize("limit", ['0', "10", "abrvalg", (), {}, []])
def test_fizzbuzz_wrong_type(limit, default_modulo):
    with pytest.raises(TypeError):
        get_fizzbuzz(limit, default_modulo)


def test_fizzbuzz_divide_by_zero(zero_modulo):
    with pytest.raises(ValueError):
        get_fizzbuzz(10, zero_modulo)


@pytest.mark.parametrize("limit, expected", [EXPECTED_10, EXPECTED_15, EXPECTED_50])
def test_fizzbuzz_sequence_defaults(limit, expected):
    assert list(fizzbuzz(limit)) == expected


@pytest.mark.parametrize("start, limit, expected",
                         [EXPECTED_START_1_1,
                          EXPECTED_START_1_10,
                          EXPECTED_START_5_10,
                          EXPECTED_START_40_50])
def test_fizzbuzz_sequence_default_with_start(start, limit, expected):
    assert list(fizzbuzz(limit, start)) == expected


@pytest.mark.parametrize("start, limit, modulo, expected", get_test_modulos())
def test_fizzbuzz_sequence_custom_modules(start, limit, modulo, expected):
    assert list(fizzbuzz(limit, start, modulo)) == expected


@pytest.mark.parametrize("limit", ['0', "10", "abrvalg", (), {}, []])
def test_fizzbuzz_sequence_wrong_type(limit):
    with pytest.raises(TypeError):
        next(fizzbuzz(limit))


def test_fizzbuzz__sequence_divide_by_zero(zero_modulo):
    with pytest.raises(ValueError):
        next(fizzbuzz(10, modulos=zero_modulo))


@pytest.mark.parametrize("start, limit", [(10, 1)])
def test_fizzbuzz_sequence_wrong_value(start, limit):
    """Incorrect params generate empty result"""
    assert list(fizzbuzz(limit, start)) == []


@pytest.mark.parametrize("limit, page_size, expected", [(10, 1, EXPECTED_DRAW_10_1),
                                                        (10, 5, EXPECTED_DRAW_10_5)])
def test_fizzbuzz_draw(limit, page_size, expected):
    """Incorrect params generate empty result"""
    assert list(draw(fizzbuzz(limit), page_size)) == None
