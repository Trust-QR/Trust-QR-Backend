from fastapi import APIRouter,Request
from  ..helper import add_product,get_detail_product,list_all_products
from fastapi.responses import JSONResponse,RedirectResponse

product = APIRouter(prefix="/product",)

@product.post("/add")
async def addProduct(request: Request):

    identifier=request.headers.get('Identifier')

    # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # if is_user(identifier)==False:
    #     RedirectResponse('localhost:3000/login')

    json_data = await request.json()

    product_contract=request.app.state.product_contract
    
    product_id = json_data["product_id"]
    product_name = json_data["product_name"]
    product_description = json_data["product_description"]
    product_category = json_data["product_category"]
    country_of_origin = json_data["country_of_origin"]
    date_of_expiry = json_data["date_of_expiry"]
    date_of_manufacturing = json_data["date_of_manufacturing"]
    price = json_data["price"]
    urls = json_data["urls"]

    key=identifier+product_id

    try:

        return JSONResponse(add_product(identifier,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry,date_of_manufacturing,price,urls,key,product_contract))

    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }


@product.get("/all")
async def getAllProduct(request: Request):

    try:
        identifier=request.headers.get('Identifier')

        # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if is_user(identifier)==False:
        #     RedirectResponse('localhost:3000/login')


        product_contract=request.app.state.product_contract

        return JSONResponse(list_all_products(identifier,product_contract))
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }



@product.get("/detail")
async def getDetailProduct(request: Request):
    try:
        identifier=request.headers.get('Identifier')

        # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if is_user(identifier)==False:
        #     RedirectResponse('localhost:3000/login')

        product_contract=request.app.state.product_contract

        product_id = request.headers.get('ProductID')

        return JSONResponse(get_detail_product(identifier,product_id,product_contract))
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }