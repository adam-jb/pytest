



# pytest      (this is all you need to type in CLI for the tests to run)

# prefix our test function names with test_, since this is what pytest expects our test functions to be named.

# Pytest expects our tests to be located in files whose names begin with test_ or end with _test.py.

import pytest



def capital_case(x):
    return x.capitalize()


# modifying capital_case() to capture types of errors
def capital_case(x):
	if not isinstance(x, str):
		raise TypeError('Please provide a string argument')
	return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_a():
	assert 'a' == 'a'



# pytest.raises(TypeError) may somehow specify the type of error pytest is expecting, yet if you force a different error 
# (eg: 1/0 for a zero division error), it will throw the appropriate error (eg: zero division error)
# I think the below means if capital_case throws a typeError pytest will treat it as a pass (ie, this is an intentionally specified error for the function to return)
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)




# this test passes: it treats a ZeroDivisionError something you explicitly handle
# if you used a different kind of error the test would fail
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

