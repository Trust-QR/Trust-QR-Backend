from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.routes.qr import qr
from scripts.routes.product import product
import uvicorn
from scripts.deploy_products import deploy_products

app = FastAPI()
app.state.product_contract=deploy_products()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qr)
app.include_router(product)


@app.get("/api/hello")
async def root():
    return {"message": "Hello World"}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

 