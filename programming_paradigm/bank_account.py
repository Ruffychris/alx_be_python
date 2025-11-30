class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute (private by convention)
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Adds amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Deducts amount from the balance if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
