import pytest

from fizzbuzz.fizzbuzz import DEFAULT_FIZBUZZ


@pytest.fixture()
def default_modulo():
    return DEFAULT_FIZBUZZ


@pytest.fixture()
def zero_modulo():
    return {0: "Dummy"}