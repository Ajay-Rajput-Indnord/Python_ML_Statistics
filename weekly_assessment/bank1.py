class BankAccount():
    def __init__(self,balance=5000):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
            self.__balance+= amount
            return f'you deposit amount is {amount} and your current balance is {self.__balance}'
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            return f'you withdraw amount is {amount} and your current balance is {self.__balance}'
        else:
            return 'low balance'
    
