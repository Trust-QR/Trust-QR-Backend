from fastapi import APIRouter
from fastapi import Request
from scripts.routes.encoding import encrypt, is_valid_email
from scripts.userDeploy import validateUser


# APIRouter creates path operations for user module

login_router = APIRouter(prefix='/api/users',)


@login_router.post('/login')
async def Signup(request: Request):
    credentials = await request.json()
    user = credentials['Email']
    password = credentials['Password']

    if is_valid_email(user) == False:
        return ({'id': 'Invalid Username or Password'})

    # print(f"user : {user}  Password : {password}")

    encoded_user = encrypt(user)
    encoded_password = encrypt(password)

    user_contract = request.app.state.Authentication
    # print(user_contract)
    # print('isUser : ',isUser(user_contract, encoded_user))
    contract_response = validateUser(encoded_user, encoded_password, user_contract)
    response = {'id': False}
    if contract_response['success']:
        response['id'] = encoded_user

    print(response)
    return (response)
