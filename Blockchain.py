import time

class Blockchain(object):
    def __init__(self):
        super(Blockchain, self).__init__()
        # WARNING: there is a way nicer to store info
        self.wallets = []
        self.transactions = []

    def _null_everything(args):
        # WARNING: don't use without purpose
        self.wallets = []
        self.transactions = []
        exit(0)

    # will be used before startup
    def _initial(self):
        print("Started successfully!")
        pass

    def getInfo(self):
        info = "Number of wallets: " + \
        str(len(self.wallets)) + "\n" + \
         "Number of transactions: " + \
         str(len(self.transactions)) + "\n";
        return info

    def getMoreInfo(self):
        info = "\nWallets:\n"
        for wallet in self.wallets:
            #ascii art :)
            info += "===============\n"
            info += ("walletID: " + str(wallet.walletID) + "\n")
            info += ("balance: " + str(wallet.balance) + "\n")
            info += "===============\n\n"
        return info

GLOBAL_BLOCKCHAIN = Blockchain()

class Wallet(object):
    def __init__(self, balance, walletID):
        global GLOBAL_BLOCKCHAIN
        super(Wallet, self).__init__()
        self.balance = balance
        self.walletID = walletID
        GLOBAL_BLOCKCHAIN.wallets.append(self)

    def makeTransaction(to_id, sum):
        global GLOBAL_BLOCKCHAIN
        time_trans = time.time()
        GLOBAL_BLOCKCHAIN.append(Transaction(self.walletID, to_id, sum, time_trans))

class Transaction(object):
    def __init__(self, id_from, id_to, sum, time_trans):
        super(Transaction, self).__init__()
        self.id_to = id_to
        self.id_from = id_from
        self.sum = sum
        self.time_trans = time_trans
