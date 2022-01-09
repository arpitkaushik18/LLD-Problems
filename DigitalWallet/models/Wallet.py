

class Wallet():
    def __init__(self, Amount):
        self.Amount = Amount
        self.TransactionHistory = []
        self.WalletId = None

    def get_Amount(self):
        return self.Amount

    def get_transaction_history(self):
        return self.TransactionHistory

    