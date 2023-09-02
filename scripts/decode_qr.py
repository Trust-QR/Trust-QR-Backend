import cv2
from pyzbar.pyzbar import decode

# Load the QR code image
qr_code_image = cv2.imread('qrcode.png')

# Decode the QR code
decoded_objects = decode(qr_code_image)

# Iterate over the decoded objects
for obj in decoded_objects:
    print(f'Type: {obj.type}')
    print(f'Data: {obj.data.decode("utf-8")}')
