import pytest
from utils import is_password_strong


class TestPasswordCheck:
    @pytest.mark.parametrize(
        'password, expected',
        [
            ('Password12!', True),
            ('SecretKey9#', True),
            ('Qwer123!', True),
            ('Пароль123!', True),
            ('Short1', False),
            ('Password123', False),
            ('Password', False),
            ('123456789', False),
            ('Password1 ', False),
            ('        ', False),
            ('', False),
        ]
    )
    def test_is_password_strong_parametrized(self, password: str, expected: bool):
        actual = is_password_strong(password)
        assert actual == expected

    @pytest.mark.skip(reason='Test is not ready yet')
    def test_password_character_diversity(self):
        pass