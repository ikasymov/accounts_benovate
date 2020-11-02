# accounts_benovate

**accounts** - сервис для перевода средств между счетами.

**Stack**: 
1. language - python (version 3.8) 
2. framework - django (version 2.1)
3. Database - PostgreSQL (version 12)


# Пример использование
 ```python
from accounts.containers import PutMoneyIntoAccounts

container = PutMoneyIntoAccounts()
container.init(from_user_id, 100, list(to_user_id)).put()

# to many_users

container.init(
    from_user_id, 
    100, 
    list(to_user_id, to_second_user_id)
).put()
```
# Пример использование в views:

```python
from django import forms

from accounts.models import MainUser
from accounts.containers import PutMoneyIntoAccounts


class PutMoneyForm(forms.Form):
    from_user = forms.ModelChoiceField(queryset=MainUser.objects.all())
    to_user = forms.ModelChoiceField(queryset=MainUser.objects.all())
    amount = forms.DecimalField()


def put_money_view(request):
    form = PutMoneyForm(request.POST)
    if form.is_valid():
        container = PutMoneyIntoAccounts()
        container.init(
            form.cleaned_data['from_user'].id,
            form.cleaned_data['amount']
            [form.cleaned_data['to_user'].id]
        ).put()
```
