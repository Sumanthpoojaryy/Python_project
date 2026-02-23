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
            print("Deposit amount must be positive.")
            return   # exit function

        self.balance += amount
        self._add_transaction("Deposit", amount)
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return   # exit function

        if amount > self.balance:
            print("Insufficient balance.")
            return   # exit function

        self.balance -= amount
        self._add_transaction("Withdraw", amount)
        print("Withdrawal successful.")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        if not isinstance(target_account, BankAccount):
            print("Invalid target account.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance for transfer.")
            return

        self.balance -= amount
        target_account.balance += amount

        self._add_transaction(f"Transfer to {target_account.account_number}", amount)
        target_account._add_transaction(f"Transfer from {self.account_number}", amount)

        print("Transfer successful.")

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Holder Name: {self.holder_name}\n"
                f"Current Balance: {self.balance:.2f}")

acc1 = BankAccount("A101", "Sumanth", 1000)
acc2 = BankAccount("A102", "Rahul", 500)

acc1.deposit(500)
acc1.withdraw(200)
acc1.transfer(300, acc2)

print(acc1)
print("\nTransaction History:")
for txn in acc1.transaction_history:
    print(txn)

