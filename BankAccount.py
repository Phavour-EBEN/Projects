class BalanceException(Exception):
    pass
"""Handling the information about an account owner """
class  BankAccount:
    def __init__(self,initialAmount,accName):
        self.Balance = initialAmount
        self.Name = accName
        print(f"\nAcccount '{self.Name}' created.\nBalance = ${self.Balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.Name}' = ${self.Balance:.2f}")

    def deposite(self,amount):
        self.Balance = self.Balance + amount
        print(f"\nDeposite Completed.")
        self.get_balance()

    def VariableTransaction(self,amount):
        if self.Balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry,not enough balance to complete transaction, \nAccount '{self.Name}' has ${self.Balance:.2f}")


    def withdrawal(self,amount):
        try:
            self.VariableTransaction(amount)
            self.Balance = self.Balance - amount
            print(f"\nWithdrawal successful")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdrawal interrupted: {error}')

    def Transfer(self,amount,account):
        try:
            print(10*"*")
            print(f"\nBeginning Transfer... 🚀🚀")
            self.VariableTransaction(amount)
            self.withdrawal(amount)
            account.deposite(amount)
            print(f"Transfer Complete... ✅")
            print(10 * "*")
        except BalanceException as error:
            print(f"Transaction interrupted ❌❌: {error}")

class InterestRewardRate(BankAccount):
    def deposite(self,amount):
        self.Balance = self.Balance + ((5/100)*amount)
        print("Deposite successful ✅")
        self.get_balance()

class SavingsAcct(InterestRewardRate):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdrawal(self,amount):
        try:
            self.VariableTransaction(amount+self.fee)
            self.Balance = self.Balance - (amount+self.fee)
            print(f"\nWithdrawal successful")
            self.get_balance()
        except BalanceException as error:
            print(f"Transaction interrupted ❌❌: {error}")