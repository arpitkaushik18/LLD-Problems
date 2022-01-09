class Bill(object):
    def __init__(self):
        self.id = None
        self.groupId = None
        self.paidAmount = None
        self.contribution = {}
        self.split=None
        self.paidBy = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setGroupId(self, groupId):
        self.groupId = groupId

    def getGroupId(self):
        return self.groupId

    def setAmount(self, paidAmount):
        self.paidAmount = paidAmount

    def getAmount(self):
        return self.paidAmount

    def setContribution(self, contribution):
        self.contribution = contribution

    def getContribution(self):
        return self.contribution

    def setsplit(self,split):
        self.split=split
    def getsplit(self):
        return self.split

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getPaidBy(self):
        return self.paidBy



