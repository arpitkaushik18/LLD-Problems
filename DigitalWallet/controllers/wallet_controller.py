class WalletController(object):
    def __init__(self,WalletService):
        self.WalletService = WalletService

    def createWallet(self, amount, user):
        return self.WalletService.create_wallet(amount,user)

    def TransferMoney(self, user1, user2, amount):
        if(amount < 0.0001):
            return "Invaid Amount"
        elif(self.WalletService.walletDetail[user1].get_Amount()<amount):
            return "Insufficent Amount"
        else:
            self.WalletService.walletDetail[user1].Amount -= amount
            self.WalletService.walletDetail[user2].Amount += amount

            self.WalletService.walletDetail[user1].TransactionHistory.append("Debit " + user2 + " " + str(amount))
            self.WalletService.walletDetail[user2].TransactionHistory.append("Credit " + user1 + " " + str(amount))



    def OverView(self):
        for wallet in self.WalletService.walletDetail:
            Wallet = self.WalletService.walletDetail.get(wallet)
            print(Wallet.WalletId + " " + str(Wallet.Amount))

    def Statement(self,id):
        for Transaction in self.WalletService.walletDetail[id].TransactionHistory:
            print(Transaction)


