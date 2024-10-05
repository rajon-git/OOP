class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return f'Your balance is: {self.balance}'
    
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print( f'Deposited: {amount}. {self.get_balance()}')
        else:
            return 'Invalid deposit amount.'
        
    def withdraw(self,amount):
        if amount >= self.min_withdraw and amount <= self.max_withdraw and amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew: {amount}. {self.get_balance()}')
        elif amount < self.min_withdraw:
            return f'Minimum withdrawal amount is {self.min_withdraw}.'
        elif amount > self.max_withdraw:
            return f'Maximum withdrawal amount is {self.max_withdraw}.'
        else:
            return 'Insufficient balance.'
        
ddbl = Bank(15000)

# ddbl.deposite(1000)
ddbl.withdraw(1000)