

# to make instances of objects which can be called by subsequent tests, make functions which create them, decorated with @pytest.fixture

# Utilizing fixtures helps us de-duplicate our code. 
# If you notice a case where a piece of code is used repeatedly in a number of tests, that might be a good candidate to use as a fixture.

# based on https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

## to view fixtures which will be created:
# pytest --fixtures


import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance: This is the docstring which will be shown when running "pytest --fixtures"'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)



def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
