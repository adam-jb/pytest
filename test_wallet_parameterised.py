


import pytest
from wallet import Wallet, InsufficientAmount
import numpy as np


# makes combinations of inputs, each of which will be piped to the functions that use them
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected




## Making inputs for this function
test_amounts = [20, 30, 40, 50, 60]
@pytest.mark.parametrize("input_amount", test_amounts)
def test_wallet_creation(input_amount):
	wallet = Wallet(input_amount)
	assert wallet.balance == input_amount




## Making inputs for this function with numpy
test_amounts = np.random.randint(1, 10, size = 10)
@pytest.mark.parametrize("input_amount", test_amounts)
def test_wallet_creation(input_amount):
	wallet = Wallet(input_amount)
	assert wallet.balance == input_amount




## Can call fixtures in combination with parametrize()
@pytest.fixture
def the_wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(0)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(the_wallet, earned, spent, expected):
    the_wallet.add_cash(earned)
    the_wallet.spend_cash(spent)
    assert the_wallet.balance == expected







## Can test every combination of multiple 1. input functions, and 2. input data
def average(n1, n2):
    return (n1 + n2) / 2

def perc_difference(n1, n2):
    return (n2 - n1)/n1 * 100

# Test the combinations of operations and inputs
@pytest.mark.parametrize("operation", [average, perc_difference])
@pytest.mark.parametrize("n1, n2", [(1, 2), (2, 3)])
def test_is_float(operation, n1, n2):
    assert isinstance(operation(n1, n2), float)
















