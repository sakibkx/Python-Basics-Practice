class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number  # Private attribute
        self._account_holder = account_holder  # Protected attribute
        self.__balance = balance if balance >= 0 else 0  # Initialize with non-negative balance

    # Getter for account number (read-only)
    @property
    def account_number(self):
        return self.__account_number

    # Getter and Setter for account holder
    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, name):
        self._account_holder = name

    # Getter and Setter for balance
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Error: Balance cannot be negative.")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds or invalid amount.")

    # Method to display account information
    def print_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate  # New attribute for interest rate

    # Method to apply interest to the balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")


# Practice Tasks
# 1. Create a bank account and perform deposits and withdrawals.
# 2. Update the account holder's name.
# 3. Create a savings account, apply interest, and print updated balance.
# 4. Test the encapsulation features to ensure controlled access.

# Example usage
# Create a regular bank account
account = BankAccount("123456789", "Alice", 1000)
account.print_account_info()

# Deposit and withdraw money
account.deposit(500)
account.withdraw(300)
account.print_account_info()

# Update account holder name
account.account_holder = "Bob"
account.print_account_info()

# Create a savings account
savings = SavingsAccount("987654321", "Charlie", 2000, 5)  # 5% interest rate
savings.print_account_info()

# Apply interest and print updated balance
savings.apply_interest()
savings.print_account_info()
