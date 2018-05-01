import Blockchain as bc

_last_id = -1

def createWallet():
    global _last_id
    _last_id += 1
    return bc.Wallet(0, _last_id)

def main():
    bc.GLOBAL_BLOCKCHAIN._initial()
    print(bc.GLOBAL_BLOCKCHAIN.getInfo())

if __name__ == '__main__':
    #This is startiong point
    main()
