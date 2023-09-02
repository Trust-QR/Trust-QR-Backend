
from scripts.deploy_products import get_detail_product


def test_get_detail_product(getContract,dummyData):
    
    for k in dummyData:

        for e in dummyData[k]:
           
            res = get_detail_product(k, e['product_id'], getContract)

            temp=[ e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'], ]
            
                
            assert res== temp, f'ERROR In GEt Deatil Product : Res and Acutal Details are {res} and {temp}'
        
