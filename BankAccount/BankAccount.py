class BankAccount:
    count = 1

    def __init__(self, name, balance=0):
        self.name = name
        # balance is private
        self._balance = balance
        self.accountNumber = BankAccount.count
        BankAccount.count += 1

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    # Overriding __str__ method here
    def __str__(self):
        return f"\nAccount Holder: {self.name}\nAccount Balance: {self.get_balance()}\n"

    def display_balance(self):
        return f"Your balance is {self.get_balance()}"
