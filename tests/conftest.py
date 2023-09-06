import pytest
from scripts.deploy_products import deploy_products

@pytest.fixture(scope="session", autouse=True)
def get_product_contract():
    return deploy_products()


@pytest.fixture(scope="session", autouse=True)
def dummyData():

    return {
           '47df8708e49e03bcdd763f331ebf5b4abff947ec5c6866d67647623cc8fafdad': [{
            'product_id': 'PROD8',
            'product_name': 'Door',
            'product_description': 'Good Door',
            'product_category': 'Furniture',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 240000.0,
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
            "price": 560000.0,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }],
            'b030f2e6e6901605fa5d467262213ecc4c403c83f1d67d0e977fd6d4e13cc869':[{
            'product_id': 'TEST10',
            'product_name': 'Bag',
            'product_description': 'Best Bag in world',
            'product_category': 'Items',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 900000.0,
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
            "price": 8900.0,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }]
    }