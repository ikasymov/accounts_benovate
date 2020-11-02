from dependency_injector import containers, providers

from .usecases import PutMoney
from accounts.repositories import (
    load_users,
    load_user,
    check_balance,
    decrease_balance,
    increase_balance
)
from django.db import transaction


class PutMoneyIntoAccounts(containers.DeclarativeContainer):
    init = providers.Factory(
        PutMoney,
        load_user=load_user,
        load_users=load_users,
        exist_money=check_balance,
        withdraw_money=decrease_balance,
        put_money=increase_balance,
        transaction=transaction.atomic
    )
