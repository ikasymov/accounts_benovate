import pytest
from django.db.models import Sum

from accounts.containers import PutMoneyIntoAccounts
from accounts.models import Transaction
from accounts.usecases.put_balance_into_account import NotEnoughMoney

TEST_USER_IDENT = 1
TEST_USERNAME = 'test_name'
TEST_TO_USER_IDENT = 10
TEST_TO_USERNAME = 'test_to_username'


@pytest.mark.django_db(transaction=True)
def test_put_money(create_user):
    from_user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    to_user = create_user(TEST_TO_USERNAME, TEST_TO_USER_IDENT)
    Transaction.objects.create(user=from_user,
                               action='encrementation',
                               value=100)

    container = PutMoneyIntoAccounts()
    container.init(from_user.id, 100, [to_user.id]).put()

    assert to_user.transactions.aggregate(balance=Sum('value')).get('balance') == 100


@pytest.mark.django_db(transaction=True)
def test_put_money_but_not_enough(create_user):
    from_user = create_user(TEST_USERNAME, TEST_USER_IDENT)
    to_user = create_user(TEST_TO_USERNAME, TEST_TO_USER_IDENT)

    with pytest.raises(NotEnoughMoney):
        container = PutMoneyIntoAccounts()
        container.init(from_user.id, 100, [to_user.id]).put()
