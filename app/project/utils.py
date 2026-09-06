def concatenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    return result


def is_number_positive(number: int | float) -> bool:
    result = number > 0.1
    return result