class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    @property
    def balance(self) -> int:
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance) -> None:
        BankAccount.total_balance -= self.balance
        self.__balance = new_balance
        BankAccount.total_balance += new_balance

# TODO: Create two accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${alice.balance}")
print(f"Bob's balance: ${bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
