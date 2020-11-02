from dataclasses import dataclass
from typing import Callable, List


class NotEnoughMoney(Exception):

    def __str__(self):
        return "Not enough money"


@dataclass
class PutMoney:
    """Зачислить деньги на счета.

    Attributes:
        from_account (int): С пользователя.
        amount (int): Сумма зачисление.
        to_accounts (list): На пользователей.
    """
    # attributes
    from_account_id: int
    amount: int
    to_account_ids: List[int]

    def load_from_account(self):
        self.from_account = self.load_user(self.from_account_id)

    def load_to_accounts(self):
        self.to_accounts = self.load_users(self.to_account_ids)

    def decrease_from_account(self):
        if self.exist_money(self.from_account, self.amount):
            self.withdraw_money(self.from_account, self.amount)
        else:
            raise NotEnoughMoney

    def increase_to_accounts(self):
        amount = self.amount / len(self.to_account_ids)
        for account in self.to_accounts:
            self.put_money(account, amount)

    def put(self):
        self.load_from_account()
        self.load_to_accounts()
        with self.transaction():
            self.decrease_from_account()
            self.increase_to_accounts()

    # dependencies
    load_user: Callable
    load_users: Callable
    exist_money: Callable
    withdraw_money: Callable
    put_money: Callable
    transaction: Callable
