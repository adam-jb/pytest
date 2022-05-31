

# run a function multiple times (1000 times in this case)

# requires pip3 install pytest-repeat

import pytest 
import random 

def generate_numbers():
    return random.randint(1, 100)

@pytest.mark.repeat(1000)
def test_generate_numbers():
    assert generate_numbers() >= 1 and generate_numbers() <= 100


