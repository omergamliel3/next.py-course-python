class BankAccount:

    # Class variable
    BANK_NAME = 'PayPy'
    
    def __init__(self, balance=0):
        self._balance = balance

    def __repr__(self):
        return f'Current balance is: {self._balance}'

    def get_balance(self):
        return self._balance

    def deposit(self, value=0):
        self._balance += value
    
    def withdraw(self, value=0):
        self._balance -= value

    

def main():
    my_account = BankAccount(1000)
    another_account = BankAccount()
    my_account.deposit(1)
    another_account.deposit(1)
    print(my_account.get_balance())
    print(another_account.get_balance())
    print(f'Bank name: {BankAccount.BANK_NAME}')

if __name__ == "__main__":
    main()
