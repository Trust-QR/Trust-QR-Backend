from scripts.userDeploy import validateUser

def testValidUser(testing_users):
    for x_user, x_user_pass in testing_users.items() :
        ans = validateUser(x_user, x_user_pass)
        assert ans['success'] == True, f'Error occured during adding user {x_user} : {ans["msg"]}'
