import pytest
from accounts.models import MainUser


def test_exist_balance():
    assert MainUser.exist_balance(100, 100)


def test_not_enough():
    assert not MainUser.exist_balance(100, 101)
