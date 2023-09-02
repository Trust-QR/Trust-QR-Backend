from scripts.userDeploy import add_newUser

def testAddUser(testing_users):
    for x_user, x_user_pass in testing_users.items() :
        ans = add_newUser(x_user, x_user_pass)
        assert ans['success'] == True, f'Error occured during adding user {x_user}'
