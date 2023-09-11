from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from scripts.routes.qr import qr
from scripts.routes.product import product
from scripts.deploy_products import deploy_products
from scripts.routes.signup import user_router
from scripts.routes.login import login_router
from scripts.routes.decode_qr import qr_router
from scripts.userDeploy import deploy_user


app = FastAPI()
app.state.Authentication = deploy_user()

app.state.product_contract=deploy_products()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(qr)
app.include_router(product)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(qr_router)

@app.get("/api/hello")
async def root():
    return {"message": "Hello World"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
