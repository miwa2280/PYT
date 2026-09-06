from utils import is_number_positive


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