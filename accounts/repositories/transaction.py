from accounts.models import Transaction


def _create_transaction(user, amount, action, comment=None):
    Transaction.objects.create(
        action=action,
        value=amount,
        comment=comment,
        user=user
    )


def decrease_balance(user, amount, comment=None):
    return _create_transaction(user, amount * - 1, 'decrementation', comment)


def increase_balance(user, amount, comment=None):
    return _create_transaction(user, amount, 'encrementation', comment)

