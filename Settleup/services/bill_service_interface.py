import abc
class BillServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addBill(self,id,groupId,paidAmount,contribution,split,paidBy):
		pass