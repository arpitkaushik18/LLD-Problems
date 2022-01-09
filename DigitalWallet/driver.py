

from controllers.user_controller import UserController
from controllers.wallet_controller import WalletController


from services.user_service import UserService
from services.wallet_service import WalletService

userController = UserController(UserService())
wallerController = WalletController(WalletService())


user1 = userController.addUser('Albus')
user2 = userController.addUser('harry')
user3 = userController.addUser('draco')
user4 = userController.addUser('Ron')
user5 = userController.addUser('Hermione')

wallet1 = wallerController.createWallet(200,user1)

wallet2 = wallerController.createWallet(200,user4)

wallerController.OverView()

wallerController.TransferMoney("ID1","ID4",200)

wallerController.Statement("ID1")


