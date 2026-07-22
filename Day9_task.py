# Task 1: The BankAccount Class & Private Attributes

class BankAccount:
    def __init__(self, account_holder, balance) :
        self.account_holder = account_holder
        self.__balance = balance   

    # Task 2: Property Decorators (Getter)
    @property
    def balance(self) :
        return self.__balance

    # Task 2: Property Decorators (Setter)
    @balance.setter
    def balance(self, new_balance) :
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = new_balance

    # Task 3: Deposit Method
    def deposit(self, amount) :
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        print("Deposit Successful!")
        print("Current Balance:", self.__balance)

    # Task 3: Withdraw Method
    def withdraw(self, amount) :
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print("Withdrawal Successful!")
        print("Current Balance:", self.__balance)


account = BankAccount("Bisma", 8000)
print("Account Holder:", account.account_holder)
print("Current Balance:", account.balance)
account.deposit(2000)
account.withdraw(3000)
account.balance = -500
account.deposit(-100)
account.withdraw(10000)
