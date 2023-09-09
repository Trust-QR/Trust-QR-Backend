from scripts.helper import inser_dummy_users, get_account, isUser
from brownie import (
    network,
    config,
    Authentication,
)


def deploy_user():
    account = get_account()
    contract = Authentication.deploy(
        {'from': account}, publish_source=config['networks'][network.show_active()].get('verify'))
    inser_dummy_users(account, contract)
    return contract


def add_newUser(user, passw, contract):
    account = get_account()
    if contract.isUserExists(user):
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


def validateUser(user, password, contract):
    account = get_account()
    if contract.isUserExists(user):
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

    # user, password = '9a89ec8fc502dd86d83ca4478779691ed0345747f166c44c7387c27c04c009db', '58d4b203ba5cdc03ec1f1d3e6837c5327d4be2a1d54ccac506f3ad22d3b8ead2'
    contract = deploy_user()
    print('Contract Deployed')
    # print(f'Adding new user : {add_newUser(user, password, contract)}')
    # v_user, v_password = '6f49813dffbb18566591b9e520941c1a1e98652531c82d7d52d612ab15b7d620', 'fe7a99dca65dcdbfa1561241afd3a967b52c2367fbfecff441171f51977ac783'
    # print(f'Validating user :  {validateUser(v_user, v_password, contract)}')

    # print(f'Checking user Existance : {isUser(contract, v_user)}')
