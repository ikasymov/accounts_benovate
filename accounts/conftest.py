import pytest

from .models import MainUser


@pytest.fixture
def create_user():
    def create(username, ident_code):
        return MainUser.objects.create_user(username=username,
                                            ident_code=ident_code)
    return create
