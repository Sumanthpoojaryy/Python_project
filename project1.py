from datetime import datetime

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transaction_history = []
        
        if initial_balance > 0:
            self._add_transaction("Initial Deposit", initial_balance)

    def _add_transaction(self, transaction_type, amount):
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self._add_transaction("Withdraw", amount)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if not isinstance(target_account, BankAccount):
            raise ValueError("Target must be a BankAccount object.")
        
        self.withdraw(amount)
        target_account.deposit(amount)
        self._add_transaction(f"Transfer to {target_account.account_number}", amount)
        target_account._add_transaction(f"Transfer from {self.account_number}", amount)

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Holder Name: {self.holder_name}\n"
                f"Current Balance: ₹{self.balance:.2f}")


acc1 = BankAccount("A101", "Sumanth", 1000)
acc2 = BankAccount("A102", "Rahul", 500)

acc1.deposit(500)
acc1.withdraw(200)
acc1.transfer(300, acc2)

print(acc1)
print("\nTransaction History:")
for txn in acc1.transaction_history:
    print(txn)
