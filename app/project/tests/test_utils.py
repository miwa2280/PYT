import pytest

from utils import is_number_positive, concatenate_two_strings

class TestIsNumberPositive:

    @pytest.mark.parametrize(
        'number, expected',
        [
            (-5, False),
            (-5, False),
            (-5, False),
            (15, True),
            (-5, False),
            (0.1, True),
            (-5, False),
        ]
    )
    def test_is_number_positive_general(self, number, expected):
        actual = is_number_positive(number)
        assert expected is actual

    @pytest.mark.skip(reason='Something strange here fix ASAP')
    def test_is_number_positive_1(self):
        1 / 0
        number = 5
        expected = True
        actual = is_number_positive(number)
        assert expected is actual

    def test_is_number_positive_2(self):
        number = -5
        expected = False
        actual = is_number_positive(number)
        assert expected is actual

def test_is_number_positive_1():
    number = 5
    expected = True
    actual = is_number_positive(number)
    assert expected is actual


def test_is_number_positive_2():
    number = -5
    expected = False
    actual = is_number_positive(number)
    assert expected is actual


def test_is_number_positive_2_1():
    number = 0.01
    expected = True
    actual = is_number_positive(number)
    assert expected is actual

def test_is_number_positive_3():
    number = -5
    expected = False
    actual = is_number_positive(number)
    assert expected is actual


def test_concatenate_two_strings_1():
    string_1 = '123'
    string_2 = '123'
    expected = "123123"
    actual = concatenate_two_strings(string_1, string_2)
    assert actual == expected, "what happened?"