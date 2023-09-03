import pytest
from scripts.deploy_products import deploy_products

@pytest.fixture(scope="session", autouse=True)
def get_product_contract():
    return deploy_products()


@pytest.fixture(scope="session", autouse=True)
def dummyData():

    return {
           '9a89ec8fc502dd86d83ca4478779691ed0345747f166c44c7387c27c04c009db': [{
            'product_id': 'PROD8',
            'product_name': 'Door',
            'product_description': 'Good Door',
            'product_category': 'Furniture',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 240000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            },
            {
            'product_id': 'PROD9',
            'product_name': 'Game',
            'product_description': 'Best Game in the world',
            'product_category': 'IT',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2030',
            "date_of_manufacturing": '07/01/2010',
            "price": 560000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }],
            '48ddb93f0b30c475423fe177832912c5bcdce3cc72872f8051627967ef278e08':[{
            'product_id': 'TEST10',
            'product_name': 'Bag',
            'product_description': 'Best Bag in world',
            'product_category': 'Items',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 900000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            },
            {
            'product_id': 'Test11',
            'product_name': 'Bed',
            'product_description': 'Best Best in the Country',
            'product_category': 'Furniture',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2010',
            "date_of_manufacturing": '07/01/2070',
            "price": 8900,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }]
    }