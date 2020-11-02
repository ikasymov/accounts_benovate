from django.db import models

from django.conf import settings


class Transaction(models.Model):

    DECR = 'decrementation'
    ENCR = 'encrementation'

    TRANSACTION_ACTION = (
        (DECR, u"Списание"),
        (ENCR, u'Зачисление'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='transactions',
        on_delete=models.CASCADE
    )
    action = models.CharField(choices=TRANSACTION_ACTION, max_length=50)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
