class Bank:
    def __init__(self,holder_name, initial_deposit):
        self.holder_name = holder_name
        self.__balance = initial_deposit  #balance kakue dekhabo na casule kore rakha etai encapsulation

    def deposit(self,amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

rafsan = Bank('Rafsan', 20000)
rafsan.deposit(10000)
print(rafsan.get_balance())
