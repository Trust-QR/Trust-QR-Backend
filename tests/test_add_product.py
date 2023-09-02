from scripts.deploy_products import add_product


def test_add_product(getContract,dummyData):
    

    for k in dummyData:
        for e in dummyData[k]:
            res = add_product(k, e['product_id'], e['product_name'], e['product_description'], e['product_category'],
                            e['country_of_origin'], e['date_of_expiry'], e['date_of_manufacturing'], e['price'], k+e['product_id'], getContract)

        assert res['success'] == 'true', f'Error in Adding Product with Data {e}'
