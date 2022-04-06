class Transaction:
    def __init__(self, inAmount=0.0, inCode='D', inNote="No Note"):
        self.__Amount = 0.0;
        self.setAmount(inAmount)
        self.__Code = 'D';
        self.setCode(inCode)
        self.__Note = "No Note"
        self.setNote(inNote)

    def setAmount(self, newAmount):
        self.__Amount = newAmount if newAmount >= 0.0 else self.__Amount

    def getAmount(self):
        return self.__Amount

    def setCode(self, newCode):
        self.__Code = newCode if newCode == 'W' or newCode == 'D' else self.__Code

    def getCode(self):
        return self.__Code

    def setNote(self, newNote):
        self.__Note = newNote if len(newNote) > 0 else self.__Note

    def getNote(self):
        return self.__Note

    def loadTransaction(self):
        self.setAmount(float(input("Enter transaction amount(DD.CC),$")))
        self.setCode(input("Enter transaction code('W' or 'D'),"))
        self.setNote(input("Enter purpose of transaction"))
