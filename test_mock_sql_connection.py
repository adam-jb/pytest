
# Code to mock connection to a SQL database

# based on https://smirnov-am.github.io/pytest-testing_database/

import pytest
import sqlite3



# CacheService is a wrapper around 'session', adding methods
class CacheService:
    def __init__(self, session): # 1
        self.session = session # 2

    def get_status(self, number):
        self.session.execute('SELECT existing FROM numbers WHERE number=?', (number,))
        return self.session.fetchone()

    def save_status(self, number, existing):
        self.session.execute('INSERT INTO numbers VALUES (?, ?)', (number, existing))
        self.session.connection.commit()

    def generate_report(self):
        self.session.execute('SELECT COUNT(*) FROM numbers')
        count = self.session.fetchone()
        self.session.execute('SELECT COUNT(*) FROM numbers WHERE existing=1')
        count_existing = self.session.fetchone()
        return count_existing[0]/count[0]



# Creates an sqlite database in memory, acting as a context manager
@pytest.fixture
def session(): # 1
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()


# add a table and a row to the session db
@pytest.fixture(autouse=True)
# autouse = True: means all tests in this script automatically load this fixture, 
                 # so no need for '@pytest.mark.usefixtures("setup_db")' in any tests below
# use 'scope' parameter of pytest.fixture to change which tests specifically get the fixture automatically
def setup_db(session): # 2
    session.execute('''CREATE TABLE numbers
                          (number text, existing boolean)''')
    session.execute('INSERT INTO numbers VALUES ("+3155512345", 1)')
    session.connection.commit()

    # to print rows in table. Not necessary at all
    """
	db_session.execute("SELECT * FROM numbers")
	rows = db_session.fetchall()
	for row in rows:
	    print(row)
	"""


# Making an instance of CacheService
@pytest.fixture
def cache(session): # 1
    return CacheService(session)



#### Running tests ####

# calls the database which has a table with one line of data in it, as made in the setup_db() fixture
def test_get(cache): # 2
    existing = cache.get_status('+3155512345')
    assert existing


# Checks a number exists in a database (accessed via 'session' fixture)
def test_get(cache): # 1
    existing = cache.get_status('+3155512345') # 3
    assert existing


# Checks a number doesn't exist in a database
def test_get_unknown(cache):
    assert cache.get_status('+315554444') is None

# Saves a number and checks it's there
def test_save(cache):
    number = '+3155512346'
    cache.save_status(number, True)
    existing = cache.get_status(number)
    assert existing

# Record more values and test ratio of True/False values
def test_report(cache):
    cache.save_status('+3155512346', True)
    cache.save_status('+3155512347', False)
    cache.save_status('+3155512348', False)
    ratio = cache.generate_report()
    assert ratio == 0.5




##### Simpler method: MagicMock() makes a generic mock thing which can act as a session and executor (you still need to
####      define the CacheService class and it's methods)

from unittest.mock import MagicMock

def test_get_mock():
    session = MagicMock() 
    executor = MagicMock()
    session.execute = executor
    cache = CacheService(session) # 2
    cache.get_status('+3155512345')
    executor.assert_called_once_with('SELECT existing FROM numbers WHERE number=?', ('+3155512345',)) # 3

## MagicMock is a Mock class with magic methods included

























