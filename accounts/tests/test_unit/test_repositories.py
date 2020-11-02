import pytest
from django.db.models import Sum

from accounts.repositories import (
    load_user,
    load_users,
    get_balance,
    check_balance,
    increase_balance,
    decrease_balance
)
from accounts.models import (
    MainUser,
    Transaction
)

TEST_USER_IDENT = 1
TEST_USERNAME = 'test_name'


@pytest.mark.django_db(transaction=True)
def test_load_user(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    assert load_user(user.id) == user


@pytest.mark.django_db(transaction=True)
def test_load_users(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    assert [user.id for user in load_users([user.id])] == \
           list(MainUser.objects.filter(id=user.id).values_list('id', flat=True))


@pytest.mark.django_db(transaction=True)
def test_get_balance(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    Transaction.objects.create(user=user, action='encrementation',
                               value=100)
    assert get_balance(user) == 100


@pytest.mark.django_db(transaction=True)
def test_check_balance(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    Transaction.objects.create(user=user, action='encrementation',
                               value=100)
    assert check_balance(user, 100)


@pytest.mark.django_db(transaction=True)
def test_not_enough_balance(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    Transaction.objects.create(user=user, action='encrementation',
                               value=100)
    assert not check_balance(user, 101)


@pytest.mark.django_db(transaction=True)
def test_increase_balance(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    increase_balance(user, 100)
    assert user.transactions.aggregate(balance=Sum('value')).get('balance') == 100


@pytest.mark.django_db(transaction=True)
def test_decrease_balance(create_user):
    user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    decrease_balance(user, 100)
    assert user.transactions.aggregate(balance=Sum('value')).get('balance') == 100 * -1


