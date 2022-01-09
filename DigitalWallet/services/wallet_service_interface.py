import abc

class WalletServiceInterface(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def create_wallet(self,amount,user):
       pass
   