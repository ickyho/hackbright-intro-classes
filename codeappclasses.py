class BankAccount(object):
	def __init__(self,name,account_balance):
		self.name = name
		self.account_balance = account_balance
	def deposit(self,deposit_amount):
		self.account_balance += deposit_amount
		return self.account_balance
	def withdrawal(self,withdrawal_amount):
		self.account_balance -= withdrawal_amount
		return self.account_balance

taryn = BankAccount("Taryn",100)
vicky = BankAccount("Vicky",100)
print taryn.deposit(100)
print vicky.withdrawal(10000)
