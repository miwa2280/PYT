def concatenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    return result


def is_number_positive(number: int | float) -> bool:
    result = number > 0
    return result

def is_password_strong(password: str) -> bool:
    if len(password) < 8:
        return False

    if " " in password:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_alpha = any(char.isalpha() for char in password)
    has_special = any(not char.isalnum() for char in password)

    result = has_digit and has_alpha and has_special
    return result