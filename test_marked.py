

### run all tests marked as 'a_big_test'
# pytest -m a_big_test


### run all tests NOT marked as 'a_big_test'
# pytest -m "not a_big_test"


import pytest
from wallet import Wallet, InsufficientAmount


@pytest.mark.a_big_test            # gives marker to test. Used for category of testing
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0




@pytest.mark.a_big_test
@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

