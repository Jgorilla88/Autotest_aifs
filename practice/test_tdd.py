import pytest
from utils.utils import is_password_strong


def test_short_password():
    '''Test password with 7 letters'''
    assert is_password_strong('asdfghj') is False


def test_long_password():
    '''Test password with 10 letters'''
    assert is_password_strong('qwertyuiop')
