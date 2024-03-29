# You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].
# Execute all the valid transactions. A transaction is valid if:
#   The given account number(s) are between 1 and n, and
#   The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
# Implement the Bank class:
#   Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
#   boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
#   boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
#   boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.

class Bank:

    def __init__(self, balance):
        self.balances = dict()

        for indx, val in enumerate(balance):
            self.balances[indx + 1] = val

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.balances and account2 in self.balances and self.balances[account1] >= money:
            self.balances[account1] -= money
            self.balances[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.balances:
            self.balances[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.balances and self.balances[account] >= money:
            self.balances[account] -= money 
            return True 
        return False 

# Test cases
bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))
