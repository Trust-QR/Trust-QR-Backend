from scripts.userDeploy import validateUser
from scripts.helper import deploy_user

def testValidUser(testing_users):
    contract = deploy_user()
    for x_user, x_user_pass in testing_users.items() :
        ans = validateUser(x_user, x_user_pass, contract)
        assert ans['success'] == True, f'Error occured during adding user {x_user} : {ans["msg"]}'

