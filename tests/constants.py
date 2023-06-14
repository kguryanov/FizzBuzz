from src.fizzbuzz.fizzbuzz import DEFAULT_DRAW_PADDING, DEFAULT_FIZBUZZ

# reusable constants
MODUL0S235_DICT = {2: "Double", 3: "Triple", 5: "Quintuple"}

# expected results for gen_fizzbuzz() function
GEN_FIZZBUZZ_EXPECTED_0_0_DICT = {0: 'FizzBuzz'}
GEN_FIZZBUZZ_EXPECTED_1_1_DICT = {1: 1}
GEN_FIZZBUZZ_EXPECTED_1_10_DICT = {**GEN_FIZZBUZZ_EXPECTED_1_1_DICT,
                                   2: 2, 3: 'Fizz', 4: 4, 5: 'Buzz', 6: 'Fizz',
                                   7: 7, 8: 8, 9: 'Fizz', 10: 'Buzz'}
GEN_FIZZBUZZ_EXPECTED_11_15_DICT = {11: 11, 12: 'Fizz', 13: 13,
                                    14: 14, 15: 'FizzBuzz'}
GEN_FIZZBUZZ_EXPECTED_16_50_DICT = {16: 16, 17: 17, 18: 'Fizz', 19: 19, 20: 'Buzz', 21: 'Fizz',
                                    22: 22, 23: 23, 24: 'Fizz', 25: 'Buzz', 26: 26, 27: 'Fizz',
                                    28: 28, 29: 29, 30: 'FizzBuzz', 31: 31, 32: 32, 33: 'Fizz',
                                    34: 34, 35: 'Buzz', 36: 'Fizz', 37: 37, 38: 38, 39: 'Fizz',
                                    40: 'Buzz', 41: 41, 42: 'Fizz', 43: 43, 44: 44, 45: 'FizzBuzz',
                                    46: 46, 47: 47, 48: 'Fizz', 49: 49, 50: 'Buzz'}

GEN_FIZZBUZZ_EXPECTED_1_15_DICT = {**GEN_FIZZBUZZ_EXPECTED_1_10_DICT,
                                   **GEN_FIZZBUZZ_EXPECTED_11_15_DICT}

GEN_FIZZBUZZ_EXPECTED_1_50_DICT = {**GEN_FIZZBUZZ_EXPECTED_1_15_DICT,
                                   **GEN_FIZZBUZZ_EXPECTED_16_50_DICT}

GEN_FIZZBUZZ_EXPECTED_0_15_DICT = {**GEN_FIZZBUZZ_EXPECTED_0_0_DICT,
                                   **GEN_FIZZBUZZ_EXPECTED_1_15_DICT}

GEN_FIZZBUZZ_EXPECTED_MODUL0S235_0_15_DICT = {0: 'DoubleTripleQuintuple', 1: 1,
                                              2: 'Double', 3: 'Triple', 4: 'Double',
                                              5: 'Quintuple', 6: 'DoubleTriple', 7: 7,
                                              8: 'Double', 9: 'Triple', 10: 'DoubleQuintuple',
                                              11: 11, 12: 'DoubleTriple', 13: 13,
                                              14: 'Double', 15: 'TripleQuintuple'}


# Parameters for gen_value() tests
GET_VALUE_TEST_PARAM_DEFAULT = {0: "FizzBuzz", 1: 1, 3: "Fizz", 5: "Buzz", 15: "FizzBuzz",
                                0b101111: 47, 0x48: "Fizz", 0o226: "FizzBuzz", 14.0: 14.0,
                                30: "FizzBuzz", 50: "Buzz"}.items()

# Parameters for  gen_fizzbuzz() tests
GEN_FIZZBUZZ_PARAM_LIMIT_10 = (10, (*GEN_FIZZBUZZ_EXPECTED_1_10_DICT.items(),))
GEN_FIZZBUZZ_PARAM_LIMIT_15 = (15, (*GEN_FIZZBUZZ_EXPECTED_1_15_DICT.items(),))
GEN_FIZZBUZZ_PARAM_LIMIT_50 = (50, (*GEN_FIZZBUZZ_EXPECTED_1_50_DICT.items(),))

GEN_FIZZBUZZ_TEST_PARAMS_LIMIT = (GEN_FIZZBUZZ_PARAM_LIMIT_10,
                                  GEN_FIZZBUZZ_PARAM_LIMIT_15,
                                  GEN_FIZZBUZZ_PARAM_LIMIT_50)

# Parameters for gen_fizzbuzz()  test with start argument
GEN_FIZZBUZZ_PARAM_START_1_LIMIT_1 = (1, 1, ((1, 1),))
GEN_FIZZBUZZ_PARAM_START_1_LIMIT_10 = (1, 10, (*GEN_FIZZBUZZ_EXPECTED_1_10_DICT.items(),))
GEN_FIZZBUZZ_PARAM_START_11_LIMIT_15 = (11, 15, (*GEN_FIZZBUZZ_EXPECTED_11_15_DICT.items(),))
GEN_FIZZBUZZ_PARAM_START_16_LIMIT_50 = (16, 50, (*GEN_FIZZBUZZ_EXPECTED_16_50_DICT.items(),))

GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT = (GEN_FIZZBUZZ_PARAM_START_1_LIMIT_1,
                                        GEN_FIZZBUZZ_PARAM_START_1_LIMIT_10,
                                        GEN_FIZZBUZZ_PARAM_START_11_LIMIT_15,
                                        GEN_FIZZBUZZ_PARAM_START_16_LIMIT_50)


# parameters for gen_fizzbuzz tests with custom modulos argument
GEN_FIZZBUZZ_PARAM_DEFAULT_MODULO_0_15 = (0, 15,
                                          DEFAULT_FIZBUZZ,
                                          (*GEN_FIZZBUZZ_EXPECTED_0_15_DICT.items(),))

GEN_FIZZBUZZ_PARAM_235MODULO_0_15 = (0, 15,
                                     MODUL0S235_DICT,
                                     (*GEN_FIZZBUZZ_EXPECTED_MODUL0S235_0_15_DICT.items(),))

GEN_FIZZBUZZ_TEST_PARAMS_START_LIMIT_MODULOS = (GEN_FIZZBUZZ_PARAM_DEFAULT_MODULO_0_15,
                                                GEN_FIZZBUZZ_PARAM_235MODULO_0_15)

# Parameters for draw() function test
DRAW_PARAM_LIMIT_10_PAGE_SIZE_1 = (10, 1, (map(lambda x: x.ljust(DEFAULT_DRAW_PADDING),
                                               ['1 => 1', '2 => 2', '3 => Fizz', '4 => 4',
                                                '5 => Buzz',
                                                '6 => Fizz', '7 => 7', '8 => 8', '9 => Fizz',
                                                '10 => Buzz'])))

DRAW_PARAM_LIMIT_10_PAGE_SIZE_5 = (10, 5, ("".join(map(lambda x: x.ljust(DEFAULT_DRAW_PADDING),
                                                       ['1 => 1', '2 => 2', '3 => Fizz', '4 => 4',
                                                        '5 => Buzz'])),
                                           "".join(map(lambda x: x.ljust(DEFAULT_DRAW_PADDING),
                                                       ['6 => Fizz', '7 => 7', '8 => 8',
                                                        '9 => Fizz',
                                                        '10 => Buzz']))))

DRAW_TEST_PARAMS = (DRAW_PARAM_LIMIT_10_PAGE_SIZE_1, DRAW_PARAM_LIMIT_10_PAGE_SIZE_5)
