# Trust QR Backend

Trust QR is a platform that uses Blockchain technology and QR codes to combat counterfeiting. Companies can register their products on the platform, and each product will be assigned a unique QR code. Consumers can scan the QR code on a product to validate product authenticity, ensuring it matches the stated brand and providing manufacturing and expiry date details.

## About
This project is based on the Blockchain Technology.

## Tech Stack
We have used these following technologies

* Frontend : Next.js, CSS
* Backend : FastAPI
* Blockchain : Ganache & Brownie
* Testing : Pytest

# [Frontend](https://github.com/Trust-QR/Trust-QR-Frontend/)
# [Backend](https://github.com/Trust-QR/Trust-QR-Backend/)

# Cloning the project
To clone the project, open a terminal and navigate to the directory where you want to clone the project. Then, run the following command :
```bash
git clone https://github.com/Trust-QR/Trust-QR-Backend.git
```

# Installing Brownie
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

To install Brownie using `pipx` :
```bash
pipx install eth-brownie
```

# OR 

To install via `pip` :
```bash
pip install eth-brownie
```
For more info [Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)

# Installing FastAPI

To install FastAPI, open a terminal and run the following command :
```bash
pip install fastapi
```
For more info [FastApi](https://fastapi.tiangolo.com/)

Once you have installed `Brownie` and `FastAPI` you can start the backend by running the following command :
```bash
brownie run scripts/server.py
```
Run your Frontend :
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
