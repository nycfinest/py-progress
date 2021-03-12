class Bank():
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        temp = self.balance - amount
        if(temp < 0):
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}")
            print(f"Current balance: {self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")
        print(f"Current balance: {self.balance}")
        
    def __str__(self):
        return f"Your account currently has {self.balance}"
    


    