from brownie import (
    accounts,
    network,
    config,
)


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    
    if index!=None:
        return accounts[index]
    if id!=None:
        return accounts.load(id).address
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts.add(config["wallets"]["dummy_key"])
    return accounts.add(config["wallets"]["from_key"])


def add_product(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,key,contract):
   
    if contract.checkProductExist(key):
      
        return {
            "success":"false",
            'msg':'Product ID Already Present'
        }
    
    txs=contract.addProduct(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,key,{'from':get_account()})

    txs.wait(1)

    return {
            "success":"true",
            'msg':'Product Added'
        }

def list_all_products(email,contract):
    
    res=contract.listProducts(email)

    return res


def get_detail_product(email,product_id,contract):

    res=contract.productDetail(email,product_id)

    return res

def insert_dummy_product_data(contract):
    dummyData={
           '9a89ec8fc502dd86d83ca4478779691ed0345747f166c44c7387c27c04c009db': [{
            'product_id': 'PROD1',
            'product_name': 'F14',
            'product_description': '5G Smarth Phone',
            'product_category': 'Electronic',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 50000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            },
            {
            'product_id': 'PROD2',
            'product_name': 'APple',
            'product_description': 'eatable',
            'product_category': 'Food',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2030',
            "date_of_manufacturing": '07/01/2010',
            "price": 70000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }],
            '48ddb93f0b30c475423fe177832912c5bcdce3cc72872f8051627967ef278e08':[{
            'product_id': 'TEST1',
            'product_name': 'LG Fridge',
            'product_description': 'Best Fridge in world',
            'product_category': 'Electronic',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2040',
            "date_of_manufacturing": '07/01/2020',
            "price": 100000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            },
            {
            'product_id': 'Test2',
            'product_name': 'FAN',
            'product_description': 'Fastest Fan in World',
            'product_category': 'Electronic',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2010',
            "date_of_manufacturing": '07/01/2070',
            "price": 8000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }],
            '87924606b4131a8aceeeae8868531fbb9712aaa07a5d3a756b26ce0f5d6ca674':[{
            'product_id': 'TEST3',
            'product_name': 'SHirt',
            'product_description': 'Best Shirt in world',
            'product_category': 'Clothing',
            'country_of_origin': 'India',
            "date_of_expiry": '07/01/2080',
            "date_of_manufacturing": '08/01/2020',
            "price": 10000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            },
            {
            'product_id': 'Test4',
            'product_name': 'CAR',
            'product_description': 'Fastest Car in World',
            'product_category': 'Automobile',
            'country_of_origin': 'USA',
            "date_of_expiry": '07/01/2010',
            "date_of_manufacturing": '07/01/2070',
            "price": 1000000,
             "urls":["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]

            }]

    }

    for k in dummyData:
        for e in dummyData[k]:
            res = add_product(k, e['product_id'], e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'], e['urls'],k+e['product_id'], contract)