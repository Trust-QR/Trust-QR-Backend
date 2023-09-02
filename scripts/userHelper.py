from brownie import network,accounts,config
LOCAL_DEV_ENV = ["ganache-local", "development"]


def getAccount () :
    if network.show_active not in LOCAL_DEV_ENV:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

