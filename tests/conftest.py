import pytest
from scripts.deploy_products import deploy_products


@pytest.fixture(scope='session', autouse=True)
def testing_users():
    return {
        'abhishekkumar232105@gmail.com': 'Abc123@',
        'huntingcoder7.me@gmail.com': 'Cbd123@',
        'abc@gmail.com': 'aBc123@',
        'example@gmail.com': 'Example123@',
        'xyz@gmail.com': 'xYz123@',
    }


@pytest.fixture(scope="session", autouse=True)
def getContract():
    return deploy_products()


@pytest.fixture(scope="session", autouse=True)
def dummyData():

    return {
        'a7coder@gmail.com': [{
            'product_id': 'PROD1',
            'product_name': 'F14',
            'product_description': '5G Smarth Phone',
            'product_category': 'Electronic',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 50000

        },
            {
            'product_id': 'PROD2',
            'product_name': 'APple',
            'product_description': 'eatable',
            'product_category': 'Food',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2030',
            "date_of_manufacturing": '07/01/2010',
            "price": 70000

        }],
        'abc@gmail.com': [{
            'product_id': 'TEST1',
            'product_name': 'LG Fridge',
            'product_description': 'Best Fridge in world',
            'product_category': 'Electronic',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 100000

        },
            {
                'product_id': 'Test2',
                'product_name': 'FAN',
                'product_description': 'Fastest Fan in World',
                'product_category': 'Electronic',
                'country_of_origin': 'India',
                "date_of_expiry": '07/01/2010',
                "date_of_manufacturing": '07/01/2070',
                "price": 8000

        }]

    }
