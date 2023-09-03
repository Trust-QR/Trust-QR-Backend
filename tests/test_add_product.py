from scripts.helper import add_product

def test_add_product(get_product_contract,dummyData):
    

    for k in dummyData:
        for e in dummyData[k]:
            res = add_product(k, e['product_id'], e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'], k+e['product_id'], get_product_contract)

        assert res['success'] == 'true', f'Error in Adding Product with Data {e}'


def test_not_add_product(get_product_contract,dummyData):
    

    for k in dummyData:
        for e in dummyData[k]:
            res = add_product(k, e['product_id'], e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'], k+e['product_id'], get_product_contract)

        assert res['success'] == 'false', f'Error in Adding Product with Data {e}'