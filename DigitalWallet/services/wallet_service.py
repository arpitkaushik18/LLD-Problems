from models.Wallet import Wallet
from services.wallet_service_interface import WalletServiceInterface

class WalletService(WalletServiceInterface):
    walletDetail = {}

    def create_wallet(self,amount,user):
        wallet = Wallet(amount)
        wallet.WalletId = user.id

        self.__class__.walletDetail[wallet.WalletId] = wallet
        return wallet
