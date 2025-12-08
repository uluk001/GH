# Simple Bank Account Class. Create a BankAccount class. Each account should have an owner name and a balance.
# The class should have methods to deposit() money, withdraw() money (don't allow withdrawal if funds are insufficient), and display_balance()


class BankAccount:
    def __init__(self, owner, balance: float = 0.0):
        self.owner = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance or amount <= 0:
            print("Insufficient funds or invalid withdrawal amount.")

        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}")

    def display_balance(self) -> None:
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance:.2f}")
