from scripts.helper import get_account,insert_dummy_product_data,add_product,list_all_products,get_detail_product
from brownie import Products, network, config

def deploy_products():

    account=get_account()
    
    contract=Products.deploy({'from':account},publish_source=config["networks"][network.show_active()].get("verify", False))

    insert_dummy_product_data(contract)

    return contract

def main():
    # email='abc@gmail.com'
    # prod_id='PROD1'
    # urls=["https://img.freepik.com/free-photo/purple-osteospermum-daisy-flower_1373-16.jpg?size=626&ext=jpg","https://img.freepik.com/free-photo/yellow-flower-white-background_1203-2149.jpg?size=626&ext=jpg"]
    # product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price = 'F14','5G Smarth Phone','Electronic','India','07/01/2040','07/01/2020',50000

    contract=deploy_products()
    print('Contract Deployed')

    # res=add_product(email,prod_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,email+prod_id,contract)
    # print(f'Product Added Res {res}')
    # res=list_all_products(email,contract)
    # print(f'Product Listed {res}')
    # res=get_detail_product(email,prod_id,contract)
    # print(f'Details of Product {res}')

    
