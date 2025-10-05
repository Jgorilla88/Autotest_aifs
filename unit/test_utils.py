import pytest
from utils.utils import is_password_strong
from utils.utils import is_email_valid


@pytest.mark.unit
class TestPasswordUtils:
    @pytest.mark.parametrize(
        'password, expected',
        [
            ('12345', False),
            ('asshole123', False),
            ('SAAM1234', False),
            ('SuperSavePassword123', True)
        ]
    )
    def test_is_strong_password(self, password, expected):
        'проверяет устойчивость пароля'
        assert is_password_strong(password) == expected


@pytest.mark.unit
class TestEmailUtils:

    @pytest.mark.parametrize(
        'email, expected',
        [
            ('test@test.ru', True),
            ('second_test@mail.com', True),
            ('@ghdfv.com', False),
            ('test@mailru.', False),
            ('test@.com', False)
        ]
    )
    def test_is_email_valid(self, email, expected):
        assert is_email_valid(email) == expected
