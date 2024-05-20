"""

ATM.py

"""

class ATM():
    serial_number = 0
    
    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit is Complete")
        
    def withdraw(self, account, amount):
        account.cuurent_balance =  account.current_balance - amount
        print("Withdraw is Complete")
        
    def check_currentbalance(self, account):
        print(account.current_balance)