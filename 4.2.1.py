from transaction import Transaction


class BankStatement:

    def __init__(self, initialBal=0.0):
        self.__BegBal = initialBal
        self.__EndBal = initialBal
        self.__TransactionLog = []
        self.__ArrangedLog = []
        self.__RunningBalLog = []
        self.__NumEntries = 0
        self.__NumDeposits = 0
        self.__NumWithdrawals = 0

    def setBegEndBals(self, BegEndBalance):
        self.__BegBal = self.__EndBal = BegEndBalance

    def getBegBal(self):
        return self.__BegBal

    def getEndBal(self):
        return self.__EndBal

    def getNumEntries(self):
        return self.__NumEntries

    def getNumDeposits(self):
        return self.__NumDeposits

    def getNumWithDrawals(self):
        return self.__NumWithdrawals

    def insertTransaction(self, transaction):
        self.__TransactionLog.append(transaction)
        self.__NumEntries += 1

        if transaction.getCode() == 'D':
            self.__NumDeposits += 1
            if len(self.__RunningBalLog) > 0:
                self.__EndBal = self.__RunningBalLog[-1] + transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)
            else:
                self.__EndBal = self.getBegBal() + transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)
        else:
            self.__NumWithdrawals += 1
            if len(self.__RunningBalLog) > 0:
                self.__EndBal = self.__RunningBalLog[-1] - transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)
            else:
                self.__EndBal = self.getBegBal() - transaction.getAmount()
                self.__RunningBalLog.append(self.__EndBal)

    def displayResults(self):
        print("The beginning transaction was: $" + str(self.__BegBal));

        for index, t in enumerate(self.__TransactionLog):
            print("Transaction: " + str(index + 1) + " was a " +
                  t.getCode() + " amount: $" + str(t.getAmount()) + " for " + t.getNote())

            print("Running Bal: $" + str(self.__RunningBalLog[index]))

        print("The ending balance is: $" + str(self.__EndBal))
        print("The number of Transactions are: " + str(self.__NumEntries))
        print("The number of Deposits are: " + str(self.__NumDeposits))
        print("The number of Withdrawals are: " + str(self.__NumWithdrawals))

    def arrangeTransactions(self):
        self.__ArrangedLog.clear()

        for t in self.__TransactionLog:
            if t.getCode() == 'D':
                self.__ArrangedLog.append(t)

        for t in self.__TransactionLog:
            if t.getCode() == 'W':
                self.__ArrangedLog.append(t)

    def printArranged(self):
        print("Printing the Deposits and Withdrawals as a group:")
        for index, t in enumerate(self.__ArrangedLog):
            print("Transaction was a " + t.getCode() +
                  " amount: $" + str(t.getAmount()) + " for " + t.getNote())

def start():
    myStatement = BankStatement()
    myStatement.setBegEndBals(15.92);

    T1 = Transaction()
    T1.setAmount(123.56)
    T1.setCode('D')
    T1.setNote('CTPay')

    T2 = Transaction(153.86, 'W', "Rent")

    T3 = Transaction()
    T3.setAmount(75.56)
    T3.setCode('D')
    T3.setNote('Tips')

    T4 = Transaction(12.56, 'D', "Gift")

    T5 = Transaction()
    T5.setAmount(73.74)
    T5.setCode('W')
    T5.setNote('Date')

    T6 = Transaction(145.75, 'D', "Loan")

    T7 = Transaction()
    T7.setAmount(40.00)
    T7.setCode('W')
    T7.setNote('Loan Payment')

    T8 = Transaction(21.74, 'W', "Groceries")

    myStatement.insertTransaction(T1)
    myStatement.insertTransaction(T2)
    myStatement.insertTransaction(T3)
    myStatement.insertTransaction(T4)
    myStatement.insertTransaction(T5)
    myStatement.insertTransaction(T6)
    myStatement.insertTransaction(T7)
    myStatement.insertTransaction(T8)

    myStatement.displayResults()

    myStatement.arrangeTransactions()
    myStatement.printArranged()

if __name__ == '__main__':
    start()