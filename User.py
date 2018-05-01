class User(object):
    def __init__(self, username, HPass, wallet):
        super(User, self).__init__()
        self.username = username
        self.HPass = HPass
        self.wallet = wallet #wallet object

    def getInfo():
        info += "\nUsername: " + str(self.username) +\
        "\nwalletID" + str(self.wallet.walletID)
