

# scope="session" will open the thing once, making the object available to all test scripts in the directory

import pytest
import json


@pytest.fixture(scope="session")
def read_config():
    with open("data/example_data.json") as f:
        config = json.load(f)
    return config

# test/test_code1.py
def test1(read_config):
    assert read_config == {}

def test2(read_config):
    assert read_config == {}


