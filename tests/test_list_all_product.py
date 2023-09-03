
from scripts.deploy_products import list_all_products

def test_all_product(get_product_contract,dummyData):

    for k in dummyData:
       
        res = list_all_products(k, get_product_contract)
        temp=[]

        for e in dummyData[k]:
           
                temp.append( [e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'],e['urls']])

        assert res[2:]==temp, 'ERROR In Listing All Products : Res and Acutal Details are {res} and {temp}'