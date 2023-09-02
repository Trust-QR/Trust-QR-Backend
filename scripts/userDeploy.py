from brownie import network, Authentication, config
from scripts.userHelper import getAccount


def get_contract():
    account = getAccount()
    if len(Authentication) <= 0:
        Authentication.deploy(
            {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    contract = Authentication[-1]
    return contract


def add_newUser(user, passw):
    account = getAccount()
    contract = get_contract()
    if contract.isUserExists(user, {'from': account}):
        return {
            'success': False,
            'msg': 'User already exist'
        }

    transation = contract.addUser(user, passw, {'from': account})
    transation.wait(1)
    return {
        'success': True,
        'msg': 'User Created'
    }


def validateUser(user, password):
    account = getAccount()
    contract = get_contract()
    if contract.isUserExists(user, {'from': account}):
        contract_password = contract.validateUser.call(user, {'from': account})
        if (contract_password == password):
            return {
                'success': True,
                'msg': 'Valid User'
            }
    
        return {
                'success': False,
                'msg': 'Password Missmatch'
            }
    
    return {
            'success': False,
            'msg': 'User does Not exists'
        }
    


def main():
    user, password = 'abhishekkumar232105@gmail.com', 'Abc123'
    # print(add_newUser(user, password))
    print(f'{validateUser(user, password)} : user')
