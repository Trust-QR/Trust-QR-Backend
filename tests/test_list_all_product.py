
from scripts.deploy_products import list_all_products

def test_all_product(getContract,dummyData):

    for k in dummyData:
       
        res = list_all_products(k, getContract)
        temp=[]

        for e in dummyData[k]:
           
                temp.append( [e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price']])

    
        assert res==temp, 'ERROR In Listing All Products : Res and Acutal Details are {res} and {temp}'