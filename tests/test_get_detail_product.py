
from scripts.deploy_products import get_detail_product


def test_get_detail_product(get_product_contract,dummyData):
    
    for k in dummyData:

        for e in dummyData[k]:
           
            res = get_detail_product(k, e['product_id'], get_product_contract)

            temp=[e['product_id'], e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'],e['urls'] ]
            
                
            assert res== temp, f'ERROR In GEt Deatil Product : Res and Acutal Details are {res} and {temp}'
        
