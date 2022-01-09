

from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.user_service import UserService
from services.group_service import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())


user1 = userController.addUser('user1','pawan')
user2 = userController.addUser('user2','gyan')
user3 = userController.addUser('user3','abhi')
user4 = userController.addUser('user4','nishant')
user5 = userController.addUser('user5','ds')

members = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','avengers',members)


contribution = {'user1': 0,'user2':10,'user3':10,'user4':10,'user5':70}

bill1 = billController.addBill('bill1','group1',500,contribution,"percent","user1")

balance = billController.splitBill('user2')
print (balance)