from utils import is_number_positive, concatenate_two_strings


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


def test_is_number_positive_3():
    number = -5
    expected = False
    actual = is_number_positive(number)
    assert expected is actual


def test_concatenate_two_strings_1():
    string_1 = '123'
    string_2 = '123'
    expected = "1231223"
    actual = concatenate_two_strings(string_1, string_2)
    assert actual == expected, "what happened?"