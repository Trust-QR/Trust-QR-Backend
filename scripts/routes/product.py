from fastapi import APIRouter,Request
from  ..helper import add_product,get_detail_product,list_all_products
from fastapi.responses import JSONResponse,RedirectResponse
from datetime import datetime
import hashlib

product = APIRouter(prefix="/api/product",)


@product.post("/add")
async def addProduct(request: Request):

    identifier=request.headers.get('Identifier')

    # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if isUser(identifier)==False:
        return  {
            "success": "false",
            "error": "You aren't Authorised"
        }

    sha256 = hashlib.sha256()
    sha256.update(identifier.encode('utf-8'))
    double_encoded_identifier=sha256.hexdigest()    

    json_data = await request.json()
    json_data=json_data['formData']

    product_contract=request.app.state.product_contract
    product_id = json_data["product_id"]
    product_name = json_data["product_name"]
    product_description = json_data["product_description"]
    product_category = json_data["product_category"]
    country_of_origin = json_data["country_of_origin"]
    date_of_expiry_str = json_data["date_of_expiry"]
    date_of_manufacturing_str = json_data["date_of_manufacturing"]
    price = float(json_data["price"])*100
    urls = json_data["urls"]

    date_of_manufacturing = datetime.strptime(date_of_manufacturing_str, "%Y-%m-%d")
    date_of_expiry = datetime.strptime(date_of_expiry_str, "%Y-%m-%d")

    # Check if date_of_manufacturing is before date_of_expiry
    if date_of_manufacturing > date_of_expiry:
        # Handle the case where date_of_manufacturing is not before date_of_expiry
        return {
            "success": "false",
            "error": "Date of manufacturing must be before the date of expiry."
        }
    date_of_manufacturing_day= str(date_of_manufacturing.day)
    if len(date_of_manufacturing_day)==1:
        date_of_manufacturing_day='0'+date_of_manufacturing_day

    date_of_manufacturing_month= str(date_of_manufacturing.month)
    if len(date_of_manufacturing_month)==1:
        date_of_manufacturing_month='0'+date_of_manufacturing_month

    date_of_expiry_day= str(date_of_expiry.day)
    if len(date_of_expiry_day)==1:
        date_of_expiry_day='0'+date_of_expiry_day

    date_of_expiry_month= str(date_of_expiry.month)
    if len(date_of_expiry_month)==1:
        date_of_expiry_month='0'+date_of_expiry_month
    


    date_of_manufacturing_str=f'{date_of_manufacturing_day}/{date_of_manufacturing_month}/{date_of_manufacturing.year}'
    date_of_expiry_str=f'{date_of_expiry_day}/{date_of_expiry_month}/{date_of_expiry.year}'

    
    key=double_encoded_identifier+product_id

    try:

        return JSONResponse(add_product(double_encoded_identifier,product_id,product_name,product_description,product_category,country_of_origin,date_of_expiry_str,date_of_manufacturing_str,price,urls,key,product_contract))

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
        if isUser(identifier)==False:
            return  {
                "success": "false",
                "error": "You aren't Authorised"
            }


        sha256 = hashlib.sha256()
        sha256.update(identifier.encode('utf-8'))
        double_encoded_identifier=sha256.hexdigest()

        
        product_contract=request.app.state.product_contract

        return JSONResponse(list_all_products(double_encoded_identifier,product_contract))
    
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
        if isUser(identifier)==False:
            return  {
                "success": "false",
                "error": "You aren't Authorised"
            }

        sha256 = hashlib.sha256()
        sha256.update(identifier.encode('utf-8'))
        double_encoded_identifier=sha256.hexdigest()

        product_contract=request.app.state.product_contract

        product_id = request.headers.get('ProductID')

        return JSONResponse(get_detail_product(double_encoded_identifier,product_id,product_contract))
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }
    
@product.get("/qr-detail/{double_encoded_identifier}/{product_id}")
async def getQRDetailProduct(double_encoded_identifier,product_id,request: Request):
    try:
        # double_encoded_identifier=request.headers.get('Identifier')
       
        product_contract=request.app.state.product_contract

        return JSONResponse(get_detail_product(double_encoded_identifier,product_id,product_contract))
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }