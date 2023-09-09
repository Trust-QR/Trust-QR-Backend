from fastapi import APIRouter
from fastapi import UploadFile
from pyzbar.pyzbar import decode
from PIL import Image
import io


# APIRouter creates path operations for user module

qr_router = APIRouter(prefix='/api/product',)


@qr_router.post('/upload')
async def getProductDetails(file: UploadFile) :
    
    print(f'len : {file.filename}')

    if file.filename == '':
        return "No selected file"
    imageBytes = await file.read()
    image = Image.open(io.BytesIO(imageBytes))
    qr_code = decode(image)
    ans = {'url':False}
    if qr_code:
        # print(f"Data : {qr_code[0].data.decode('utf-8')}")
        ans['url'] = qr_code[0].data.decode('utf-8')
    
    print(ans)
    return ans
    
