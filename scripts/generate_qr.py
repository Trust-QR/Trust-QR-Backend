import qrcode

data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "+1234567890",
}

import json
json_data = json.dumps(data)

# Generate a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(json_data)
qr.make(fit=True)

# Create a PIL (Python Imaging Library) image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save or display the QR code image
img.save("qrcode.png")
# img.show()


