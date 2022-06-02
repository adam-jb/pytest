

# fixture functions in a file called "conftest.py" will be discoverable by other test scripts in the directory

# Makes a mock API to test against

# based on https://smirnov-am.github.io/pytest-testing_http_client/


import requests
from urllib.parse import quote
import pytest
import responses

class NumberValidationException(Exception):
    pass



# Code snippet to catch HTTPError from requests
def check_existence(number):
    try:
        response = requests.get('http://127.0.0.1:8080/', params={'number': number}) 
        response.raise_for_status() 
        return response.json()['exists'] 
    except (requests.exceptions.HTTPError, KeyError) as e:
        raise NumberValidationException('something went wrong when calling api') from e




# Make mock API at URL 'http://127.0.0.1:8080' which can handle three example input numbers
@pytest.fixture
def api_response():   
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number='+quote('+31'), 
                 json={'exists': False}, status=200)
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number=' + quote('+3155512345'),
                 json={'exists': True}, status=200)
        rsps.add(responses.GET, 'http://127.0.0.1:8080/?number=' + quote('+311234555'),
                 json={'exists': True}, status=200)
        yield rsps 


# Send number to mock API
@pytest.mark.usefixtures("api_response")
def test_non_existing_number_responses_fixture():
    number = '+31'
    assert not check_existence(number)


















