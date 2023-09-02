from scripts.helper import get_account
from brownie import Products, network, config

def deploy_products():

    account=get_account()
    
    if len(Products)<=0:
        Products.deploy({'from':account},publish_source=config["networks"][network.show_active()].get("verify", False))

    contract=Products[-1]

    return contract

def add_product(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,key,contract=None,account=None):
    if contract== None:
        contract=deploy_products()
    
    if account == None:
        account=get_account()    

    if contract.checkProductExist(key):
      
        return {
            "success":"false",
            'msg':'Product ID Already Present'
        }
    
    txs=contract.addProduct(email,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,key,{'from':account})

    txs.wait(1)

    return {
            "success":"true",
            'msg':'Product Added'
        }

def list_all_products(email,contract=None):
    
    if contract== None:
        contract=deploy_products()

    res=contract.listProducts(email)

    return res


def get_detail_product(email,product_id,contract=None):

    if contract== None:
        contract=deploy_products()    
   
    res=contract.productDetail(email,product_id)

    return res

def main():
    email='abc@gmail.com'
    prod_id='PROD1'

    product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price = 'F14','5G Smarth Phone','Electronic','India','07/01/2040','07/01/2020',50000

    deploy_products()
    print('Contract Deployed')
    res=add_product(email,prod_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,email+prod_id)
    print(f'Product Added Res {res}')
    res=list_all_products(email)
    print(f'Product Listed {res}')
    res=get_detail_product(email,prod_id)
    print(f'Details of Product {res}')

    
