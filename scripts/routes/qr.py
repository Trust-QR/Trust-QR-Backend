from fastapi import APIRouter, Request
from starlette.responses import FileResponse
from tempfile import NamedTemporaryFile
import qrcode
import json
from fastapi.responses import JSONResponse,RedirectResponse


qr = APIRouter(prefix="/qr",)

def generate_qr(data):
    json_data = json.dumps(data)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(json_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    with NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        img.save(temp_file.name)
        return temp_file.name


@qr.post("/generate")
async def generate_qr_endpoint(request: Request):
    
    try:

        identifier=request.headers.get('Identifier')

        # Add this Check !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # if is_user(identifier)==False:
        #     RedirectResponse('localhost:3000/login')

        json_data = await request.json()

        qr_code_image_path = generate_qr(json_data)

        return FileResponse(qr_code_image_path, headers={
            "Content-Disposition": "attachment; filename=qrcode.png"
        })
    
    except Exception as e:
        return {
            "success":"false",
            'error':str(e)
        }
