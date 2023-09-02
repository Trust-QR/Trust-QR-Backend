import pytest
from scripts.userDeploy import get_contract




@pytest.fixture(scope='session', autouse=True)
def testing_users():
    return {
        'abhishekkumar232105@gmail.com': 'Abc123@',
        'huntingcoder7.me@gmail.com': 'Cbd123@',
        'abc@gmail.com': 'aBc123@',
        'example@gmail.com': 'Example123@',
        'xyz@gmail.com': 'xYz123@',
    }
