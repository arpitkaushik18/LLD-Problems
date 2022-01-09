from services.bill_service_interface import BillServiceInterface
from models.Bill import Bill

class BillService(BillServiceInterface):
    billDetails = {}
    def addBill(self,id,groupId,paidAmount,contribution,split,paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(paidAmount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        bill.setsplit(split)
        self.__class__.billDetails[id] = bill
        return bill


