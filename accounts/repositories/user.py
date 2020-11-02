from decimal import Decimal
from typing import List

from django.db.models import Sum

from accounts.models import MainUser


def load_user(user_id: int) -> MainUser:
    return MainUser.objects.get(id=user_id)


def load_users(user_ids: List[int]):
    return MainUser.objects.filter(id__in=user_ids)


def get_balance(user: MainUser) -> Decimal:
    return user.transactions.aggregate(balance=Sum('value')).get('balance') or 0


def check_balance(user: MainUser, amount) -> bool:
    balance = get_balance(user)
    return user.exist_balance(balance, amount)
