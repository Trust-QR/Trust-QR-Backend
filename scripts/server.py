from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from scripts.routes.signup import user_router
from scripts.routes.login import login_router
from scripts.routes.decode_qr import qr_router
from scripts.userDeploy import deploy_user

app = FastAPI()
app.state.Authentication = deploy_user()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(login_router)
app.include_router(qr_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post('/api/signup')
# def input_root(body:dict):
#     print(body['Email'])
#     print(body['Password'])



def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)
