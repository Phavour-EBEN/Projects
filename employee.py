from BankAccount import *

Dave = BankAccount(1000, "Dave Wooddog")
Sara = BankAccount(2000, "Sara Woody")

Dave.get_balance()
Sara.get_balance()

Dave.deposite(600)
Sara.deposite((500))

Dave.withdrawal(3000)
Dave.withdrawal(600)

Dave.Transfer(100,Sara)

Jim = InterestRewardRate(500, "Jim")
Jim.Transfer(200, Dave)
Jim.Transfer(50, Sara)

Blay = SavingsAcct(1000, "Blay")
Blay.get_balance()

Blay.deposite(100)
Blay.withdrawal(50)

Blay.Transfer(50,Jim)