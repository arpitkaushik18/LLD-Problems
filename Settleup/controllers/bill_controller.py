class BillController(object):
    def __init__(self, billService):
        self.billService = billService

    def addBill(self,id,groupId,paidAmount,contribution,split,paidBy):
        return self.billService.addBill(id,groupId,paidAmount,contribution,split,paidBy)

    def splitBill(self, userId):
        balance = 0
        print(self.billService.billDetails)
        for billId in self.billService.billDetails:
            bill = self.billService.billDetails.get(billId)
            print(bill.getContribution())
            if(userId==bill.getPaidBy()):
                return "User Requried Money from All"
            else:
                if(bill.getsplit()=="Exact"):
                    balance+=bill.getContribution().get(userId)
                elif(bill.getsplit()=="Equal"):
                    balance+=bill.getAmount()/len(bill.getContribution())
                else:
                    balance+=(bill.getAmount()*bill.getContribution().get(userId))/100
        return balance



