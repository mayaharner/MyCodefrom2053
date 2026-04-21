from bank_account import BankAccount

account1 = BankAccount("12345", 10000)
print(account1)
account1.deposit(5000)
print(account1)
account1.withdraw(7000)
print(account1)
account1.get_balance()
print(account1)