"""
Tests for module fizzbuzz
"""

import pytest

from fizzbuzz.fizzbuzz import get_value, gen_fizzbuzz, draw, DEFAULT_FIZBUZZ
from tests.constants import GET_VALUE_TEST_PARAM_DEFAULT, GEN_FIZZBUZZ_TEST_PARAMS_LIMIT, \
    GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT, GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT_MODULOS, \
    DRAW_TEST_PARAMS


@pytest.mark.parametrize("test_input, expected", GET_VALUE_TEST_PARAM_DEFAULT)
def test_get_value_default_modulos(test_input, expected, default_modulo):
    assert get_value(test_input, default_modulo) == expected


@pytest.mark.parametrize("limit", ['0', "10", "abrvalg", (), {}, []])
def test_get_value_wrong_type(limit, default_modulo):
    with pytest.raises(TypeError):
        get_value(limit, default_modulo)


def test_get_value_divide_by_zero(zero_modulo):
    with pytest.raises(ValueError):
        get_value(10, zero_modulo)


@pytest.mark.parametrize("limit, expected", GEN_FIZZBUZZ_TEST_PARAMS_LIMIT)
def test_gen_fizzbuzz_defaults(limit, expected):
    assert tuple(gen_fizzbuzz(limit)) == expected


@pytest.mark.parametrize("start, limit, expected", GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT)
def test_gen_fizzbuzz_defaults_with_start(start, limit, expected):
    assert tuple(gen_fizzbuzz(limit, start)) == expected


@pytest.mark.parametrize("start, limit, modulo, expected",
                         GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT_MODULOS)
def test_gen_fizzbuzz_custom_modulos(start, limit, modulo, expected):
    assert tuple(gen_fizzbuzz(limit, start, modulo)) == expected


@pytest.mark.parametrize("limit", ['0', "10", "abrvalg", (), {}, []])
def test_gen_fizzbuzz_wrong_type(limit):
    with pytest.raises(TypeError):
        next(gen_fizzbuzz(limit))


def test_gen_fizzbuzz_divide_by_zero(zero_modulo):
    with pytest.raises(ValueError):
        next(gen_fizzbuzz(10, modulos=zero_modulo))


@pytest.mark.parametrize("start, limit", [(10, 1)])
def test_gen_fizzbuzz_wrong_value(start, limit):
    """Incorrect params generate empty result"""
    assert list(gen_fizzbuzz(limit, start)) == []


@pytest.mark.parametrize("limit, page_size, expected", DRAW_TEST_PARAMS)
def test_draw(limit, page_size, expected):
    assert draw(gen_fizzbuzz(limit), page_size) == "\n".join(expected)
