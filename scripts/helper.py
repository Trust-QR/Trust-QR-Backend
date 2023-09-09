from brownie import (
    accounts,
    network,
    config,
    Authentication,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    # accounts[0]
    # accounts.add("env")
    # accounts.load("id")
    if index != None:
        return accounts[index]
    if id != None:
        return accounts.load(id).address
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts.add(config["wallets"]["dummy_key"])
    return accounts.add(config["wallets"]["from_key"])



def inser_dummy_users(account, contract):
    users = {
        '4402e59c33140da1dc542132c371f78f119554d33aeb38072f786d12d64c9d15': 'fe7a99dca65dcdbfa1561241afd3a967b52c2367fbfecff441171f51977ac783',
        '9a89ec8fc502dd86d83ca4478779691ed0345747f166c44c7387c27c04c009db': '58d4b203ba5cdc03ec1f1d3e6837c5327d4be2a1d54ccac506f3ad22d3b8ead2',
        '87924606b4131a8aceeeae8868531fbb9712aaa07a5d3a756b26ce0f5d6ca674': '6763650f183eedbcca2f87f45b8175597ea70cba5d9d651db428447bd126a579',
        '48ddb93f0b30c475423fe177832912c5bcdce3cc72872f8051627967ef278e08': 'b186a1e47e904f69f4d4fcdbc9f22a1056493ccc9c81510b9d502b3b317c283d',
    }
    for user, passw in users.items():
        transation = contract.addUser(user, passw, {'from': account})
        transation.wait(1)

def isUser(contract, user_id):
    if contract.isUserExists(user_id) :
        return True
    return False


# crytojs SHA256
