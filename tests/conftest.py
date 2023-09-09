import pytest
from scripts.deploy_products import deploy_products


@pytest.fixture(scope='session', autouse=True)
def testing_users():
    return {
        '9a89ec8fc502dd86d83ca4478779691ed0345747f166c44c7387c27c04c009db': '58d4b203ba5cdc03ec1f1d3e6837c5327d4be2a1d54ccac506f3ad22d3b8ead2',
        '87924606b4131a8aceeeae8868531fbb9712aaa07a5d3a756b26ce0f5d6ca674': '6763650f183eedbcca2f87f45b8175597ea70cba5d9d651db428447bd126a579',
        '48ddb93f0b30c475423fe177832912c5bcdce3cc72872f8051627967ef278e08': 'b186a1e47e904f69f4d4fcdbc9f22a1056493ccc9c81510b9d502b3b317c283d',
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
