from utils import calculate_discount, get_full_name, is_even

def test_calculate_discount_20_percent():
    price = 100
    discount = 20
    expected = 80.0
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_50_percent():
    price = 200
    discount = 50
    expected = 100.0
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_zero_discount():
    price = 150
    discount = 0
    expected = 150.0
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_zero_price():
    price = 0
    discount = 30
    expected = 0.0
    actual = calculate_discount(price, discount)
    assert actual == expected

def test_calculate_discount_float_values():
    price = 99.9
    discount = 10
    expected = 89.91
    actual = calculate_discount(price, discount)
    assert abs(actual - expected) < 1e-9

def test_is_even_positive_even():
    number = 4
    expected = True
    actual = is_even(number)
    assert actual is expected

def test_is_even_positive_odd():
    number = 7
    expected = False
    actual = is_even(number)
    assert actual is expected

def test_is_even_negative_even():
    number = -8
    expected = True
    actual = is_even(number)
    assert actual is expected

def test_is_even_negative_odd():
    number = -3
    expected = False
    actual = is_even(number)
    assert actual is expected

def test_is_even_zero():
    number = 0
    expected = True
    actual = is_even(number)
    assert actual is expected

def test_get_full_name_standard():
    first = "Михайло"
    last = "Лисий"
    expected = "Михайло Лисий"
    actual = get_full_name(first, last)
    assert actual == expected


def test_get_full_name_short():
    first = "Кирило"
    last = "Коваль"
    expected = "Кирило Коваль"
    actual = get_full_name(first, last)
    assert actual == expected


def test_get_full_name_long():
    first = "Олександр"
    last = "Константинопольський"
    expected = "Олександр Константинопольський"
    actual = get_full_name(first, last)
    assert actual == expected


def test_get_full_name_single_char():
    first = "А"
    last = "Б"
    expected = "А Б"
    actual = get_full_name(first, last)
    assert actual == expected


def test_get_full_name_another_valid():
    first = "Василь"
    last = "Шевченко"
    expected = "Василь Шевченко"
    actual = get_full_name(first, last)
    assert actual == expected