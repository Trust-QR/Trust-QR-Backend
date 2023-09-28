from scripts.userDeploy import add_newUser
from scripts.helper import deploy_user

def testAddUser(testing_users):
    contract = deploy_user()
    for x_user, x_user_pass in testing_users.items() :
        ans = add_newUser(x_user, x_user_pass, contract)
        assert ans['success'] == False, f'Error occured during adding user {x_user}'
