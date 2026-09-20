import pytest
from utils import is_password_strong


class TestPasswordCheck:
    @pytest.mark.parametrize(
        'password, expected',
        [
            ('Password123!', True),     # Надежный
            ('Secret#9', True),         # 8 символов
            ('Qwer123!', True),         # 8 символов
            ('Пароль123!', True),       # Кириллица
            ('Short1!', False),         # Меньше 8 символов
            ('Password123', False),     # Без спецсимвола
            ('Password!!!!', False),    # Без цифр
            ('123456789!#', False),     # Без букв
            ('Pass word1!', False),     # Есть пробел
            ('        ', False),        # Только пробелы
            ('', False),                # Пустая строка
        ]
    )
    def test_is_password_strong_parametrized(self, password: str, expected: bool):
        actual = is_password_strong(password)
        assert actual == expected

    @pytest.mark.skip(reason='Test is not ready yet')
    def test_password_character_diversity(self):
        pass