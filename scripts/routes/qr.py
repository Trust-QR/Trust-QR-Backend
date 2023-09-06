from fastapi import APIRouter, Request
from starlette.responses import FileResponse
from tempfile import NamedTemporaryFile
import qrcode
# import json
from fastapi.responses import JSONResponse,RedirectResponse
import hashlib

qr = APIRouter(prefix="/api/qr",)

def generate_qr(double_encoded_identifier,data):
    # json_data = json.dumps(data)
    product_id=data['product_id']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    url=f'http://192.168.63.181:8070/product/qr/{double_encoded_identifier}/{product_id}'
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    with NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        img.save(temp_file.name)
        return temp_file.name


@qr.post("/generate")
async def generate_qr_endpoint(request: Request):
    
    try:

        identifier=request.headers.get('Identifier')
        sha256 = hashlib.sha256()
        sha256.update(identifier.encode('utf-8'))
        double_encoded_identifier=sha256.hexdigest()

        # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if is_user(identifier)==False:
        #     RedirectResponse('localhost:3000/login')

        json_data = await request.json()
        # json_data['price']='Rs. '+str(json_data['price'])

        qr_code_image_path = generate_qr(double_encoded_identifier,json_data)

        return FileResponse(qr_code_image_path, headers={
            "Content-Disposition": "attachment; filename=qrcode.png"
        })
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }
